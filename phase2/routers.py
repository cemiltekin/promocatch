from __future__ import annotations

from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Path, Query, Response, status
from sqlalchemy.orm import Session

import schemas
import services
from database import get_db


router = APIRouter(prefix="/campaigns", tags=["Campaigns"])


@router.get("", response_model=list[schemas.CampaignRead])
def get_campaigns(
    q: Optional[str] = Query(
        default=None,
        min_length=1,
        description="Search text in campaign title/description.",
    ),
    platform: Optional[str] = Query(
        default=None,
        min_length=2,
        description="Platform name filter (min 2 chars).",
    ),
    min_discount: Optional[int] = Query(
        default=None,
        ge=1,
        le=100,
        description="Minimum discount filter (1-100, integer).",
    ),
    max_discount: Optional[int] = Query(
        default=None,
        ge=1,
        le=100,
        description="Maximum discount filter (1-100, integer).",
    ),
    db: Session = Depends(get_db),
):
    """Control layer endpoint for retrieving campaigns with optional filters."""
    return services.list_campaigns(
        db=db,
        q=q,
        platform=platform,
        min_discount=min_discount,
        max_discount=max_discount,
    )


@router.get("/platforms/list", response_model=list[str])
def get_platforms_list(db: Session = Depends(get_db)):
    """Control layer endpoint for retrieving all unique platforms."""
    return services.get_all_platforms(db)

@router.get("/stats/summary", response_model=schemas.CampaignStats)
def get_campaign_stats(db: Session = Depends(get_db)):
    """Control layer endpoint for retrieving aggregate statistics."""
    return services.get_campaign_stats(db)

@router.get("/recent/list", response_model=list[schemas.CampaignRead])
def get_recent_campaigns_list(db: Session = Depends(get_db)):
    """Control layer endpoint for retrieving the most recently added campaigns."""
    return services.get_recent_campaigns(db)

@router.get("/discount/highest", response_model=schemas.CampaignRead)
def get_highest_discount(db: Session = Depends(get_db)):
    """Control layer endpoint for retrieving the campaign with the highest discount."""
    campaign = services.get_highest_discount_campaign(db)
    if not campaign:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No campaigns available.")
    return campaign

@router.post("/{campaign_id}/click", response_model=schemas.ClickResponse)
def simulate_click(
    campaign_id: int = Path(..., ge=1, description="Campaign identifier (positive integer)."),
    db: Session = Depends(get_db)
):
    """Control layer endpoint to simulate a user click on a campaign."""
    response = services.simulate_campaign_click(db, campaign_id)
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Campaign not found.")
    return response

@router.delete("/bulk/clear", response_model=schemas.BulkDeleteResponse)
def clear_all(db: Session = Depends(get_db)):
    """Control layer endpoint to delete all campaigns (utility)."""
    return services.clear_all_campaigns(db)


@router.get("/{campaign_id}", response_model=schemas.CampaignRead)
def get_campaign(
    campaign_id: int = Path(..., ge=1, description="Campaign identifier (positive integer)."),
    db: Session = Depends(get_db),
):
    """Control layer endpoint for retrieving a campaign by id."""
    campaign = services.get_campaign(db, campaign_id)
    if not campaign:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Campaign not found.")
    return campaign


@router.post(
    "",
    response_model=schemas.CampaignRead,
    status_code=status.HTTP_201_CREATED,
)
def create_campaign(
    campaign: schemas.CampaignCreate,
    db: Session = Depends(get_db),
):
    """Control layer endpoint for adding a newly discovered campaign."""
    return services.add_campaign(db, campaign)


@router.put("/{campaign_id}", response_model=schemas.CampaignRead)
def update_campaign(
    campaign: schemas.CampaignUpdate,
    campaign_id: int = Path(..., ge=1, description="Campaign identifier (positive integer)."),
    db: Session = Depends(get_db),
):
    """Control layer endpoint for updating an existing campaign."""
    updated_campaign = services.update_campaign(db, campaign_id, campaign)
    if not updated_campaign:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Campaign not found.")
    return updated_campaign


@router.delete("/{campaign_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_campaign(
    campaign_id: int = Path(..., ge=1, description="Campaign identifier (positive integer)."),
    db: Session = Depends(get_db),
):
    """Control layer endpoint for deleting an existing campaign."""
    deleted = services.delete_campaign(db, campaign_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Campaign not found.")
    return Response(status_code=status.HTTP_204_NO_CONTENT)

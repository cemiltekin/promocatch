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

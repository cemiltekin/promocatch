from typing import Optional

from sqlalchemy.orm import Session

import models
import schemas


def get_all_campaigns(
    db: Session,
    q: Optional[str] = None,
    platform: Optional[str] = None,
    min_discount: Optional[int] = None,
    max_discount: Optional[int] = None,
) -> list[models.Campaign]:
    """Fetch campaign rows from the database with optional filters."""
    query = db.query(models.Campaign)

    if q:
        search = f"%{q}%"
        query = query.filter(
            models.Campaign.title.ilike(search) | models.Campaign.description.ilike(search)
        )

    if platform:
        platform_search = f"%{platform}%"
        query = query.filter(models.Campaign.platform.ilike(platform_search))

    if min_discount is not None:
        query = query.filter(models.Campaign.discount_rate >= min_discount)

    if max_discount is not None:
        query = query.filter(models.Campaign.discount_rate <= max_discount)

    return query.order_by(models.Campaign.id.desc()).all()


def get_campaign_by_id(db: Session, campaign_id: int) -> Optional[models.Campaign]:
    """Fetch a single campaign by identifier."""
    return db.query(models.Campaign).filter(models.Campaign.id == campaign_id).first()


def create_campaign(db: Session, campaign: schemas.CampaignCreate) -> models.Campaign:
    """Persist a new campaign row in SQLite."""
    db_campaign = models.Campaign(**campaign.model_dump())
    db.add(db_campaign)
    db.commit()
    db.refresh(db_campaign)
    return db_campaign


def update_campaign(
    db: Session,
    db_campaign: models.Campaign,
    campaign: schemas.CampaignUpdate,
) -> models.Campaign:
    """Apply updates to an existing campaign and persist the changes."""
    update_data = campaign.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_campaign, key, value)
    db.commit()
    db.refresh(db_campaign)
    return db_campaign


def delete_campaign(db: Session, db_campaign: models.Campaign) -> None:
    """Delete an existing campaign row from the database."""
    db.delete(db_campaign)
    db.commit()


def count_campaigns(db: Session) -> int:
    """Return the number of campaigns currently stored."""
    return db.query(models.Campaign).count()

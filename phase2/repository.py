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

from sqlalchemy import func


def get_platforms(db: Session) -> list[str]:
    """Return a list of unique platform names."""
    results = db.query(models.Campaign.platform).distinct().all()
    return [r[0] for r in results if r[0]]


def get_stats(db: Session) -> dict:
    """Return aggregate statistics for all campaigns."""
    total = db.query(models.Campaign).count()
    if total == 0:
        return {"total_campaigns": 0, "average_discount": 0.0, "max_discount": 0}

    avg_disc = db.query(func.avg(models.Campaign.discount_rate)).scalar()
    max_disc = db.query(func.max(models.Campaign.discount_rate)).scalar()

    return {
        "total_campaigns": total,
        "average_discount": round(float(avg_disc), 2) if avg_disc else 0.0,
        "max_discount": int(max_disc) if max_disc else 0
    }


def get_recent_campaigns(db: Session, limit: int = 3) -> list[models.Campaign]:
    """Return the most recently added campaigns."""
    return db.query(models.Campaign).order_by(models.Campaign.id.desc()).limit(limit).all()


def get_highest_discount(db: Session) -> Optional[models.Campaign]:
    """Return the campaign with the highest discount rate."""
    return db.query(models.Campaign).order_by(models.Campaign.discount_rate.desc(), models.Campaign.id.desc()).first()


def clear_all_campaigns(db: Session) -> int:
    """Delete all campaigns and return the deleted count."""
    count = db.query(models.Campaign).delete()
    db.commit()
    return count

from typing import Optional

from sqlalchemy.orm import Session

import models
import repository
import schemas


ENGLISH_SAMPLE_CAMPAIGNS = [
    schemas.CampaignCreate(
        title="Spring Fashion Sale",
        platform="StyleHub",
        description="Get an extra discount at checkout on selected fashion brands.",
        discount_rate=20,
    ),
    schemas.CampaignCreate(
        title="Grocery Cashback Weekend",
        platform="Bonus Plus",
        description="Earn bonus points on grocery purchases at partner markets this weekend.",
        discount_rate=15,
    ),
    schemas.CampaignCreate(
        title="Coffee Club Weekday Offer",
        platform="Coffee Club",
        description="Enjoy a weekday discount on your second drink at selected coffee chains.",
        discount_rate=30,
    ),
]

LEGACY_CAMPAIGN_FIXES = {
    "Giyimde Bahar Firsati": ENGLISH_SAMPLE_CAMPAIGNS[0],
    "Market Alisverisine Bonus": ENGLISH_SAMPLE_CAMPAIGNS[1],
    "Kahve Zincirlerinde Firsat": ENGLISH_SAMPLE_CAMPAIGNS[2],
    "FENERBAHÃE ÃRÃNLERÄ° BEDAVA": schemas.CampaignCreate(
        title="Official Merchandise Giveaway",
        platform="Fan Store",
        description="Selected fan merchandise is available at no cost for a limited-time promotion.",
        discount_rate=100,
    ),
    "FENERBAHÇE ÜRÜNLERİ BEDAVA": schemas.CampaignCreate(
        title="Official Merchandise Giveaway",
        platform="Fan Store",
        description="Selected fan merchandise is available at no cost for a limited-time promotion.",
        discount_rate=100,
    ),
}


def list_campaigns(
    db: Session,
    q: Optional[str] = None,
    platform: Optional[str] = None,
    min_discount: Optional[int] = None,
    max_discount: Optional[int] = None,
) -> list[models.Campaign]:
    """Domain service for listing campaigns with optional filters."""
    return repository.get_all_campaigns(
        db=db,
        q=q.strip() if q else None,
        platform=platform.strip() if platform else None,
        min_discount=min_discount,
        max_discount=max_discount,
    )


def get_campaign(db: Session, campaign_id: int) -> Optional[models.Campaign]:
    """Domain service for fetching a single campaign."""
    return repository.get_campaign_by_id(db, campaign_id)


def add_campaign(db: Session, campaign: schemas.CampaignCreate) -> models.Campaign:
    """Domain service for applying business rules before saving a campaign."""
    normalized_campaign = schemas.CampaignCreate(
        title=campaign.title.strip(),
        platform=campaign.platform.strip(),
        description=campaign.description.strip(),
        discount_rate=campaign.discount_rate,
    )
    return repository.create_campaign(db, normalized_campaign)


def update_campaign(
    db: Session,
    campaign_id: int,
    campaign: schemas.CampaignUpdate,
) -> Optional[models.Campaign]:
    """Domain service for updating an existing campaign."""
    db_campaign = repository.get_campaign_by_id(db, campaign_id)
    if not db_campaign:
        return None

    normalized_data = campaign.model_dump(exclude_unset=True)
    if "title" in normalized_data and normalized_data["title"] is not None:
        normalized_data["title"] = normalized_data["title"].strip()
    if "platform" in normalized_data and normalized_data["platform"] is not None:
        normalized_data["platform"] = normalized_data["platform"].strip()
    if "description" in normalized_data and normalized_data["description"] is not None:
        normalized_data["description"] = normalized_data["description"].strip()

    return repository.update_campaign(
        db,
        db_campaign,
        schemas.CampaignUpdate(**normalized_data),
    )


def delete_campaign(db: Session, campaign_id: int) -> bool:
    """Domain service for deleting a campaign."""
    db_campaign = repository.get_campaign_by_id(db, campaign_id)
    if not db_campaign:
        return False

    repository.delete_campaign(db, db_campaign)
    return True


def seed_initial_campaigns(db: Session) -> None:
    """Ensure demo data exists and uses the current English sample content."""
    if repository.count_campaigns(db) == 0:
        for campaign in ENGLISH_SAMPLE_CAMPAIGNS:
            repository.create_campaign(db, campaign)

    repair_legacy_campaigns(db)


def repair_legacy_campaigns(db: Session) -> None:
    """Replace legacy or mojibake demo records with the current English samples."""
    for campaign in repository.get_all_campaigns(db):
        replacement = LEGACY_CAMPAIGN_FIXES.get(campaign.title)
        if not replacement:
            continue

        repository.update_campaign(
            db,
            campaign,
            schemas.CampaignUpdate(**replacement.model_dump()),
        )

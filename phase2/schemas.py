from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class CampaignBase(BaseModel):
    title: str = Field(..., min_length=3, max_length=120)
    platform: str = Field(..., min_length=2, max_length=80)
    description: str = Field(..., min_length=10)
    discount_rate: int = Field(..., ge=1, le=100)


class CampaignCreate(CampaignBase):
    pass


class CampaignUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=3, max_length=120)
    platform: Optional[str] = Field(None, min_length=2, max_length=80)
    description: Optional[str] = Field(None, min_length=10)
    discount_rate: Optional[int] = Field(None, ge=1, le=100)


class CampaignRead(CampaignBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

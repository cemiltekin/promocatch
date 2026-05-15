from sqlalchemy import Column, Integer, String, Text

from database import Base


class Campaign(Base):
    """Database entity representing a retail or finance promotion."""

    __tablename__ = "campaigns"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(120), nullable=False, index=True)
    platform = Column(String(80), nullable=False, index=True)
    description = Column(Text, nullable=False)
    discount_rate = Column(Integer, nullable=False)

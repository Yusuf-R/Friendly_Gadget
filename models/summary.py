#!/usr/bin/env python3
"""Base class for summary table. This class maps to the 'brand' table."""

from models.base import Base, Mobile
from sqlalchemy import Column, ForeignKey, String


class Summary(Mobile, Base):
    """Base class for summary. This class maps to the 'brand' table."""
    __tablename__ = "summaries"
    model_id = Column(String(60), ForeignKey("models.id"), nullable=False)
    Release = Column(String(32), nullable=True)
    Screen = Column(String(32), nullable=True)
    Memory = Column(String(32), nullable=True)
    Storage = Column(String(32), nullable=True)
    Camera = Column(String(32), nullable=True)
    Battery = Column(String(32), nullable=True)
    Gaming = Column(String(32), nullable=True)
    Photography = Column(String(32), nullable=True)
    SocialMedia = Column(String(32), nullable=True)
    Publishing = Column(String(32), nullable=True)
    Marketting = Column(String(32), nullable=True)
    Multimedia = Column(String(32), nullable=True)
    Basic = Column(String(32), nullable=True)

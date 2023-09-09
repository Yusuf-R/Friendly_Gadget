#!/usr/bin/env python3
"""Base class for summary table. This class maps to the 'brand' table."""

from models.base import Mobile, Base
from sqlalchemy import Column, String, ForeignKey


class Summary(Mobile, Base):
    """Base class for summary. This class maps to the 'brand' table."""

    __tablename__ = "summaries"
    # name = Column(String(60), nullable=False)
    # img = Column(String(256), nullable=True)
    model_id = Column(String(60), ForeignKey("models.id"), nullable=False)
    Release = Column(String(32), nullable=True)
    Screen = Column(String(32), nullable=True)
    Memory = Column(String(32), nullable=True)
    Storage = Column(String(32), nullable=True)
    Camera = Column(String(32), nullable=True)
    Battery = Column(String(32), nullable=True)

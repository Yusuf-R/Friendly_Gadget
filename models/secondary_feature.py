#!/usr/bin/env python3
"""Base class for the secondary features"""

from models.base import Mobile, Base
from sqlalchemy import Column, String, ForeignKey


class Secondary(Mobile, Base):
    """Base class for the secondary features"""
    __tablename__ = "secondary"
    inner_key = Column(String(256))
    inner_value = Column(String(256))
    feature_id = Column(String(60), ForeignKey("features.id"))

#!/usr/bin/env python3
"""This the base template for all model object instances."""

from models.base import Base, Mobile
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship


class Model(Mobile, Base):
    """Model class"""

    __tablename__ = "models"
    model_name = Column(String(32), unique=True, nullable=False)
    brand_id = Column(String(60), ForeignKey("brands.id"), nullable=False)
    model_img = Column(String(256), nullable=True)
    features = relationship(
        "Feature", backref="models", cascade="all, delete, delete-orphan"
    )
    summaries = relationship(
        "Summary", backref="models", cascade="all, delete, delete-orphan"
    )

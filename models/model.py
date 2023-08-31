#!/usr/bin/env python3
"""This the base template for all model object instances."""

from models.base import Mobile, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Model(Mobile, Base):
    """Model class"""

    __tablename__ = "models"
    model_name = Column(String(32), nullable=False)
    brand_id = Column(String(60), ForeignKey("brands.id"), nullable=False)
    features = relationship(
        "Features", backref="models", cascade="all, delete, delete-orphan"
    )

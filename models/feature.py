#!/usr/bin/env python3
"""Feature template for all object instances"""

from models.base import Base, Mobile
from sqlalchemy import Column, ForeignKey, JSON, String
from sqlalchemy.orm import relationship


class Feature(Mobile, Base):
    """
    Docstring: Subclass of Mobile. This class maps to the 'model' table.
    Attributes:
        __tablename__ = "features"
        model_id = Column(String(60), ForeignKey("models.id"), nullable=False)
        secondary_details = relationship(
        "Secondary", backref="features", cascade="all, delete, delete-orphan"
        )
    """

    __tablename__ = "features"
    model_id = Column(String(60), ForeignKey("models.id"), nullable=False)
    secondary_details = relationship(
        "Secondary", backref="features", cascade="all, delete, delete-orphan"
    )
    PhoneDetails = Column(JSON, nullable=True)
    NetworkDetails = Column(JSON, nullable=True)
    LaunchDetails = Column(JSON, nullable=True)
    BodyDetails = Column(JSON, nullable=True)
    DisplayDetails = Column(JSON, nullable=True)
    PlatformDetails = Column(JSON, nullable=True)
    MemoryDetails = Column(JSON, nullable=True)
    MainCameraDetails = Column(JSON, nullable=True)
    SelfieCameraDetails = Column(JSON, nullable=True)
    SoundDetails = Column(JSON, nullable=True)
    CommunicationsDetails = Column(JSON, nullable=True)
    FeaturesDetails = Column(JSON, nullable=True)
    BatteryDetails = Column(JSON, nullable=True)

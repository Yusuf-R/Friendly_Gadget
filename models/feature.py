#!/usr/bin/env python3
"""Feature template for all object instances"""


from models.base import Mobile, Base
from sqlalchemy import Column, String, ForeignKey, JSON
from sqlalchemy.orm import relationship


class Features(Mobile, Base):
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
    LaunchDetails = Column(JSON, nullable=True)
    NetworkDetails = Column(JSON, nullable=True)
    DisplayDetails = Column(JSON, nullable=True)
    BodyDetails = Column(JSON, nullable=True)
    PlatformDetails = Column(JSON, nullable=True)
    Processor = Column(JSON, nullable=True)
    ChipSet = Column(JSON, nullable=True)
    MemoryDetails = Column(JSON, nullable=True)
    MainCamera = Column(JSON, nullable=True)
    SelfieCamera = Column(JSON, nullable=True)
    Battery = Column(JSON, nullable=True)

from models.base import Mobile, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Brand(Mobile, Base):
    """Base class for mobiles. This class maps to the 'mobiles' table."""

    __tablename__ = "brands"
    brand_name = Column(String(16), nullable=False)
    models = relationship(
        "Model", backref="brands", cascade="all, delete, delete-orphan"
    )

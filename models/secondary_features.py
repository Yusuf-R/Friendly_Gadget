from models.base import Mobile, Base
from sqlalchemy import Column, String, ForeignKey


class Secondary(Mobile, Base):
    __tablename__ = "secondary"
    inner_key = Column(String(256))
    inner_value = Column(String(256))
    feature_id = Column(String(60), ForeignKey("features.id"))

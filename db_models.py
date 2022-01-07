from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    """
    SQLAlchemy User's table
    """
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    hashed_password = Column(String)
    x_data_type = Column(String)
    y_data_type = Column(String)
    correlation_value = Column(Float, nullable=True)
    correlation_p_value = Column(Float, nullable=True)

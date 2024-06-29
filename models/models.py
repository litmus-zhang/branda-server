from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, JSON

from sqlalchemy.orm import relationship


from config.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String, index=True)
    lastname = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    brands = relationship("Brand", back_populates="owner")


class Brand(Base):
    __tablename__ = "brands"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    font = Column(String, index=True)
    strategy = Column(String, index=True)
    color = Column(String, index=True)
    logo = Column(String, index=True)
    messaging = Column(String, index=True)
    photography = Column(String, index=True)
    illustration = Column(String, index=True)
    presentation = Column(String, index=True)

    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="brands")

from core.db import Base
from sqlalchemy import Column, ForeignKey, String, Integer, Text, DateTime
from sqlalchemy.orm import relationship

class Post(Base):
    __tablename__ = "microblog_posts"
    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String)
    text = Column(String(350))
    date = Column(DateTime)
    user = Column(Integer, ForeignKey("user.id"))
    user_id = relationship("User")
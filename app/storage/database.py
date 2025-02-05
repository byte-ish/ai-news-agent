import os

from sqlalchemy import Column, DateTime, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.logger import logger  # ✅ FIXED: Import logger

# Load database URL from environment
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///news.db")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class NewsArticle(Base):
    __tablename__ = "news_articles"

    id = Column(String, primary_key=True, index=True)
    title = Column(String, index=True)
    url = Column(String, unique=True, index=True)
    summary = Column(String)
    timestamp = Column(DateTime)


try:
    Base.metadata.create_all(bind=engine)
    logger.info("✅ Database tables created successfully.")
except Exception as e:
    logger.error("❌ Database initialization failed: %s", str(e), exc_info=True)

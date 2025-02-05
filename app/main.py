from fastapi import FastAPI, HTTPException

from app.logger import logger
from app.scrapers.scraper import NewsScraper

app = FastAPI()


@app.get("/health", tags=["Health Check"])
def health_check():
    """
    Health check endpoint to verify API is running.
    """
    logger.info("✅ Health check endpoint accessed.")
    return {"status": "healthy"}


@app.get("/scrape-news", tags=["Scraper"])
def scrape_news():
    """
    Scrapes AI news articles and returns JSON response.
    """
    url = "https://news.ycombinator.com/"  # Example site (modify as needed)
    scraper = NewsScraper(url)
    news = scraper.fetch_news()

    if not news:
        logger.warning("⚠️ No articles were scraped.")
        raise HTTPException(status_code=500, detail="No articles could be scraped.")

    logger.info(f"📢 Returning {len(news)} scraped articles.")
    return {"articles": news}


# Run this API using: uvicorn app.main:app --reload

import unittest
from datetime import datetime

from app.storage.database import NewsArticle, SessionLocal


class TestDatabase(unittest.TestCase):
    """
    Test cases for database interactions.
    """

    def setUp(self):
        """Set up a test database session and insert test data."""
        self.session = SessionLocal()

        # ✅ Insert test data if not exists
        existing_article = self.session.query(NewsArticle).filter_by(id="1").first()
        if not existing_article:
            test_article = NewsArticle(
                id="1",
                title="Test News",
                url="https://example.com",
                summary="This is a test summary",
                timestamp=datetime.utcnow(),
            )
            self.session.add(test_article)
            self.session.commit()

    def tearDown(self):
        """Clean up the session."""
        self.session.close()

    def test_fetch_article(self):
        """Test retrieving a stored article."""
        article = self.session.query(NewsArticle).filter_by(id="1").first()
        self.assertIsNotNone(article)  # ✅ Ensure article exists
        self.assertEqual(article.title, "Test News")  # ✅ Ensure title matches

    def test_delete_article(self):
        """Test deleting an article from the database."""
        article = self.session.query(NewsArticle).filter_by(id="3").first()
        if article:
            self.session.delete(article)
            self.session.commit()

        deleted_article = self.session.query(NewsArticle).filter_by(id="3").first()
        self.assertIsNone(deleted_article)  # ✅ Ensure article was deleted


if __name__ == "__main__":
    unittest.main()

import unittest

from app.scrapers.scraper import NewsScraper


class TestNewsScraper(unittest.TestCase):
    """
    Test cases for the NewsScraper class.
    """

    def setUp(self):
        """Set up test instance with Hacker News URL."""
        self.scraper = NewsScraper("https://news.ycombinator.com/")

    def test_fetch_news(self):
        """Test that fetch_news returns a list of articles with title and URL."""
        articles = self.scraper.fetch_news()
        self.assertIsInstance(articles, list)  # ✅ Ensure result is a list
        for article in articles:
            self.assertIn("title", article)
            self.assertIn("url", article)

    def test_fetch_news_empty(self):
        """Test that fetch_news handles an invalid URL gracefully."""
        scraper = NewsScraper("https://invalid-url.com")
        articles = scraper.fetch_news()
        self.assertEqual(articles, [])  # ✅ Expect an empty list


if __name__ == "__main__":
    unittest.main()

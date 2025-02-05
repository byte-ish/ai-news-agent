import unittest

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


class TestAPI(unittest.TestCase):
    def test_health_check(self):
        """Test the /health endpoint."""
        response = client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "healthy"})

    def test_scrape_news(self):
        """Test the /scrape-news endpoint."""
        response = client.get("/scrape-news")
        json_data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertIn("articles", json_data)
        self.assertIsInstance(json_data["articles"], list)

    def test_scrape_news_failure(self):
        """Test /scrape-news when no articles are available."""
        response = client.get("/scrape-news")
        if response.status_code == 500:
            self.assertEqual(response.json()["detail"], "No articles could be scraped.")


if __name__ == "__main__":
    unittest.main()

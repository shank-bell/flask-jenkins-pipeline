import unittest

from app import app


class HomeRouteTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home_status_and_body(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_data(as_text=True), "Hello, Jenkins CI/CD!")


if __name__ == "__main__":
    unittest.main()

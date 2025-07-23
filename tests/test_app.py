import unittest
import os
import app

os.environ['TESTING'] = 'true'

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.app
        self.client = self.app.test_client()

        if app.mydb.is_closed():
            app.mydb.connect()
        app.mydb.create_tables([app.TimelinePost])

    def tearDown(self):
        app.mydb.drop_tables([app.TimelinePost])
        app.mydb.close()

    def test_home(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        html = response.get_data(as_text=True)
        self.assertIn("<h1>", html)
        self.assertIn("Timeline", html)

    def test_timeline_api(self):
        response = self.client.post("/api/timeline_post", data={
            "name": "Test User",
            "email": "test@example.com",
            "content": "Test post content"
        })
        self.assertEqual(response.status_code, 200)

        response = self.client.get("/api/timeline_post")
        self.assertEqual(response.status_code, 200)
        json = response.get_json()
        self.assertIn("timeline_posts", json)
        self.assertEqual(len(json["timeline_posts"]), 1)
        self.assertEqual(json["timeline_posts"][0]["name"], "Test User")
        self.assertEqual(json["timeline_posts"][0]["email"], "test@example.com")

    def test_timeline_page(self):
        response = self.client.get("/timeline")
        self.assertEqual(response.status_code, 200)
        html = response.get_data(as_text=True)
        self.assertIn("<form", html)
        self.assertIn("name=", html)

    def test_malformed_timeline_post(self):
        response = self.client.post("/api/timeline_post", data={
            "name": "",
            "email": "not-an-email",
            "content": ""
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn("Invalid", response.get_data(as_text=True))

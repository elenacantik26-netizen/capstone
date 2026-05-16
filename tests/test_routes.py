import unittest
from service import app
from service import routes


class TestAccountRoutes(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        routes.accounts = {}
        routes.next_id = 1

    def test_health(self):
        response = self.client.get('/health')
        self.assertEqual(response.status_code, 200)

    def test_cors_headers(self):
        response = self.client.get(
            '/health',
            headers={'Origin': 'http://example.com'}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn('Access-Control-Allow-Origin', response.headers)

    def test_create_account(self):
        response = self.client.post(
            '/accounts',
            json={'name': 'John', 'email': 'john@example.com'}
        )
        self.assertEqual(response.status_code, 201)

    def test_list_accounts(self):
        response = self.client.get('/accounts')
        self.assertEqual(response.status_code, 200)

    def test_read_account(self):
        self.client.post(
            '/accounts',
            json={'name': 'Jane', 'email': 'jane@example.com'}
        )
        response = self.client.get('/accounts/1')
        self.assertEqual(response.status_code, 200)

    def test_update_account(self):
        self.client.post(
            '/accounts',
            json={'name': 'Jane', 'email': 'jane@example.com'}
        )
        response = self.client.put(
            '/accounts/1',
            json={'name': 'Jane Updated', 'email': 'jane@example.com'}
        )
        self.assertEqual(response.status_code, 200)

    def test_delete_account(self):
        self.client.post(
            '/accounts',
            json={'name': 'Jane', 'email': 'jane@example.com'}
        )
        response = self.client.delete('/accounts/1')
        self.assertEqual(response.status_code, 204)


if __name__ == '__main__':
    unittest.main()

from application import app
import unittest


class FlaskTestCase(unittest.TestCase):

    # Ensure a redirect to the login page
    def test_index_redirect(self):
        tester = app.test_client(self)
        response = tester.get(
            '/index',
            content_type='html/text',
            follow_redirects=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Please log in to access this page.' in response.data)

    # Ensure a 302 on index page without a redirect follow
    def test_index_no_redirect(self):
        tester = app.test_client(self)
        response = tester.get(
            '/index',
            content_type='html/text',
            follow_redirects=False,
        )
        self.assertEqual(response.status_code, 302)

    # Ensure logoutpage returns and redirects
    def test_logout_redirect(self):
        tester = app.test_client(self)
        response = tester.get(
            '/logout', content_type='html/text', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Please login to continue' in response.data)

    # Ensure a 302 on logout page without a redirect follow
    def test_logout_no_redirect(self):
        tester = app.test_client(self)
        response = tester.get(
            '/logout', content_type='html/text', follow_redirects=False)
        self.assertEqual(response.status_code, 302)

    # Ensure the login page loads correctly
    def test_login_page_load(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue(b'Sign In' in response.data)

    # Ensure the login page logs in correctly
    # def test_login_page_login(self):
    #     tester = app.test_client(self)
    #     response = tester.post(
    #         '/login',
    #         data=dict(username="admin", password="admin"),
    #         follow_redirects=True)
    #     # self.assertEqual(response.status_code, 200)

    #     self.assertIn(b"Hi, admin", response.data)


if __name__ == '__main__':
    unittest.main()

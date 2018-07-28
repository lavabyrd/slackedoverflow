import os
import application
import unittest
import tempfile


class applicationTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, application.app.config['DATABASE'] = tempfile.mkstemp()
        application.app.testing = True
        self.app = application.app.test_client()
        with application.app.app_context():
            return ""

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(application.app.config['DATABASE'])

    # def test_empty_db(self):
    #     rv = self.app.get('/')
    #     print(rv)
    #     assert b'No entries here so far' in rv.data

    def test_login_logout(self):
        rv = self.login('admin', 'default')
        assert b'You were logged in' in rv.data
        rv = self.logout()
        assert b'You were logged out' in rv.data
        rv = self.login('adminx', 'default')
        assert b'Invalid username' in rv.data
        rv = self.login('admin', 'defaultx')
        assert b'Invalid password' in rv.data


def logout(self):
    return self.app.get('/logout', follow_redirects=True)


if __name__ == '__main__':
    unittest.main()

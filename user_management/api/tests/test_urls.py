from django.core.urlresolvers import resolve, reverse
from django.test import TestCase


class TestURLs(TestCase):
    """Ensure the urls work."""

    def check_url(self, view_name, url, url_name, url_args=None, url_kwargs=None):
        reversed_url = reverse(url_name, args=url_args, kwargs=url_kwargs)
        self.assertEqual(reversed_url, url)
        resolved_view_name = resolve(url).func.__name__
        self.assertEqual(resolved_view_name, view_name)

    def test_auth_token_url(self):
        self.check_url(
            view_name='GetToken',
            url='/auth',
            url_name='auth')

    def test_password_reset_confirm_url(self):
        self.check_url(
            view_name='PasswordResetView',
            url='/auth/password_reset/confirm/a/x-y',
            url_name='password_reset_confirm',
            url_kwargs={'uidb64': 'a', 'token': 'x-y'})

    def test_password_reset_url(self):
        self.check_url(
            view_name='PasswordResetEmailView',
            url='/auth/password_reset',
            url_name='password_reset')

    def test_profile_detail_url(self):
        self.check_url(
            view_name='ProfileDetailView',
            url='/profile',
            url_name='profile_detail')

    def test_password_change_url(self):
        self.check_url(
            view_name='PasswordChangeView',
            url='/profile/password',
            url_name='password_change')

    def test_register_url(self):
        self.check_url(
            view_name='UserRegister',
            url='/register',
            url_name='register')

    def test_user_detail_url(self):
        self.check_url(
            view_name='UserDetailView',
            url='/users/1',
            url_name='user_detail',
            url_kwargs={'pk': 1})

    def test_user_list_url(self):
        self.check_url(
            view_name='UserListView',
            url='/users',
            url_name='user_list')

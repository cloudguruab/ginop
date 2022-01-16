import pytest
from ..api.models import User

class TestUserModel:
    def setup_method(self):
        self.username = "testuser"
        self.email = "testuser@testbase.com"

        self.test_user = User.objects.create_user(
            username=self.username,
            email=self.email
        )

    def test_create_user(self):
        assert isinstance(self.test_user, User)

    def test_default_user_is_active(self):
        assert self.test_user.is_active

    def test_default_user_is_staff(self):
        assert not self.test_user.is_staff

    def test_default_user_is_superuser(self):
        assert not self.test_user.is_superuser

    def test_get_full_name(self):
        assert self.test_user.get_full_name() == 'Test User'

    def test_get_short_name(self):
        assert self.test_user.get_short_name() == self.email

    def test_unicode(self):
        assert self.test_user.__unicode__() == self.username
        
class TestChainEventsModel:
    def setup_method(self):
        pass
    

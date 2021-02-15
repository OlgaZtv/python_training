import pytest
from model.group import Group
from fixture.application import Application
from fixture.application2 import ApplicationContact


@pytest.fixture(scope="session")
def app(request):
    fixture = Application()
    fixture = ApplicationContact()
    request.addfinalizer(fixture.destroy)
    return fixture

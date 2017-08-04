import pytest
from fixture.application import Apllication


@pytest.fixture
def app(request):
    fixture = Apllication()
    request.addfinalizer(fixture.destroy)
    return fixture

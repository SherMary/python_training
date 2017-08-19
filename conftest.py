import pytest
from fixture.application import Apllication

fixture = None

@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        fixture = Apllication()
    else:
        if not fixture.is_valid():
            fixture = Apllication()
    fixture.session.ensure_login(username="admin", password="secret")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

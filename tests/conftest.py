import pytest


@pytest.fixture(params=["path"])
def data(request):
    with open(request.param) as f:
        yield f.read()

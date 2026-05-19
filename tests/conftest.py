from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

import src.app as app_module


@pytest.fixture
def client() -> TestClient:
    return TestClient(app_module.app)


@pytest.fixture(autouse=True)
def restore_activities_state() -> None:
    original = deepcopy(app_module.activities)
    yield
    app_module.activities.clear()
    app_module.activities.update(deepcopy(original))

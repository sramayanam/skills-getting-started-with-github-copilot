from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app

BASELINE_ACTIVITIES = deepcopy(activities)


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities_state() -> None:
    # Arrange: restore a clean in-memory DB snapshot before each test.
    activities.clear()
    activities.update(deepcopy(BASELINE_ACTIVITIES))

    yield

    # Assert/cleanup: restore baseline to avoid state leaks across tests.
    activities.clear()
    activities.update(deepcopy(BASELINE_ACTIVITIES))

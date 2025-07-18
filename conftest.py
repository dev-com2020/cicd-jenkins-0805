"""
Przygotowanie środowiska testowego
"""

import os
import pytest


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "slow: marks tests as slow (deselect with '-m \"not slow\"')"
    )
    config.addinivalue_line("markers", "integration: marks tests as integration tests")


@pytest.fixture(autouse=True)
def setup_test_environment():
    # Setup wykonywany przed każdym testem
    os.environ["TESTING"] = "true"
    yield
    # Cleanup po każdym teście
    if "TESTING" in os.environ:
        del os.environ["TESTING"]


# Generowanie raportów
"""
pytest --cov=app --cov-report=html --cov-report=xml --junitxml=test-results.xml
"""

"""Test types."""
from _pytest.config import Config


def pytest_configure(config: Config) -> None:
    """Configure test types."""
    config.addinivalue_line("markers", "prod: Computationally expensive, full tests.")

"""Tests for the CLI interface."""
import click.testing
import pytest

from hello_world import console


@pytest.fixture
def runner():
    """Make a testing fixture."""
    return click.testing.CliRunner()


def test_main_succeeds(runner):
    """Run CLI interface with no arguments."""
    result = runner.invoke(console.main)
    assert result.exit_code == 0


# tests/test_console.py
@pytest.mark.prod
def test_main_succeeds_in_production_env(runner):
    """Run expensive production tests."""
    result = runner.invoke(console.main)
    assert result.exit_code == 0

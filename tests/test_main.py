"""Tests for the main module."""

import pytest
from incomp_depend.main import main


def test_main_runs():
    """Test that main function runs without error."""
    try:
        main()
    except Exception as e:
        pytest.fail(f"main() raised {type(e).__name__} unexpectedly!")

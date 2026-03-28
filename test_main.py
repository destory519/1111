#!/usr/bin/env python3
"""
Tests for the 1111 project.
"""

import unittest
from io import StringIO
from contextlib import redirect_stdout
from main import main


class TestMain(unittest.TestCase):
    """Test cases for the main function."""

    def test_main_output(self):
        """Test that main() outputs '1111'."""
        captured_output = StringIO()
        with redirect_stdout(captured_output):
            main()
        self.assertEqual(captured_output.getvalue().strip(), "1111")


if __name__ == "__main__":
    unittest.main()

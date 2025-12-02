#!/usr/bin/env python3
"""
Tests for the 1111 project.
"""

import unittest
from io import StringIO
import sys
from main import main


class TestMain(unittest.TestCase):
    """Test cases for the main function."""

    def test_main_output(self):
        """Test that main() outputs '1111'."""
        captured_output = StringIO()
        original_stdout = sys.stdout
        try:
            sys.stdout = captured_output
            main()
        finally:
            sys.stdout = original_stdout
        self.assertEqual(captured_output.getvalue().strip(), "1111")


if __name__ == "__main__":
    unittest.main()

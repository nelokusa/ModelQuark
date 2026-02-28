# test_modelquark.py
"""
Tests for ModelQuark module.
"""

import unittest
from modelquark import ModelQuark

class TestModelQuark(unittest.TestCase):
    """Test cases for ModelQuark class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ModelQuark()
        self.assertIsInstance(instance, ModelQuark)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ModelQuark()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

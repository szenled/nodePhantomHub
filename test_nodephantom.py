# test_nodephantom.py
"""
Tests for nodePhantom module.
"""

import unittest
from nodephantom import nodePhantom

class TestnodePhantom(unittest.TestCase):
    """Test cases for nodePhantom class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = nodePhantom()
        self.assertIsInstance(instance, nodePhantom)
        
    def test_run_method(self):
        """Test the run method."""
        instance = nodePhantom()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

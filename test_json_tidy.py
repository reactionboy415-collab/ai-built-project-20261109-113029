import unittest
from io import StringIO
from json_tidy import tidy_json

class TestJSONTidy(unittest.TestCase):
    
    def test_valid_json_formatting(self):
        """Test basic formatting of valid JSON."""
        raw = '{"a":1,"b":[2,3]}'
        expected = '{\n    "a": 1,\n    "b": [\n        2,\n        3\n    ]\n}'
        self.assertEqual(tidy_json(raw), expected)

    def test_sort_keys(self):
        """Test that keys are sorted when requested."""
        raw = '{"z": 1, "a": 2}'
        result = tidy_json(raw, sort_keys=True)
        self.assertTrue(result.index('"a"') < result.index('"z"'))

    def test_indentation(self):
        """Test custom indentation levels."""
        raw = '{"a": 1}'
        result = tidy_json(raw, indent=2)
        self.assertEqual(result, '{\n  "a": 1\n}')

    def test_invalid_json(self):
        """Test that clear errors are raised for invalid JSON."""
        raw = '{"a": 1, }' # Trailing comma
        with self.assertRaisesRegex(ValueError, "Invalid JSON:.*line 1"):
            tidy_json(raw)

    def test_empty_string(self):
        """Test behavior with empty input."""
        with self.assertRaises(ValueError):
            tidy_json("")

if __name__ == "__main__":
    unittest.main()
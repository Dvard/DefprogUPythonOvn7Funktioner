import unittest
import ovn1


class TestOvn1(unittest.TestCase):
	def test_maximum(self):
		test_data = [1, 2, 3]
		self.assertEqual(3, ovn1.maximum(test_data))

		test_data = [4, 1, 8, 7]
		self.assertEqual(8, ovn1.maximum(test_data))

		test_data = [8, 32, 1]
		self.assertEqual(max(test_data), ovn1.maximum(test_data))

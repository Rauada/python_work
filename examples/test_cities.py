import unittest

from city_functions import get_formatted_city

class CityTestCase(unittest.TestCase):
	"""Test for city_functions.py"""
	def test_city_country(self):
		"""Do names like Santiago, Chile work?"""
		formatted_name = get_formatted_city('santiago',50000,'chile')
		self.assertEqual(formatted_name,'Santiago, Chile - Population 50000')

if __name__ == '__main__':
 	unittest.main()
import unittest

from proj.sample import haversine


class TestUtils(unittest.TestCase):

    # @unittest.skip('')
    def test_haversine(self):
        start_lat = 55.60587
        start_lon = 13.00073
        end_lat = 55.70584
        end_lon = 13.19321

        distance = haversine(start_lat, start_lon, end_lat, end_lon)
        self.assertEqual(distance, 16.412368673447)

if __name__ == '__main__':
    unittest.main()

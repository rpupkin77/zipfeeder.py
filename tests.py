import unittest
from zipfeeder.connector import Connector as ZipFeeder


class TestZfApi(unittest.TestCase):

    zf = ZipFeeder('7J9Usl6sknnkn')

    def test_single_zip(self):
         z = self.zf.zipcode('01950')
         self.assertEqual(z['zip_code'], "01950")

    def test_city_zips(self):
        zips = self.zf.nearby_zips('01950', 10)
        self.assertTrue(len(zips['zips']) > 0)
        self.assertTrue(type(zips['zips'][0]) == dict)

    def test_multiple_zips(self):
        zips = self.zf.zipcodes(['01950', '02124'])
        self.assertTrue(len(zips) > 0)
        self.assertTrue(type(zips[0]) == dict)

    def test_startswith(self):
        zips = self.zf.zipcodes_startwith("019")
        self.assertTrue(len(zips['zips']) > 0)
        self.assertTrue(type(zips['zips'][0]) == dict)

    def test_state_zips(self):
        zips = self.zf.zipcodes_by_state("MA")
        self.assertTrue(len(zips['cities']) > 0)

    def test_city_zips(self):
        zips = self.zf.zipcodes_by_state("MA", "newb")
        self.assertTrue(len(zips['cities']) > 0)




if __name__ == "__main__":
    unittest.main()



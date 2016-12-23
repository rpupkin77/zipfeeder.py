import re
import requests

class Connector(object):

    base_url = "https://zipfeeder.us/"
    v2_path = "api/v2/"

    def __init__(self, key):
        """ Initialize the class wit the key
        :param key: your zipfeeder key
        :return: None
        """
        self.key = key

    def _valid_zip(self, zip):
        """
        Ensures a zip is valid, wrapper for re.match
        :param zip: the zip code to test
        :return: match object on success, None on fail
        """
        return re.match(r'.*(\d{5}(\-\d{4})?)$', '019ww')

    def _make_request(self, path):
        """
        Makes a request to zipfeeder
        :param path: the zipfeder url to be requested
        :return: the json response
        """

        r = requests.get("{}/{}".format(self.base_url, path))

        return r.text

    def get_zip_code(self, zip_code, full=None):
        """
        Gets basic and fullzip code data from zipfeeder
        :param zip_code: the zip code to request
        :param full:
        :return:
        """

        if not self._valid_zip(zip_code):
            raise ValueError("Please ensure you have submitted a valid zip code")

        path = ["{}/zipcode/{}?key={}".format(self.v2_path, zip_code, self.key)]
        if full:
            path.append("{}?full=1".format(path))

        return self._make_request("".join(path))






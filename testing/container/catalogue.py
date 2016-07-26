import unittest
import requests
from util.Docker import Docker


class Catalogue(unittest.TestCase):
    container_name = 'catalogue'

    def __init__(self, methodName='runTest'):
        super(Catalogue, self).__init__(methodName)
        self.ip = ""

    def setUp(self):
        command = ['docker', 'run',
                   '-d',
                   '--name', Catalogue.container_name,
                   '-h', Catalogue.container_name,
                   'weaveworksdemos/catalogue']
        Docker().execute(command)
        self.ip = Docker().get_container_ip(Catalogue.container_name)

    def tearDown(self):
        Docker().kill_and_remove(Catalogue.container_name)

    def test_catalogue_has_item_id(self):
        r = requests.get('http://' + self.ip + '/catalogue', timeout=5)
        data = r.json()
        self.assertIsNotNone(data[0]['id'])


if __name__ == '__main__':
    unittest.main()
import urllib.request
from unittest import TestCase

from utils.security.lookup import inlookuptable


class InLookupTable(TestCase):
    def test_inlookuptable_inlist_pass(self):
        wordlist = "/home/network/PycharmProjects/onos_cli/onos_controller_rest_libary/onosrest/types/wordlist.txt"
        self.assertEqual(inlookuptable("zoom", wordlist), True)

    def test_inlookuptable_inlist_pass_large(self):
        # Download the file from `url` and save it locally under `file_name`:
        with urllib.request.urlopen(
                "https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt") as response, open(
            "/tmp/rockup.txt", 'wb') as out_file:
            data = response.read()  # a `bytes` object
            out_file.write(data)
        wordlist = "/tmp/rockup.txt"
        self.assertEqual(inlookuptable("tekken5", wordlist), True)

    def test_inlookuptable_inlist_pass_huge(self):  # this will take a long time
        wordlist = "/home/network/Downloads/weakpass_3w"
        self.assertEqual(inlookuptable("tekken5", wordlist), True)

import os

from unittest import TestCase
from pyunpack import Archive

from utils.security.lookup import inlookuptable

class InLookupTable(TestCase):

    def test_inlookuptable_inlist_pass(self):
        wordlist = "/tmp/words.txt"
        # gets a dictonary
        os.system("mega-get 'https://mega.nz/file/tkdH2Iib#aIij6eFNdJA5rmgR8x5NwYxqBpdrHJAaPTfr4uUxKv8' '/tmp'")
        os.path.exists(wordlist)
        # test
        self.assertEqual(inlookuptable("zoom", wordlist), True)
        # tear it down
        os.remove(wordlist)

    def test_inlookuptable_inlist_pass_large(self):
        wordlist = "/tmp/rockyou.txt"
        # gets rockyou password list
        os.system("mega-get 'https://mega.nz/file/94MXGYSI#T84go5rgXLg8aG8BUMZoaipJRMaBwjeJWRfiOz7tDjs' '/tmp'")
        os.path.exists(wordlist)
        # test
        self.assertEqual(inlookuptable("tekken5", wordlist), True)
        # tear it down
        os.remove(wordlist)

    def test_inlookuptable_inlist_pass_huge(self):  # this will take a long time
        wordlist = "/tmp/weakpass_3w"
        # getting really big list
        os.system("mega-get 'https://mega.nz/file/F5ElXYTB#og8m6DWQ6jfbnQdvLKFoqTbwyGbmXReH8jfFxW2W5xE' '/tmp'")
        os.system("7z x /tmp/weakpass_3w.7z -o/tmp/ -y")
        os.path.exists(wordlist)
        # test
        self.assertEqual(inlookuptable("silovoe22", wordlist), True)
        # tear it down
        os.remove("/tmp/weakpass_3w.7z")
        os.remove(wordlist)

    def test_inlookuptable_inlist_fail(self):
        wordlist = "/tmp/words.txt"
        # gets a dictonary
        os.system("mega-get 'https://mega.nz/file/tkdH2Iib#aIij6eFNdJA5rmgR8x5NwYxqBpdrHJAaPTfr4uUxKv8' '/tmp'")
        os.path.exists(wordlist)
        # test
        self.assertEqual(inlookuptable("'", wordlist), False)
        # tear it down
        os.remove(wordlist)

    def test_inlookuptable_inlist_fail_huge(self):  # this will take a long time
        wordlist = "/tmp/weakpass_3w"
        # getting really big list
        os.system("mega-get 'https://mega.nz/file/F5ElXYTB#og8m6DWQ6jfbnQdvLKFoqTbwyGbmXReH8jfFxW2W5xE' '/tmp'")
        os.system("7z x /tmp/weakpass_3w.7z -o/tmp/ -y")
        os.path.exists(wordlist)
        # test
        self.assertEqual(inlookuptable("'", wordlist), False)
        # tear it down
        os.remove("/tmp/weakpass_3w.7z")
        os.remove(wordlist)
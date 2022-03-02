import os

from unittest import TestCase

from utils.security.lookup import inlookuptable

class InLookupTable(TestCase):

    def test_inlookuptable_inlist_pass(self):
        wordlist = "/test/repo/words.txt"
        os.path.exists(wordlist)
        # test
        self.assertEqual(inlookuptable("zoom", wordlist), True)


    def test_inlookuptable_inlist_pass_large(self):
        wordlist = "/test/repo/rockyou.txt"
        os.path.exists(wordlist)
        # test
        self.assertEqual(inlookuptable("tekken5", wordlist), True)

    def test_inlookuptable_inlist_pass_huge(self):  # this will take a long time
        wordlist = "/test/repo/weakpass_3w.7z"
        # getting really big list
        os.path.exists(wordlist)
        # test
        self.assertEqual(inlookuptable("silovoe22", wordlist), True)

    def test_inlookuptable_inlist_fail(self):
        wordlist = "/test/repo/words.txt"
        os.path.exists(wordlist)
        # test
        self.assertEqual(inlookuptable("'", wordlist), False)

    def test_inlookuptable_inlist_fail_huge(self):  # this will take a long time
        wordlist = "/test/repo/weakpass_3w.7z"
        # getting really big list
        os.path.exists(wordlist)
        # test
        self.assertEqual(inlookuptable("'", wordlist), False)

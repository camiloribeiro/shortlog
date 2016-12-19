# -*- coding: utf-8 -*-
import unittest
import shortlog
from subprocess import Popen, PIPE


class ShortlogTest(unittest.TestCase):

    expectation = filter(None, list(Popen(["git", "shortlog", "-ns"], stdout=PIPE).communicate())[0].split("\n"))

    def test_format_author_list(self):
        author_list = [[[212], ['Joshua Peek']]]
        self.assertEqual((shortlog.format_author_list(author_list)),  '   212\tJoshua Peek')

    def test_get_all_commits(self):
        self.assertEqual((shortlog.get_shortlog(dry=False)).split("\n")[0], self.expectation[0])
        self.assertEqual(len((shortlog.get_shortlog(dry=False)).split("\n")), len(self.expectation))

    # This test might fail in repositories with several committers duo to a unkown second sorting factor.
    # I have tryed to oder with last commit date, first commit date and name, none worked.
    def test_get_all_commits_each_commit(self):
        counter = 0
        for line in self.expectation:
            self.assertEqual((shortlog.get_shortlog(dry=False)).split("\n")[counter], line.replace("\n", ""))
            counter += 1

if __name__ == '__main__':
    unittest.main()

import unittest
from unittest.mock import patch
import yt_lang

class TestYTCommentLang(unittest.TestCase):
	def setUp(self):
		self.url1 = "https://youtu.be/jNQXAC9IVRw"

	def testLang(self):
		comments = yt_lang.get_comments(self.url1)
		self.assertIsNotNone(comments)

	def testArgs(self):
		args = yt_lang.parse_args([self.url1])
		self.assertTrue(args.parentId == self.url1)

    
if __name__ == '__main__':
	unittest.main()
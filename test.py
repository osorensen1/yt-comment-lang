import unittest
from unittest.mock import patch
import yt_lang

class TestYTCommentLang(unittest.TestCase):
	def setUp(self):
		self.url1 = "jNQXAC9IVRw"

	def testLang(self):
		comments = yt_lang.get_comments(self.url1)
		self.assertIsNotNone(comments)
		self.assertNotEqual(len(comments['items']), 0)

	def testArgs(self):
		args = yt_lang.parse_args([self.url1])
		self.assertTrue(args.videoId == self.url1)

		

    
if __name__ == '__main__':
	unittest.main()
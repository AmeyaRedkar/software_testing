#import unittest package to test post.py
from unittest import TestCase,main  
from post import Post

class PostTest(TestCase): #inherit TestCase from unittest

# things that are to be tested are in function & start function name with test
	def test_create_post(self):

		p=Post("testTitle","testContent") #object of post class

#self.assertEqual("text given","text required") this function will compare both.

		self.assertEqual("testTitle",p.title) 
		self.assertEqual("testContent",p.content)

# main() function will start the process of comparing.

main()

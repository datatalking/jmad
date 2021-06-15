# SOURCE
# FILENAME

from django.test import LiveServerTestCase
from selenium import webdriver


class StudenTestCase(LiveServerTestCase):
	
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicity_wait(2)
	
	def test_student_find_solos(self):
		"""
		Test that a user can search for solos
		:return:
		"""
		self.fail('Incomplete Test')
		# Steve is a jazz student who would like to find more
		# examples of solos so he can improve his own
		# improvisation. He visits the home page of JMAD.
		
		# He knows he's in the right place because he can see
		# the name of the site in the heading.
	
		# He sees the inputs of the search form, including
		# lavels and placeholders.
		
		# He types in the name of his instrument and submits it
		
		# he sees too many search results...
		
		# ... so he adds an artist to his search query and
		# gets a more managable list
		
		# He clicks on a search results
		
		# The solo page has the title, artist, and album for
		# this paticular solo
		
		# He also sees the start time and end time of the solo
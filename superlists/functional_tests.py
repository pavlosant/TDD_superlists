from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self): 
        self.browser= webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        # A new app for TODO Lists has the following homepage
        self.browser.get('http://localhost:8000')

        #The page title and header mention to-do lists
        #assert 'To-Do' in browser.title
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')
        #User is asked to enter a to-do item straight away
        #User types "Buy peacock feathers"

        #When User press enters the page updates and now the page lists 
        #"1.Buy peacock feathers" as an item in a todo list

        #Theres is still a text box inviting for another item 
        #User enters whatever as second item
        #The page updates with BOTH items in list

        #Does the site remember the list?
    
if __name__ =='__main__':
        unittest.main(warnings='ignore')
        


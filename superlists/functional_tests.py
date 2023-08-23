from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        # A new app for TODO Lists has the following homepage
        self.browser.get('http://localhost:8000')

        # The page title and header mention to-do lists
        # assert 'To-Do' in browser.title
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element("tag name", 'h1').text
        self.assertIn('To-Do', header_text)

        # User is asked to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'), 'Enter a to-do item'
        )

        # User types "Buy peacock feathers"
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        # When User press enters the page updates and now the page lists
        # "1.Buy peacock feathers" as an item in a todo list
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )

        # Theres is still a text box inviting for another item
        # User enters whatever as second item
        self.fail("Finish the test!")
        # The page updates with BOTH items in list

        # Does the site remember the list?


if __name__ == '__main__':
    unittest.main(warnings='ignore')

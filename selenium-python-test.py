import unittest
from selenium import webdriver

# Source: https://www.techbeamers.com/selenium-python-test-suite-unittest/

class SearchText(unittest.TestCase):
    def setUp(self):
        # create a new Firefox session
        # self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        # navigate to the application home page
        self.driver.get("http://www.google.com/")

    def test_search_by_text(self):
        # get the search textbox
        self.search_field = self.driver.find_element_by_name("q")

        # enter search keyword and submit
        self.search_field.send_keys("Selenium WebDriver Interview questions")
        self.search_field.submit()

        #get the list of elements which are displayed after the search
        #currently on result page usingfind_elements_by_class_namemethod

        lists = self.driver.find_elements_by_class_name("g")  # changed from r to g
        no=len(lists)
        print(no)
        self.assertEqual(14, len(lists)) # changed 11 to 14

    def tearDown(self):
        # close the browser window
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()   
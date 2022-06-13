from selenium import webdriver
import unittest

class CalculatorTest(unittest.TestCase):

    def setUp(self):
        #create a headless Chrome browser
        op = webdriver.ChromeOptions()
        op.add_argument('headless')

        self.driver = webdriver.Chrome("/Users/nabeel/Documents/selenium/chromedriver73", options=op)

    def test_addition(self):
        self.driver.get("file:///Users/nabeel/Documents/selenium/cal/calculator.html")
        self.driver.find_element_by_name("-234234").click()
        self.driver.find_element_by_name("+").click()
        self.driver.find_element_by_name("345345").click()
        self.driver.find_element_by_name("=").click()
        value = self.driver.find_element_by_id("result").get_attribute("value")
        self.assertEqual('111111', value)

    def test_substraction(self):
        self.driver.get("file:///Users/nabeel/Documents/selenium/cal/calculator.html")
        self.driver.find_element_by_name("234823").click()
        self.driver.find_element_by_name("-").click()
        self.driver.find_element_by_name("-23094823").click()
        self.driver.find_element_by_name("=").click()
        value = self.driver.find_element_by_id("result").get_attribute("value")
        self.assertEqual('-23329646', value)

    def test_division(self):
        self.driver.get("file:///Users/nabeel/Documents/selenium/cal/calculator.html")
        self.driver.find_element_by_name("4000").click()
        self.driver.find_element_by_name("/").click()
        self.driver.find_element_by_name("200").click()
        self.driver.find_element_by_name("=").click()
        value = self.driver.find_element_by_id("result").get_attribute("value")
        self.assertEqual('20', value)

    def test_multiplication(self):
        self.driver.get("file:///Users/nabeel/Documents/selenium/cal/calculator.html")
        self.driver.find_element_by_name("423").click()
        self.driver.find_element_by_name("*").click()
        self.driver.find_element_by_name("525").click()
        self.driver.find_element_by_name("=").click()
        value = self.driver.find_element_by_id("result").get_attribute("value")
        self.assertEqual('222075', value)

    def tearDown(self):
            #close the browser window
            self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)

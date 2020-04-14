import unittest
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By


class MainTests(unittest.TestCase):

    def test_demo_konto(self):
        driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe")
        driver.get('http://automationpractice.com/index.php')
        driver.find_element(By.XPATH, "//a[@class = 'login']").click()
        sleep(1)
        driver.find_element(By.XPATH, "//input[@id = 'email']").send_keys('adrian@o2.pl')
        driver.find_element(By.XPATH, "//input[@id = 'passwd']").send_keys('123456')
        driver.find_element(By.XPATH, "//button[@id = 'SubmitLogin']").click()
        sleep(1)
        title = driver.find_element(By.XPATH, "//a[@class = 'account']").text
        assert 'Adrian Nowak' == title
        print(title)
        driver.quit()

    def test_demo_zakupy(self):
        driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe")
        driver.get('http://automationpractice.com/index.php')
        sleep(0.5)
        driver.find_element(By.XPATH,
                            "//a[@href = 'http://automationpractice.com/index.php?id_product=1&controller=product']").click()
        driver.find_element(By.XPATH, "//button[@class = 'exclusive']").click()
        sleep(1)
        driver.find_element(By.XPATH, "//a[@class = 'btn btn-default button button-medium']").click()
        driver.find_element(By.XPATH, "//a[@class = 'button btn btn-default standard-checkout button-medium']").click()
        driver.find_element(By.XPATH, "//input[@id = 'email']").send_keys("asd@o2.pl")
        driver.find_element(By.XPATH, "//input[@id = 'passwd']").send_keys("123456")
        driver.find_element(By.XPATH, "//button[@id = 'SubmitLogin']").click()
        driver.find_element(By.XPATH, "//button[@class = 'button btn btn-default button-medium']").click()
        driver.find_element(By.XPATH, "//input[@id = 'cgv']").click()
        driver.find_element(By.XPATH,
                            "//button[@class = 'button btn btn-default standard-checkout button-medium']").click()
        driver.find_element(By.XPATH, "//a[@class = 'cheque']").click()
        driver.find_element(By.XPATH, "//button[@type = 'submit']").click()
        driver.find_element(By.XPATH, "//a[@title = 'My Store']").click()
        driver.quit()

    def test_demo_newsletter(self):

            driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe")
            driver.get('http://automationpractice.com/index.php')
            driver.find_element(By.XPATH, "//input[@id = 'newsletter-input']").send_keys("robert@wp.pl")
            driver.find_element(By.XPATH, "//button[@class = 'btn btn-default button button-small']").click()
            title = driver.find_element(By.XPATH, "//p[@class = 'alert alert-success']").text
            assert 'Newsletter : You have successfully subscribed to this newsletter.' == title
            driver.quit()





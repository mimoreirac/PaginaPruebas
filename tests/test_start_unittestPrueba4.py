import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class ClickAndSendKeys(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://mimoreirac.github.io/PaginaPruebas/")

    def testId(self):
        liga = self.driver.find_element(By.XPATH, "//a[contains(text(), 'Pagina 2')]")
        if liga is not None:
            liga.click()

        nombre = self.driver.find_element(By.ID, "Segundo")
        if nombre is not None:
            nombre.send_keys("Martin")

        time.sleep(5)

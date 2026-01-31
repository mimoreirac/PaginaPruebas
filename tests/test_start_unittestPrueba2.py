import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class FindbyIdName(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://mimoreirac.github.io/PaginaPruebas/")

    def testName(self):
        elemento2 = self.driver.find_element(By.NAME, "ultimo")
        if elemento2 is not None:
            print("El elemento by NAME fue encontrado")

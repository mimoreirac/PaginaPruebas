import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class FindbyIdName(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://mimoreirac.github.io/PaginaPruebas/")

    def testIdName(self):
        elemento = self.driver.find_element(By.ID, "noImportante")
        if elemento is not None:
            print("El elemento by ID fue encontrado")

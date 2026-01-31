import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class FindbyIdName(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://mimoreirac.github.io/PaginaPruebas/")

    def testClase(self):
        elemento = self.driver.find_element(By.CLASS_NAME, "rojo")
        if elemento is not None:
            print("El elemento by CLASS_NAME rojo fue encontrado")

    def testLink(self):
        elemento2 = self.driver.find_element(By.LINK_TEXT, "Pagina 2")
        if elemento2 is not None:
            print("El elemento by LINK_TEXT Pagina 2 fue encontrado")

    def testLinkParcial(self):
        elemento2 = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Pagi")
        if elemento2 is not None:
            print("El elemento by PARTIAL_LINK_TEXT Pagi fue encontrado")

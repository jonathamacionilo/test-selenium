from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

class Bot:
    def __init__(self):
        self.driver = None

    def initiate_bot(self):
        try:
            # Inicializa o WebDriver do Firefox usando o GeckoDriverManager
            self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        except Exception as e:
            print(f"Erro ao iniciar o bot: {e}")
    
    def abrir_pagina_youtube(self):
        if self.driver is None:
            self.initiate_bot()
        if self.driver:
            self.driver.get('https://www.youtube.com.br')

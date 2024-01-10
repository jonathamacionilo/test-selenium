from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

class Bot:
    def __init__(self):
        self.driver = None

    def initiate_bot(self):
        try:
            # Enforce headless mode for Streamlit Cloud
            options = Options()
            options.headless = True

            # Use GeckoDriverManager for driver management
            self.driver = webdriver.Firefox(
                service=Service(GeckoDriverManager().install()),
                options=options
            )
        except Exception as e:
            print(f"Erro ao iniciar o bot: {e}\nVerifique a compatibilidade do driver e as configurações do Streamlit Cloud.")

    def abrir_pagina_youtube(self):
        if self.driver is None:
            self.initiate_bot()
        if self.driver:
            self.driver.get('https://www.youtube.com.br')

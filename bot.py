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
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")
            options.add_argument("--disable-features=NetworkService")
            options.add_argument("--window-size=1920x1080")
            options.add_argument("--disable-features=VizDisplayCompositor")
            # Use GeckoDriverManager for driver management
            self.driver = webdriver.Chrome(
                options=get_webdriver_options(), service=get_webdriver_service()
            )
        except Exception as e:
            print(f"Erro ao iniciar o bot: {e}\nVerifique a compatibilidade do driver e as configurações do Streamlit Cloud.")

    def abrir_pagina_youtube(self):
        if self.driver is None:
            self.initiate_bot()
        if self.driver:
            self.driver.get('https://www.youtube.com.br')

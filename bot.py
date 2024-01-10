from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Bot:
    def __init__(self):
        self.driver = None

    def initiate_bot(self):
        try:
            # Configuração do serviço do ChromeDriver
            chrome_service = Service(ChromeDriverManager().install())
            
            # Inicialização do WebDriver do Chrome utilizando o serviço do ChromeDriver
            self.driver = webdriver.Chrome(service=chrome_service)
        except Exception as e:
            print(f"Erro ao iniciar o bot: {e}")
    
    def abrir_pagina_youtube(self):
        if self.driver is None:
            self.initiate_bot()
        self.driver.get('https://www.youtube.com.br')

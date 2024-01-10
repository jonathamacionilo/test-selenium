# arquivo bot.py
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class Bot:
    def __init__(self):
        self.driver = None

    def initiate_bot(self):
        # Especifique o caminho local do chromedriver na raiz do seu projeto
        chromedriver_path = "./chromedriver"
        # Opções do ChromeDriver
        options = webdriver.ChromeOptions()
        
        # Desabilitar o sandbox para a execução na Streamlit Sharing
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        
        # Inicialize o WebDriver do Chrome utilizando o chromedriver local e as opções definidas
        self.driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)
    
    def abrir_pagina_youtube(self):
        if self.driver is None:
            self.initiate_bot()
        self.driver.get('https://www.youtube.com.br')

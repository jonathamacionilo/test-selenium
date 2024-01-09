# arquivo bot.py
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class BotGLPI:
    def __init__(self):
        self.driver = None

    def initiate_bot(self):
        # Especifique o caminho local do chromedriver na raiz do seu projeto
        chromedriver_path = "./chromedriver"
        
        # Inicialize o WebDriver do Chrome utilizando o chromedriver local
        self.driver = webdriver.Chrome(executable_path=chromedriver_path)
    
    def abrir_pagina_youtube(self):
        if self.driver is None:
            self.initiate_bot()
        self.driver.get('https://www.youtube.com.br')

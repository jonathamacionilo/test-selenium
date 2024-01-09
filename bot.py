from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Bot:
    def __init__(self):
        self.driver = None

    def initiate_bot(self):
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )
    
    def acessar_youtube(self):
        if self.driver is None:
            self.initiate_bot()
        self.driver.get('https://youtube.com')
        

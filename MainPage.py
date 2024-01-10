from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
import streamlit as st

def abrir_youtube():
    try:
        options = Options()
        options.add_argument("--headless")
        
        # Inicializa o serviço do GeckoDriver usando o GeckoDriverManager
        service = Service(GeckoDriverManager().install())

        # Inicializa o WebDriver do Firefox com as opções definidas
        driver = webdriver.Firefox(service=service, options=options)
        
        driver.get('https://www.youtube.com/')
        
        st.write("YouTube acessado com sucesso!")
        
        driver.quit()
        
    except Exception as e:
        st.write(f"Não foi possível acessar o YouTube: {e}")

if __name__ == "__main__":
    abrir_youtube()

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
import streamlit as st

def abrir_youtube():
    try:
        options = Options()
        options.add_argument("--headless")
        
        # Defina o caminho do binário do Firefox
        firefox_binary = '/path/to/your/firefox-binary'  # Substitua pelo caminho do seu binário do Firefox

        # Inicializa o serviço do GeckoDriver usando o GeckoDriverManager
        service = Service(GeckoDriverManager().install())

        # Define o binário do Firefox para o WebDriver
        options.binary_location = firefox_binary

        # Inicializa o WebDriver do Firefox com as opções definidas
        driver = webdriver.Firefox(service=service, options=options)
        
        driver.get('https://www.youtube.com/')
        
        st.write("YouTube acessado com sucesso!")
        
        driver.quit()
        
    except Exception as e:
        st.write(f"Não foi possível acessar o YouTube: {e}")

if __name__ == "__main__":
    abrir_youtube()

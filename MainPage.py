import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def abrir_youtube():
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get('https://www.youtube.com')
        st.success("YouTube foi acessado com sucesso!")
    except Exception as e:
        st.error(f"Ocorreu um erro ao acessar o YouTube: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    st.title('Acesso ao YouTube com Selenium')
    st.write("Clique no botão abaixo para acessar o YouTube.")

    if st.button('Acessar YouTube'):
        abrir_youtube()

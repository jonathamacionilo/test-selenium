import streamlit as st
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options

def verificar_acesso_youtube():
    options = Options()
    options.headless = True

    driver = None
    try:
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
        driver.get('https://www.youtube.com')
        return True
    except Exception as e:
        st.error(f"Não foi possível acessar o YouTube: {e}")
        return False
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    st.title('Verificar Acesso ao YouTube')
    st.write("Clique no botão abaixo para verificar se é possível acessar o YouTube.")

    if st.button('Verificar Acesso'):
        acesso = verificar_acesso_youtube()
        if acesso:
            st.success("Foi possível acessar o YouTube!")
        else:
            st.error("Não foi possível acessar o YouTube.")

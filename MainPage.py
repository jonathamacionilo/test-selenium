import streamlit as st
from streamlit_selenium import st_selenium

def abrir_youtube():
    try:
        # Inicia a sessão do navegador
        with st_selenium() as browser:
            # Abre o site do YouTube
            browser.get("https://www.youtube.com/")
            st.write("YouTube acessado com sucesso!")
            
    except Exception as e:
        st.write(f"Não foi possível acessar o YouTube: {e}")

if __name__ == "__main__":
    abrir_youtube()

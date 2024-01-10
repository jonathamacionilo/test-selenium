import streamlit as st
from bot import Bot

chamada = Bot()

st.title('Teste Webdrive, Selenium')

botao = st.button(
    'YOUTUBE',
    type='primary'
)
if botao:
    chamada.abrir_pagina_youtube()
    

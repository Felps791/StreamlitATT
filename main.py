import streamlit as st

def calcIMC():
    st.title("Calculadora de IMC")
    st.latex(r"\text{IMC} = \frac{\text{Peso}}{\text{Altura}^2}")
    st.image("/workspaces/StreamlitATT/IMCTable.png")


st.title("Atividade 1 - Streamlit")

calcIMC()
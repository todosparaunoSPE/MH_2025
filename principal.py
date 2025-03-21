# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 10:16:36 2025

@author: jperezr
"""

import streamlit as st

# Título de la aplicación
st.title("CAP de las AFORE y Nuevas Ubicaciones de CAP para PENSIONISSSTE")

# Sidebar con información
st.sidebar.title("Información")
st.sidebar.write("Nombre: Javier Horacio Pérez Ricárdez")

# Botón para descargar el archivo en el sidebar
with open("enoe2025_02.pdf", "rb") as file:
    btn = st.sidebar.download_button(
        label="Descargar ENOE 2025-02",
        data=file,
        file_name="enoe2025_02.pdf",
        mime="application/pdf"
    )

# Estilo CSS para la marca de agua en la parte inferior izquierda
st.markdown(
    """
    <style>
    .watermark {
        position: fixed;
        bottom: 10px;  # Coloca la marca de agua en la parte inferior
        left: 10px;    # Alinea la marca de agua a la izquierda
        opacity: 0.6;
        font-size: 18px;
        font-weight: bold;
        color: gray;
        z-index: 1000;  # Asegura que la marca de agua esté por encima de otros elementos
        text-align: left;  # Alinea el texto a la izquierda
        width: auto;  # Evita que el contenedor ocupe todo el ancho
        white-space: nowrap;  # Evita que el texto se divida en varias líneas
    }
    </style>
    <div class="watermark">Javier Horacio Pérez Ricárdez</div>
    """,
    unsafe_allow_html=True
)

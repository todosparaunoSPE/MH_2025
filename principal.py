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

# Estilo CSS para la marca de agua en la parte superior izquierda
st.markdown(
    """
    <style>
    .watermark {
        position: fixed;
        top: 10px;  # Cambia 'bottom' por 'top'
        left: 10px;  # Cambia 'right' por 'left'
        opacity: 0.6;
        font-size: 18px;
        font-weight: bold;
        color: gray;
    }
    </style>
    <div class="watermark">Javier Horacio Pérez Ricárdez</div>
    """,
    unsafe_allow_html=True
)

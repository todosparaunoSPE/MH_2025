# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 12:29:47 2025

@author: jperezr
"""

import streamlit as st
import pandas as pd
import os

# Mostrar el nombre del creador en la barra lateral
st.sidebar.markdown("### Creado por: **Javier Horacio Pérez Ricárdez**")   

st.sidebar.markdown("Marzo del 2025")  

# Crear la carpeta 'mapas1' si no existe
if not os.path.exists('mapas1'):
    os.makedirs('mapas1')

# Cargar datos automáticamente
@st.cache_data
def cargar_datos():
    return pd.read_csv('PEA_distribuida.csv')

# Cargar datos en un DataFrame
df = cargar_datos()

# Agregar sección de Ayuda en la barra lateral
st.sidebar.title("Ayuda")
st.sidebar.info(
    "Esta aplicación permite visualizar la distribución de la PEA por AFORE en los diferentes estados de México. "
    "Selecciona un estado en el menú desplegable para ver los datos correspondientes. "
    "También puedes acceder a enlaces externos con más información específica de cada estado."
)

# Título de la app
st.title("Distribución de la PEA por AFORE")

# Selección de estado
estado_seleccionado = st.selectbox("Selecciona un Estado", df["Estado"].unique())

# Filtrar datos según el estado seleccionado
df_filtrado = df[df["Estado"] == estado_seleccionado]

# Mostrar el DataFrame filtrado
st.write("### Datos filtrados:")
st.dataframe(df_filtrado)

# Diccionario de enlaces por estado
enlaces_estados = {
    "Aguascalientes": "https://todosparaunospe.github.io/1_SH/",
    "Baja California": "https://todosparaunospe.github.io/2_SH/",
    "Baja California Sur": "https://todosparaunospe.github.io/3_SH/",
    "Campeche": "https://todosparaunospe.github.io/4_SH/",
    "CDMX": "https://todosparaunospe.github.io/5_SH/",
    "Chiapas": "https://todosparaunospe.github.io/6_SH/",
    "Chihuahua": "https://todosparaunospe.github.io/7_SH/",
    "Coahuila": "https://todosparaunospe.github.io/8_SH/",
    "Colima": "https://todosparaunospe.github.io/9_SH/",
    "Durango": "https://todosparaunospe.github.io/10_SH/",
    "Estado de México": "https://todosparaunospe.github.io/11_SH/",
    "Guanajuato": "https://todosparaunospe.github.io/12_SH/",
    "Guerrero": "https://todosparaunospe.github.io/13_SH/",
    "Hidalgo": "https://todosparaunospe.github.io/14_SH/",
    "Jalisco": "https://todosparaunospe.github.io/15_SH/",
    "Michoacán": "https://todosparaunospe.github.io/16_SH/",
    "Morelos": "https://todosparaunospe.github.io/17_SH/",
    "Nayarit": "https://todosparaunospe.github.io/18_SN/",
    "Nuevo León": "https://todosparaunospe.github.io/19_SN/",
    "Oaxaca": "https://todosparaunospe.github.io/20_SH/",
    "Puebla": "https://todosparaunospe.github.io/21_SH/",
    "Querétaro": "https://todosparaunospe.github.io/22_SH/",
    "Quintana Roo": "https://todosparaunospe.github.io/23_SH/",
    "San Luis Potosí": "https://todosparaunospe.github.io/24_SH/",
    "Sinaloa": "https://todosparaunospe.github.io/25_SH/",
    "Sonora": "https://todosparaunospe.github.io/26_SH/",
    "Tabasco": "https://todosparaunospe.github.io/27_SH/",
    "Tamaulipas": "https://todosparaunospe.github.io/28_SH/",
    "Tlaxcala": "https://todosparaunospe.github.io/29_SH/",
    "Veracruz": "https://todosparaunospe.github.io/30_SH/",
    "Yucatán": "https://todosparaunospe.github.io/31_SH/",
    "Zacatecas": "https://todosparaunospe.github.io/32_SH/"
}

# Mostrar enlace según el estado seleccionado
if estado_seleccionado in enlaces_estados:
    st.write(f"### [Ver más información sobre {estado_seleccionado}]({enlaces_estados[estado_seleccionado]})")



# Estilo CSS para la marca de agua
st.markdown(
    """
    <style>
    .watermark {
        position: fixed;
        bottom: 10px;
        right: 10px;
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

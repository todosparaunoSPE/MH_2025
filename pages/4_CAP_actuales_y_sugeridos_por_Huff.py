# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 09:03:01 2025

@author: jperezr
"""

import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
import os


# Mostrar el nombre del creador en la barra lateral
st.sidebar.markdown("### Creado por: **Javier Horacio Pérez Ricárdez**")   

st.sidebar.markdown("Marzo del 2025")  

# Crear carpeta si no existe
output_folder = "mapas_unidos"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Cargar datos automáticamente
@st.cache_data
def cargar_datos():
    return pd.read_csv("CAP_actuales_y_Huff.csv")

df = cargar_datos()

# Sidebar - Sección de Ayuda
st.sidebar.title("Ayuda")
st.sidebar.info("""
Esta aplicación permite visualizar las AFORE disponibles en cada estado de México.

**¿Cómo usar la aplicación?**
1. Selecciona un estado en el desplegable.
2. Se mostrarán los datos filtrados para ese estado.
3. Se proporcionará un enlace con información adicional del estado seleccionado.
""")

# Mostrar datos originales
st.title("Visualización de AFORE por Estado")
st.write("Datos cargados:")
st.dataframe(df)

# Selección del Estado
estado_seleccionado = st.selectbox("Selecciona un Estado:", df["Estado"].unique())

# Filtrar datos por Estado
df_filtrado = df[df["Estado"] == estado_seleccionado]

# Mostrar datos filtrados
st.write(f"Datos filtrados para el Estado: {estado_seleccionado}")
st.dataframe(df_filtrado)

# Mostrar enlace correspondiente
enlaces = {
    "Aguascalientes": "https://todosparaunospe.github.io/1_CH/",
    "Baja California": "https://todosparaunospe.github.io/2_CH/",
    "Baja California Sur": "https://todosparaunospe.github.io/3_CH/",
    "Campeche": "https://todosparaunospe.github.io/4_CH/",
    "CDMX": "https://todosparaunospe.github.io/5_CH/",
    "Chiapas": "https://todosparaunospe.github.io/6_CH/",
    "Chihuahua": "https://todosparaunospe.github.io/7_CH/",
    "Coahuila": "https://todosparaunospe.github.io/8_CH/",
    "Colima": "https://todosparaunospe.github.io/9_CH/",
    "Durango": "https://todosparaunospe.github.io/10_CH/",
    "Estado de México": "https://todosparaunospe.github.io/11_CH/",
    "Guanajuato": "https://todosparaunospe.github.io/12_CH/",
    "Guerrero": "https://todosparaunospe.github.io/13_CH/",
    "Hidalgo": "https://todosparaunospe.github.io/14_CH/",
    "Jalisco": "https://todosparaunospe.github.io/15_CH/",
    "Michoacán": "https://todosparaunospe.github.io/16_CH/",
    "Morelos": "https://todosparaunospe.github.io/17_CH/",
    "Nayarit": "https://todosparaunospe.github.io/18_CH/",
    "Nuevo León": "https://todosparaunospe.github.io/19_CH/",
    "Oaxaca": "https://todosparaunospe.github.io/20_CH/",
    "Puebla": "https://todosparaunospe.github.io/21_CH/",
    "Querétaro": "https://todosparaunospe.github.io/22_CH/",
    "Quintana Roo": "https://todosparaunospe.github.io/23_CH/",
    "San Luis Potosí": "https://todosparaunospe.github.io/24_CH/",
    "Sinaloa": "https://todosparaunospe.github.io/25_CH/",
    "Sonora": "https://todosparaunospe.github.io/26_CH/",
    "Tabasco": "https://todosparaunospe.github.io/27_CH/",
    "Tamaulipas": "https://todosparaunospe.github.io/28_CH/",
    "Tlaxcala": "https://todosparaunospe.github.io/29_CH/",
    "Veracruz": "https://todosparaunospe.github.io/30_CH/",
    "Yucatán": "https://todosparaunospe.github.io/31_CH/",
    "Zacatecas": "https://todosparaunospe.github.io/32_CH/"
}

if estado_seleccionado in enlaces:
    st.write(f"Más información sobre {estado_seleccionado}: [Haz clic aquí]({enlaces[estado_seleccionado]})")

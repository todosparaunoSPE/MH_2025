# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 09:32:24 2025

@author: jperezr
"""

import streamlit as st
import pandas as pd
import folium
import os
from streamlit_folium import folium_static


# Mostrar el nombre del creador en la barra lateral
st.sidebar.markdown("### Creado por: **Javier Horacio Pérez Ricárdez**")   

st.sidebar.markdown("Marzo del 2025")  


# Crear carpeta si no existe
output_folder = "mapas_unidos"
os.makedirs(output_folder, exist_ok=True)

# Cargar datos automáticamente
@st.cache_data
def cargar_datos():
    return pd.read_csv("nuevas_ubicaciones.csv")

df = cargar_datos()

# Agregar sección de Ayuda en la barra lateral
st.sidebar.title("Ayuda")
st.sidebar.write("Esta aplicación carga automáticamente un archivo CSV con nuevas ubicaciones de AFORE y muestra los datos en un DataFrame. También genera un mapa con los puntos de ubicación de las AFORE, asignando colores específicos a los CAP actuales y sugeridos.")

# Mostrar datos originales
st.title("Mapa de Nuevas Ubicaciones de AFORE")
st.write("Datos cargados:")
st.dataframe(df)

# Crear mapa
st.write("Mapa de AFORE con nuevas ubicaciones")
st.write("[CAP actuales de PENSIONISSSTE y CAP sugeridos por el modelo de Huff](https://todosparaunospe.github.io/33_NH/)")
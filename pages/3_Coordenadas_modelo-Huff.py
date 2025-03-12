# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 14:10:59 2025

@author: jperezr
"""

import streamlit as st
import pandas as pd
import numpy as np


# Mostrar el nombre del creador en la barra lateral
st.sidebar.markdown("### Creado por: **Javier Horacio Pérez Ricárdez**")   

st.sidebar.markdown("Marzo del 2025")  


def huff_model(data, estado_seleccionado):
    """
    Implementa el modelo de Huff para calcular una nueva ubicación de un CAP
    basado en la latitud, longitud y atracción de las AFORE.
    """
    estado_data = data[data['Estado'] == estado_seleccionado]
    
    if estado_data.empty:
        return None, None, None
    
    # Calcular la probabilidad de visita basada en la atracción
    estado_data['probabilidad'] = estado_data['atracción'] / estado_data['atracción'].sum()
    
    # Calcular número de visitantes esperados en cada CAP
    estado_data['visitantes_estimados'] = estado_data['probabilidad'] * estado_data['PEA']
    
    # Aplicamos una media ponderada según la atracción de cada ubicación existente
    latitud_nueva = np.average(estado_data['latitud'], weights=estado_data['atracción'])
    longitud_nueva = np.average(estado_data['longitud'], weights=estado_data['atracción'])
    
    return estado_data, latitud_nueva, longitud_nueva

# Configurar la aplicación Streamlit
st.title("Modelo de Huff para Centros de Atención al Público (CAP)")

# Sidebar con sección de ayuda
st.sidebar.title("Ayuda")
st.sidebar.info(
    "**Descripción de la Aplicación:**\n"
    "Esta aplicación utiliza el Modelo de Huff para determinar la mejor ubicación para un nuevo Centro de Atención al Público (CAP) de AFORE PENSIONISSSTE.\n\n"
    "**Cálculos Realizados:**\n"
    "- Se carga un archivo CSV con información de los CAP existentes, incluyendo su latitud, longitud, atracción y la PEA del estado.\n"
    "- Se calcula la probabilidad de que una persona visite cada CAP basado en su nivel de atracción.\n"
    "- Se estima el número de visitantes esperados en cada CAP utilizando la PEA del estado.\n"
    "- Se calcula la ubicación óptima del nuevo CAP mediante una media ponderada de las coordenadas de los CAP existentes según su atracción.\n\n"
    "**Resultados:**\n"
    "- Se muestra un DataFrame con los CAP actuales, su nivel de atracción, probabilidades de visita y visitantes estimados.\n"
    "- Se sugiere la latitud y longitud óptima para el nuevo CAP basado en los cálculos anteriores."
)

# Botón para descargar el manual de la aplicación
with open("Modelo_de_Huff.pdf", "rb") as file:
    btn = st.sidebar.download_button(
        label="📥 Descargar Manual",
        data=file,
        file_name="Modelo_de_Huff.pdf",
        mime="application/pdf"
    )

# Cargar el archivo CSV automáticamente
archivo_csv = "dataset_HUFF.csv"
data = pd.read_csv(archivo_csv)

# Mostrar los datos en un DataFrame
st.subheader("Datos del archivo CSV")
st.dataframe(data)

# Selectbox para elegir el Estado
todos_estados = data['Estado'].unique()
estado_seleccionado = st.selectbox("Seleccione un Estado:", todos_estados)

# Aplicar el modelo de Huff
if estado_seleccionado:
    estado_filtrado, latitud_nueva, longitud_nueva = huff_model(data, estado_seleccionado)
    
    if estado_filtrado is not None:
        st.subheader("Resultados del modelo de Huff")
        st.dataframe(estado_filtrado)
        
        # Crear un nuevo DataFrame con la ubicación sugerida del nuevo CAP
        resultado_df = pd.DataFrame({
            'Estado': [estado_seleccionado],
            'Latitud nueva': [latitud_nueva],
            'Longitud nueva': [longitud_nueva]
        })
        
        st.subheader("Ubicación propuesta para el nuevo CAP")
        st.dataframe(resultado_df)
    else:
        st.warning("No hay datos suficientes para calcular una nueva ubicación para este estado.")



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

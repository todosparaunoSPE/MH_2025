# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 08:48:07 2025

@author: jperezr
"""

import pandas as pd
import streamlit as st
import plotly.express as px

# Mostrar el nombre del creador en la barra lateral
st.sidebar.markdown("### Creado por: **Javier Horacio Pérez Ricárdez**")   

st.sidebar.markdown("Marzo del 2025")  


# Cargar datos de los CAPs (AFOREs) y los estados
@st.cache_data
def cargar_datos():
    df = pd.read_csv('data.csv')  # Asegúrate de tener el archivo CSV con los datos correctos
    
    # Limpiar la columna 'PEA' (eliminar comas y convertir a número)
    df['PEA'] = df['PEA'].replace({',': ''}, regex=True).astype(float)
    
    return df

# Interfaz de Streamlit
st.title('Datos originales y PEA dividida entre total de CAPs de las AFORE en cada entidad federativa')

# Sección de Ayuda en la barra lateral
st.sidebar.title("Ayuda")
st.sidebar.info(
    "**Descripción de la Aplicación:**\n"
    "Esta aplicación permite visualizar la distribución de la Población Económicamente Activa (PEA) en relación con los Centros de Atención al Público (CAP) de las AFORE en cada estado.\n\n"
    "**Características:**\n"
    "- Muestra los datos originales del archivo CSV.\n"
    "- Permite seleccionar un estado para analizar la PEA total.\n"
    "- Calcula la distribución de la PEA entre los CAPs de cada AFORE.\n"
    "- Presenta un gráfico con el número de CAPs por AFORE en la entidad seleccionada."
)

# Cargar datos de los CAPs y los estados
df = cargar_datos()

# Mostrar los datos originales del archivo CSV
st.write("Datos originales del archivo data.csv:")
st.dataframe(df)

# Selección de estado
estado_seleccionado = st.selectbox('Selecciona un estado', df['Estado'].unique())

# Obtener la PEA total del estado seleccionado
pea_estado = df[df['Estado'] == estado_seleccionado]['PEA'].iloc[0]

# Mostrar PEA total del estado seleccionado con separador de miles
st.write(f"PEA total del estado de {estado_seleccionado}: {pea_estado:,.0f}")

# Filtrar datos de los CAPs correspondientes a ese estado
cap_estado = df[df['Estado'] == estado_seleccionado].copy()

# Contar el número total de CAPs en el estado seleccionado
total_caps_estado = len(cap_estado)

# Asignar 1 a cada CAP (cada CAP se contabiliza como 1)
cap_estado['CAP_count'] = 1

# Calcular la PEA asignada dividiendo la PEA total entre el número de CAPs
pea_asignada_por_cap = pea_estado / total_caps_estado
cap_estado['PEA_asignada'] = pea_asignada_por_cap

# Aplicar formato con separador de miles y 4 decimales
cap_estado['PEA_asignada'] = cap_estado['PEA_asignada'].map(lambda x: f"{x:,.4f}")

# Reorganizar las columnas en el DataFrame
columnas_ordenadas = ['Nombre (AFORE)', 'latitud', 'longitud', 'atracción', 
                      'CAP_count', 'PEA_asignada']
st.write("Distribución de la PEA entre los CAPs:")
st.dataframe(cap_estado[columnas_ordenadas])

# Mostrar el valor único de PEA asignada con formato correcto
st.write(f"**PEA asignada = {pea_asignada_por_cap:,.4f}**")

# Contar el número de CAPs por AFORE
cap_por_afore = cap_estado['Nombre (AFORE)'].value_counts().reset_index()
cap_por_afore.columns = ['Nombre (AFORE)', 'Número de CAP']

# Mostrar gráfico de número de CAPs por AFORE
fig = px.bar(cap_por_afore, x='Nombre (AFORE)', y='Número de CAP', 
             title="Número de CAP por AFORE", 
             labels={'Número de CAP': 'Cantidad de CAP', 'Nombre (AFORE)': 'AFORE'},
             color='Nombre (AFORE)')
st.plotly_chart(fig)



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

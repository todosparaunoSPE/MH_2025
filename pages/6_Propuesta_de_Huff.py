# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 09:13:49 2025

@author: jperezr
"""

import streamlit as st
import pandas as pd

# Título principal
st.title("Propuesta de ubicación de nuevos CAP en las 32 entidades federativas")

# Sección de Ayuda en la barra lateral
st.sidebar.title("ℹ️ Ayuda")
st.sidebar.write("""
Este aplicativo carga automáticamente el archivo **propuesta_de_Huff.csv**  
y muestra su contenido en una tabla interactiva.  

### ¿Cómo funciona?
1. **Carga automática del archivo** CSV.
2. **Muestra los datos completos** en un DataFrame de Streamlit.
3. **Filtro por Estado:** Puedes seleccionar una entidad para ver solo sus datos.
4. **Si el archivo no se encuentra**, se muestra un mensaje de error.

📌 **Desarrollado por:** *Javier Horacio Pérez Ricárdez*
""")

# Cargar automáticamente el archivo CSV
csv_file = "propuesta_de_Huff.csv"

try:
    df = pd.read_csv(csv_file)
    
    # Mostrar DataFrame sin filtrar inicialmente
    st.dataframe(df)

    # Verificar si la columna de estados existe
    estado_column = "Estado"  # Asegúrate de que el nombre de la columna es correcto
    if estado_column in df.columns:
        # Lista de estados únicos
        estados = df[estado_column].unique()
        estados = sorted(estados)  # Ordenar alfabéticamente

        # Crear filtro debajo del DataFrame
        estado_seleccionado = st.selectbox("Selecciona un Estado para filtrar:", ["Todos"] + list(estados))

        # Filtrar datos
        if estado_seleccionado != "Todos":
            df = df[df[estado_column] == estado_seleccionado]
            st.dataframe(df)  # Mostrar DataFrame filtrado

except FileNotFoundError:
    st.error(f"❌ El archivo '{csv_file}' no se encontró. Asegúrate de que está en el mismo directorio que este script.")
except Exception as e:
    st.error(f"⚠️ Ocurrió un error al cargar el archivo: {e}")



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



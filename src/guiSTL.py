# import libraries
import streamlit as st
from main import *
import plotly.graph_objects as go
import os
from PIL import Image


# Folder picker button
st.set_page_config(layout="wide")

with st.sidebar:
   st.title('Make List of Files inside folder')
   imageName = 'DALL·E 2023-11-16 12.46.23 - immagine rettangolare di una città del futuro con la digital art. colori chiari.png'
   #isertImage(imageName, width = 280)


   # Utilizza st.markdown per inserire i link
   st.markdown("## Contacts")
   st.write("Name: Domenico")
   st.write("Surname: Gaudioso")
   st.write("📧 dome.gaudioso@gmail.com")
   st.markdown("📱 [LinkedIn]({'https://www.linkedin.com/in/il_tuo_profilo_linkedin'})", unsafe_allow_html=True)
   st.markdown("💻 [GitHub]({'https://github.com/DomenicoGaudioso'})", unsafe_allow_html=True)

   st.markdown("## About")
   # Link di Streamlit
   st.markdown(f"[Streamlit]({'https://www.streamlit.io/'})", unsafe_allow_html=True)
   # Link di SciPy
   st.markdown(f"[SciPy]({'https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.differential_evolution.html'})", unsafe_allow_html=True)
   # Link di Sobol Sequences (sobol_seq su PyPI)
   st.markdown(f"[SALib]({'https://salib.readthedocs.io/en/latest/'})", unsafe_allow_html=True)


st.write('Please insert path folder:')
dirname = st.text_input('Path Folder', '\\')

#if clicked:
dirname = os.path.normpath(dirname)

data, folderName = openFolder(dirname)
st.title('Make List of Files inside folder')

st.write('Please insert path folder:')
dirname = st.text_input('Path Folder', '\\')
#if clicked:
dirname = os.path.normpath(dirname)

data, folderName = openFolder(dirname)

option = st.selectbox(
    'Chose the dataframe',
    folderName)

index = folderName.index( option )

st.dataframe(data[index], column_config={
        "URL": st.column_config.LinkColumn("URL")
    },
    hide_index=False,)

if st.button('write excel file'):
    createExcelfromMultipleDataFrame(data, folderName, dirname)


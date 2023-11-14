# import libraries
import streamlit as st
from main import *



# Folder picker button
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


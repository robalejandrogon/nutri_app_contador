from pandas.core.frame import DataFrame
import streamlit as st
import pandas as pd
import base64
import numpy as np
from datetime import date
import SessionState
import datetime
from datetime import timedelta
import os
#import beepy as beep
from github import Github
import requests
import io
from io import BytesIO
#from streamlit_metrics import metric, metric_row

if 'desayuno' not in st.session_state:
    st.session_state['desayuno']=0
if 'snack' not in st.session_state:
    st.session_state['snack']=0
if 'merienda' not in st.session_state:
    st.session_state['merienda']=0
if 'cena' not in st.session_state:
    st.session_state['cena']=0
if 'pollo_normal' not in st.session_state:
    st.session_state['pollo_normal']=0
if 'pollo_sin_sal' not in st.session_state:
    st.session_state['pollo_sin_sal']=0
if 'pescado_normal' not in st.session_state:
    st.session_state['pescado_normal']=0
if 'pescado_sin_sal' not in st.session_state:
    st.session_state['pescado_sin_sal']=0
if 'salmon_normal' not in st.session_state:
    st.session_state['salmon_normal']=0
if 'salmon_sin_sal' not in st.session_state:
    st.session_state['salmon_sin_sal']=0
if 'camarones_normal' not in st.session_state:
    st.session_state['camarones_normal']=0
if 'camarones_sin_sal' not in st.session_state:
    st.session_state['camarones_sin_sal']=0
if 'atunes_normal' not in st.session_state:
    st.session_state['atunes_normal']=0
if 'atunes_sin_sal' not in st.session_state:
    st.session_state['atunes_sin_sal']=0
if 'e_buffalo' not in st.session_state:
    st.session_state['e_buffalo']=0
if 'e_carnes_frias' not in st.session_state:
    st.session_state['e_carnes_frias']=0
if 'd_liz' not in st.session_state:
    st.session_state['d_liz']=0
if 'e_cesar' not in st.session_state:
    st.session_state['e_cesar']=0
if 'h_normal' not in st.session_state:
    st.session_state['h_normal']=0
if 'h_chilaca' not in st.session_state:
    st.session_state['h_chilaca']=0
if 'h_champ' not in st.session_state:
    st.session_state['h_champ']=0
if 'h_haw' not in st.session_state:
    st.session_state['h_haw']=0
if 'platillos_normales' not in st.session_state:
    st.session_state['platillos_normales']=0
if 'platillos_sin_sal' not in st.session_state:
    st.session_state['platillos_sin_sal']=0
if 'ensaladas' not in st.session_state:
    st.session_state['ensaladas']=0
if 'hamburguesas' not in st.session_state:
    st.session_state['hamburguesas']=0
if 'platillos_totales' not in st.session_state:
    st.session_state['platillos_totales']=0

st.title('Contador')
today = date.today()
#commented the next 2 lines 
#file1 = open('myfile.txt', 'r')
#lines = file1.readlines()

url = "https://raw.githubusercontent.com/robalejandrogon/files/main/myfile.txt" # Make sure the url is the raw version of the file on GitHub
download = requests.get(url).content
lines = pd.read_csv(io.StringIO(download.decode('utf-8')),header=None)[0].tolist()
print(lines)
st.sidebar.markdown(today)
actualizar = st.sidebar.button('Actualizar')

st.sidebar.metric("Platillos totales",str(lines[26]),int(lines[26])-st.session_state['platillos_totales'])
with st.sidebar.expander("Desglose"):
    st.metric("Ensaladas",str(lines[22]),int(lines[22])-st.session_state['ensaladas'])
    st.metric("Hamburguesas",str(lines[23]),int(lines[23])-st.session_state['hamburguesas'])
    st.metric("Platillos normales",str(lines[24]),int(lines[24])-st.session_state['platillos_normales'])
    st.metric("Platillos sin sal",str(lines[25]),int(lines[25])-st.session_state['platillos_sin_sal'])

col1, col2, col3, col4,col5 = st.columns(5)
col1.subheader('Tiempos')
col1.write(' ')
col1.metric("Desayuno",str(lines[18]),int(lines[18])-st.session_state['desayuno'])
col1.metric("Snack",str(lines[19]),int(lines[19])-st.session_state['snack'])
col1.metric("Merienda",str(lines[20]),int(lines[20])-st.session_state['merienda'])
col1.metric("Cena",str(lines[21]),int(lines[21])-st.session_state['cena'])
col2.subheader('Ensaladas')
col2.metric("E. Buffalo",str(lines[10]),int(lines[10])-st.session_state['e_buffalo'])
col2.metric("E. Carnes frias",str(lines[11]),int(lines[11])-st.session_state['e_carnes_frias'])
col2.metric("D. liz",str(lines[12]),int(lines[12])-st.session_state['d_liz'])
col2.metric("E. Cesar",str(lines[13]),int(lines[13])-st.session_state['e_cesar'])
col3.subheader('Hamb.')
col3.metric("H Normal",str(lines[14]),int(lines[14])-st.session_state['h_normal'])
col3.metric("H Chilaca",str(lines[15]),int(lines[15])-st.session_state['h_chilaca'])
col3.metric("H Champ",str(lines[16]),int(lines[16])-st.session_state['h_champ'])
col3.metric("H Haw",str(lines[17]),int(lines[17])-st.session_state['h_haw'])
col4.subheader('Platillos Normal')
col4.metric("Pollo normal",str(lines[0]),int(lines[0])-st.session_state['pollo_normal'])
col4.metric("Pescado normal",str(lines[3]),int(lines[3])-st.session_state['pescado_normal'])
col4.metric("Salmón normal",str(lines[5]),int(lines[5])-st.session_state['salmon_normal'])
col4.metric("Camarones normal",str(lines[7]),int(lines[7])-st.session_state['camarones_normal'])
col4.metric("Atunes normal",str(lines[9]),int(lines[9])-st.session_state['atunes_normal'])
col5.subheader('Platillos sin sal')
col5.metric("Pollo sin sal",str(lines[1]),int(lines[1])-st.session_state['pollo_sin_sal'])
col5.metric("Pescado sin sal",str(lines[2]),int(lines[2])-st.session_state['pescado_sin_sal'])
col5.metric("Salmón sin sal",str(lines[4]),int(lines[4])-st.session_state['salmon_sin_sal'])
col5.metric("Camarones sin sal",str(lines[6]),int(lines[6])-st.session_state['camarones_sin_sal'])
col5.metric("Atunes sin sal",str(lines[8]),int(lines[8])-st.session_state['atunes_sin_sal'])


st.session_state['desayuno'] = int(lines[18])
st.session_state['snack'] = int(lines[19])
st.session_state['merienda'] = int(lines[20])
st.session_state['cena'] = int(lines[21])
st.session_state['e_buffalo'] = int(lines[10])
st.session_state['e_carnes_frias'] = int(lines[11])
st.session_state['d_liz'] = int(lines[12])
st.session_state['e_cesar'] = int(lines[13])
st.session_state['h_normal'] = int(lines[14])
st.session_state['h_chilaca'] = int(lines[15])
st.session_state['h_champ'] = int(lines[16])
st.session_state['h_haw'] = int(lines[17])
st.session_state['platillos_normales'] = int(lines[24])
st.session_state['platillos_sin_sal'] = int(lines[25])
st.session_state['ensaladas'] = int(lines[23])
st.session_state['hamburguesas'] = int(lines[22])
st.session_state['platillos_totales'] = int(lines[26])
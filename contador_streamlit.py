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
import streamlit.components.v1 as components
import requests
import io
from io import BytesIO
#from streamlit_metrics import metric, metric_row
from streamlit_autorefresh import st_autorefresh
from urllib.request import urlopen
import urllib
import mysql.connector

count = st_autorefresh(interval=4000,key="fizzbuzzcounter")

mydb = mysql.connector.connect(
  host="sql555.main-hosting.eu ",
  user="u591727659_robalejandro",
  password="RobalejandroTest1234",
  database="u591727659_test")

sql="""SELECT 
              platillos_pollo_normal, 
              platillos_pollo_sin_sal, 
              pescado_sin_sal, 
              pescado_normal, 
              salmon_sin_sal, 
              salmon_normal, 
              camarones_sin_sal, 
              camarones_normal, 
              atun_sin_sal, 
              atun_normal, 
              e_buffalo, 
              e_carnes_frias, 
              d_liz, 
              e_cesar, 
              h_normal, 
              h_chilaca, 
              h_champ, 
              h_haw, 
              desayuno, 
              snack, 
              merienda, 
              cena, 
              ensaladas, 
              hamburguesas, 
              platillos_normales, 
              platillos_sin_sal, 
              platillos_totales FROM pedidos WHERE id_pedido = 0 """
mycursor = mydb.cursor()
mycursor.execute(sql)
myresult = mycursor.fetchall()
print(f'result: {myresult}')
h_list=[]
for index,x in enumerate(myresult[0]):
  h_list.append(x)
mycursor.close()
mydb.close()

print(f'h_list len :{len(h_list)}')

if 'lista_pedido' not in st.session_state:
    st.session_state['lista_pedido']=[]
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

if h_list == st.session_state['lista_pedido']:
    print('No ha habido cambios')
else:
    components.html(
    """
        <audio controls autoplay>
            <source src="https://rgzzapps.com/bell.wav" autoplay type="audio/wav">
        </audio>
    """,
    )
    print('Lista ha cambiado')

st.title('Contador')
today = date.today()

st.sidebar.markdown(today)
actualizar = st.sidebar.button('Actualizar')

st.sidebar.metric("Platillos totales",str(h_list[26]),int(h_list[26])-st.session_state['platillos_totales'])
with st.sidebar.expander("Desglose"):
    st.metric("Ensaladas",str(h_list[22]),int(h_list[22])-st.session_state['ensaladas'])
    st.metric("Hamburguesas",str(h_list[23]),int(h_list[23])-st.session_state['hamburguesas'])
    st.metric("Platillos normales",str(h_list[24]),int(h_list[24])-st.session_state['platillos_normales'])
    st.metric("Platillos sin sal",str(h_list[25]),int(h_list[25])-st.session_state['platillos_sin_sal'])

col1, col2, col3, col4,col5 = st.columns(5)
col1.subheader('Tiempos')
col1.write(' ')
col1.metric("Desayuno",str(h_list[18]),int(h_list[18])-st.session_state['desayuno'])
col1.metric("Snack",str(h_list[19]),int(h_list[19])-st.session_state['snack'])
col1.metric("Merienda",str(h_list[20]),int(h_list[20])-st.session_state['merienda'])
col1.metric("Cena",str(h_list[21]),int(h_list[21])-st.session_state['cena'])
col2.subheader('Ensaladas')
col2.metric("E. Buffalo",str(h_list[10]),int(h_list[10])-st.session_state['e_buffalo'])
col2.metric("E. Carnes frias",str(h_list[11]),int(h_list[11])-st.session_state['e_carnes_frias'])
col2.metric("D. liz",str(h_list[12]),int(h_list[12])-st.session_state['d_liz'])
col2.metric("E. Cesar",str(h_list[13]),int(h_list[13])-st.session_state['e_cesar'])
col3.subheader('Hamb.')
col3.metric("H Normal",str(h_list[14]),int(h_list[14])-st.session_state['h_normal'])
col3.metric("H Chilaca",str(h_list[15]),int(h_list[15])-st.session_state['h_chilaca'])
col3.metric("H Champ",str(h_list[16]),int(h_list[16])-st.session_state['h_champ'])
col3.metric("H Haw",str(h_list[17]),int(h_list[17])-st.session_state['h_haw'])
col4.subheader('Platillos Normal')
col4.metric("Pollo normal",str(h_list[0]),int(h_list[0])-st.session_state['pollo_normal'])
col4.metric("Pescado normal",str(h_list[3]),int(h_list[3])-st.session_state['pescado_normal'])
col4.metric("Salmón normal",str(h_list[5]),int(h_list[5])-st.session_state['salmon_normal'])
col4.metric("Camarones normal",str(h_list[7]),int(h_list[7])-st.session_state['camarones_normal'])
col4.metric("Atunes normal",str(h_list[9]),int(h_list[9])-st.session_state['atunes_normal'])
col5.subheader('Platillos sin sal')
col5.metric("Pollo sin sal",str(h_list[1]),int(h_list[1])-st.session_state['pollo_sin_sal'])
col5.metric("Pescado sin sal",str(h_list[2]),int(h_list[2])-st.session_state['pescado_sin_sal'])
col5.metric("Salmón sin sal",str(h_list[4]),int(h_list[4])-st.session_state['salmon_sin_sal'])
col5.metric("Camarones sin sal",str(h_list[6]),int(h_list[6])-st.session_state['camarones_sin_sal'])
col5.metric("Atunes sin sal",str(h_list[8]),int(h_list[8])-st.session_state['atunes_sin_sal'])


st.session_state['desayuno'] = int(h_list[18])
st.session_state['snack'] = int(h_list[19])
st.session_state['merienda'] = int(h_list[20])
st.session_state['cena'] = int(h_list[21])
st.session_state['e_buffalo'] = int(h_list[10])
st.session_state['e_carnes_frias'] = int(h_list[11])
st.session_state['d_liz'] = int(h_list[12])
st.session_state['e_cesar'] = int(h_list[13])
st.session_state['h_normal'] = int(h_list[14])
st.session_state['h_chilaca'] = int(h_list[15])
st.session_state['h_champ'] = int(h_list[16])
st.session_state['h_haw'] = int(h_list[17])
st.session_state['platillos_normales'] = int(h_list[24])
st.session_state['platillos_sin_sal'] = int(h_list[25])
st.session_state['ensaladas'] = int(h_list[23])
st.session_state['hamburguesas'] = int(h_list[22])
st.session_state['platillos_totales'] = int(h_list[26])
st.session_state['lista_pedido'] = h_list

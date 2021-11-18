from pandas.core.frame import DataFrame
import streamlit as st
import pandas as pd
import base64
import numpy as np
from datetime import date
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

count = st_autorefresh(interval=5000,key="fizzbuzzcounter")

mydb = mysql.connector.connect(
  host="sql555.main-hosting.eu ",
  user="u591727659_robalejandro",
  password="RobalejandroTest1234",
  database="u591727659_test")

sql="""SELECT * FROM pedidos_v3 WHERE id_pedido = 0 """
mycursor = mydb.cursor()
mycursor.execute(sql)
myresult = mycursor.fetchall()
print(f'result: {myresult}')
h_list=[]
for index,x in enumerate(myresult[0]):
  h_list.append(x)
mycursor.close()

sql2='''
    SELECT gramaje from gramaje
'''
mycursor2 = mydb.cursor()
mycursor2.execute(sql2)
myresult2 = mycursor2.fetchall()  
print(f'result2 :{myresult2}')
h_list2=[]
df4= pd.DataFrame([],columns=['Pedido específico'])
if len(myresult2)>0:
    for index,x in enumerate(myresult2):
        h_list2.append(str(x[0]))
    print(f'H_list :{h_list2}')
    xtra = {'Pedido específico': h_list2}
    df4 = df4.append(pd.DataFrame(xtra))
mycursor2.close()
mydb.close()

print(f'h_list len :{len(h_list)}')

df_ensaladas = pd.DataFrame({'Buffalo':[h_list[31],h_list[32],h_list[33],h_list[34],h_list[35],h_list[36]],
                             'Carnes frias':[h_list[37],h_list[38],h_list[39],h_list[40],h_list[41],h_list[42]],
                             'D.liz':[h_list[43],h_list[44],h_list[45],h_list[46],h_list[47],h_list[48]],
                             'Cesar':[h_list[49],h_list[50],h_list[51],h_list[52],h_list[53],h_list[54]]},
                             index=['Alitas','Buffalo','Mostaza','Limon pepper','Natural','BBqs'])
df_hamburguesas = pd.DataFrame({'Ham. Normal':[h_list[19],h_list[20],h_list[21]],
                             'Ham. Chilaca':[h_list[22],h_list[23],h_list[24]],
                             'Ham. Champ':[h_list[25],h_list[26],h_list[27]],
                             'Ham. Haw':[h_list[28],h_list[29],h_list[30]]},
                             index=['Pan thin','Pan Margarita','Pan Lechuga'])

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
if 'h_normal_pan_thin' not in st.session_state:
    st.session_state['h_normal_pan_thin']=0
if 'h_normal_pan_margarita' not in st.session_state:
    st.session_state['h_normal_pan_margarita']=0
if 'h_normal_pan_lechuga' not in st.session_state:
    st.session_state['h_normal_pan_lechuga']=0
if 'h_chilaca_pan_thin' not in st.session_state:
    st.session_state['h_chilaca_pan_thin']=0
if 'h_chilaca_pan_margarita' not in st.session_state:
    st.session_state['h_chilaca_pan_margarita']=0
if 'h_chilaca_pan_lechuga' not in st.session_state:
    st.session_state['h_chilaca_pan_lechuga']=0
if 'h_champ_pan_thin' not in st.session_state:
    st.session_state['h_champ_pan_thin']=0
if 'h_champ_pan_margarita' not in st.session_state:
    st.session_state['h_champ_pan_margarita']=0
if 'h_champ_pan_lechuga' not in st.session_state:
    st.session_state['h_champ_pan_lechuga']=0
if 'h_haw_pan_thin' not in st.session_state:
    st.session_state['h_haw_pan_thin']=0
if 'h_haw_pan_margarita' not in st.session_state:
    st.session_state['h_haw_pan_margarita']=0
if 'h_haw_pan_lechuga' not in st.session_state:
    st.session_state['h_haw_pan_lechuga']=0
if 'e_buffalo_alitas' not in st.session_state:
    st.session_state['e_buffalo_alitas']=0
if 'e_buffalo_buffalo' not in st.session_state:
    st.session_state['e_buffalo_buffalo']=0
if 'e_buffalo_mostaza' not in st.session_state:
    st.session_state['e_buffalo_mostaza']=0
if 'e_buffalo_limon_pepper' not in st.session_state:
    st.session_state['e_buffalo_limon_pepper']=0
if 'e_buffalo_natural' not in st.session_state:
    st.session_state['e_buffalo_natural']=0
if 'e_buffalo_bbqs' not in st.session_state:
    st.session_state['e_buffalo_bbqs']=0
if 'e_carnes_frias_alitas' not in st.session_state:
    st.session_state['e_carnes_frias_alitas']=0
if 'e_carnes_frias_buffalo' not in st.session_state:
    st.session_state['e_carnes_frias_buffalo']=0
if 'e_carnes_frias_mostaza' not in st.session_state:
    st.session_state['e_carnes_frias_mostaza']=0
if 'e_carnes_frias_limon_pepper' not in st.session_state:
    st.session_state['e_carnes_frias_limon_pepper']=0
if 'e_carnes_frias_natural' not in st.session_state:
    st.session_state['e_carnes_frias_natural']=0
if 'e_carnes_frias_bbqs' not in st.session_state:
    st.session_state['e_carnes_frias_bbqs']=0
if 'e_dliz_alitas' not in st.session_state:
    st.session_state['e_dliz_alitas']=0
if 'e_dliz_buffalo' not in st.session_state:
    st.session_state['e_dliz_buffalo']=0
if 'e_dliz_mostaza' not in st.session_state:
    st.session_state['e_dliz_mostaza']=0
if 'e_dliz_limon_pepper' not in st.session_state:
    st.session_state['e_dliz_limon_pepper']=0
if 'e_dliz_natural' not in st.session_state:
    st.session_state['e_dliz_natural']=0
if 'e_dliz_bbqs' not in st.session_state:
    st.session_state['e_dliz_bbqs']=0
if 'e_cesar_alitas' not in st.session_state:
    st.session_state['e_cesar_alitas']=0
if 'e_cesar_buffalo' not in st.session_state:
    st.session_state['e_cesar_buffalo']=0
if 'e_cesar_mostaza' not in st.session_state:
    st.session_state['e_cesar_mostaza']=0
if 'e_cesar_limon_pepper' not in st.session_state:
    st.session_state['e_cesar_limon_pepper']=0
if 'e_cesar_natural' not in st.session_state:
    st.session_state['e_cesar_natural']=0
if 'e_cesar_bbqs' not in st.session_state:
    st.session_state['e_cesar_bbqs']=0
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
if 'panini_carnes_frias' not in st.session_state:
    st.session_state['panini_carnes_frias']=0
if 'panini_pollo' not in st.session_state:
    st.session_state['panini_pollo']=0

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
st.markdown("""<hr style="height:2px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)
today = date.today()

st.sidebar.markdown(today)

st.sidebar.metric("Platillos totales",str(h_list[63]),int(h_list[63])-st.session_state['platillos_totales'])
with st.sidebar.expander("Desglose"):
    st.metric("Ensaladas",str(h_list[59]),int(h_list[59])-st.session_state['ensaladas'])
    st.metric("Hamburguesas",str(h_list[60]),int(h_list[60])-st.session_state['hamburguesas'])
    st.metric("Platillos normales",str(h_list[61]),int(h_list[61])-st.session_state['platillos_normales'])
    st.metric("Platillos sin sal",str(h_list[62]),int(h_list[62])-st.session_state['platillos_sin_sal'])

col1, col2,col4,col5,col9= st.columns(5)
col1.subheader('Tiempos')
col1.write(' ')
col1.metric("Desayuno",str(h_list[55]),int(h_list[55])-st.session_state['desayuno'])
col1.metric("Snack",str(h_list[56]),int(h_list[56])-st.session_state['snack'])
col1.metric("Merienda",str(h_list[57]),int(h_list[57])-st.session_state['merienda'])
col1.metric("Cena",str(h_list[58]),int(h_list[58])-st.session_state['cena'])
col2.subheader('Ensaladas')
col2.metric("E. Buffalo total",str(h_list[11]),int(h_list[11])-st.session_state['e_buffalo'])
col2.metric("E. Carnes frias total",str(h_list[12]),int(h_list[12])-st.session_state['e_carnes_frias'])
col2.metric("D. liz total",str(h_list[13]),int(h_list[13])-st.session_state['d_liz'])
col2.metric("E. Cesar total",str(h_list[14]),int(h_list[14])-st.session_state['e_cesar'])
#col3.subheader('Hamburguesas')
#col3.metric("H Normal pan thin",str(h_list[19]),int(h_list[19])-st.session_state['h_normal_pan_thin'])
#col3.metric("H Normal pan margarita",str(h_list[20]),int(h_list[20])-st.session_state['h_normal_pan_margarita'])
#col3.metric("H Normal pan lechuga",str(h_list[21]),int(h_list[21])-st.session_state['h_normal_pan_lechuga'])
col4.subheader('Platillos Normal')
col4.metric("Pollo normal",str(h_list[1]),int(h_list[1])-st.session_state['pollo_normal'])
col4.metric("Pescado normal",str(h_list[4]),int(h_list[4])-st.session_state['pescado_normal'])
col4.metric("Salmón normal",str(h_list[6]),int(h_list[6])-st.session_state['salmon_normal'])
col4.metric("Camarones normal",str(h_list[8]),int(h_list[8])-st.session_state['camarones_normal'])
col4.metric("Atunes normal",str(h_list[10]),int(h_list[10])-st.session_state['atunes_normal'])
col5.subheader('Platillos sin sal')
col5.metric("Pollo sin sal",str(h_list[2]),int(h_list[2])-st.session_state['pollo_sin_sal'])
col5.metric("Pescado sin sal",str(h_list[3]),int(h_list[3])-st.session_state['pescado_sin_sal'])
col5.metric("Salmón sin sal",str(h_list[5]),int(h_list[5])-st.session_state['salmon_sin_sal'])
col5.metric("Camarones sin sal",str(h_list[7]),int(h_list[7])-st.session_state['camarones_sin_sal'])
col5.metric("Atunes sin sal",str(h_list[9]),int(h_list[9])-st.session_state['atunes_sin_sal'])
col9.subheader('Paninis')
col9.metric('Panini carnes frias',str(h_list[64]))
col9.metric('Panini pollo',str(h_list[65]))

col6,col7,col8= st.columns(3)
col6.subheader('Ensaladas')
col6.table(df_ensaladas)
col7.subheader('Hamburguesas')
col7.table(df_hamburguesas)
col8.subheader('Pedidos especificos')
col8.table(df4)

st.session_state['desayuno'] = int(h_list[55])
st.session_state['snack'] = int(h_list[56])
st.session_state['merienda'] = int(h_list[57])
st.session_state['cena'] = int(h_list[58])
st.session_state['e_buffalo'] = int(h_list[11])
st.session_state['e_carnes_frias'] = int(h_list[12])
st.session_state['d_liz'] = int(h_list[13])
st.session_state['e_cesar'] = int(h_list[14])
st.session_state['h_normal'] = int(h_list[15])
st.session_state['h_chilaca'] = int(h_list[16])
st.session_state['h_champ'] = int(h_list[17])
st.session_state['h_haw'] = int(h_list[18])
st.session_state['platillos_normales'] = int(h_list[61])
st.session_state['platillos_sin_sal'] = int(h_list[62])
st.session_state['ensaladas'] = int(h_list[59])
st.session_state['hamburguesas'] = int(h_list[60])
st.session_state['platillos_totales'] = int(h_list[63])
st.session_state['lista_pedido'] = h_list

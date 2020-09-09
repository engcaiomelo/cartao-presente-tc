import streamlit as st
from decode import Decode
import pandas as pd
import numpy as np

def Valid(df, COD):
    x = df['Codigo']
    for i in range(len(x)):
        if x[i] == COD:
            return False

    #for i in df['Codigo']:
    #    if i == COD:
    #        return True
    #    else:
    #        return False

def Insert(df, COD, VALOR):
    row = [VALOR, COD]
    insert_loc = df.index.max()

    if np.isnan(insert_loc):
        df.loc[0] = row
    else:
        df.loc[insert_loc + 1] = row


#df = pd.DataFrame(columns=['indice','Valor', 'Codigo'])
df = pd.read_csv('table.csv')


st.image('tqc.png', use_column_width=True)
COD = st.text_input(label='Cole o código do QrCode - Cartão Presente', key='COD')
VALOR = st.radio('Valor dos Cartão Presente', (50, 100, 150, 200, 250, 300), key='VALOR')
if st.button('verificar', key='VERIFICAR'):
    if Decode(COD, VALOR):
        if Valid(df, COD) == False:
            st.warning('Este Cartão Presente já foi utilizado')
            #st.write(Valid(df, COD))    # apenas para teste

        else:
            Insert(df, COD, VALOR)
            df.to_csv('table.csv', index_label=False )
            st.success('Cartão Presente Validado')
            #st.write(Valid(df, COD))    # apenas para teste


    else:
        st.warning('Verifique novamente se o código QrCode e o valor do cartão estão corretos')


data = st.dataframe(df)




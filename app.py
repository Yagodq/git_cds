#Bibliotecas
import pandas as pd
import numpy as np
import stramlit as st

#Funções 
def load_data():
    return pd.read_csv('data/processed/bikes_completed.csv')

def main():
    df = load_data()

    st.dataframe( df )

if __name__ == '__main__':
    main()

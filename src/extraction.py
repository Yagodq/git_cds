#Bibliotecas
import pandas as pd

#Funções 
def load_data():
    return pd.read_csv('data/processed/bikes_completed.csv')
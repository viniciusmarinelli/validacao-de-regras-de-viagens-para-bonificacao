import pandas as pd
import os
# import win32com.client as win32
import time 
from datetime import datetime


trips_table = pd.read_csv("./data/trips_sample.csv", delimiter=';', encoding='utf-8') #Carregando a tabela de viagens

drivers_table = pd.read_excel("./data/drivers_sample.xlsx") #Carregando a tabela de motoristas

df_triple = pd.DataFrame(trips_table) #criando um dataFrame

df_drivers = pd.DataFrame(drivers_table) #criando um dataFrame

df_triple['Data Viagem'] = pd.to_datetime(df_triple['Data Viagem'], errors='coerce', dayfirst=True).dt.date #Convertendo a coluna de data para o formato datetime

group_triple = df_triple.groupby(['Data Viagem', 'Driver']).agg({
    'Id Viagem': list,
    'Status de registro': list,
    'Tipo de Viagem': list}).reset_index() #Agrupando os dados por data e motorista, e agregando as colunas de viagem, status e tipo em listas

merge_table = pd.merge(group_triple, df_drivers, left_on='Driver', right_on='Driver', how='left') #Fazendo um merge entre as tabelas de viagens e motoristas

df_triple.drop(columns=['Driver'], inplace=True) #Removendo a coluna de driver, pois ela já foi agregada na tabela de merge

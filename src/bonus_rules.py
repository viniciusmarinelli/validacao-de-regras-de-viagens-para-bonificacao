import pandas as pd
import os
# import win32com.client as win32
import time 
from datetime import datetime

def third_leg(df):
    # Filtrando viagens que podem de 3ª Perna
    
    filter_third_leg = df[df['Id Viagem'].apply(len) >= 2].copy()
    
    def decide(status_list):
        # se todos concluídos
        if all(s == 'Concluído' for s in status_list):
            return "Bonificar"
        # se nenhum em andamento e tem status diferente de concluída
        elif all(s != 'Não Iniciado' for s in status_list):
            return "Justificar"
        else:
            return "Não Bonificar"

    filter_third_leg['Decisao'] = filter_third_leg['Status de registro'].apply(decide)
    return filter_third_leg

def lean_cattle_saturday(df):

    # Garante datetime para o .dt
    if not pd.api.types.is_datetime64_any_dtype(df['Data Viagem']):
        df['Data Viagem'] = pd.to_datetime(df['Data Viagem'], errors='coerce')

    df['Dia Semana'] = df['Data Viagem'].dt.day_name()
    
    # Tipo de Viagem vem como LISTA (agrupado), então filtra SOMENTE grupos onde TODOS são 'Magro' (exclui Gordo)
    triple_lean_cattle_saturday = df[
        (df['Tipo de Viagem'].apply(lambda tipos: all(t == 'Magro' for t in tipos))) & 
        (df['Dia Semana'] == 'Saturday')
    ].copy()

    def decide(status_list):
        if all(s  == 'Concluído' for s in status_list):
            return "Bonificar"
        elif all(s != 'Não Iniciado' for s in status_list):
            return "Justificar"
        else:
            return "Não Bonificar"
    
    triple_lean_cattle_saturday['Decisao'] = triple_lean_cattle_saturday['Status de registro'].apply(decide)
    return triple_lean_cattle_saturday
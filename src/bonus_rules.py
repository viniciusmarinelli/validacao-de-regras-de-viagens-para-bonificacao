import pandas as pd
import os
# import win32com.client as win32
import time 
from datetime import datetime

def third_leg(df):
    # Filtrando viagens que podem de 3ª Perna
    
    filter_third_leg = df[df['Id Viagem'].apply(len) >= 2].copy
    
    def decide(status_list):
        # se todos concluídos
        if all(s == 'Concluída' for s in status_list):
            return "Bonificar"
        # se nenhum em andamento e tem status diferente de concluída
        if all(s != 'Em andamento' for s in status_list):
            return "Justificar"
        return "Não Bonificar"

    filter_third_leg['Decisao'] = filter_third_leg['Status de registro'].apply(decide)
    return filter_third_leg

def lean_cattle_saturday(df):

    df['Dia Semana'] = df['Data Viagem'].dt.day_name()
    triple_lean_cattle_saturday = df[(df['Tipo de Viagem'] == 'Magro') & (df['Dia Semana'] == 'Saturday')]

    def decide(status_list):
        if all(s  == 'Concluída' for s in status_list):
            return "Bonificar"
        elif all(s != 'Em andamento' for s in status_list):
            return "Justificar"
        else:
            return "Não Bonificar"
    
    triple_lean_cattle_saturday['Decisao'] = triple_lean_cattle_saturday['Status de registro'].apply(decide)
    return triple_lean_cattle_saturday
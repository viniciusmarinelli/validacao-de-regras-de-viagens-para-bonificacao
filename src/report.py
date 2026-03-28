import pandas as pd
import os
# import win32com.client as win32
import time 
from datetime import datetime

def generate_report(df_third_leg, df_lean_cattle_saturday):
    with pd.ExcelWriter('./outputs/report.xlsx') as writer:
        df_third_leg.to_excel(writer, sheet_name='Third Leg', index=False)
        df_lean_cattle_saturday.to_excel(writer, sheet_name='Lean Cattle Saturday', index=False)
    return "Relatório gerado com sucesso!"
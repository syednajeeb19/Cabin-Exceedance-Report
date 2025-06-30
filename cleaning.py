# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 18:16:05 2024

@author: SyedNajeebURehman
"""

import pandas as pd
import numpy as np

def data_cleaning(src_path):
    df=pd.read_excel(src_path)
    df.drop(columns = ['Reporting Time', 'Time Pattern', 'FT Exceedance\n(Single Event) \n(in HH:mm)\n        ','FDP Exceedance\n(Single Event)\n(in HH:mm)\n        '], inplace = True)
    df['Location Pattern'] = df['Location Pattern'].str.rstrip(' , ')
    df['Flight Number(s)'] = df['Flight Number(s)'].str.replace('/', ' ')
    df['Actual_Pattern'] = df['Location Pattern'] + '--' + df['Flight Number(s)']
    df['Unique_Concatenate'] = df['Flight Date'] + df['Actual_Pattern']
    df['Staff Number'] = df['Staff Number'].astype('str')
    df['Name With SAP_ID'] = df['Crew Name'] + ' (' + df['Staff Number'] + ')'
    df.drop(columns = ['Crew Name', 'Staff Number'], inplace = True)
    df['Total_Crew_Members'] = df.groupby('Unique_Concatenate')['Name With SAP_ID'].transform('nunique')
    df.sort_values(by = 'Unique_Concatenate', inplace = True)
    df.reset_index(drop = True, inplace = True)
    
    clean_data=df.copy()

    df_grouped = df.groupby('Unique_Concatenate')['Name With SAP_ID'].apply(lambda x : ', '.join(x)).reset_index()
    df_merged = df.drop('Name With SAP_ID', axis = 1).merge(df_grouped, on = 'Unique_Concatenate')
    df_merged.drop_duplicates(subset = 'Unique_Concatenate', inplace = True)
    df_merged.drop(columns = ['Rank', 'Base', 'Actual_Pattern', 'Unique_Concatenate'], inplace = True)
        
    
    return clean_data,df_merged




    

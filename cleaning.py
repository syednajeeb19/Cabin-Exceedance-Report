# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 18:16:05 2024

@author: SyedNajeebURehman
"""

import pandas as pd
import numpy as np

def data_cleaning(src_path):
    df=pd.read_csv(src_path)
    df.drop(columns = ['EQUIPMENT_CODE', 'TIME_PATTERN', 'REPORTING_TIME', 'FT_EXCEEDENCE', 'FDP_EXCEEDENCE', 'FT_EXCEEDENCE_TOTAL', 'FDP_EXCEEDENCE_TOTAL'], inplace = True)
    df['LOCATION_PATTERN'] = df['LOCATION_PATTERN'].str.rstrip(' , ')
    df['DUTY_PATTERN'] = 'AI' + df['DUTY_PATTERN'].str.replace('/', ' AI')
    df['ACTUAL_PATTERN'] = df['LOCATION_PATTERN'] + '--' + df['DUTY_PATTERN']
    df['UNIQUE_CONCATENATE'] = df['START_DATE'] + df['ACTUAL_PATTERN']
    df['STAFF_NUMBER'] = df['STAFF_NUMBER'].astype('str')
    df['NAME WITH SAP_ID'] = df['NAME'] + ' (' + df['STAFF_NUMBER'] + ')'
    df.drop(columns = ['NAME', 'STAFF_NUMBER'], inplace = True)
    df['TOTAL_CREW_MEMBERS'] = df.groupby('UNIQUE_CONCATENATE')['NAME WITH SAP_ID'].transform('nunique')
    df.sort_values(by = 'UNIQUE_CONCATENATE', inplace = True)
    df.reset_index(drop = True, inplace = True)
    df['START_DATE']=pd.to_datetime(df['START_DATE'],format='mixed')
    
    clean_data=df.copy()
    
    df_grouped = df.groupby('UNIQUE_CONCATENATE')['NAME WITH SAP_ID'].apply(lambda x : ', '.join(x)).reset_index()
    df_merged = df.drop('NAME WITH SAP_ID', axis = 1).merge(df_grouped, on = 'UNIQUE_CONCATENATE')
    df_merged.drop_duplicates(subset = 'UNIQUE_CONCATENATE', inplace = True)
    
    
    return clean_data,df_merged




    
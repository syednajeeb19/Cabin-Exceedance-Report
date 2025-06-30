# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 18:32:15 2024

@author: SyedNajeebURehman
"""

import streamlit as st
from cleaning import data_cleaning

st.title("CABIN EXCEEDANCE REPORT")

upload_file=st.file_uploader("Choose a file to Upload",type="xlsx")

if upload_file is not None:
    clean_data,merged_data=data_cleaning(upload_file)
    st.write("Clean_data_1")
    st.dataframe(clean_data.head())
    
    st.write("Merged_data")
    st.dataframe(merged_data.head())
    
    file1=clean_data.to_csv(index=False)
    file2=merged_data.to_csv(index=False)
    
    st.download_button(label='Download_Clean_file',
                       data=file1,
                       file_name='Crew_Exceedance_Report_Overall_Data.csv',
                       mime="text/csv"
                     )
    
     
    st.download_button(label='Download_Merged_file',
                       data=file2,
                       file_name='Crew_Exceedance_Report_CABIN.csv',
                       mime="text/csv"
                     )
    




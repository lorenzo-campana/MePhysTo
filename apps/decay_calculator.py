import streamlit as st
import pandas as pd
import numpy as np
import datetime
import re

def app():
    
    st.title('Decay Calculator')

    nuclide_list=pd.read_csv("data/nuclide.csv")

    nuclide=st.text_input("Nuclide", value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, placeholder=None)
    start_activity=st.number_input("Start Activity (MBq)", key=None, help=None, on_change=None, args=None, kwargs=None)


    with st.expander("Start Date"):
        start_date=st.date_input("Date", value=None, min_value=None, max_value=None, key="start", help=None, on_change=None, args=None, kwargs=None)
        start_time= st.time_input("Time", value=None, key="start", help=None, on_change=None, args=None, kwargs=None)

    with st.expander("End Date"):

        end_date=st.date_input("Date", value=None, min_value=None, max_value=None, key="end", help=None, on_change=None, args=None, kwargs=None)
        end_time= st.time_input("Time", value=None, key="end", help=None, on_change=None, args=None, kwargs=None)


    col1,col2,col3,col4=st.columns(4)
    with col1:
        calculate=st.button("Calculate", key=None, help=None, on_click=None, args=None, kwargs=None)

    with col2:
        if calculate:
            
            nuclide_number=str(re.findall(r'\d+',nuclide)[0])
            nuclide_symbol=str(re.findall("[a-zA-Z]+", nuclide)[0])

            half_life=float(nuclide_list[(nuclide_list['symbol'] == nuclide_symbol) & (nuclide_list['a'] == int(nuclide_number))]["half_life_sec"].iloc[0])


            time_diff=datetime.datetime.combine(end_date,end_time)-datetime.datetime.combine(start_date,start_time)
            time_diff=time_diff.total_seconds()
            final_activity=float(start_activity)*0.5**(int(time_diff)/half_life)
            st.write("Final Activity: "+ str(final_activity)+" MBq")


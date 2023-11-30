# -*- coding: utf-8 -*-
"""
Created on Tue November 30 11:24:00 2023

@author: FKAMP
"""
import pandas as pd
import streamlit as st
from PIL import Image
import datetime

st.set_page_config(layout="wide", 
                   page_icon='wise_men_crown.ico',
                   page_title='Seaway7 progress overview',
                   menu_items={'Get help' : 'mailto:fabian.kamp@seaway7.com',
                               'Report a Bug' : 'mailto:fabian.kamp@seaway7.com'}
                   )


header1, header2 = st.columns([1,5])
image1 = Image.open('Cofra_logo.PNG')
header1.image(image1, width=150)

horizontal_line = '''
            
    ---
    

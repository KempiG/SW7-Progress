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



def main():
    
    technique = st.sidebar.radio("""Choose visualization""", ['General project overview', 'Details'])
    
    #####CDC#####
    if technique == 'General project overview':
        header2.title("""General project data import""")

        uploads = st.sidebar.file_uploader('Upload project excel', 
                                           accept_multiple_files=True, 
                                           type='excel')
        radio1 = st.sidebar.radio('Show only completed locations', ['yes','no'])
        radio2 = st.sidebar.radio('Save output as?', ['Excel file','CSV file'])        
        

        if len(uploads) == 1:
            st.write(f' **{len(uploads)}** file imported')
        else:
            st.write(f' **{len(uploads)}** files imported')
        
        if len(uploads) > 0:
            list_ = []
            for file_ in uploads:
                ##### only for new file type
                headers = [0,1]
                df = pd.read_excel(file_, sheet_name = 1 , index_col=False, usecols=(range(100)), header=1)
                #####
                list_.append(df)
                
            new_name = uploads[0].name
            new_name=new_name.split('_')
            new_name=new_name[0]
            
            col1, col2 = st.columns([2,4])
            start_button = col1.button('Process .excel files', key='1')
            
            st.markdown(horizontal_line)
            
            if start_button:
                with st.spinner(text='In progress...'):
                    frame = CDC_funcs.convert(list_, radio1, radio2, new_name)    
                
                    if radio2 == 'CSV file':
                        tmp_download_link = CDC_funcs.download_link_csv(frame, 
                                                                        f'{new_name}.csv', 
                                                                        'Click here to download CSV file!')
                    elif radio2 == 'Excel file':
                        tmp_download_link = CDC_funcs.download_link_excel(frame, 
                                                                          f'{new_name}.xlsx', 
                                                                          'Click here to download excel file!')
                    st.markdown(tmp_download_link, unsafe_allow_html=True)                    
                    
                st.markdown(horizontal_line)
                
                CDC_funcs.show_preview(frame)
                st.success('Done!')



if __name__ == "__main__":
    main()
    

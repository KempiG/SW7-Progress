# -*- coding: utf-8 -*-
"""
Created on Tue November 30 11:24:00 2023

@author: FKAMP
"""
import pandas as pd
import streamlit as st
from PIL import Image
import datetime
import openpyxl
import matplotlib.pyplot as plt


def download_link_csv(object_to_download, download_filename, download_link_text):
    """
    Generates a link to download the given object_to_download.

    object_to_download (str, pd.DataFrame):  The object to be downloaded.
    download_filename (str): filename and extension of file. e.g. mydata.csv
    download_link_text (str): Text to display for download link.

    Examples:
    download_link(YOUR_DF, 'YOUR_DF.csv', 'Click here to download data!')
    download_link(YOUR_STRING, 'YOUR_STRING.txt', 'Click here to download your text!')

    """
    if isinstance(object_to_download, pd.DataFrame):
        object_to_download = object_to_download.to_csv(index=True)
    
    b64 = base64.b64encode(object_to_download.encode()).decode()

    return f'<a href="data:file/txt;base64,{b64}" download="{download_filename}">{download_link_text}</a>'


def download_link_excel(object_to_download, download_filename, download_link_text):
    """
    Generates a link to download the given object_to_download.

    object_to_download (str, pd.DataFrame):  The object to be downloaded.
    download_filename (str): filename and extension of file. e.g. mydata.csv
    download_link_text (str): Text to display for download link.

    Examples:
    download_link(YOUR_DF, 'YOUR_DF.csv', 'Click here to download data!')
    download_link(YOUR_STRING, 'YOUR_STRING.txt', 'Click here to download your text!')

    """
    if isinstance(object_to_download, pd.DataFrame):
        towrite = io.BytesIO()
        object_to_download = object_to_download.to_excel(towrite, index=True)
        towrite.seek(0)
    
    b64 = base64.b64encode(towrite.read()).decode()

    return f'<a href="data:file/txt;base64,{b64}" download="{download_filename}">{download_link_text}</a>'






st.set_page_config(layout="wide", 
                   page_icon='wise_men_crown.ico',
                   page_title='Seaway7 progress overview',
                   menu_items={'Get help' : 'mailto:fabian.kamp@seaway7.com',
                               'Report a Bug' : 'mailto:fabian.kamp@seaway7.com'}
                   )


header1, header2 = st.columns([1,5])
image1 = Image.open('wise_men_crown.ico')
header1.image(image1, width=150)

horizontal_line = '''
            
    ---
'''


def main():
    
    technique = st.sidebar.radio("""Choose visualization""", ['General project overview', 'Details'])
    
    #####General info#####
    if technique == 'General project overview':
        header2.title("""General project data import""")

        uploads = st.sidebar.file_uploader('Upload project excel', 
                                           accept_multiple_files=True,type='xlsx')
        radio1 = st.sidebar.radio('Show only completed locations', ['Yes','No'])
        radio2 = st.sidebar.radio('Save output as?', ['Excel file','CSV file'])        
        

        if len(uploads) == 1:
            st.write(f' **{len(uploads)}** file imported')
        else:
            st.write(f' **{len(uploads)}** files imported')
        
        if len(uploads) > 0:
            list_ = []
            for file_ in uploads:
                ##### only for new file typ
                st.write(f'{file_} file uploaded')
                df = pd.read_excel(file_,sheet_name=1,header=1,skiprows=[2,3,4,5,6])
                df = df.drop(df[df["WTG"].isna()].index)
                st.dataframe(df)


                
                #data = pd.ExcelFile(file_)
                #output=pd.DataFrame()
                #names = data.sheet_names
                #for name in names:
                    #if ('overview' in name.lower()):
                        #df = data.parse(name)
                        #output = pd.concat([output, df], ignore_index = True)
                        #output = header=1,skiprows=[2,3,4,5,6]
                #st.dataframe(output)
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
                    #frame = CDC_funcs.convert(list_, radio1, radio2, new_name) 
                    fig, ax = plt.subplots(figsize=[18,3], facecolor='white')
                    #ax.set_yticks([0, 0.2])
                    ax.plot(df.iloc[:,6],df.iloc[:,2])
                    #plt.show()
                    ax.set_yticklabels(['Operational', 'Delay'])
                    #ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
                    #fig.suptitle(f'{date} - {base_unit}', fontsize=20)
                    ax.grid(linestyle="--")
                    fig.autofmt_xdate()    
                    st.write(fig)   
                    
                    if radio2 == 'CSV file':
                        st.write("CSV!")
                    #    tmp_download_link = download_link_csv(frame, 
                    #                                                    f'{new_name}.csv', 
                    #                                                    'Click here to download CSV file!')
                    elif radio2 == 'Excel file':
                        st.write("Excel!")
                    #    tmp_download_link = download_link_excel(frame, 
                    #                                                      f'{new_name}.xlsx', 
                    #                                                      'Click here to download excel file!')
                    #st.markdown(tmp_download_link, unsafe_allow_html=True)                    
                    
                st.markdown(horizontal_line)
                
                #CDC_funcs.show_preview(frame)
                st.success('Done!')

  #####Details#####
    elif technique == 'Details':
        header2.title("""Project details""")
  #      #col1, col2 = st.columns(2)
  #      uploads = st.sidebar.file_uploader('Upload log files', 
  #                                         accept_multiple_files=True, 
  #                                         type='ext',
  #                                         help="""Select one or multiple Excel files with project data""")                
  #      radio1 = st.sidebar.radio('Save as?', ['Excel file','CSV file'])
        #radio2 = st.sidebar.radio('Show platform thickness map?', ['No', 'Yes'])
        
        # if radio2 == 'Yes':
        #     wp_select = st.sidebar.selectbox('Choose method to calculate cable tension', 
        #                                  ('Lowest force plus fixed number','Manual choice'))
        #     if wp_select == 'Lowest force plus fixed number':
        #         fixed_nr = st.sidebar.number_input('Fixed number',
        #                                          value = 5,
        #                                          step = 1)
        #     elif wp_select == 'Manual choice':
        #         fixed_nr = st.sidebar.number_input('Cutoff force between working platform and soft soil',
        #                                            value = 50,
        #                                            step = 1)
        # elif radio2 == 'No':
        #     wp_select = 'No'
        #     fixed_nr = 'No'
        
   #     wp_select = 'No'
   #     fixed_nr = 'No'
        
   #     radio3 = st.sidebar.radio('Which columns?', 
   #                               ['Default columns (recommended)', 'Columns from file'],
   #                               help="""**Default columns:** The output file will always contain the same columns
   #                               independent of the columns in the uploaded EXT files  
   #                               **Columns from file:**
   #                               The output file will contain all the columns in the uploaded EXT files, 
   #                               note that this can differ based on the CMS version""")
                                
   #     if len(uploads) == 1:
   #         st.write(f' **{len(uploads)}** file imported')
   #     else:
   #         st.write(f' **{len(uploads)}** files imported')
            
   #     if len(uploads) > 0:
   #         list_, headerlist = PVD_funcs.list_ext(uploads, radio3)
                        
   #         col1, col2 = st.columns([2,4])
            
   #         if 'bool' not in st.session_state:
   #             st.session_state.bool = False            
            
   #         start_button = col1.button('Start processing / Reset')
                  
   #         if start_button:
   #             st.session_state.bool = not st.session_state.bool
                        
   #         st.markdown(horizontal_line)
            
            #if st.session_state.bool:
            #    with st.spinner(text='In progress...'):
            #        frame, time_text = PVD_funcs.convert(list_, headerlist, wp_select, fixed_nr)
                    
                    ## Output on screen ##    
             #       col1, col2, col3 = st.columns(3)
             #       col1.metric('Number of drains [-]', len(frame))
             #       col2.metric('Linear meter [m]', round(frame['Max. depth [m]'].sum(),2))
             #       col3.metric('Average installation depth [m]', round(frame['Max. depth [m]'].mean(),2))
                    
                    ## Download link ##
             #       if radio1 == 'CSV file':
             #           tmp_download_link = CDC_funcs.download_link_csv(frame, 
             #                                                           'PVD_data_processed.csv', 
             #                                                           'Click here to download CSV file!')
             #       elif radio1 == 'Excel file':
             #           tmp_download_link = CDC_funcs.download_link_excel(frame, 
             #                                                             'PVD_data_processed.xlsx', 
             #                                                             'Click here to download excel file!')
             #      st.markdown(tmp_download_link, unsafe_allow_html=True)                  
                
                
             #   st.markdown(horizontal_line)
                
                
             #  st.write('**Preview:**')
             # PVD_funcs.show_preview(frame)


             #    st.markdown(horizontal_line)
                
                
             #   st.write('**Productivity:**')
             #   col1, col2 = st.columns(2)
                
             #   base_units = []
             #   dates = []
             #   for file in list_:
             #       base_unit = file['Base unit [-]'].iloc[0]
             #       base_units.append(base_unit)
             #       date = file['date [YYYYMMDD]'].iloc[0]
             #       dates.append(date)
                                
             #   dates_str = [str(x) for x in dates]
             #   dates_str = [x[6:]+'-'+x[4:6]+'-'+x[:4] for x in dates_str]
             #   date_base_units = []
             #   date_base_units = [dates_str[i] + ' / ' + base_units[i] for i in range(len(dates_str))]
             #   date_base_units.sort()
             #   date_base_unit = st.selectbox('Select date + base unit', date_base_units)
                                
             #   date, base_unit = date_base_unit.split(' / ')
             #   day = datetime.datetime.strptime(date, '%d-%m-%Y').date()
                
             #   frame['time_text'] = time_text
             #   frame_filtered = frame[(frame["Base unit [-]"]==base_unit) & (frame["date [YYYYMMDD]"] == day)]
                
             #   with st.expander('Properties'):
             #       col1, col2, col3 = st.columns(3)
             #       delta = col1.number_input('Delay time [minutes]', 
             #                                 value=5, 
             #                                 help='If no drain is installed in this time, it is counted as delay. Default is set to 5 minutes')
             #       delta = delta * 60
                    
             #       start_of_shift = datetime.time((frame_filtered['time [HHMMSS]'].iloc[0]).hour, 0)
             #       start_time = col2.time_input('Start of shift', value=start_of_shift)
             #       start_time = start_time.strftime("%H%M%S")
             #       start_time = pd.Series([start_time])
                    
             #       if frame_filtered['time [HHMMSS]'].iloc[-1] > datetime.time(23, 45):
             #           end_of_shift = datetime.time(23, 59)
             #       else:
             #           end_of_shift = datetime.time((frame_filtered['time [HHMMSS]'].iloc[-1]).hour + 1, 0)
             #       end_time = col3.time_input('End of shift', value=end_of_shift)
             #       end_time = end_time.strftime("%H%M%S")
             #       end_time = pd.Series([end_time])                
                
             #   PVD_funcs.show_delay(frame_filtered, delta, start_time, end_time, date, base_unit)
                
             #   st.markdown(horizontal_line)
             #   st.caption('🏗️ New version under construction: https://cofra-cms-processing-tool.streamlitapp.com/')
                
                #dataFrameSerialization = "legacy"
                #frame["drain_timedelta"] = pd.Timedelta(0)
                #frame["drain_timedelta"].dt.seconds
                # Determine the timedelta per baseunit
                # for base_unit in frame["Base unit [-]"].unique():
                #     frame.update(
                #         (
                #             frame.loc[df["Base unit [-]"]==base_unit, "time [HHMMSS]"] - frame.loc[df["Base unit [-]"]==base_unit, "time [HHMMSS]"].shift(1)
                #         ).rename("drain_timedelta")
                #     )
                #     #print(base_unit, "completed")
                
                # # Set the starting date
                # frame["start"] = frame["time [HHMMSS]"] - frame.drain_timedelta
                
                #st.code(frame)
                #st.write(frame)
                
                
                # if radio2 == 'Yes':
                #     cs = st.slider('Cross_section', 
                #                    min_value=wp_frame['Y [m]'].min(),
                #                    max_value=wp_frame['Y [m]'].max())
                #     st.write(cs)
                #     PVD_funcs.show_wp(wp_frame, cs)
                #PVD_funcs.show_preview_altair(frame) 
                #PVD_funcs.show_preview_bokeh(frame)
                
                #st.success('Done!')


if __name__ == "__main__":
    main()
    

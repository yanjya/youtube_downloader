import streamlit as st
import pandas as pd
from pytube import YouTube
import base64
from io import BytesIO

def main():
    path = st.text_input('YOUTUBE link')
    option = st.selectbox(
        'Select type of download',
        ('MP3', 'MP4'))
    
    matches = ['MP3', 'MP4']
    if st.button("download"): 
        video_object = YouTube(path)
        video_name = st.empty()
        video_name.text("Video: " + str(video_object.title))
        loading_text = st.empty()
        loading_text.text("loading.....")
        if option=='MP3':
            stream = video_object.streams.get_audio_only()
        elif option=='MP4':
            stream = video_object.streams.get_highest_resolution()
        
        # 下載檔案到暫時資料夾
        temp_file_path = stream.download(output_path='/tmp')
        
        # 轉換檔案為 base64
        with open(temp_file_path, 'rb') as f:
            file_data = f.read()
        file_data_encoded = base64.b64encode(file_data).decode()
        
        # 提供下載連結
        video_name.empty()
        loading_text.empty()
        st.write(f'Klick Download link👇 ')
        st.markdown(f'<a href="data:file/txt;base64,{file_data_encoded}" download="{stream.default_filename}">Download {stream.default_filename}</a>', unsafe_allow_html=True)

if __name__ == '__main__':
    main()
import streamlit as st
import os

st.set_page_config(page_title="Audio Playback App", layout="centered")

st.title("🎵 Audio Playback Interface")
st.caption("Upload file audio dan dengarkan langsung di sini.")

audio_file = st.file_uploader("📁 Upload audio file", type=["wav", "mp3", "ogg", "flac"])

if audio_file:
    # Tampilkan player
    st.audio(audio_file, format=f'audio/{audio_file.type.split("/")[-1]}')

else:
    st.info("Silakan upload file audio berformat `.wav`, `.mp3`, `.ogg`, atau `.flac`")

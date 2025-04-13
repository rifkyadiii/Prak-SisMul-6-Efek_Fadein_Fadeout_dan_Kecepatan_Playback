import streamlit as st
from pydub.utils import mediainfo
import tempfile
import os

st.title("🎵 Audio Playback Interface")

audio_file = st.file_uploader("📁 Upload audio file", type=["wav", "mp3", "ogg", "flac"])

if audio_file:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(audio_file.read())
        tmp_file_path = tmp_file.name

    try:
        info = mediainfo(tmp_file_path)
        st.success("✅ Audio berhasil dimuat!")
        st.markdown("**Detail Audio:**")
        st.write({
            "Format": info.get("format_name", "-"),
            "Sample Rate": info.get("sample_rate", "-"),
            "Channels": info.get("channels", "-"),
            "Duration (s)": round(float(info.get("duration", 0)), 2)
        })
    except Exception as e:
        st.error(f"❌ Gagal membaca metadata audio. Error: {str(e)}")
    
    os.remove(tmp_file_path)

    st.audio(audio_file, format=f'audio/{audio_file.type.split("/")[-1]}')
else:
    st.info("Silakan upload file audio berformat `.wav`, `.mp3`, `.ogg`, atau `.flac`")

import streamlit as st
from pydub.utils import mediainfo
import os

st.set_page_config(page_title="Audio Playback App", layout="centered")

st.title("🎵 Audio Playback Interface")
st.caption("Upload file audio dan dengarkan langsung di sini.")

audio_file = st.file_uploader("📁 Upload audio file", type=["wav", "mp3", "ogg", "flac"])

if audio_file:
    # Tampilkan player
    st.audio(audio_file, format=f'audio/{audio_file.type.split("/")[-1]}')
    
    # Simpan sementara untuk info file
    with open("temp_audio", "wb") as f:
        f.write(audio_file.read())

    try:
        info = mediainfo("temp_audio")
        st.success("✅ Audio berhasil dimuat!")
        st.markdown("**Detail Audio:**")
        st.write({
            "Format": info.get("format_name", "-"),
            "Sample Rate": info.get("sample_rate", "-"),
            "Channels": info.get("channels", "-"),
            "Duration (s)": round(float(info.get("duration", 0)), 2)
        })
    except:
        st.warning("Gagal membaca metadata audio.")

    # Hapus file sementara setelah dibaca
    os.remove("temp_audio")

else:
    st.info("Silakan upload file audio berformat `.wav`, `.mp3`, `.ogg`, atau `.flac`")


import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
import av
from src.haar_cascades import detect_face_haar
from src.yunet import detect_face_yunet

st.set_page_config(
    page_title="Real-Time Face Detection",
    page_icon="👦",
    layout="wide"
)

# Sidebar controls
st.sidebar.title("Settings")
model_choice = st.sidebar.selectbox(
    "Select Face Detection Model",
    ["YuNet", "Haar Cascades"]
)

# Face detection processor
class FaceDetectionTransformer(VideoTransformerBase):
    def __init__(self):
        self.model_choice = model_choice

    def recv(self, frame) -> av.VideoFrame:
        img = frame.to_ndarray(format="bgr24")
        
        if self.model_choice == "YuNet":
            detect_face_yunet(img)
                    
        elif self.model_choice == "Haar Cascades":
            detect_face_haar(img)

        new_frame = av.VideoFrame.from_ndarray(img, format="bgr24")
        new_frame.pts = frame.pts
        new_frame.time_base = frame.time_base
        return new_frame

# Main app
st.title("Real-Time Face Detection 👦")
st.write("""
This app demonstrates real-time face detection using different models.
Select your preferred model from the sidebar and adjust the confidence threshold.
""")

# WebRTC streamer
webrtc_ctx = webrtc_streamer(
    key="face-detection",
    video_processor_factory=FaceDetectionTransformer,
    rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
    media_stream_constraints={"video": True, "audio": False},
    video_html_attrs={
        "autoPlay": True,
        "controls": True,
        "controlsList": "nofullscreen",
        "style": {"width": "100%"},
        "muted": True
    },
    async_processing=True,
)

# Instructions
st.sidebar.markdown("### Instructions")
st.sidebar.info("""
1. Select your preferred model
2. Allow camera access when prompted
""")

# Notes
st.sidebar.markdown("### Notes")
st.sidebar.warning("""
- YuNet provides the best balance of speed/accuracy
- Haar Cascades works but is less accurate
""")
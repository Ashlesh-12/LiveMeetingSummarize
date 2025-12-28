import streamlit as st
import cv2
import os
import zipfile
from io import BytesIO
from PIL import Image
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Video Frame Extractor",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for a premium look
st.markdown("""
<style>
    .main {
        background-color: #0e1117;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #ff4b4b;
        color: white;
    }
    .stDownloadButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #00c853;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

def extract_frames(video_path, extraction_mode, extraction_value):
    """Extracts frames from the video based on the chosen mode and value."""
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        return None

    frames = []
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    if extraction_mode == "Every Nth Frame":
        step = extraction_value
    else:  # Every N Seconds
        step = int(fps * extraction_value)
    
    if step < 1:
        step = 1

    count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        if count % step == 0:
            # Convert BGR (OpenCV) to RGB (PIL/Streamlit)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frames.append(frame_rgb)
        
        count += 1
    
    cap.release()
    return frames

def create_zip(frames):
    """Creates a ZIP file in memory containing the extracted frames."""
    buf = BytesIO()
    with zipfile.ZipFile(buf, "w") as zf:
        for i, frame in enumerate(frames):
            img = Image.fromarray(frame)
            img_buf = BytesIO()
            img.save(img_buf, format="JPEG")
            zf.writestr(f"frame_{i:04d}.jpg", img_buf.getvalue())
    return buf.getvalue()

def main():
    st.title("🎬 Video Frame Extractor")
    st.markdown("Upload a video and extract frames with ease. Perfect for datasets, analysis, or capturing that perfect moment.")

    with st.sidebar:
        st.header("Settings")
        uploaded_file = st.file_uploader("Choose a video file", type=["mp4", "avi", "mov", "mkv"])
        
        extraction_mode = st.radio(
            "Extraction Mode",
            ["Every Nth Frame", "Every N Seconds"],
            index=0
        )
        
        if extraction_mode == "Every Nth Frame":
            extraction_value = st.number_input("Nth Frame", min_value=1, value=30, step=1)
        else:
            extraction_value = st.number_input("Every N Seconds", min_value=0.1, value=1.0, step=0.1)
        
        extract_button = st.button("Extract Frames")

    if uploaded_file is not None:
        # Save uploaded file to a temporary location
        tfile = "temp_video.mp4"
        with open(tfile, 'wb') as f:
            f.write(uploaded_file.read())
        
        st.video(tfile)

        if extract_button:
            with st.spinner("Extracting frames..."):
                frames = extract_frames(tfile, extraction_mode, extraction_value)
                
                if frames:
                    st.success(f"Successfully extracted {len(frames)} frames!")
                    
                    # Create ZIP file for download
                    zip_data = create_zip(frames)
                    st.download_button(
                        label="📥 Download All Frames (ZIP)",
                        data=zip_data,
                        file_name="extracted_frames.zip",
                        mime="application/zip"
                    )

                    # Display frames in a grid
                    st.subheader("Frame Preview")
                    cols = st.columns(4)
                    for i, frame in enumerate(frames[:40]): # Preview first 40 frames
                        with cols[i % 4]:
                            st.image(frame, use_container_width=True, caption=f"Frame {i}")
                    
                    if len(frames) > 40:
                        st.info(f"Showing first 40 frames out of {len(frames)}.")
                else:
                    st.error("Could not extract frames. Please check the video file.")
        
        # Cleanup temporary file
        if os.path.exists(tfile):
            os.remove(tfile)
    else:
        st.info("Please upload a video file in the sidebar to begin.")

if __name__ == "__main__":
    main()

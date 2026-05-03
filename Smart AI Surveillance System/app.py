import streamlit as st
import cv2
import pandas as pd
import os
import numpy as np
import time
from datetime import datetime
from ultralytics import YOLO
import tempfile

# Load YOLO model
model = YOLO("yolov8n.pt")

# Create folders
if not os.path.exists("outputs"):
    os.makedirs("outputs")

# Logging function
def log_detection(obj):
    data = {"object": obj, "time": datetime.now()}
    df = pd.DataFrame([data])
    if os.path.exists("logs.csv"):
        df.to_csv("logs.csv", mode='a', header=False, index=False)
    else:
        df.to_csv("logs.csv", index=False)

# Draw boxes function
def process_frame(frame, target_object):
    results = model(frame)
    detected_count = 0

    for result in results:
        for box in result.boxes:
            cls_id = int(box.cls[0])
            label = model.names[cls_id]
            conf = float(box.conf[0])

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            cv2.rectangle(frame, (x1,y1),(x2,y2),(0,255,0),2)
            cv2.putText(frame, f"{label} {conf:.2f}", (x1,y1-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)

            detected_count += 1

            # Alert + save image
            if label == target_object:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"outputs/{label}_{timestamp}.jpg"
                cv2.imwrite(filename, frame)
                log_detection(label)

    return frame, detected_count

# UI
st.title("🧠 Smart AI Surveillance System")

st.sidebar.header("Settings")
mode = st.sidebar.selectbox("Mode", ["Webcam", "Image", "Video"])
target_object = st.sidebar.text_input("Alert Object", "person")

# IMAGE MODE
if mode == "Image":
    file = st.file_uploader("Upload Image", type=["jpg","png","jpeg"])
    if file:
        file_bytes = file.read()
        np_arr = np.frombuffer(file_bytes, np.uint8)
        frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        frame, count = process_frame(frame, target_object)

        st.image(frame, channels="BGR")
        st.write(f"Objects detected: {count}")

# VIDEO MODE
elif mode == "Video":
    file = st.file_uploader("Upload Video", type=["mp4","avi"])
    if file:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(file.read())

        cap = cv2.VideoCapture(tfile.name)
        stframe = st.empty()

        prev_time = 0

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame, count = process_frame(frame, target_object)

            # FPS calculation
            curr_time = time.time()
            fps = 1 / (curr_time - prev_time) if prev_time else 0
            prev_time = curr_time

            cv2.putText(frame, f"FPS: {int(fps)}", (10,30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0), 2)

            stframe.image(frame, channels="BGR")

# WEBCAM MODE
elif mode == "Webcam":
    run = st.checkbox("Start Webcam")
    FRAME_WINDOW = st.image([])
    cap = cv2.VideoCapture(0)

    prev_time = 0

    while run:
        ret, frame = cap.read()
        if not ret:
            break

        frame, count = process_frame(frame, target_object)

        curr_time = time.time()
        fps = 1 / (curr_time - prev_time) if prev_time else 0
        prev_time = curr_time

        cv2.putText(frame, f"FPS: {int(fps)}", (10,30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0), 2)

        FRAME_WINDOW.image(frame, channels="BGR")

# Logs
st.subheader("📊 Detection Logs")
if os.path.exists("logs.csv"):
    logs = pd.read_csv("logs.csv")
    st.dataframe(logs)
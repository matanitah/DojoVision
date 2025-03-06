import cv2
import numpy as np
import json
import os

def load_video(video_path):
    """Load a video and return frames as a list."""
    cap = cv2.VideoCapture(video_path)
    frames = []
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    cap.release()
    return frames

def preprocess_frames(frames):
    """Apply preprocessing steps such as resizing and normalization."""
    processed = [cv2.resize(frame, (224, 224)) / 255.0 for frame in frames]
    return np.array(processed)

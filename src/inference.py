import torch
import cv2
import numpy as np

def predict(model, frame):
    """Run inference on a single frame."""
    frame = cv2.resize(frame, (224, 224)) / 255.0
    frame = torch.tensor(frame, dtype=torch.float32).permute(2, 0, 1).unsqueeze(0)
    with torch.no_grad():
        output = model(frame)
    return output.argmax(dim=1).item()

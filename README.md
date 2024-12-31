# Face-Emotion-Detector

A real-time face emotion detection application using OpenCV and the FER library. The application detects faces using Haar Cascades and analyzes emotions with FER in a live webcam feed.

---

## Features ✨
- **Real-Time Face Detection**: Detects faces in a webcam feed using Haar Cascade Classifier.
- **Emotion Recognition**: Identifies the dominant emotion (e.g., happiness, anger, sadness) and its confidence score.
- **Live Feedback**: Displays detected emotions directly on the video feed.

---

## How It Works 🔍
1. **Face Detection**:
   - Uses OpenCV's Haar Cascade Classifier to identify and localize faces in the webcam feed.
2. **Emotion Detection**:
   - Extracts face regions and passes them to the `FER` library for emotion recognition.
3. **Display Results**:
   - Displays the detected emotion with its confidence percentage on the webcam feed.

---

## Requirements 🛠️

### Python Version
- Python 3.8 or higher

### Python Libraries
The dependencies for this project are listed in the `requirements.txt` file. Install them using:

```bash
pip install -r requirements.txt
```

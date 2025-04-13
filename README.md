# Expression Detection Project

This project is a real-time facial expression (emotion) detection system built with Python, OpenCV, and the `fer` library. It uses a webcam feed to detect faces and identify the dominant emotion being expressed.

## 🔍 Features

- Real-time emotion detection using your webcam
- Efficient performance by processing every 3rd frame
- Visual indicators with bounding boxes and emotion labels
- Utilizes OpenCV's Haar Cascade for face detection
- Powered by the `FER` deep learning model for emotion classification

## 🛠️ Technologies Used

- Python
- OpenCV (`cv2`)
- [FER](https://github.com/justinshenk/fer) (Facial Expression Recognition)

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/expression-detection.git
   cd expression-detection
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the required packages:**
   ```bash
   pip install opencv-python fer
   ```

## 🚀 Usage

Simply run the Python script:

```bash
python emotion_detection.py
```

Press **`q`** to quit the application.

## 📄 How It Works

- The webcam captures frames in real-time.
- OpenCV detects faces in the frame using Haar Cascade.
- Every third frame is processed to reduce computational load.
- The `FER` model analyzes the face regions and predicts emotions like:
  - Happy
  - Sad
  - Angry
  - Disgust
  - Fear
  - Neutral
  - Surprise
- The dominant emotion is displayed on top of each detected face.

## 📷 Output

The application opens a window titled **"Optimized Emotion Detection"** showing:
- Green rectangles around detected faces
- The name of the dominant emotion above each face

## ❗ Note

- Make sure your webcam is working and accessible.
- Lighting conditions can affect detection accuracy.

## 📌 Future Improvements

- Add support for recording or saving analysis results
- Enhance face-emotion matching accuracy for multiple faces
- Add GUI controls or emotion statistics

## 🧑‍💻 Author

Gurkirat Singh – [@Gurkirat2k3](https://github.com/Gurkirat2k3

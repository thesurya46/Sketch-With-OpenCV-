# Air Sketch :-

A simple air drawing application using hand tracking with MediaPipe and OpenCV.

## Description

Air Sketch turns your webcam into a virtual whiteboard. Using a single hand, you can draw in the air by making a "pinch" gesture (bringing thumb and index finger close together). The index fingertip acts as a virtual pen, drawing smooth red lines on a transparent canvas overlaid on the live camera feed.

## Features

- **Pinch-to-draw**: Bring thumb and index finger close to start drawing; release to stop.
- **Smooth drawing**: Lines are smoothed using exponential moving average for natural feel.
- **Clear button**: A virtual "CLEAR" button in the top-left corner. Pinch while hovering the index finger over it to erase the entire canvas.
- **Mirror view**: Camera feed is flipped horizontally for intuitive control.
- **Real-time hand landmarks**: Visual feedback with MediaPipe hand skeleton overlay.

## Requirements :

- Python 3.6+
- OpenCV (`opencv-python`)
- MediaPipe (`mediapipe`)
- NumPy (`numpy`)

## Installation
bash
pip install opencv-python mediapipe numpy

## Contact & Support
work.suryasnata@gmail.com


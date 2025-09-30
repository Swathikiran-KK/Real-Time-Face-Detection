# Real-Time Face Detection with OpenCV and MediaPipe

A minimal, real-time face detection app that uses a webcam stream to detect faces and draw bounding boxes with confidence scores. Built with OpenCV for video capture/rendering and MediaPipe Face Detection for fast on-device inference.

---

## Problem Statement

Detect human faces reliably and efficiently from a live camera feed for interactive use cases such as HCI prototypes, attendance/analytics dashboards, and camera UX overlays.

---

## Objectives

- Perform real-time multi-face detection on frames from a default webcam.
- Overlay tight bounding boxes and display per-face confidence scores.
- Keep the implementation lightweight, readable, and CPU-friendly.

---

## Methodology

- Capture frames with OpenCV’s `VideoCapture` and present results in a GUI window.
- Convert BGR frames to RGB before inference, aligning with MediaPipe’s vision models.
- Use MediaPipe Face Detection to get relative bounding boxes and scores per frame.
- Convert relative coordinates to pixel coordinates and draw overlays using OpenCV.

---

## Features

- Real-time face detection with per-frame updates.
- Multi-face support with confidence labels.
- Compact, production-ready script structure that’s easy to extend.

---

## Requirements

- Python 3.8+
- [OpenCV](https://pypi.org/project/opencv-python/)
- [MediaPipe](https://pypi.org/project/mediapipe/)


---

## Results

- Shows bounding boxes and confidence scores around detected faces in real time.
- Maintains smooth performance on typical laptop webcams.
- Works well with standard lighting; performance can degrade under poor lighting or occlusions.

---

## Limitations

- Detects faces but does not recognize or track identities.
- No temporal tracking of detected faces between frames.
- Sensitive to camera quality and environment conditions.

---

## Troubleshooting

- **Webcam not opening:** Ensure no other app is using the webcam; try changing camera index.
- **No detections:** Lower `min_detection_confidence` or improve lighting.
- **Mirrored video undesired:** Remove or modify the horizontal flip line (`cv2.flip`).

---

## Future Work

- Upgrade to MediaPipe’s new Tasks “Face Detector” API.
- Add Face Mesh detection for richer tracking and augmented reality effects.
- Incorporate face tracking algorithms to assign persistent IDs.
- Combine with face recognition models for identity verification.

---

## Acknowledgments

- OpenCV for video and graphics utilities.
- MediaPipe for efficient face detection solutions.



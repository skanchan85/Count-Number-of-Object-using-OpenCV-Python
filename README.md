# Count-Number-of-Object-using-OpenCV-Python

A Python-based computer vision application that detects and counts objects in images/video using OpenCV.

## Overview

Manually counting objects in images or video feeds is time-consuming and error-prone. This project uses image processing techniques with OpenCV to automatically detect and count objects, making it useful for inventory checks, quality control, and similar real-world tasks.

##  Features

-  **Object Detection** – Identifies distinct objects within an image/frame
-  **Automatic Counting** – Returns the total count of detected objects
-  **Image Processing Pipeline** – Uses techniques like grayscale conversion, thresholding, and contour detection
-  **Visual Output** – Displays the processed image with detected objects highlighted/labeled

## Tech Stack

- **Language:** Python
- **Library:** OpenCV
- **Concepts Used:** Image Processing, Contour Detection, Thresholding

##  Getting Started

### Prerequisites
- Python 3.x installed
- OpenCV library

### Installation & Running

1. Clone the repository
   ```bash
   git clone https://github.com/your-username/object-counting-opencv.git
   ```
2. Navigate to the project directory
   ```bash
   cd object-counting-opencv
   ```
3. Install dependencies
   ```bash
   pip install opencv-python numpy
   ```
4. Run the script
   ```bash
   python object_counter.py
   ```

##  Project Structure

```
Count-Number-of-Object-using-OpenCV-Python/
│-- object_counter.py
│-- Countin_object/
    │--static/ index.html
    │--.....
│--front.html
│--yolov8s.pt
│-- README.md
```

##  Future Improvements

- Real-time object counting via webcam feed
- Support for counting specific object types using ML-based classification
- Web-based interface for uploading and processing images
- Export count results to CSV/report

## Author

**Kanchan Salunkhe** <br>
Entry-level Software Developer | Pune, Maharashtra <br>
[Linkedin](https://www.linkedin.com/in/kanchan85)

## 📄 License

This project is open source and available for learning/demo purposes.

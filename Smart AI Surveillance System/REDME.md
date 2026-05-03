# 🧠 Smart AI Surveillance System (YOLO-based Object Detection)

## 📌 Overview

This project is a **real-time AI-based object detection system** built using Python. It uses the YOLO (You Only Look Once) model to detect and classify objects from:

* 📷 Images
* 🎥 Videos
* 📡 Live Webcam

The system also includes:

* 🚨 Custom alert detection
* 📊 Logging system (CSV)
* 🖥️ Interactive web interface

---

## 🚀 Features

* ✅ Real-time object detection using YOLOv8
* ✅ Webcam, Image, and Video support
* ✅ Custom object alert system (e.g., detect only "person")
* ✅ Automatic image capture when object is detected
* ✅ Detection logs stored in CSV file
* ✅ FPS (Frames Per Second) display
* ✅ Clean UI using Streamlit

---

## 🛠️ Tech Stack

* Python
* OpenCV
* Ultralytics YOLOv8
* Streamlit
* Pandas
* NumPy

---

## 📁 Project Structure

```
smart-ai-surveillance/
│── app.py
│── logs.csv          # Auto-generated
│── outputs/          # Saved detection images
```

---

## ⚙️ Installation & Setup (Run Locally)

### 🔹 Step 1: Clone or Download Project

```bash
git clone <your-repo-link>
cd smart-ai-surveillance
```

---

### 🔹 Step 2: Create Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate environment:

#### Windows:

```bash
venv\Scripts\activate
```

#### Mac/Linux:

```bash
source venv/bin/activate
```

---

### 🔹 Step 3: Install Dependencies

```bash
pip install ultralytics opencv-python streamlit pandas numpy
```

---

### 🔹 Step 4: Run the Application

```bash
python -m streamlit run app.py
```

👉 This will open the app in your browser (usually at `http://localhost:8501`)

---

## 🧪 How to Use

1. Open the app in browser
2. Select mode:

   * Webcam
   * Image Upload
   * Video Upload
3. Enter target object (e.g., `person`, `bottle`, `car`)
4. Start detection

---

## 📊 Output

* Detected objects with bounding boxes
* Confidence scores
* FPS (performance metric)
* Detection logs in `logs.csv`
* Captured images saved in `outputs/`

---

## 🧠 How It Works

1. Input is captured (image/video/webcam)
2. Each frame is passed to YOLO model
3. Model detects objects and returns:

   * Object label
   * Bounding box
   * Confidence score
4. OpenCV draws boxes on frame
5. If target object detected:

   * Log entry is created
   * Image is saved
6. Output is displayed in Streamlit UI

---

## 📌 Example Alert

If user sets:

```
Target Object: person
```

👉 System will:

* Detect "person"
* Save image in `outputs/`
* Log entry in `logs.csv`

---

## ⚠️ Troubleshooting

### ❌ Error: `streamlit not recognized`

✔ Use:

```bash
python -m streamlit run app.py
```

---

### ❌ Webcam not opening

✔ Check:

* Camera permissions
* Close other apps using camera

---

### ❌ Model not loading

✔ Ensure internet is available (first run downloads model)

---

## 🔥 Future Enhancements

* 🔊 Sound alert system
* 📧 Email notifications
* 🧠 Custom-trained YOLO model
* 📊 Dashboard with analytics
* 🌐 Cloud deployment

---

## 🎯 Use Cases

* Smart surveillance systems
* Security monitoring
* Smart cities
* Retail analytics
* Traffic monitoring

---

## 👨‍💻 Author

Your Name

---

## 📜 License

This project is for educational purposes.

---

## ⭐ Tip for Presentation

Say this line in your demo:

> "This system uses YOLOv8 for real-time object detection and supports multiple input modes with alert and logging functionality, making it suitable for surveillance and monitoring applications."

---

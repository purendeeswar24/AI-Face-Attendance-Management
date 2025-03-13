import gradio as gr
import cv2
import numpy as np
import pandas as pd
import os
import datetime
import pytz  # For IST timezone
import pickle
from insightface.app import FaceAnalysis

# Paths
IMAGE_PATH = "registered_faces/"
ATTENDANCE_FILE = "attendance.xlsx"
ENCODINGS_FILE = "face_encodings.pkl"

# Ensure required folders exist
os.makedirs(IMAGE_PATH, exist_ok=True)

# Initialize InsightFace model
face_app = FaceAnalysis(name="buffalo_l", providers=["CPUExecutionProvider"])
face_app.prepare(ctx_id=0, det_size=(640, 640))

# Set Indian Standard Time (IST)
IST = pytz.timezone("Asia/Kolkata")

# Function to compute and save face encodings
def compute_encodings():
    encodings = {}

    for filename in os.listdir(IMAGE_PATH):
        img_path = os.path.join(IMAGE_PATH, filename)
        img = cv2.imread(img_path)

        if img is None:
            continue  # Skip unreadable files

        faces = face_app.get(img)
        if faces:
            encodings[filename] = faces[0].normed_embedding.tolist()

    with open(ENCODINGS_FILE, "wb") as f:
        pickle.dump(encodings, f)

# Function to register a face
def register_face(name, image):
    if not name.strip():
        return "❌ Error: Please enter a valid name!"
    
    if image is None:
        return "❌ Error: Please upload an image!"

    # Convert Gradio image to OpenCV BGR format
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # Detect faces
    faces = face_app.get(image)

    if not faces:
        return "❌ No face detected! Please try again with a clearer image."

    img_path = os.path.join(IMAGE_PATH, f"{name}.jpg")

    # Save original image
    cv2.imwrite(img_path, image)

    # Compute and save encodings
    compute_encodings()

    return f"✅ Face registered successfully for {name}!"

# Function to recognize a face and mark attendance
def recognize_face(image):
    if image is None:
        return "❌ Error: Please upload an image!"
    
    if not os.path.exists(ENCODINGS_FILE) or not os.listdir(IMAGE_PATH):
        return "❌ No registered faces found!"

    with open(ENCODINGS_FILE, "rb") as f:
        known_encodings = pickle.load(f)

    # Convert Gradio image to OpenCV BGR format
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # Detect faces
    faces = face_app.get(image)

    if not faces:
        return "❌ No face detected!"

    test_embedding = np.array(faces[0].normed_embedding)

    # Compare with stored embeddings
    min_dist = float("inf")
    best_match = "Unknown"

    for name, encoding in known_encodings.items():
        dist = np.linalg.norm(np.array(encoding) - test_embedding)
        if dist < min_dist and dist < 1.2:  # Adjust threshold as needed
            min_dist = dist
            best_match = os.path.splitext(name)[0]

    if best_match != "Unknown":
        mark_attendance(best_match)
        return f"✅ Attendance marked for {best_match}!"
    else:
        return "❌ No matching face found!"

# Function to mark attendance
def mark_attendance(name):
    date_today = datetime.datetime.now(IST).strftime("%Y-%m-%d")
    current_time = datetime.datetime.now(IST).strftime("%H:%M:%S")

    try:
        df = pd.read_excel(ATTENDANCE_FILE)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Name", "Date", "Time"])

    new_entry = pd.DataFrame({"Name": [name], "Date": [date_today], "Time": [current_time]})
    df = pd.concat([df, new_entry], ignore_index=True)
    df.to_excel(ATTENDANCE_FILE, index=False)

# Function to download attendance file
def download_attendance():
    return ATTENDANCE_FILE if os.path.exists(ATTENDANCE_FILE) else "❌ No attendance records found!"

# Gradio UI
with gr.Blocks() as app:
    gr.Markdown("# 📸 Fast Facial Recognition Attendance System")
    
    with gr.Tab("Register Face"):
        name_input = gr.Textbox(label="Enter Name")
        image_input = gr.Image(label="Capture Face", type="numpy")
        register_btn = gr.Button("Register Face")
        register_output = gr.Markdown()
        register_btn.click(register_face, inputs=[name_input, image_input], outputs=register_output)
    
    with gr.Tab("Mark Attendance"):
        image_input2 = gr.Image(label="Upload or Capture Face", type="numpy")
        recognize_btn = gr.Button("Recognize & Mark Attendance")
        recognize_output = gr.Markdown()
        recognize_btn.click(recognize_face, inputs=[image_input2], outputs=recognize_output)
    
    with gr.Tab("Download Attendance"):
        download_btn = gr.Button("Download Attendance Excel")
        download_output = gr.File()
        download_btn.click(download_attendance, outputs=download_output)

# Run Gradio app
app.launch()

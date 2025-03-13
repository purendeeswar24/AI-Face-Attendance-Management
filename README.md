# **Fast Facial Recognition Attendance System - README**  -🔗 Live Demo: https://huggingface.co/spaces/purendeeswar/Face-Attendance-Pro

## **📌 Overview**  
The **Fast Facial Recognition Attendance System** is a **Gradio-based AI application** that enables **efficient and automated attendance tracking** using **facial recognition**. The system allows users to:  

✅ **Register Faces** – Capture and store facial embeddings for employees/students.  
✅ **Recognize Faces & Mark Attendance** – Automatically identify registered faces and record attendance.  
✅ **Download Attendance Reports** – Export attendance logs in **Excel format** for record-keeping.  

This application utilizes **InsightFace for facial analysis**, **OpenCV for image processing**, and **Pandas for attendance management**.  

---

## **📂 Project Structure**  

```
📦 Fast-Facial-Recognition-Attendance  
 ┣ 📂 registered_faces/      # Directory to store registered face images  
 ┣ 📜 attendance.xlsx        # Excel file for storing attendance records  
 ┣ 📜 face_encodings.pkl     # Pickle file for storing face embeddings  
 ┣ 📜 main.py                # Main Gradio application script  
 ┣ 📜 requirements.txt       # Required dependencies  
 ┣ 📜 README.md              # Project documentation  
```

---

## **🛠 Technologies Used**  

- **Python 3.x** – Core programming language  
- **Gradio** – For UI and web-based interaction  
- **OpenCV** – For image processing  
- **InsightFace** – AI-powered facial recognition  
- **NumPy** – Mathematical operations  
- **Pandas** – Attendance record handling  
- **Pickle** – Data storage for face encodings  
- **Pytz** – Timezone management (Indian Standard Time)  

---

## **🚀 Features**  

### **1️⃣ Face Registration**  
- Users can upload or capture an image of their face.  
- The system detects and extracts facial features.  
- The image is saved in the `registered_faces/` directory.  
- Facial embeddings are computed and stored in `face_encodings.pkl`.  

### **2️⃣ Face Recognition & Attendance Marking**  
- Users upload or capture their face to check-in.  
- The system compares the face with registered encodings.  
- If a match is found, attendance is recorded in `attendance.xlsx`.  
- The system ensures **duplicate attendance is avoided for the same day**.  

### **3️⃣ Attendance Report Download**  
- Users can download attendance records in **Excel format**.  
- Attendance logs include **Name, Date, and Time**.  

---

## **💻 Installation & Setup**  

### **Step 1: Clone the Repository**  
```sh
git clone https://github.com/your-repo/Fast-Facial-Recognition-Attendance.git
cd Fast-Facial-Recognition-Attendance
```

### **Step 2: Install Dependencies**  
Ensure **Python 3.x** is installed. Then, install the required packages:  
```sh
pip install -r requirements.txt
```

### **Step 3: Run the Application**  
```sh
python main.py
```
**➡ The Gradio interface will launch in your browser!**  

---

## **📌 Configuration & Customization**  

🔹 **Adjust Face Recognition Sensitivity:** Modify the **distance threshold** inside the `recognize_face()` function (`1.2` can be adjusted for accuracy).  
🔹 **Set a Different Timezone:** Modify the `IST = pytz.timezone("Asia/Kolkata")` setting in `main.py`.  
🔹 **Change Storage Paths:** Update `IMAGE_PATH`, `ATTENDANCE_FILE`, and `ENCODINGS_FILE` variables.  

---

## **📝 Attendance Data Format**  

| Name  | Date       | Time     |  
|--------|------------|------------|  
| John Doe  | 2024-03-12  | 09:15:30 |  
| Alice Smith  | 2024-03-12  | 09:17:45 |  
| Bob Johnson  | 2024-03-12  | 10:02:10 |  

- **Date Format:** `YYYY-MM-DD`  
- **Time Format:** `HH:MM:SS (IST)`  

---

## **🔍 Troubleshooting & FAQs**  

### **1️⃣ No Face Detected Error**  
✔ Ensure **proper lighting** and **clear visibility of face**.  
✔ Try **different angles or closer positioning** to the camera.  
✔ Use **high-resolution images** for better detection.  

### **2️⃣ No Matching Face Found**  
✔ Ensure the **face is registered before attempting recognition**.  
✔ Re-register the face with a **clearer image**.  
✔ Lower the **distance threshold** in the `recognize_face()` function.  

### **3️⃣ Gradio App Not Launching**  
✔ Check for missing dependencies using `pip install -r requirements.txt`.  
✔ Restart the script using `python main.py`.  
✔ Try opening `http://127.0.0.1:7860/` manually in the browser.  

---

## **📜 License**  
This project is licensed under the **MIT License**.  

---

## **👥 Contributors**  
Developed by **[Your Name]**  
📧 Email: [Your Email]  
🔗 LinkedIn: [Your LinkedIn Profile]  

---

## **💡 Future Enhancements**  
🔹 Implement **Live Camera Detection** instead of static image uploads.  
🔹 Add **Multi-Face Recognition** for group attendance marking.  
🔹 Integrate with **Cloud Storage** for remote attendance tracking.  
🔹 Develop a **Mobile-Friendly Version** using a React/Flutter UI.  

---

## **⭐ Support & Feedback**  
If you find this project useful, **give it a star ⭐ on GitHub!**  
For feedback or feature requests, **open an issue or contact me directly.**  

🚀 **Let’s build smarter attendance systems together!**  

---

This README provides a **professional, structured, and user-friendly guide** to your **Facial Recognition Attendance System**. Let me know if you'd like any modifications! 😊

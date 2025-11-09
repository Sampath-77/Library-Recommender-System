# 📚 Contextual Library Book Recommender System

A Machine Learning powered **Library Book Recommendation System** that suggests books based on the *context* of the reader — such as subject, genre, age group, reading level, and user-input keywords.  
This project demonstrates **data preprocessing, NLP feature extraction, vector similarity, and deployment using Streamlit**.

---

### 👨‍💻 Created by: **Sampath Kumar N A**

---

## 📌 Features

✅ Context-aware recommendation (genre + subject + tags + keywords)  
✅ NLP-based book similarity using **TF-IDF / CountVectorizer + cosine similarity**  
✅ Cleaned and preprocessed library dataset  
✅ `.pkl` model + metadata files for fast loading  
✅ Streamlit web interface for user interaction  
✅ Search-based book selection  
✅ Lightweight & fast — suitable for mini project demo  
✅ Extensible for library management systems  

---

## 📂 Repository Structure

├── contextual_library_recommender.ipynb # Jupyter Notebook (data cleaning + model building)
├── book_dict.pkl # Dictionary of all books + metadata
├── similarity.pkl # Precomputed similarity matrix
├── app.py # Streamlit application
├── requirements.txt # Dependencies list
├── DATASET.csv # Library book dataset
├── IMAGE_INPUT.png # Screenshot: User input interface
└── IMAGE_OUTPUT.png # Screenshot: Recommendation output

yaml
Copy code

---

## ⚙️ Installation & Setup

1️⃣ Clone the Repository
```bash
git clone <your-github-repo-url>
cd Contextual-Library-Recommender
```
---
2️⃣ Install Dependencies
```bash
Copy code
pip install -r requirements.txt
```
---
3️⃣ Run the App
```bash
Copy code
streamlit run app.py
🧠 How It Works
🧹 Data Cleaning & Preprocessing
Removed null values and duplicates

Extracted useful book fields (title, author, genre, category, summary, etc.)

Created a context column by combining multiple features
```
---
##🔍 NLP & Similarity Model
``` bash
Converted book text features into vectors using TF-IDF / CountVectorizer

Calculated similarity using Cosine Similarity

Exported processed objects → book_dict.pkl and similarity.pkl
```
---
##⚡ Fast Runtime via Pickle
```bash
Model trained once in notebook

Streamlit app loads .pkl files for instant recommendation
```
---
##🌐 Deployment
```bash
UI built using Streamlit

Can be deployed locally or hosted via Streamlit Cloud / ngrok
```
---
##🎥 Screenshots
```bash
Input Interface	Output Recommendation
	
```
---
##📌 More About This Project
```bash
🔹 Designed as a mini project for academic submission
🔹 Can be integrated into digital library management systems
🔹 Works offline — no external API required
🔹 Can be extended to hybrid/user-based recommendation later
🔹 Demonstrates ML + NLP + Deployment skills in a small scale use case
```
---
🔗 Connect With Me
👨‍💻 GitHub: [https://github.com/Sampath-77]
💼 LinkedIn: [https://www.linkedin.com/in/sampth/]
---
**Project By: Sampath Kumar N A

# 🏥 Dr Symp  
### Smart Symptom-Based Screening & Hospital Routing System

Dr Symp is a full-stack web application designed to **reduce overcrowding at hospital reception counters** by digitizing the initial screening and routing process.

Instead of standing in long queues just to get assigned a department, patients can now **identify their probable disease, department, and hospital before even arriving**.

---

## 🚨 Problem Statement

Hospitals, especially in urban areas, face severe **overcrowding at reception and screening counters**.

Patients typically:
- Wait in long queues for registration  
- Are unsure which department to visit  
- Get incorrectly routed, causing delays  
- Increase congestion in already crowded systems  

This leads to:
- Inefficient hospital workflows  
- Delayed treatment  
- Frustrating patient experience  

---

## 🎯 Objective

To **minimize hospital counter congestion** by:

- Digitizing symptom-based screening  
- Predicting probable diseases early  
- Routing patients to correct departments  
- Allowing pre-visit hospital selection  
- Generating digital receipts in advance  

---

## 💡 Solution Overview

Dr Symp introduces a **pre-hospital digital screening system** where users:

1. Enter personal details  
2. Select symptoms via UI  
3. Get predicted diseases  
4. View corresponding departments  
5. Find hospitals offering those departments  
6. Download a digital appointment receipt  

---

## ⚙️ Key Features

- 🧠 Symptom-based disease prediction  
- ⚖️ Weighted matching algorithm  
- 🏥 Department mapping system  
- 📍 Hospital filtering based on departments  
- 📄 PDF receipt generation  
- 🔐 Token-based access (no login required)  
- ⚡ Dynamic UI with real-time results  

---

## 🏗️ System Architecture

```
                ┌──────────────────────┐
                │      User (Browser)  │
                │  (HTML + Bootstrap)  │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │   Frontend (JS UI)   │
                │  - Symptom Selector  │
                │  - Accordion UI      │
                │  - Hospital Cards    │
                └──────────┬───────────┘
                           │ HTTP Requests
                           ▼
                ┌──────────────────────┐
                │   Flask Backend      │
                │   (Application Layer)│
                └──────────┬───────────┘
                           │
        ┌──────────────────┼──────────────────┐
        ▼                  ▼                  ▼
┌──────────────┐  ┌────────────────┐  ┌────────────────┐
│ Disease      │  │ Hospital       │  │ PDF Generation │
│ Service      │  │ Service        │  │ Service        │
│              │  │                │  │                │
│ - Matching   │  │ - Dept → Hosp  │  │ - Receipt Gen  │
│ - Weight Calc│  │ - Filtering    │  │ - Download     │
└──────┬───────┘  └──────┬─────────┘  └──────┬─────────┘
       │                 │                   │
       └────────────┬────┴──────────────┬────┘
                    ▼                   ▼
              ┌────────────────────────────┐
              │        SQLite DB           │
              │----------------------------│
              │ patients                   │
              │ symptom_table              │
              │ disease_table              │
              │ disease_symptom_mapping    │
              │ department_disease         │
              │ hospitals                  │
              │ hospital_department        │
              └────────────────────────────┘

```
---

## 🧠 Core Workflow

1. User inputs symptoms  
2. Symptoms mapped to IDs  
3. Weighted matching algorithm runs  

4. Top diseases are ranked  
5. Diseases mapped to departments  
6. Hospitals filtered by departments  
7. User selects hospital  
8. PDF receipt is generated  

---

## 🗄️ Database Design

### Main Tables

- **patients** → stores user data  
- **symptom_table** → list of symptoms  
- **disease_table** → diseases  
- **disease_symptom_mapping_weighted** → prediction logic  
- **department_disease** → disease → department mapping  
- **hospitals** → hospital list  
- **hospital_department** → hospital → department mapping  

---

## 🧩 Project Structure

```
byteverse26/
│
├── app/                        # Main application package
│   │
│   ├── __init__.py            # App factory + DB init
│   ├── models.py              # All DB models
│   │
│   ├── routes/                # Route controllers
│   │   ├── main.py            # Main UI routes
│   │   ├── api.py             # API endpoints (hospitals)
│   │   └── pdf.py             # PDF generation routes
│   │
│   ├── services/              # Business logic layer
│   │   ├── disease.py         # Disease prediction logic
│   │   └── hospital.py        # Hospital search logic
│   │
│   ├── templates/             # Jinja2 HTML templates
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── book_appointment.html
│   │
│   ├── static/                # Static assets
│   │   ├── css/
│   │   │   ├── style.css
│   │   │   └── section.css
│   │   ├── js/
│   │
│
├── instance/                  # Database folder
│   └── project.db             # SQLite database
│
├── run.py                     # Entry point
├── init_db.py                 # DB creation script (optional)
├── requirements.txt           # Dependencies
└── README.md

```

---

## 🔐 Security Approach

- Each user gets a **unique access token**
- No login required  
- Users can only access their own data via token  

---

## ⚡ Tech Stack

### Frontend
- HTML  
- CSS  
- Bootstrap  
- JavaScript  

### Backend
- Flask  
- SQLAlchemy  

### Database
- SQLite  

### Tools
- ReportLab (PDF generation)

---

## 🚀 Installation & Setup

### 1. Clone Repository
```
git clone https://github.com/Nitish1244219211/byteverse26
```
---

### 2. Install Dependencies
```
pip install flask flask_sqlalchemy reportlab
```
---
### 3. Setup Environment
```
python3 -m venv .venv
```
---
### 4. Activate Environment
#### For Windows
```
.venv\Scripts\activate
```
#### For Mac/Linux
```
.venv/bin/activate
```
---
### 5. Run Application
```
python run.py
```
---

## 🌱 Future Enhancements

- Real-time hospital slot booking  
- Doctor availability integration  
- AI chatbot for symptom input  
- Mobile app version  
- Integration with hospital systems  

---

## 🏁 Conclusion

Dr Symp transforms the **manual, overcrowded hospital entry process** into a **smart, digital-first experience**, reducing wait times and improving patient routing efficiency.

---

## 💬 Tagline

**Dr Symp — Skip the queue. Get the care.**
# 📊 AutoEDA Agentic AI
<img width="1920" height="1080" alt="Screenshot (40)" src="https://github.com/user-attachments/assets/b42c9dd7-a640-48fc-81d4-1f573f400702" />
<img width="1920" height="1080" alt="Screenshot (41)" src="https://github.com/user-attachments/assets/2c85ae07-7529-429d-9108-35c3701ae661" />


An **Agentic AI-powered Data Analysis platform** that allows users to upload any CSV dataset and automatically perform:

- Exploratory Data Analysis (EDA)
- Data Cleaning
- Conversational Data Analysis (Chat with Data)
- Rule-based AutoML
- Report Export

Built using **Streamlit**, **scikit-learn**, and **Groq LLaMA models**.

---

## 🚀 Features

✅ Upload any CSV dataset  
✅ Automatic target detection  
✅ Data quality & statistical analysis  
✅ Correlation discovery  
✅ Data cleaning agent  
✅ Chat with dataset using LLM  
✅ Rule-based AutoML (classification & regression)  
✅ Export analysis report  

---

## 🧠 Agent Architecture

Each stage of the pipeline is implemented as an **independent AI agent**:

| Agent | File | Responsibility |
|-----|-----|----------------|
| UI Orchestrator | `app.py` | Streamlit interface |
| EDA Agent | `eda.py` | Data understanding |
| Cleaning Agent | `clean.py` | Handle missing values & duplicates |
| Chat Agent | `chat_agent.py` | LLM-powered Q&A |
| AutoML Agent | `automl.py` | Model training & evaluation |
| Export Agent | `export.py` | Generate reports |

---

## 🤖 AutoML Strategy

This project implements a **rule-based AutoML pipeline** using scikit-learn:

- Automatically detects problem type
- Selects baseline + ensemble models
- Evaluates performance using:
  - Accuracy (classification)
  - R² score (regression)

Models used:
- Linear / Logistic Regression
- Random Forest

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Pandas, NumPy
- scikit-learn
- Groq LLaMA 3.1
- Matplotlib & Seaborn

---

## 📦 Installation

```bash
git clone https://github.com/your-username/AutoEDA-Agentic-AI.git
cd AutoEDA-Agentic-AI
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt

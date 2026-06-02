# resume-analyzer-nlp
Resume anlyzer project usign spacy , nltk , pdfplumber , docx library

NOTE :- Open this code in integrated terminal to run this code 

# Resume Analyzer using NLP

An intelligent Resume Analyzer built using Python, NLTK, spaCy, Regex, and PDF/DOCX processing libraries.

This project automatically extracts important information from resumes such as:

* Candidate Name
* Email Address
* Phone Number
* Technical Skills

The system supports both PDF and DOCX resume formats.

---

# Features

* PDF Resume Parsing using pdfplumber
* DOCX Resume Parsing using python-docx
* NLP-based text preprocessing using NLTK
* Named Entity Recognition (NER) using spaCy
* Regex-based email and phone extraction
* Skill extraction using keyword matching
* Modular and reusable architecture

---

# Technologies Used

* Python
* NLTK
* spaCy
* Regex
* pdfplumber
* python-docx

---

# Project Workflow

Resume File
↓
Text Extraction
↓
Text Cleaning
↓
NER & Regex Extraction
↓
Skills Detection
↓
Structured Output

---

# Installation

Clone the repository:

```bash
git clone <your-github-repo-link>
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install spaCy model:

```bash
python -m spacy download en_core_web_sm
```

---

# Run the Project

```bash
python main.py
```

---

# Sample Output

```python
{
'name': 'Aman Kumar',
'email': 'aman67834@gmail.com',
'phone': '6798237812', 
'skills': ['machine learning', 'sql', 'power bi', 'nlp', 'python', 'numpy', 'java', 'pandas']
}
```

---

# Future Improvements

* ATS Resume Scoring
* Job Description Matching
* Streamlit Web Application
* OCR Support for Image-based Resumes
* Transformer-based NLP Models
* Advanced Skill Matching using PhraseMatcher

---

# Learning Outcomes

Through this project, I learned:

* NLP preprocessing techniques
* Resume parsing architecture
* Named Entity Recognition (NER)
* Regex pattern matching
* File processing in Python
* Modular software design
* Practical application of NLP in real-world systems

---

# Author

Aman Kumar

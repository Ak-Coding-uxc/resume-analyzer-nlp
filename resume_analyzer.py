import re
import pdfplumber
import spacy

from docx import Document

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nlp = spacy.load("en_core_web_sm")

SKILLS_DB = [
    "python",
    "java",
    "sql",
    "machine learning",
    "deep learning",
    "nlp",
    "tensorflow",
    "pandas",
    "numpy",
    "excel",
    "power bi"
]

def extract_pdf_text(file_path):

    full_text = ""

    with pdfplumber.open(file_path) as pdf:

        for page in pdf.pages:

            text = page.extract_text()

            if text:
                full_text += text + "\n"

    return full_text

def extract_docx_text(file_path):

    doc = Document(file_path)

    all_text = []

    for para in doc.paragraphs:
        all_text.append(para.text)

    return "\n".join(all_text)


def clean_text(text):

    # LOWERCASE
    text = text.lower()


    # REMOVE SPECIAL CHARACTERS
    text = re.sub(r"[^a-zA-Z0-9 ]", " ", text)


    # TOKENIZATION
    tokens = word_tokenize(text)


    # STOPWORDS
    stop_words = set(stopwords.words("english"))


    filtered_words = []


    for word in tokens:

        if word not in stop_words:

            filtered_words.append(word)


    # LEMMATIZATION
    lemmatizer = WordNetLemmatizer()


    final_words = []


    for word in filtered_words:

        lemma = lemmatizer.lemmatize(word)

        final_words.append(lemma)


    return final_words

def extract_email(text):

    match = re.search(r"\S+@\S+", text)

    if match:
        return match.group()

    return None

def extract_phone(text):

    match = re.search(r"\d{10}", text)

    if match:
        return match.group()

    return None

def extract_name(text):

    doc = nlp(text)

    for ent in doc.ents:

        if ent.label_ == "PERSON":
            return ent.text

    return None

def extract_skills(text):

    text = text.lower()

    
    text = re.sub(r"[^a-zA-Z0-9 ]", " ", text)


    found_skills = []


    for skill in SKILLS_DB:

        if skill in text:
            found_skills.append(skill)


    return list(set(found_skills))

def analyze_resume(file_path):


    # CHECK FILE TYPE
    if file_path.endswith(".pdf"):

        text = extract_pdf_text(file_path)

    
    elif file_path.endswith(".docx"):

        text = extract_docx_text(file_path)

    
    else:
        return "Unsupported file format"



    # EXTRACT INFORMATION
    name = extract_name(text)

    email = extract_email(text)

    phone = extract_phone(text)

    skills = extract_skills(text)



    # FINAL OUTPUT
    result = {

        "name": name,
        "email": email,
        "phone": phone,
        "skills": skills
    }


    return result

result = analyze_resume("dummy_resume.pdf")

print(result)

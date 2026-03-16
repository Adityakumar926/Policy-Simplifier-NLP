# Policy Simplifier NLP

An intelligent **Policy Simplification System** that converts complex policy or legal text into simple and easy-to-understand language using **Natural Language Processing (NLP)** and **Machine Learning**.

This project is designed to help users understand complicated policies from government, finance, or organizational documents by simplifying them into clear and readable text.

---

## Project Overview

Policies and legal documents are often written in complex language that is difficult for the general public to understand.  
This system uses **NLP techniques and transformer-based models** to simplify policy text automatically.

The system can:

- Accept complex policy text as input
- Analyze and process the text using NLP
- Simplify the sentences while keeping the meaning intact
- Display a clearer and easier version of the policy

---

## Features

- Policy text simplification using NLP
- Transformer-based language model support
- Rule-based simplification techniques
- Grammar correction and readability improvement
- Web interface using Flask
- Supports long policy inputs

---

## Technologies Used

- Python
- Flask
- Natural Language Processing (NLP)
- Transformers Library
- PyTorch
- NLTK
- HTML / CSS
- Machine Learning

---

## Project Structure

```
Policy-Simplifier-NLP
│
├── app.py
├── model.py
├── test.py
├── requirements.txt
├── Indian_Policy_Texts.docx
│
├── instance
│ └── users.db
│
├── templates
│ ├── index.html
│ ├── login.html
│ ├── register.html
│ ├── forgot_password.html
│ └── reset_password.html
│
└── README.md
```

---

## Installation

### 1. Clone the repository
git clone https://github.com/Adityakumar926/Policy-Simplifier-NLP.git

### 2. Navigate to the project directory
cd Policy-Simplifier-NLP

### 3. Install dependencies
pip install -r requirements.txt

---

## Running the Project

Start the Flask server:
python app.py

Then open your browser and go to:
http://127.0.0.1:5000/

---

## Example Use Case

**Input (Complex Policy Text):**

> "Employees are required to adhere to organizational compliance protocols and ensure adherence to regulatory standards."

**Simplified Output:**

> "Employees must follow company rules and meet required regulations."

---

## Future Improvements

- Multi-language policy simplification
- Improved summarization techniques
- Better semantic understanding
- Integration with government policy datasets
- Advanced readability scoring

---

## Author

**Aditya Kumar**

B.Tech – Computer Science Engineering  
Machine Learning & NLP Enthusiast

GitHub:  
https://github.com/Adityakumar926

---

## License

This project is for educational and research purposes.

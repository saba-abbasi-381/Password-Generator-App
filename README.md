# 🔐 Password Generator

A simple and interactive password generator built with **Python and Streamlit**. The application allows users to choose a password length and optionally include symbols when generating a random password.

## 📌 Overview

The **Password Generator** is a beginner-friendly Python project developed to practice random data generation, string handling, functions, conditional logic, and Streamlit application development.

Users can select a password length between **4 and 50 characters** and choose whether symbols should be included in the generated password.

The password is generated using combinations of:

* Uppercase letters
* Lowercase letters
* Numbers
* Optional symbols

## ✨ Features

* 🔐 Generate random passwords
* 🔢 Choose password length from 4 to 50 characters
* 🔤 Include uppercase and lowercase letters
* 🔢 Include numbers
* 🔣 Optional symbols
* ⚠️ Validate password length
* 🖥️ Simple and interactive Streamlit interface

## 🛠️ Technologies Used

* **Python**
* **Streamlit**
* **random module**
* **string module**
* **Python Functions**

## 🧩 Project Structure

```text
Password-Generator/
│
├── app.py
├── backend.py
├── requirements.txt
└── README.md
```

### `app.py`

Contains the Streamlit frontend and handles:

* Password length input
* Symbol selection
* Generate button interaction
* Displaying the generated password
* Showing validation messages

### `backend.py`

Contains the `password_generator()` function responsible for:

* Validating the requested password length
* Creating the available character set
* Adding symbols when requested
* Randomly selecting characters
* Returning the generated password

### `requirements.txt`

Contains the Python dependency required to run the application:

```text
streamlit
```

## 🔄 How It Works

The application follows this process:

```text
Select Password Length
        ↓
Choose Whether to Include Symbols
        ↓
Validate Length
        ↓
Create Character Set
        ↓
Randomly Select Characters
        ↓
Generate Password
        ↓
Display Result
```

### Password Character Set

Without symbols, the generator uses:

```text
Letters + Numbers
```

When symbols are enabled:

```text
Letters + Numbers + Symbols
```

## ⚙️ Installation & Usage

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Open the project directory

```bash
cd Password-Generator
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## 🧠 Python Concepts Practiced

This project helped me practice:

* Defining and calling functions
* Function parameters
* Conditional statements
* String manipulation
* Python's `string` module
* Python's `random` module
* Random character selection
* Input validation
* Streamlit widgets
* Displaying results dynamically

## 📚 What I Learned

Through this project, I practiced turning a simple Python function into an interactive web application.

I learned how to:

* Work with Python's built-in `string` module
* Generate random values using `random`
* Build a configurable password generator
* Validate user input
* Connect backend Python logic with a Streamlit frontend
* Manage Python dependencies using `requirements.txt`

## 🔮 Future Improvements

Possible future improvements include:

* Use Python's `secrets` module for security-focused password generation
* Add options for excluding similar characters
* Add an option to require at least one number, uppercase letter, lowercase letter, and symbol
* Add password strength feedback
* Add a copy-to-clipboard feature
* Improve the user interface
* Add more customization options

## 👩‍💻 Author

**Saba Abbasi**

Aspiring AI Engineer | Python Developer

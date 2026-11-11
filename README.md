# Farah Moutaki — Personal Portfolio

## About

This repository contains my personal portfolio website, developed using **Python** and **Streamlit** as part of the *Fundamentals of Programming* course (M1 SIA, Université Bourgogne Europe).

The website presents my academic background, professional experience, technical skills, personal projects and interests. It also provides access to my GitHub and LinkedIn profiles, as well as a contact form.

## Website Pages

The portfolio is organized into seven sections:

- **About Me:** Personal introduction and profile.
- **Education:** Academic background, certifications and languages.
- **Experience:** Professional experience and previous positions.
- **Projects:** Programming projects with descriptions, GitHub links and tag-based filtering.
- **Skills:** Technical skills and proficiency levels.
- **My Interests:** Personal interests and hobbies.
- **Contact Me:** Contact form.

## Technologies Used

- **Python:** Main programming language.
- **Streamlit:** Web application framework and interface.
- **Pandas:** Data handling and visualization.
- **Git & GitHub:** Version control and project hosting.

## Project Structure

```text
portfolio/
│
├── app.py
├── hello.py
├── data.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── pages/
│   ├── home.py
│   ├── education.py
│   ├── experience.py
│   ├── projects.py
│   ├── skills.py
│   ├── my_interests.py
│   └── contact.py
│
├── assets/
│   ├── photo.jpeg
│   └── ...
│
└── .streamlit/
    └── config.toml
```

The `app.py` file configures the application and its navigation. The `data.py` file centralizes the website content, while the individual Python files in the `pages/` directory handle the display of each section. The `assets/` directory contains the images and other resources used throughout the website.

## Installation and Execution

### Requirements

- Python 3
- pip

### 1. Clone the repository

```bash
git clone https://github.com/farahmprojects/portfolio.git
cd portfolio
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
streamlit run app.py
```

The website will then be available locally at:

`http://localhost:8501`

## Author

**Farah Moutaki**

- [GitHub](https://github.com/farahmprojects)
- [LinkedIn](https://www.linkedin.com/in/farah-moutaki-a05477421/)
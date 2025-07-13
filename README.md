# 🧾 Resume Builder Web App (Flask + HTML to PDF)

This is a simple and functional web application developed using **Python Flask** that allows users to fill in their resume details and generate a professional PDF resume instantly.  
The app uses `pdfkit` with `wkhtmltopdf` to convert a dynamic HTML template into a downloadable PDF.

---

## 🚀 Features

- 📝 Resume form with fields like name, email, skills, and projects
- 📄 Generates clean, professional resume as PDF
- ⚙️ Uses Flask for backend and Jinja2 for templating
- 🧾 Converts HTML to PDF using `pdfkit` and `wkhtmltopdf`
- 💻 Easy to run locally and customize layout/style

---

## 🧰 Tech Stack

- **Frontend:** HTML, CSS (Basic), Jinja2 (Templating)
- **Backend:** Python Flask
- **PDF Generator:** pdfkit + wkhtmltopdf
- **Runtime:** Python 3.x

---

## 📁 Folder Structure

resume-builder-flask/
├── app.py
├── templates/
│ ├── resume_form.html
│ └── resume_template.html
├── output/ ← Generated PDF stored here
└── README.md

yaml
Copy
Edit

---

## 🛠️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/resume-builder-flask.git
cd resume-builder-flask
2. Install Required Packages
bash
Copy
Edit
pip install flask
pip install pdfkit
3. Install wkhtmltopdf
Download & install for Windows (64-bit):
🔗 https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_msvc2015-win64.exe

⚠️ Important: Add this path to your system environment variables:

makefile
Copy
Edit
C:\Program Files\wkhtmltopdf\bin
Or manually set the path in your app.py like this:

python
Copy
Edit
path_to_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)
▶️ Run the App
bash
Copy
Edit
python app.py
Open browser and go to:

arduino
Copy
Edit
http://localhost:5000
Fill out the resume form

Click "Generate Resume"

Your resume will download as a PDF

🧠 Project Summary
This project shows the ability to build a real-world Flask app that handles user input, uses templating, and integrates external tools (wkhtmltopdf) for PDF generation.
It demonstrates full-stack understanding, form handling, file processing, and output delivery.

🙌 Author
Tellamekala Harikrishna
Final Year CS–IoT Student at QIS College of Engineering and Technology, Ongole, AP.
Passionate about Web Development & Python Projects.

🔗 GitHub: github.com/harikrishnatellamekala

🔗 LinkedIn: linkedin.com/in/tellamekala-harikrishna

📌 Note
This project was created as part of my learning journey to explore full-stack concepts using Flask and PDF generation techniques.
Future upgrades may include dynamic templates, authentication, and database storage.

yaml
Copy
Edit

---

### ✅ Final Steps for You:

- Replace `your-username` in the clone link with your GitHub username
- Save this content into your project folder as `README.md`
- Push to GitHub:

```bash
git add README.md
git commit -m "Added Resume Builder Project README"
git push

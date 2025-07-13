from flask import Flask, render_template, request, send_file
import pdfkit
import os

app = Flask(__name__)

# ✅ Set path to wkhtmltopdf.exe
path_to_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)

# ✅ PDF generation options
options = {
    'enable-local-file-access': '',
    'quiet': '',
    'disable-smart-shrinking': '',
    'load-error-handling': 'ignore',
    'load-media-error-handling': 'ignore'
}

@app.route('/')
def form():
    return render_template("resume_form.html")

@app.route('/create-resume', methods=['POST'])
def create_resume():
    data = request.form
    html = render_template("resume_template.html", data=data)

    # ✅ Debug prints
    print("[✔] Resume HTML generated.")
    print("[✔] Saving to PDF...")

    output_path = "output/resume.pdf"

    try:
        pdfkit.from_string(html, output_path, configuration=config, options=options)
        print("[✔] PDF generation complete:", os.path.exists(output_path))
    except Exception as e:
        print("[❌] PDF generation failed:", str(e))
        return f"Error occurred: {e}"

    return send_file(output_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

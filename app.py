from flask import Flask, render_template, make_response
import pdfkit

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/print')
def print_cv():
    return render_template('print.html')


@app.route('/download-cv')
def download_cv():
    options = {
        'page-size': 'A4',
        'margin-top': '0mm',
        'margin-right': '0mm',
        'margin-bottom': '0mm',
        'margin-left': '0mm',
        'encoding': "UTF-8",
        'custom-header': [
            ('Accept-Encoding', 'gzip')
        ],
        'no-outline': None,
        'enable-local-file-access': True,  # Allow local file access if needed for images
    }
        
    rendered = render_template('print.html')
    pdf = pdfkit.from_string(rendered, False,options=options)
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=cv.pdf'
    return response

if __name__ == "__main__":
    app.run(port=5000,debug=True)

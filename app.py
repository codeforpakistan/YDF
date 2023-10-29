import os
import uuid
from flask import Flask, request, render_template
import PyPDF2  # or import pdfplumber

from openai_helpers import get_completion_from_messages

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("upload.html")


@app.route("/upload", methods=["POST"])
def upload():
    uploaded_file = request.files["file"]

    if uploaded_file.filename != "":
        # Save the uploaded PDF file in a temporary folder named data,
        # if the folder doesn't exist, create one.

        if not os.path.exists("data"):
            os.makedirs("data")
        pdf_filename = os.path.join("data", str(uuid.uuid4()) + uploaded_file.filename)
        uploaded_file.save(pdf_filename)

        # Parse the PDF file using PyPDF2
        parsed_pdf_in_dict = parse_pdf_with_pyPDF2(pdf_filename)

        # change the dict to text format for display, key will be page num
        text = ""
        for page_num in parsed_pdf_in_dict.keys():
            text += f"{page_num}: {parsed_pdf_in_dict[page_num]}\n"

        response = get_completion_from_messages(text)

        # or, parse the PDF file using pdfplumber
        # text = parse_pdf_with_pdfplumber(pdf_filename)

        return response
    return "No file uploaded."


# return json format text per page num
def parse_pdf_with_pyPDF2(pdf_filename):
    result = {}
    with open(pdf_filename, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page_num in range(len(pdf_reader.pages)):
            # text += pdf_reader.pages[page_num].extract_text()
            result[page_num] = pdf_reader.pages[page_num].extract_text()
    return result


# Or, if you prefer using pdfplumber:
# def parse_pdf_with_pdfplumber(pdf_filename):
#     text = ''
#     with pdfplumber.open(pdf_filename) as pdf:
#         for page in pdf.pages:
#             text += page.extract_text()
#     return text

if __name__ == "__main__":
    app.run(debug=True)

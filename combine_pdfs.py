import sys
from PyPDF2 import PdfReader, PdfWriter

# function to combine multiple PDFs into a single PDF
def combine_pdfs(pdf_list, output_file):
    pdf_writer = PdfWriter()

    # iterate through each PDF file and add each page to the writer
    for pdf_file in pdf_list:
        try:
            pdf_reader = PdfReader(pdf_file)
            for page in pdf_reader.pages:
                pdf_writer.add_page(page)
        except FileNotFoundError:
            print(f"Error: File {pdf_file} not found. Please check the file path.")
            return

    with open(output_file, 'wb') as out:
        pdf_writer.write(out)
    print(f"PDFs combined successfully into {output_file}")

# main function to run the script
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python combine_pdfs.py output.pdf file1.pdf file2.pdf ...")
    else:
        output_pdf = sys.argv[1]
        input_pdfs = sys.argv[2:]
        combine_pdfs(input_pdfs, output_pdf)
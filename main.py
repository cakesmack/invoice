import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("*xlsx")

for i in filepaths:
    df = pd.read_excel(i, sheet_name='Sheet 1')
    pdf = FPDF(orientation='p', unit='mm', format='A4')
    pdf.add_page()
    pdf.set_font(family='Times', size=16, style='B')
    filename = Path(i).stem
    invoice_no = filename.split('-')[0]
    print(invoice_no)
    pdf.cell(w=50, h=8, txt=f'Invoice No. {invoice_no}')
    pdf.output(f'PDFs/{filename}.pdf')
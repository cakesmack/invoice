import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("*xlsx")

for i in filepaths:
    pdf = FPDF(orientation='p', unit='mm', format='A4')
    pdf.add_page()

    filename = Path(i).stem
    invoice_no, date =filename.split('-')

    pdf.set_font(family='Times', size=16, style='B')
    pdf.cell(w=50, h=8, txt=f'Invoice No. {invoice_no}', ln=1)
    
    pdf.set_font(family='Times', size=12)
    pdf.cell(w=50, h=8, txt=f'Date: {date}', ln=1)

    df = pd.read_excel(i, sheet_name='Sheet 1')

    #add column headers
    columns = df.columns
    columns = [item.replace('_',' ').title() for item in columns]
    pdf.set_font(family='Times', style='B')
    pdf.cell(w=50, h=8, txt=f'Invoice No. {invoice_no}', ln=1)
    pdf.cell(w=30,h=8, txt=columns[0], border=1)
    pdf.cell(w=50,h=8,txt=columns[1], border=1)
    pdf.cell(w=40,h=8,txt=columns[2],border=1)
    pdf.cell(w=30,h=8,txt=columns[3],border=1)
    pdf.cell(w=30,h=8,txt=columns[4],border=1, ln=1)    

    #add rows to table
    for index, row in df.iterrows():
        pdf.set_font(family='Times', size=10)
        pdf.set_text_color(80,80,90)    
        pdf.cell(w=30,h=8, txt=str(row['product_id']), border=1)
        pdf.cell(w=50,h=8,txt=row['product_name'], border=1)
        pdf.cell(w=40,h=8,txt=str(row['amount_purchased']),border=1)
        pdf.cell(w=30,h=8,txt=str(row['price_per_unit']),border=1)
        pdf.cell(w=30,h=8,txt=str(row['total_price']),border=1, ln=1)

    total_price = df['total_price'].sum()

    pdf.set_font(family='Times', style='B')
    pdf.cell(w=30,h=8, txt='', border=1)
    pdf.cell(w=50,h=8,txt='', border=1)
    pdf.cell(w=40,h=8,txt='',border=1)
    pdf.cell(w=30,h=8,txt='',border=1)
    pdf.cell(w=30,h=8,txt=str(total_price),border=1, ln=1) 

    pdf.set_font(family='Times', style='B')
    pdf.cell(w=30,h=8,txt=f'Total amount due is £{total_price}',ln=1)

    pdf.set_font(family='Times', size=14, style='B')
    pdf.cell(w=25,h=8,txt='PythonHow',)
    pdf.image('pythonhow.png', w=10)

    pdf.output(f'PDFs/{filename}.pdf')
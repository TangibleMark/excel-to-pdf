import tkinter
from ExcelReader import ExcelReader
from PdfFormFiller import PdfFormFiller

# main
excel_reader = ExcelReader("suppleance_records_good.xlsx")

test = PdfFormFiller('REQUEST_FOR_SUPPLEANCE_FORM_.pdf', 'test.pdf')
test.write_department()
test.write_sub_emp_number('11111')
test.write_name_of_replacement('mark')
# excel_reader.get_rows()

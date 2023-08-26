from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.generic import BooleanObject, NameObject, IndirectObject

class MyClass:
    def __init__(self):
        pass

    def set_need_appearances_writer(self, writer: PdfWriter):
        # See 12.7.2 and 7.7.2 for more information:
        # http://www.adobe.com/content/dam/acom/en/devnet/acrobat/pdfs/PDF32000_2008.pdf
        try:
            catalog = writer._root_object
            # get the AcroForm tree
            if "/AcroForm" not in catalog:
                writer._root_object.update({
                NameObject("/AcroForm"): IndirectObject(len(writer._objects), 0, writer)
            })

            need_appearances = NameObject("/NeedAppearances")
            writer._root_object["/AcroForm"][need_appearances] = BooleanObject(True)
            # del writer._root_object["/AcroForm"]['NeedAppearances']
            return writer

        except Exception as e:
            print('set_need_appearances_writer() catch : ', repr(e))
            return writer

    def change_field(self, field_name, field_value, new_pdf_name):
        reader = PdfReader("REQUEST_FOR_SUPPLEANCE_FORM_.pdf")
        writer = PdfWriter()
        self.set_need_appearances_writer(writer)

        # Get the first page from the pdf
        page = reader.pages[0]

        # Duplicate that page onto a new pdf
        writer.add_page(page)

        writer.update_page_form_field_values(
            writer.pages[0], {f"{field_name}": f"{field_value}"}
        )

        # write "output" to PyPDF2-output.pdf
        with open(f"{new_pdf_name}.pdf", "wb") as output_stream:
            writer.write(output_stream)



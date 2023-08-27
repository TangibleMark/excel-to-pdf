from pypdf import PdfReader, PdfWriter


class PdfFormFiller:
    def __init__(self, old_pdf_name, new_pdf_name):
        self.old_pdf_name = old_pdf_name
        self.new_pdf_name = new_pdf_name

        reader = PdfReader(self.old_pdf_name)
        writer = PdfWriter()
        # Get the first page from the pdf
        page = reader.pages[0]

        # Duplicate that page onto a new pdf
        writer.add_page(page)

        # write "output" to PyPDF2-output.pdf
        with open(f"{self.new_pdf_name}.pdf", "wb") as output_stream:
            writer.write(output_stream)

    # def set_need_appearances_writer(writer):
    #     # See 12.7.2 and 7.7.2 for more information:
    #     # http://www.adobe.com/content/dam/acom/en/devnet/acrobat/
    #     #     pdfs/PDF32000_2008.pdf
    #     try:
    #         catalog = writer._root_object
    #         # get the AcroForm tree and add "/NeedAppearances attribute
    #         if "/AcroForm" not in catalog:
    #             writer._root_object.update(
    #                 {
    #                     NameObject("/AcroForm"): IndirectObject(
    #                         len(writer._objects), 0, writer
    #                     )
    #                 }
    #             )
    #
    #         need_appearances = NameObject("/NeedAppearances")
    #         writer._root_object["/AcroForm"][
    #             need_appearances] = BooleanObject(True)
    #         return writer
    #
    #     except Exception as e:
    #         print("set_need_appearances_writer() catch : ", repr(e))
    #         return writer

    def change_field(self, field_name, field_value):
        reader = PdfReader(self.old_pdf_name, strict=False)


        writer = PdfWriter()
        writer.add_page(reader.pages[0])

        writer.update_page_form_field_values(
            writer.pages[0], {f"{field_name}": f"{field_value}"}
        )

        # write "output" to PyPDF2-output.pdf
        with open(f"{self.new_pdf_name}.pdf", "wb") as output_stream:
            writer.write(output_stream)

    def write_department(self):
        self.change_field('DEPARTMENT', 'champ')

    def write_sub_emp_number(self, value):
        self.change_field('#', value)

    def write_name_of_replacement(self, value):
        self.change_field('NAME OF REPLACEMENT', value)

    def write_courses_taught(self, value):
        self.change_field('COURSE(S) TAUGHT', value)

    def write_absent_emp_number(self, value):
        self.change_field('ABSENT INSTRUCTOR EMPL #', value)

    def write_name_of_absent(self, value):
        self.change_field('ABSENT INSTRUCTOR', value)

    def write_reason_for_absence(self, value):
        self.change_field('RAISON FOR ABSENCE', value)

    def write_date_of_absence(self, value):
        self.change_field('DATE#0', value)

    def write_time_from(self, value):
        self.change_field('FROM#0', value)

    def write_time_to(self, value):
        self.change_field('TO#0', value)

    def write_hours_worked(self, value):
        self.change_field('HOURS WORKED#0', value)

    def print_fields(self):
        reader = PdfReader(self.old_pdf_name)
        print(reader.get_fields())

# Week
# Sub ID
# Sub
# Absent
# Absent ID
# Day
# Course
# Block
# Hours
# Completed
# Stage of Process
# Paid
# Note

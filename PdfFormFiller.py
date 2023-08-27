from pypdf import PdfReader, PdfWriter


class PdfFormFiller:
    def __init__(self, old_pdf_name, new_pdf_name):
        self.old_pdf_name = old_pdf_name
        self.new_pdf_name = new_pdf_name
        self.writer = PdfWriter()

        reader = PdfReader(self.old_pdf_name)

        # Get the first page from the pdf
        page = reader.pages[0]

        # Duplicate that page onto a new pdf
        self.writer.add_page(page)

    def change_field(self, field_name, field_value):
        self.writer.update_page_form_field_values(
            self.writer.pages[0], {f"{field_name}": f"{field_value}"}
        )

    def write_department(self):
        self.change_field('DEPARTMENT', 'Mathematics')

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

    def write_all_changes(self):
        # write "output" to PyPDF2-output.pdf
        with open(f"{self.new_pdf_name}", "wb") as output_stream:
            self.writer.write(output_stream)

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

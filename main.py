import tkinter as tk
from tkinter import filedialog, messagebox
from ExcelReader import ExcelReader

# pyinstaller --onefile main.py

# main
root = tk.Tk()
root.title("Absentee Excel to Pdf")


# Function to open a file dialog and get the selected file
def browse_excel_file():
    file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
    excel_file_entry.delete(0, tk.END)  # Clear any previous entry
    excel_file_entry.insert(0, file_path)  # Insert selected file path


def browse_pdf_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    pdf_file_entry.delete(0, tk.END)  # Clear any previous entry
    pdf_file_entry.insert(0, file_path)  # Insert selected file path


# Function to process Excel data and create PDFs
def calculate_excel_data():
    excel_file_path = excel_file_entry.get()  # Get the selected Excel file path
    pdf_file_path = pdf_file_entry.get()

    if not excel_file_path:
        messagebox.showerror("Error", "Please select an Excel file.")
        return

    excel_reader = ExcelReader(excel_file_path, pdf_file_path)
    excel_reader.get_rows(lower_entry.get(), upper_entry.get())


# Create labels and entry widgets
lower_label = tk.Label(root, text="Starting Row:")
upper_label = tk.Label(root, text="Ending Row(inclusive):")
excel_file_label = tk.Label(root, text="Excel File:")
pdf_file_label = tk.Label(root, text="Pdf File:")
lower_entry = tk.Entry(root)
upper_entry = tk.Entry(root)
excel_file_entry = tk.Entry(root)
pdf_file_entry = tk.Entry(root)


browse_excel_button = tk.Button(root, text="Browse", command=browse_excel_file)
browse_pdf_button = tk.Button(root, text="Browse", command=browse_pdf_file)
calculate_button = tk.Button(root, text="Excel to PDFs", command=lambda: calculate_excel_data())

# Organize widgets using grid layout
lower_label.grid(row=0, column=0, padx=10, pady=5)
lower_entry.grid(row=0, column=1, padx=10, pady=5)
upper_label.grid(row=1, column=0, padx=10, pady=5)
upper_entry.grid(row=1, column=1, padx=10, pady=5)
excel_file_label.grid(row=2, column=0, padx=10, pady=5)
excel_file_entry.grid(row=2, column=1, padx=10, pady=5)
pdf_file_label.grid(row=3, column=0, padx=10, pady=5)
pdf_file_entry.grid(row=3, column=1, padx=10, pady=5)
browse_excel_button.grid(row=2, column=2, padx=10, pady=5)
browse_pdf_button.grid(row=3, column=2, padx=10, pady=5 )
calculate_button.grid(row=4, columnspan=3, padx=10, pady=10)


# Run the GUI event loop
root.mainloop()


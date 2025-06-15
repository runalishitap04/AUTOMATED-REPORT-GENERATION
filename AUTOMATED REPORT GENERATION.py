import csv
from statistics import mean, median
from fpdf import FPDF
import os

# Read and analyze data
def read_data(filename):
    try:
        with open(filename, newline='') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
            scores = [int(row["Score"]) for row in data]
        return data, scores
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return [], []
    except Exception as e:
        print(f"An error occurred: {e}")
        return [], []

# Generate PDF report
def generate_report(data, scores, output_file="report.pdf"):
    if not data or not scores:
        print("No data to generate report.")
        return

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)

    # Title
    pdf.cell(200, 10, "Student Score Report", ln=True, align='C')

    # Basic Stats
    pdf.set_font("Arial", '', 12)
    pdf.ln(10)
    pdf.cell(200, 10, f"Average Score: {mean(scores):.2f}", ln=True)
    pdf.cell(200, 10, f"Median Score: {median(scores):.2f}", ln=True)
    pdf.cell(200, 10, f"Highest Score: {max(scores)}", ln=True)
    pdf.cell(200, 10, f"Lowest Score: {min(scores)}", ln=True)

    # Table Header
    pdf.ln(10)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(100, 10, "Name", border=1)
    pdf.cell(40, 10, "Score", border=1)
    pdf.ln()

    # Table Rows
    pdf.set_font("Arial", '', 12)
    for row in data:
        pdf.cell(100, 10, row["Name"], border=1)
        pdf.cell(40, 10, row["Score"], border=1)
        pdf.ln()

    # Save PDF
    pdf.output(output_file)
    print(f"Report saved to {output_file}")

# Main function
if __name__ == "__main__":
    filename = "data.csv"
    data, scores = read_data(filename)
    generate_report(data, scores)

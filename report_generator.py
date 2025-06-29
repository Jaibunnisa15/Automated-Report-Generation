import csv
from fpdf import FPDF
from collections import defaultdict

# Read CSV data
def read_data(filename):
    data = []
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

# Analyze data: total and average salary per department
def analyze_data(data):
    department_stats = defaultdict(list)
    for row in data:
        department = row['Department']
        salary = float(row['Salary'])
        department_stats[department].append(salary)
    
    summary = {}
    for dept, salaries in department_stats.items():
        total = sum(salaries)
        average = total / len(salaries)
        summary[dept] = {'total': total, 'average': average, 'count': len(salaries)}
    return summary

# Generate PDF Report
def generate_pdf(summary, output_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "Department Salary Report", ln=True, align="C")

    pdf.ln(10)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(60, 10, "Department", border=1)
    pdf.cell(40, 10, "Employees", border=1)
    pdf.cell(40, 10, "Total Salary", border=1)
    pdf.cell(40, 10, "Avg Salary", border=1)
    pdf.ln()

    pdf.set_font("Arial", '', 12)
    for dept, stats in summary.items():
        pdf.cell(60, 10, dept, border=1)
        pdf.cell(40, 10, str(stats['count']), border=1)
        pdf.cell(40, 10, f"${stats['total']:.2f}", border=1)
        pdf.cell(40, 10, f"${stats['average']:.2f}", border=1)
        pdf.ln()

    pdf.output(output_path)
    print(f"Report saved to {output_path}")

# Main
if __name__ == "__main__":
    data = read_data("data.csv")
    summary = analyze_data(data)
    generate_pdf(summary, "output_report.pdf")

import pandas as pd

def analyze_excel(path):
    xls = pd.ExcelFile(path)
    sheet = xls.sheet_names[0]
    df = pd.read_excel(xls, sheet_name=sheet)
    report_lines = []
    report_lines.append(f"Файл: {path}")
    report_lines.append(f"Лист: {sheet}")
    report_lines.append(f"Размер: {df.shape[0]} строк x {df.shape[1]} столбцов")
    report_lines.append("Колонки и типы:")
    report_lines.append(str(df.dtypes))
    report_lines.append("\nБазовая статистика (числовые):")
    report_lines.append(str(df.describe()))
    return "\n\n".join(report_lines)
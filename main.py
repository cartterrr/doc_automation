import tkinter as tk
from tkinter import filedialog, messagebox
from modules.pdf_utils import merge_pdfs, extract_text_from_pdf
from modules.docx_utils import extract_text_from_docx
from modules.excel_utils import analyze_excel

def choose_merge_pdfs():
    files = filedialog.askopenfilenames(
        title="Выберите PDF для объединения",
        filetypes=[("PDF files", "*.pdf")]
    )
    if not files:
        return
    out = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("PDF files", "*.pdf")],
        title="Сохранить как"
    )
    if not out:
        return
    try:
        merge_pdfs(files, out)
        messagebox.showinfo("Готово", f"PDF объединён и сохранён: {out}")
    except Exception as e:
        messagebox.showerror("Ошибка", str(e))

def choose_extract_docx():
    file = filedialog.askopenfilename(
        title="Выберите .docx",
        filetypes=[("Word files", "*.docx")]
    )
    if not file:
        return
    try:
        text = extract_text_from_docx(file)
        out = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt")],
            title="Сохранить текст как"
        )
        if not out:
            return
        with open(out, "w", encoding="utf-8") as f:
            f.write(text)
        messagebox.showinfo("Готово", f"Текст сохранён: {out}")
    except Exception as e:
        messagebox.showerror("Ошибка", str(e))

def choose_extract_pdf_text():
    file = filedialog.askopenfilename(
        title="Выберите .pdf",
        filetypes=[("PDF files", "*.pdf")]
    )
    if not file:
        return
    try:
        text = extract_text_from_pdf(file)
        out = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt")],
            title="Сохранить текст как"
        )
        if not out:
            return
        with open(out, "w", encoding="utf-8") as f:
            f.write(text)
        messagebox.showinfo("Готово", f"Текст сохранён: {out}")
    except Exception as e:
        messagebox.showerror("Ошибка", str(e))

def choose_analyze_excel():
    file = filedialog.askopenfilename(
        title="Выберите Excel (.xlsx)",
        filetypes=[("Excel files", "*.xlsx;*.xls")]
    )
    if not file:
        return
    try:
        report = analyze_excel(file)
        out = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt")],
            title="Сохранить отчёт как"
        )
        if not out:
            return
        with open(out, "w", encoding="utf-8") as f:
            f.write(report)
        messagebox.showinfo("Готово", f"Отчёт сохранён: {out}")
    except Exception as e:
        messagebox.showerror("Ошибка", str(e))

# --- Основное окно приложения ---
root = tk.Tk()
root.title("Doc Automation")
root.geometry("420x280")

# Заголовок
tk.Label(root, text="Автоматизация офисных файлов", font=("Arial", 14, "bold")).pack(pady=10)

# Кнопки
btn_pdf_merge = tk.Button(root, text="Объединить PDF", width=30, command=choose_merge_pdfs)
btn_pdf_merge.pack(pady=6)

btn_pdf_text = tk.Button(root, text="Извлечь текст из PDF", width=30, command=choose_extract_pdf_text)
btn_pdf_text.pack(pady=6)

btn_docx = tk.Button(root, text="Извлечь текст из DOCX", width=30, command=choose_extract_docx)
btn_docx.pack(pady=6)

btn_excel = tk.Button(root, text="Анализ Excel (basic)", width=30, command=choose_analyze_excel)
btn_excel.pack(pady=6)

# --- Подпись автора в правом нижнем углу ---
label_author = tk.Label(
    root,
    text="by Соболев Ярослав Михайлович",
    font=("Arial", 9, "italic"),
    fg="gray"
)
label_author.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)

# Запуск приложения
root.mainloop()

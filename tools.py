import os
from PyPDF2 import PdfReader

class FinancialDocumentTool:
    @staticmethod
    async def read_data_tool(path='data/sample.pdf'):
        if not os.path.exists(path):
            return "File not found."
        try:
            reader = PdfReader(path)
            full_report = ""
            for page in reader.pages:
                content = page.extract_text() or ""
                while "\n\n" in content:
                    content = content.replace("\n\n", "\n")
                full_report += content + "\n"
            return full_report
        except Exception as e:
            return f"Error reading PDF: {str(e)}"

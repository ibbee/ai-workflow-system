import pdf_handler as pdh
import llm
import prompts
import parser
from Models import models

def pdf_analysis(file):
    pdf_text = pdh.read_pdf(file)

    prompt = prompts.build_prompt(pdf_text)

    output = parser.parse_llm_response(llm.analyze_resume(prompt))

    analysis = models.ResumeAnalysis(**output)

    return analysis
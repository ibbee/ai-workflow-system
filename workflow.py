import pdf_handler as pdh
import llm
import prompts
import parser

def pdf_analysis(file):
    pdf_text = pdh.read_pdf(file)

    prompt = prompts.build_prompt(pdf_text)

    output = parser.parse_llm_response(llm.analyze_resume(prompt))

    return output
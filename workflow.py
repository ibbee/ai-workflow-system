import pdf_handler as pdh
import llm
import prompts
import parser
from mapper import model_mapper

def pdf_analysis(mode, file):
    pdf_text = pdh.read_pdf(file)

    prompt = prompts.build_prompt(mode, pdf_text)
    
    output = parser.parse_llm_response(llm.analyze_resume(prompt))

    #print(output)

    analysis = model_mapper(mode)(**output)

    return analysis
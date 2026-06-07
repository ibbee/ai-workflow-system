def build_prompt(text):
    return f"""
You are an information extraction assistant.

Extract the following information from the resume.

Return ONLY valid JSON.

{{
    "name": "",
    "skills": [],
    "education": "",
    "experience_summary": ""
}}

Resume:

{text}
"""
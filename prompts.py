def build_prompt(mode, text):
    resume_prompt = f"""
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
    
    summary_prompt = f"""
Your are an assistant helping people save time by summarizing the provided text.

Summarize the document in 5-10 concise sentences.

Return only Valid JSON.

{{
    "summary": ""
}}

Text:

{text}
"""
    
    keyword_prompt = f"""
You are a keyword extraction assistant.

Extract the 10 most important keywords fromprovided text.

Return only Valid JSON.

{{
    "keywords": []
}}

Text:

{text}
"""
    
    if mode == 'resume':
        return resume_prompt
    elif mode == 'summary':
        return summary_prompt
    elif mode == 'keywords':
        return keyword_prompt
    
    return None
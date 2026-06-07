from pydantic import BaseModel

class ResumeAnalysis(BaseModel):
    name: str
    skills: list[str]
    education: list
    experience_summary: str
from fastapi import FastAPI, UploadFile, File, HTTPException
import workflow
from mapper import mode_to_model

app = FastAPI()

VALID_MODES = list(mode_to_model.keys())

@app.post('/upload-pdf/')
def upload_pdf(files: list[UploadFile] = File(...),mode:str = 'resume'):
    for pdf in files:
        if pdf.content_type != 'application/pdf':
            raise HTTPException(
                status_code=400,
                detail=f'Only PDFs are allowed, {pdf.filename} is an invalid file'
            )
    if mode not in VALID_MODES:
            raise HTTPException(
                 status_code=400,
                 detail="Unsupported analysis mode."
            )
    try:
        api_output = []
        for pdf in files:
            result = workflow.pdf_analysis(mode,pdf)
            api_output.append({'file-names':pdf.filename,
                    'analysis': result.model_dump()})
        return {'results' : api_output}
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
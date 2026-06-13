from fastapi import FastAPI, UploadFile, File, HTTPException
import workflow
from mapper import mode_to_model

app = FastAPI()

VALID_MODES = list(mode_to_model.keys())

@app.post('/upload-pdf/')
def upload_pdf(file: UploadFile = File(...),mode:str = 'resume'):
    if file.content_type != 'application/pdf':
        raise HTTPException(
            status_code=400,
            detail='Only PDFs are allowed'
        )
    if mode not in VALID_MODES:
            raise HTTPException(
                 status_code=400,
                 detail="Unsupported analysis mode."
            )
    try:
        result = workflow.pdf_analysis(mode,file)
        return {'file-name':file.filename,
                'analysis':result.model_dump()}
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
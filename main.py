from fastapi import FastAPI, UploadFile, File, HTTPException
import workflow

app = FastAPI()

@app.post('/upload-pdf')
def upload_pdf(file: UploadFile = File(...)):
    if file.content_type != 'application/pdf':
        raise HTTPException(
            status_code=400,
            detail='Only PDFs are allowed'
        )
    result = workflow.pdf_analysis(file)
    return {'file-name':file.filename,
            'analysis':result}
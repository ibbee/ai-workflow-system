from fastapi import FastAPI, UploadFile, File, HTTPException
import pdfhandler as pdh

app = FastAPI()

@app.post('/upload-pdf')
async def upload_pdf(file: UploadFile = File(...)):
    if file.content_type != 'application/pdf':
        raise HTTPException(
            status_code=400,
            detail='Only PDFs are allowed'
        )
    pdf_text = pdh.read_pdf(file)
    print(pdf_text)
    return {'file-name':file.filename,
            'file-content':pdf_text[:100]}
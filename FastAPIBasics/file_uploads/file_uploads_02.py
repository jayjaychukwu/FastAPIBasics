"""
Using the UploadFile that allows you use meta data about the file
and helps handle large uploads by saving to disk
"""

from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.post("/files")
async def upload_file(file: UploadFile = File(...)):
    return {"file_name": file.filename, "content_type": file.content_type}

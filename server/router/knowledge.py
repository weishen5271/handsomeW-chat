from fastapi import APIRouter, File, UploadFile
from server.service import save_vector
import mimetypes
# create router
knowledge_router = APIRouter(
    prefix='/knowledge',
    tags = ['knowledge']
)



@knowledge_router.get('/') 
async def welcome() -> dict:
    return { "message": "Welcome to my Page"}


@knowledge_router.post('/import/file') 
async def import_file(file: UploadFile = File(...)):
    mime_type, _ = mimetypes.guess_type(file.filename)
    contents = await file.read()
    with open(file.filename, "wb") as f:
        f.write(contents)
    result = save_vector(file.filename,mime_type)
    return result;
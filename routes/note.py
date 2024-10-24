from fastapi import APIRouter
from models.note import Note
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from config.db import notescollection
from schemas.note import noteEntity,notesEntity
from fastapi.templating import Jinja2Templates

note = APIRouter()
templates = Jinja2Templates(directory="templates")

@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    print("hi")
    try:
        docs = notescollection.find()  # Fetch all documents
        newDocs = []

        for doc in docs:
            # Ensure the document has the necessary fields
            if "title" in doc and "_id" in doc:
                newDocs.append({
                    "id": str(doc["_id"]),  # ObjectId needs to be stringified
                    "title": doc["title"],
                    "desc": doc["desc"],
                    "important": doc["important"]
                })


        return templates.TemplateResponse("index.html", {"request": request, "newDocs": newDocs})

    except Exception as e:
        print(f"Error fetching documents from MongoDB: {e}")
        return HTMLResponse(content="An error occurred while fetching notes.", status_code=500)


@note.post("/",)
async def create_item(request: Request):
    form = await request.form()
    formDict = dict(form)
    if "important" in formDict:
        formDict["important"] = True if formDict["important"] == "on" else False
    else:
        formDict["important"] = False  # Default to False if checkbox not selected    note = notescollection.insert_one(dict(formDict))
    note = notescollection.insert_one(dict(formDict))
    return RedirectResponse(url="/", status_code=303)

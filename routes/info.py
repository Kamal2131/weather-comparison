from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


router = APIRouter()

templates = Jinja2Templates(directory="templates")
router.mount("/static", StaticFiles(directory="static"), name="static")

@router.get("/about", response_class=HTMLResponse)
def about(request: Request):
    return templates.TemplateResponse("about.html", {
        "request": request,
    })
    
@router.get("/contact")
def contact_page(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})

@router.post("/contact")
def submit_contact(request: Request, name: str = Form(...), email: str = Form(...), message: str = Form(...)):
    print(f"📩 New message from {name} ({email}):\n{message}")
    return RedirectResponse("/contact", status_code=302)
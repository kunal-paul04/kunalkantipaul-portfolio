from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from lib.mongo_lib import database_connection
from fastapi.templating import Jinja2Templates

route = APIRouter()
templates = Jinja2Templates(directory="templates")


@route.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    # Create MongoDB connection on demand
    conn = database_connection()
    about = conn.portfolio.intro.find({})
    resume = conn.portfolio.resume.find_one({})
    skillset = conn.portfolio.skillset.find({})
    tech_skill = conn.portfolio.tech_skill.find({})
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"resume": resume, "skillset": skillset, "intro": about, "tech_skill": tech_skill}
    )


@route.get("/about", response_class=HTMLResponse)
async def read_item(request: Request):
    # Create MongoDB connection on demand
    conn = database_connection()
    certificates = conn.portfolio.certification.find({})
    education_list = conn.portfolio.education.find({})
    work_list = conn.portfolio.job.find({})
    return templates.TemplateResponse(
        request=request,
        name="about.html",
        context={"certificates": certificates, "education_list": education_list, "work_list": work_list}
    )


@route.get("/portfolio", response_class=HTMLResponse)
async def read_item(request: Request):
    # Create MongoDB connection on demand
    conn = database_connection()
    portfolio = conn.portfolio.projects.find({})
    return templates.TemplateResponse(
        request=request,
        name="projects.html",
        context={"projects": portfolio}
    )


@route.get("/contact", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse(request=request, name="contact.html")

from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from models.intro import Intro
from models.resume import Resume
from lib.mongo_lib import database_connection
from schemas.schema import intro_list, intro, certificate_list_entity, certification, skillset_list, skillset, resume, education_list, education, work_list, work, tech_skill_list, tech_skill, project_list, projects
from fastapi.templating import Jinja2Templates

route = APIRouter()
conn = database_connection()
templates = Jinja2Templates(directory="templates")


@route.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    # to fetch data from a collection, use: <connection_var>.<db name>.<collection name>
    about = conn.portfolio.intro.find({})
    resume = conn.portfolio.resume.find_one({})
    skillset = conn.portfolio.skillset.find({})
    tech_skill = conn.portfolio.tech_skill.find({})
    return templates.TemplateResponse(request=request, name="index.html", context={"resume": resume, "skillset": skillset, "intro": about, "tech_skill": tech_skill})


@route.get("/about", response_class=HTMLResponse)
async def read_item(request: Request):
    # to fetch data from a collection, use: <connection_var>.<db name>.<collection name>
    certificates = conn.portfolio.certification.find({})
    education_list = conn.portfolio.education.find({})
    work_list = conn.portfolio.job.find({})
    return templates.TemplateResponse(request=request, name="about.html", context={"certificates": certificates, "education_list": education_list, "work_list": work_list})


@route.get("/portfolio", response_class=HTMLResponse)
async def read_item(request: Request):
    # to fetch data from a collection, use: <connection_var>.<db name>.<collection name>
    portfolio = conn.portfolio.projects.find({})
    return templates.TemplateResponse(request=request, name="projects.html", context={"projects": portfolio})


@route.get("/contact", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse(request=request, name="contact.html")

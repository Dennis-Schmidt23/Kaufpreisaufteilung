from pathlib import Path

from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.forms import FORM_SECTIONS

from app.calculator.data.nhk import nhk_form_options
from app.calculator.engine import CalculationEngine
from app.form_mapper import map_form_to_input_data

BASE_DIR = Path(__file__).resolve().parent.parent
templates = Jinja2Templates(directory=BASE_DIR / "templates")

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "title": "Kaufpreisaufteilung nach BMF-Arbeitshilfe",
            "form_sections": FORM_SECTIONS,
            "nhk_options": nhk_form_options(),
        },
    )


@router.post("/calculate")
async def calculate(request: Request):

    form = await request.form()

    data = map_form_to_input_data(form)

    engine = CalculationEngine()

    result = engine.calculate(data)

    return templates.TemplateResponse(
        request=request,
        name="result.html",
        context={
            "datan": data,
            "result": result,
        },
    )
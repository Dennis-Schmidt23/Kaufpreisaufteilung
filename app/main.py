from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Kaufpreisaufteilung")

@app.get("/", response_class=HTMLResponse)
def index():
    return """
    <h1>Kaufpreisaufteilung nach BMF</h1>
    <p>Die Anwendung läuft erfolgreich.</p>
    """
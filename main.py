from fastapi import  FastAPI, Request
from fastapi.responses import FileResponse, HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
import os

from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory=".")

# Redireciona o caminho "/" para "index.html"
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    print("Passou em root")
    return templates.TemplateResponse("index.html", {"request": request})

# Rota que processa o modelo e renderiza a página HTML com os dados
@app.get("/ambiente", response_class=HTMLResponse)
async def ambiente(request: Request):
    dados = [
        {"id": 1, "nome": "Produto A", "preco": 10.99},
        {"id": 2, "nome": "Produto B", "preco": 25.50},
        {"id": 3, "nome": "Produto C", "preco": 7.30}
    ]
    
    print("Passou em ambiente")# Gerar o conteúdo HTML com o template
    html_content = templates.get_template("ambiente.html").render(request=request, dados=dados)
    
    # Adicionar um JSON no head do HTML
    html_content = html_content.replace(
        "</head>", 
        f'<script type="text/javascript">const dados = {dados};</script></head>'
    )

    return HTMLResponse(content=html_content)

# Rota que processa o modelo e renderiza a página HTML com os dados
@app.get("/lancamento", response_class=HTMLResponse)
async def lancamento(request: Request):
    dados = [
        {"id": 1, "nome": "Produto A", "preco": 10.99},
        {"id": 2, "nome": "Produto B", "preco": 25.50},
        {"id": 3, "nome": "Produto C", "preco": 7.30}
    ]
    
    print("Passou em lançamento")# Gerar o conteúdo HTML com o template
    html_content = templates.get_template("lancamento.html").render(request=request, dados=dados)
    
    # Adicionar um JSON no head do HTML
    html_content = html_content.replace(
        "</head>", 
        f'<script type="text/javascript">const dados = {dados};</script></head>'
    )

    return HTMLResponse(content=html_content)
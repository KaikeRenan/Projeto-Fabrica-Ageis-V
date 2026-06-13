# Projeto-Fabrica-Ageis-V
Projeto desenvolvido para a disciplina de fábrica de projetos ágeis V

# Como rodar o projeto

1. Clonar repositório 
```bash 
git clone https://github.com/KaikeRenan/Projeto-Fabrica-Ageis-V.git
```
2. Entrar na pasta do projeto
```bash 
cd Projeto-Fabrica-Ageis-V
```
3. Criar o ambiente virtual 
```bash 
python -m venv .venv
```
4. Instalar as dependências 
```bash 
pip install -r requirements.txt
```
5. Rodar a aplicação 
```bash 
python -m uvicorn main:app --reload
```

# Acesso à aplicação

aplicação estará disponível em:
```bash
http://127.0.0.1:8000
```

# Swagger
```bash
http://127.0.0.1:8000/docs
```

# ReDoc
```bash
http://127.0.0.1:8000/redoc
```
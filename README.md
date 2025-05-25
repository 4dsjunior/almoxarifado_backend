# Almoxarifado 11.0 Plus+ Backend

## Instalação - TESTE

1. Clone o projeto:
    git clone https://github.com/4dsjunior/almoxarifado_backend.git

2. Entre na pasta do projeto:
    cd almoxarifado_backend

3. Instale as dependências:
    poetry install

4. Copie o arquivo de exemplo do ambiente:
    cp .env.example .env

5. Rode a API:
    poetry run uvicorn interfaces.api.main:app --reload

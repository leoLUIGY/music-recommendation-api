# Music Recommendation API

API responsável pelo gerenciamento de **preferências musicais**, desenvolvida em **Python / Flask**, como parte de uma arquitetura de microsserviços.

## Tecnologias

* Python 3.9
* Flask
* Flask-OpenAPI3
* Swagger / OpenAPI
* CORS
* Docker

## Funcionalidades

A API disponibiliza operações para:

* Consultar uma preferência por ID
* Consultar todas as preferências
* Criar uma nova preferência
* Atualizar uma preferência
* Excluir uma preferência

## Executar com Docker

Clone o projeto:

```bash
git clone https://github.com/leoLUIGY/music-recommendation-api.git
cd music-recommendation-api
```

Crie a imagem:

```bash
docker build -t music-recommendation-api .
```

Execute o container:

```bash
docker run -p 5001:5001 music-recommendation-api
```

## Swagger

Após iniciar o container, acesse:

```text
http://localhost:5001/openapi/swagger
```

Através do Swagger é possível visualizar e testar as rotas disponíveis da API.

## Arquitetura

A API é consumida pelo **Music API Gateway**, que centraliza as requisições da aplicação e encaminha as operações relacionadas às preferências musicais para este serviço.

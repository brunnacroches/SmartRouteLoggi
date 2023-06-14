# Estrutura para o projeto de otimização de rotas

├── init
│   └── schema.sql
├── requirements.txt
├── run.py
├── src
│   ├── __init__.py
│   ├── configs
│   │   └── api_configs.py
│   ├── controllers
│   │   ├── interfaces
│   │   │   └── route_optimization_controller.py
│   │   ├── tests
│   │   │   └── route_optimization_controller.py
│   │   └── route_optimization_controller.py
│   ├── errors
│   │   ├── error_handler.py
│   │   └── error_types
│   │       ├── http_not_found.py
│   │       ├── http_request_error.py
│   │       └── http_unprocessable_entity.py
│   ├── infra
│   │   └── db
│   │       ├── entities
│   │       │   ├── routes.py
│   │       │   └── api_performance.py
│   │       ├── interfaces
│   │       │   └── routes_repository.py
│   │       ├── repositories
│   │       │   ├── routes_repository.py
│   │       │   └── routes_repository_test.py
│   │       └── settings
│   │           ├── base.py
│   │           └── connection.py
│   ├── main
│   │   ├── adapters
│   │   │   └── request_adapter.py
│   │   ├── composers
│   │   │   └── route_optimization_composer.py
│   │   ├── routes
│   │   │   └── route_optimization_routes.py
│   │   └── server
│   │       └── server.py
│   ├── validators
│   │   ├── route_optimization_validator.py
│   │   └── route_optimization_validator_test.py
│   └── views
│       ├── http_types
│       │   ├── http_request.py
│       │   └── http_response.py
│       ├── interfaces
│       │   └── view_interface.py
│       ├── route_optimization_view.py
│       └── route_optimization_view_test.py
└── storage.db

## Nesta estrutura

- configs/api_configs.py armazena as configurações das APIs de cálculo de rotas.

- controllers/route_optimization_controller.py é responsável por processar as entradas do usuário, solicitar rotas do modelo e atualizar a visão com as rotas propostas e o histórico de desempenho das APIs.

- infra/db/entities/routes.py e infra/db/entities/api_performance.py definem as entidades de rota e desempenho da API que são armazenadas no banco de dados.

- infra/db/interfaces/routes_repository.py define a interface para o repositório de rotas, que é responsável por interagir com o banco de dados.

- infra/db/repositories/routes_repository.py implementa o repositório de rotas.

- main/composers/route_optimization_composer.py é responsável por compor os objetos necessários para a rota de otimização.

- main/routes/route_optimization_routes.py define as rotas da API para a otimização de rotas.

- validators/route_optimization_validator.py valida as entradas do usuário para a otimização de rotas.

- views/route_optimization_view.py é responsável por apresentar os dados ao usuário.

from src.infra.configs.connection import DBConnectionHandler
from src.infra.repositories.product_repository import ProductRepository
from src.main.server.server import app

# Instancia o objeto DBConnectionHandler
db_hanlde = DBConnectionHandler()


# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)


# Conecta ao banco de dados
db_hanlde.connect_to_db()

# Obtém a conexão com o banco de dados
db_connection = db_hanlde.get_db_connection()


# Verificando se a conexão foi estabelecida
if db_connection is not None:
    print("Conexão com o banco de dados estabelecida com sucesso!")
else:
    print("Falha ao estabelecer conexão com o banco de dados.")

# Instancia a classe ProductRepository com a conexão db_connection
products_repository = ProductRepository(db_connection)

# Realiza o cadastro dos Produtos
name = "Caixa de Bombons"
weight = 12.8

response = products_repository.insert_product(name, weight)
print(response)


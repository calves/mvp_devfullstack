# mvp engenharia de software sprint I

1 - Executar os comandos sql abaixo no PostgreSQL:

	1.1 - 
		CREATE DATABASE tarefas_db
		  WITH
		  OWNER = postgres
		  ENCODING = 'UTF8'
		  CONNECTION LIMIT = -1
		  IS_TEMPLATE = False;
	
	1.2 - 
		CREATE TABLE IF NOT EXISTS tarefa(
			id SERIAL PRIMARY KEY, 
            titulo TEXT, 
            descricao VARCHAR(200), 
            status bool, 
            data   timestamp
		)

2 - Para executar a API:

	2.1 - As libs estão no arquivo requirements.txt na raiz do projeto.
	2.2 - Abra o terminal e execute (env)$ pip install -r requirements.txt
	2.3 - Execute o comando: flask run --host 0.0.0.0 --port 5000 para executar a API
	2.4 - Abra a url http://localhost:5000/#/ no navegador

3 - Para exibir a documentação swagger

	3.1 - Abra a url http://127.0.0.1:5000/openapi/swagger  no navegador
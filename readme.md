[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-%23FE5196?logo=conventionalcommits&logoColor=white)](https://conventionalcommits.org)

# Projeto ✨
 Projeto de portifólio construido e atualizado com ferramentas e ideias que desenvolvi durante meus estudos.

 - Utilizando um arquitetura funcional de componentes;
 - Utiliza um design patterns [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) para facilitar a compreensão dos commits ;
 
 # Construção 🚧
 - Foi utilizado [Python](https://docs.python.org/3/) como linguagem principal da aplicação frontend ;
 - Foi utilizado [Flask](https://flask.palletsprojects.com/en/2.3.x/) para realizar as requisições e consumo de APIs;
 - Foi utilizado [Docker](https://docs.docker.com/) para a configuração do ambiente de desenvolvimento, facilitando a integração entre os microsserviços ;

# Execução ▶️ 
Existem duas formas de iniciar o projeto;

1 - Caso você tenha o Docker-compose configurado na sua maquina, insira no terminal o seguinte comando para criar um container com a imagem atualizada do projeto
```
docker-compose up
```
após isso, digite o seguinte comando para subir o container
```
docker-compose start
```

2 - Caso você não possua o Docker-compose configurado, insira o seguinte comando no terminal para instalar todas as dependências do projeto
```
pip install -r /requirements.txt
```
Após instalar as dependências você deve iniciar o projeto localmente digite o seguinte comando para  subir o projeto de forma local
```
src/__init__.py
```

# Testes 🦾

Ainda não inclui os testes de componentes e unitários dentro do projeto...
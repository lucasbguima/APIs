# Reservapi

Reservapi é uma API para agendamento de reservas em hotéis.

  - Cadastro de Usuários
  - Cadastro de Hotéis
  - Agendamentos

Sua base foi criada utilizando-se Django e Django Rest Framework:

* [Django](https://docs.djangoproject.com/en/3.1/) - The web framework for perfectionists with deadlines.
* [Django-Rest-Framework](https://www.django-rest-framework.org/) - A powerful and flexible toolkit for building Web APIs.

# Instalação

### Requisitos
Para rodar o projeto em Django é necessário ter no mínimo Python 2.3 instalado na máquina.

Essa API faz parte do pacote de APIs do desenvolvedor Lucas B Guima, portanto ao clonar o repositório, você estará instalando todo o pacote de APIs.

### Passo 1

Clone o diretório Reservapi para seu computador utilizando o comando:
```sh
$ git-clone https://github.com/lucasbguima/APIs.git
```
Obs: Todos subdiretórios do repositório APIs serão clonados. 

### Passo 2
Entre na pasta do Reservapi e Crie e Ative um ambiente virtual chamado "venv":

```sh
$ cd reservapi
$ pipenv venv
$ venv\scripts\activate
```

OBS: Por padrão, confira seu sistema operacional ao executar o comando acima:

WINDOWS: utilize barra invertida "\" para separar os diretórios.
LINUX OU MACoS: utilize barra normal "/" para separar os diretórios.

### Passo 3

Entre na pasta do Backend, crie e rode as migrations:

```sh
$ cd backend
$ python manage.py makemigrations
$ python manage.py migrate
```

### Passo 4

Crie um super-usuário para ser o administrador:

```sh
$ python manage.py createsuperuser
```
Obs: será solicitado no terminal 3 campos (nome, e-mail e senha), utilize-os quando for acessar a página de login da administração do site. 

### Passo 5

Para rodar o servidor de desenvolvimento:

```sh
$ python manage.py runserver
```

# Links

Para acessar o servidor rodando no link da administração:
- http://localhost:8000/admin

Para acessar os endpoints da API:
- http://localhost:8000/api/users
- http://localhost:8000/api/hotels
- http://localhost:8000/api/agendamentos

O link principal http://localhost:8000 está inativo.


Licença
----

MIT

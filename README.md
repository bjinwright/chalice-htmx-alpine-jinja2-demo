# chalice-htmx-alpine-jinja2-demo

This is a demo of a simple Chalice app that uses HTMX, Alpine, and Jinja2. It's a simple app that allows you             to
view the data from the [JSONPlaceHolder](https://jsonplaceholder.typicode.com) API</a>. The data is
fetched from the API using HTMX and then rendered using Jinja2.

## Demo

[https://chalice.b-cdn.net](https://chalice.b-cdn.net)

## Run Locally

Install Poetry
```shell
pip install poetry
```
Use Poetry to install the requirements
```shell
poetry install
```
Run the Chalice local server
```shell
poetry run chalice local
```
Deploy it to your AWS account
```shell
poetry run chalice deploy
```
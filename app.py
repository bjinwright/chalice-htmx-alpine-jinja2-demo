import requests
from chalice import Chalice

from chalicelib.utilities.html import render_template, generic_list_view, generic_detail_view

app = Chalice(app_name='nuclei')


@app.route('/')
def index():
    return render_template(app.current_request, 'index.html', {'name': 'james'})


# Posts
@app.route('/posts/{page}', methods=['GET'])
def get_posts(page):
    page = int(page)

    return generic_list_view(
        app.current_request,
        'https://jsonplaceholder.typicode.com/posts',
        'posts/list.html',
        current_page=page,
        partial_template='posts/partials/list.html',
        extra_context={'title': 'Posts'},
        title_template='Posts - {page_obj}'
    )


@app.route('/posts/detail/{post_id}', methods=['GET'])
def get_post(post_id):
    return generic_detail_view(
        app.current_request,
        f'https://jsonplaceholder.typicode.com/posts/{post_id}',
        'posts/detail.html',
        extra_context={'title': 'Post'},
        partial_template='posts/partials/detail.html')


@app.route('/posts/{post_id}/comments', methods=['GET'])
def get_post_comments(post_id):
    return generic_list_view(
        app.current_request,
        f'https://jsonplaceholder.typicode.com/posts/{post_id}/comments',
        'list.html',
        partial_template='includes/list.includes.html',
        extra_context={'title': 'Comments'}
    )


@app.route('/posts/{post_id}/comments/{comment_id}', methods=['GET'])
def get_post_comment(post_id, comment_id):
    return generic_detail_view(
        f'https://jsonplaceholder.typicode.com/posts/{post_id}/comments/{comment_id}',
        'detail.html')


# Albums
@app.route('/albums/{page}', methods=['GET'])
def get_albums(page):
    page = int(page)
    return generic_list_view(
        app.current_request,
        'https://jsonplaceholder.typicode.com/albums',
        'list.html',
        current_page=page,
        partial_template='includes/list.includes.html',
        extra_context={'title': 'Albums'}
    )


@app.route('/albums/{album_id}', methods=['GET'])
def get_album(album_id):
    album = requests.get(
        f'https://jsonplaceholder.typicode.com/albums/{album_id}').json()
    return generic_list_view(
        app.current_request,
        f'https://jsonplaceholder.typicode.com/albums/{album_id}/photos',
        'list.html',
        extra_context={'album': album})


# Todos
@app.route('/todos', methods=['GET'])
def get_todos():
    return generic_list_view(
        app.current_request,
        'https://jsonplaceholder.typicode.com/todos',
        'list.html',
        partial_template='includes/list.includes.html',
        extra_context={'title': 'Todos'}
    )


@app.route('/todos/{todo_id}', methods=['GET'])
def get_todo(todo_id):
    return generic_detail_view(
        f'https://jsonplaceholder.typicode.com/todos/{todo_id}',
        'detail.html')


# Users
@app.route('/users', methods=['GET'])
def get_users():
    return generic_list_view(
        app.current_request,
        'https://jsonplaceholder.typicode.com/users',
        'list.html')


@app.route('/users/dropdown', methods=['GET'])
def get_users_dropdown():
    return generic_list_view(
        app.current_request,
        'https://jsonplaceholder.typicode.com/users',
        'users/dropdown.html',1, per_page=100)
import requests
from chalice import Chalice

from chalicelib.utilities.html import render_template, generic_list_view, generic_detail_view

app = Chalice(app_name='nuclei')


@app.route('/')
def index():
    return render_template(
        app.current_request,
        'index.html',
        {'name': 'james'},
        title_template='Chalice + HTMX + Alpine + Jinja2 Demo'
    )


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
        partial_template='posts/partials/detail.html',
        title_template='{object[title]}'
    )


@app.route('/posts/detail/{post_id}/comments', methods=['GET'])
def get_post_comments(post_id):
    return generic_list_view(
        app.current_request,
        f'https://jsonplaceholder.typicode.com/posts/{post_id}/comments',
        'list.html',
        partial_template='includes/list.includes.html',
        extra_context={'title': 'Comments'}
    )


# Albums
@app.route('/albums/{page}', methods=['GET'])
def get_albums(page):
    page = int(page)
    return generic_list_view(
        app.current_request,
        'https://jsonplaceholder.typicode.com/albums',
        'albums/list.html',
        current_page=page,
        partial_template='albums/partials/list.html',
        extra_context={'title': 'Albums'},
        title_template='Albums - {page_obj}'
    )


@app.route('/albums/detail/{album_id}', methods=['GET'])
def get_album(album_id):
    return generic_detail_view(
        app.current_request,
        f'https://jsonplaceholder.typicode.com/albums/{album_id}',
        'albums/detail.html',
        extra_context={'title': 'Album', 'album_id': album_id},
        partial_template='albums/partials/detail.html',
        title_template='{object[title]}'
    )

@app.route('/albums/detail/{album_id}/photos', methods=['GET'])
def get_album_photos(album_id):
    return generic_list_view(
        app.current_request,
        f'https://jsonplaceholder.typicode.com/photos/?albumId={album_id}',
        'albums/partials/photos/list.html',
        current_page=1,
        partial_template='albums/partials/photos/list.html',
        extra_context={'title': 'Photos'}
    )
# Users
@app.route('/users/{page}', methods=['GET'])
def get_users(page):
    page = int(page)
    return generic_list_view(
        app.current_request,
        'https://jsonplaceholder.typicode.com/users',
        'users/list.html',
        current_page=page,
        partial_template='users/partials/list.html',
        extra_context={'title': 'Users'},
        title_template='Users - {page_obj}'
    )


@app.route('/users/detail/{user_id}', methods=['GET'])
def get_user(user_id):
    return generic_detail_view(
        app.current_request,
        f'https://jsonplaceholder.typicode.com/users/{user_id}',
        'users/detail.html',
        extra_context={'title': 'User'},
        partial_template='users/partials/detail.html',
        title_template='{object[name]}'
    )


@app.route('/users/dropdown', methods=['GET'])
def get_users_dropdown():
    return generic_list_view(
        app.current_request,
        'https://jsonplaceholder.typicode.com/users',
        'users/dropdown.html', 1, per_page=100)

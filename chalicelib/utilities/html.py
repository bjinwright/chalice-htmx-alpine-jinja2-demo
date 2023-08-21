from pathlib import Path

import requests
from chalice import Response
from envs import env
from jinja2 import Environment, FileSystemLoader

from chalicelib.utilities.paginate import Page

TEMPLATE_DIR = Path(__file__).parent.parent / 'templates'
JINJA2_ENV = Environment(loader=FileSystemLoader(str(TEMPLATE_DIR)))
BASE_PATH = env('BASE_PATH','')

def first_letters_filter(s):
    words = s.split()
    if not words:
        return None
    first_word = words[0]
    last_word = words[-1]
    return f"{first_word[0]}{last_word[0]}".upper()


JINJA2_ENV.filters['first_letters'] = first_letters_filter


def render_template(
        request, html_template, context,
        partial_template=None, headers=None, title_template=None):
    context['base_path'] = BASE_PATH

    headers = headers or {}
    # If the request is an HX request, the USE-PARTIAL header is set
    # and the partial template is set, use
    # the partial template instead of the full template.
    if request.headers.get('HX-Request') and \
            request.headers.get('Use-Partials') and partial_template:
        template_name = JINJA2_ENV.get_template(partial_template)
    else:
        template_name = JINJA2_ENV.get_template(html_template)
    template = JINJA2_ENV.get_template(template_name)
    base_headers = {
        'Content-Type': 'text/html'
    }
    if title_template:
        title = title_template.format(**context)
        headers['New-Title'] = title
    base_headers.update(headers)
    return Response(template.render(context),
                    status_code=200, headers=base_headers)


def get_filter_url(query: dict):
    """
    Get the filter url
    :param url:
    :param query:
    :param page:
    :return:
    """
    # Remove ignored query params
    if query:
        if '_page' in query:
            del query['_page']
    else:
        query = {}
    url = ''
    if query:
        url += '?'
        for key, value in query.items():
            if value:
                url += f'{key}={value}&'
        url = url[:-1]
    return url


def generic_list_view(request, url, html_template,
                      current_page,partial_template=None,
                      extra_context=None, per_page=10,
                      headers=None, title_template=None):
    filters = get_filter_url(request.query_params)
    url = f"{url}{filters}"
    object_list = requests.get(url).json()
    # NOTE: This is not how I would do pagination in production. Ideally there
    # would be page information in the JSON object received from the API.
    page_obj = Page(current_page, object_list, per_page=per_page)
    # NOTE: This is a hack to get the url prefix for the pagination links. If this were
    # a production app I would figure out a way to reverse the url in the template.
    url_prefix = f"/{request.path.split('/')[1]}/"
    context = {
        'object_list': object_list,
        'page_obj': page_obj,
        'filters': filters,
        'url_prefix': url_prefix
    }
    if extra_context:
        context.update(extra_context)
    return render_template(request, html_template, context,
                           partial_template=partial_template,
                           headers=headers, title_template=title_template)


def generic_detail_view(request, url, html_template, partial_template=None, extra_context=None,
                        title_template: str = None, headers=None):
    r = requests.get(url)
    context = {'object': r.json()}
    if extra_context:
        context.update(extra_context)
    return render_template(request, html_template, context, partial_template, headers=headers,
                           title_template=title_template)

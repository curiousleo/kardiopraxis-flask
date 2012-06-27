from flask import Flask, redirect, url_for, render_template, \
                  render_template_string

from flask.ext.flatpages import FlatPages
from flask.ext.assets import Environment

from markdown import markdown

# configuration
DEBUG = True
MENU = (
    ('Startseite', 'index'),
    ('Praxisteam', 'praxisteam'),
    ('Sprechstunden', 'sprechstunden'),
    ('Leistungen', 'leistungen'),
    ('Anfahrt', 'anfahrt'),
    ('Kooperationen', 'kooperationen'),
    ('Pflichtangaben', 'pflichtangaben'),
)
DEFAULT_TEMPLATE = 'layout.html'
DEFAULT_JS = []
ASSET_DIR = 'gen'
MARKDOWN_EXTENSIONS = ['tables', 'extra']
FLATPAGES_HTML_RENDERER = 'kardiopraxis.render_html'

# create app
app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
assets = Environment(app)

# define views
@app.route('/', defaults={'path': 'index'})
@app.route('/<path:path>.htm') # use legacy URLs
def page(path):
    '''Render Markdown-formatted page.'''
    page = pages.get_or_404(path)

    meta_or_default = lambda x, y: page.meta.get(x, app.config[y])
    template = meta_or_default('template', 'DEFAULT_TEMPLATE')
    js = meta_or_default('js', 'DEFAULT_JS')

    return render_template(template, page=page, js=js)

# page rendering function
def render_html(text):
    '''Render Markdown to HTML in three steps:

    1. Render as Jinja2 template string (executing macros) => Markdown
    2. Render as Markdown => HTML
    3. Typogrify => Nicer HTML (if typogrify is available)
    '''
    md = render_template_string(text)
    html = markdown(md, extensions=app.config['MARKDOWN_EXTENSIONS'])
    try:
        from typogrify import typogrify
        return typogrify(html)
    except ImportError:
        return html

# run app
if __name__ == '__main__':
    app.run()

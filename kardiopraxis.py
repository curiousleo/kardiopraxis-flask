from flask import Flask, request, session, g, redirect, url_for, \
                  abort, render_template, flash

from markdown import markdown
from typogrify import typogrify

# configuration
DEBUG = True
MENU = (
    ('Startseite', 'index.html'),
    ('Praxisteam', 'praxisteam.html'),
    ('Sprechstunden', 'sprechstunden.html'),
    ('Leistungen', 'leistungen.html'),
    ('Anfahrt', 'anfahrt.html'),
    ('Kooperationen', 'kooperationen.html'),
    ('Pflichtangaben', 'pflichtangaben.html'),
)
START_PAGE = 'index.html'
MARKDOWN_EXTENSIONS = ['tables', 'extra']
FREEZER_BASE_URL = 'file:///home/leo/Code/kardiopraxis-flask/build'

# create app
app = Flask(__name__)
app.config.from_object(__name__)

# define views
@app.route('/')
def start_page():
    '''Redirect to START_PAGE.'''
    return redirect(url_for('page', filename=START_PAGE))

@app.route('/<filename>')
def page(filename):
    '''Render Markdown-formatted page.'''
    return render_template(filename)

# custom jinja2 filters
@app.template_filter('markdown_extra')
def markdown_filter(s):
    return typogrify(markdown(s,
                     extensions=app.config['MARKDOWN_EXTENSIONS']))

# run app
if __name__ == '__main__':
    app.run()

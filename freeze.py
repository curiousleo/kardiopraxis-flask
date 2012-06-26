from flask.ext.frozen import Freezer
from kardiopraxis import app

# create freezer
freezer = Freezer(app)

@freezer.register_generator
def page():
    for __, name in app.config['MENU']:
        yield '/{}/'.format(name)

@freezer.register_generator
def legacy_page():
    for __, name in app.config['MENU']:
        yield '/{}.htm'.format(name)

# run freezer
if __name__ == '__main__':
    freezer.freeze()

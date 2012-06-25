from flask.ext.frozen import Freezer
from kardiopraxis import app

# create freezer
freezer = Freezer(app)

# run freezer
if __name__ == '__main__':
    freezer.freeze()

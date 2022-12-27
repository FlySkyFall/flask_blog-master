import os

from flask import Flask
from config import Config

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'ikljsdehgfno;slkefjhgwielkjtnmgfwoiehjnewrkgn'


app.config.from_object(Config)
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'fpri.db')))

import app
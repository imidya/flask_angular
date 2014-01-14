import os
import json
from flask import Flask

app = Flask(__name__)
app.debug = True

import flask_angular.controller
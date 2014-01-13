import os
import json
from flask import Flask, request, Response, render_template, url_for

app = Flask(__name__)

import flask_angular.controller
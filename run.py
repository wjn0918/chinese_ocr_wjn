#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask, render_template, jsonify, Blueprint, request 
from flask_docs import ApiDoc
from scheduler import *
import json

app = Flask(__name__)

# Local loading
# app.config['API_DOC_CDN'] = False

# Disable document pages
# app.config['API_DOC_ENABLE'] = False

# Api Document needs to be displayed
app.config['API_DOC_MEMBER'] = ['api']

ApiDoc(app)

api = Blueprint('api', __name__)

@api.route('/rec', methods=['POST'])
def rec():
    """extract txt from any file

    recognition txt from doc,docx,pdf
    

    Args:
        string: file_url
 
    Returns:
        string: content of file 
    """
    data = request.get_data()
    data = json.loads(data)
    result = []
    for index, file_url in enumerate(data['file_url']):
        result.append(recognition(file_url))
    return jsonify(result)






app.register_blueprint(api, url_prefix='/api')


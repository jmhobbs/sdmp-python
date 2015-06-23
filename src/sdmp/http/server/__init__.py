# -*- coding: utf-8 -*-

from flask import Flask, Request, request, render_template
import os.path
from werkzeug.wrappers import BaseRequest
from sdmp.node import Node
from .config import BaseConfig


def create_app(name="sdmp.http"):
    app = Flask('sdmp.http',
                template_folder=os.path.join(os.path.dirname(__file__), "templates"))

    app.config.from_object(BaseConfig)
    app.config.from_envvar('CONFIG', silent=True)
    app.debug = app.config.get('DEBUG', False)

    class RawRequest(Request, BaseRequest):
        want_form_data_parsed = False

    app.request_class = RawRequest

    node = Node()
    node.load_private_key_from_file(
        app.config['NODE_PRIVATE_KEY_PATH'],
        app.config.get('NODE_PRIVATE_KEY_PASSPHRASE')
    )

    @app.route("/", methods=("GET", "POST"))
    def sdmp_request():
        if request.method == "POST":
            return request.get_data()
        return render_template("index.html")

    return app

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, jsonify


def create_app():
    app = Flask(__name__)

    @app.route("/", defaults={"path": ""})
    @app.route("/<path:path>")
    def catch_all(path):
        print("Path: {}".format(path))
        return render_template("vue/index.html")

    @app.route("/api/v1/foo")
    def api_foo():
        return jsonify("API V1 FOO"), 200

    return app

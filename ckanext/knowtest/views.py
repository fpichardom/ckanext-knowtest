from flask import Blueprint


knowtest = Blueprint(
    "knowtest", __name__)


def page():
    return "Hello, knowtest!"


knowtest.add_url_rule(
    "/knowtest/page", view_func=page)


def get_blueprints():
    return [knowtest]

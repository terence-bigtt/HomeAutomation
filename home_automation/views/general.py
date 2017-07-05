from flask import Blueprint, render_template, request
from home_automation.controllers.general.main_menu import get_configured_menu
from jinja2 import Undefined

mod = Blueprint('general', __name__)


@mod.route("/")
def index():
    menu = get_configured_menu()
    iframe_href = request.args.get('iframe_href')
    template_args = {"menu": menu.items, "iframe_href": iframe_href}
    filtered_args = {k: template_args.get(k) for k in template_args.keys() if template_args.get(k) is not None}
    return render_template('general/index.html', **filtered_args)

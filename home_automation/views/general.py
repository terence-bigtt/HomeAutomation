from flask import Blueprint, render_template, Response
from home_automation.controllers.general.main_menu import get_configured_menu
from home_automation.controllers.general.links import get_configured_links
from home_automation.controllers.monitoring.ipcam import get_configured_ip_cams

mod = Blueprint('general', __name__)

menu = get_configured_menu()
cams = get_configured_ip_cams()


@mod.route("/")
def index():
    return render_template('general/index.html', menu=menu.items)


@mod.route("/links")
def links():
    links = get_configured_links()
    return render_template("general/links.html", links=links.links, menu=menu.items)






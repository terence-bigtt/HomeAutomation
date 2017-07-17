from flask import Blueprint, render_template, request
from home_automation.controllers.general.main_menu import get_configured_menu
from home_automation.controllers.general.links import get_configured_links
from home_automation.controllers.monitoring.ipcam import get_configured_ip_cams

mod = Blueprint('general', __name__)

menu = get_configured_menu()
conf_links = get_configured_links()
cams = get_configured_ip_cams()


@mod.route("/")
def index():
    return render_template('general/index.html', menu=menu.items)


@mod.route("/links")
def links():
    return render_template("general/links.html", links=conf_links.links, menu=menu.items)


@mod.route("/monitor")
def monitor():
    return render_template("general/cam_monitor.html", menu=menu.items, cams=cams)


@mod.route("/config/menu")
def menu_config():
    return render_template("settings/menu_configuration.html")

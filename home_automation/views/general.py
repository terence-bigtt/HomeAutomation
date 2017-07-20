from flask import Blueprint, render_template, request
from home_automation.controllers.general.main_menu import get_configured_menu
from home_automation.controllers.general.links import get_configured_links
from home_automation.controllers.monitoring.ipcam import cams, get_cam


mod = Blueprint('general', __name__)

menu = get_configured_menu()
conf_links = get_configured_links()


@mod.route("/")
def index():
    return render_template('general/index.html', menu=menu.items)


@mod.route("/links")
def links():
    return render_template("general/links.html", links=conf_links.links, menu=menu.items)


@mod.route("/monitor")
def monitor():
    cam_id = request.args.get("id")
    selected_cams = cams
    if cam_id is not None:
        selected_cams = [get_cam(cam_id)]
    return render_template("general/cam_monitor.html", menu=menu.items, cams=selected_cams)


@mod.route("/config/menu")
def menu_config():
    return render_template("settings/menu_configuration.html")

import logging
import threading

import bottle
import conf
import nmoperations
import pify

_nm = None
_conf = None


def load_tpl(path: str) -> str:
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError:
        logging.error("load_tpl: template not found: {}".format(path))


@bottle.route("/")
def index():
    return bottle.template(load_tpl("web/views/pify.tpl"), pify_server_title=_conf.pify_server_title(),
                           networks=_nm.get_ssids())


@bottle.route("/refresh")
def refresh():
    timer = threading.Timer(5, pify.refresh, (_nm,))
    timer.start()
    return bottle.template(load_tpl("web/views/refresh.tpl"), pify_server_title=_conf.pify_server_title())


@bottle.route("/forget")
def forget_devices():
    timer = threading.Timer(5, pify.forget_networks, (_nm,))
    timer.start()
    return bottle.template(load_tpl("web/views/refresh.tpl"), pify_server_title=_conf.pify_server_title())


@bottle.post("/connect/open")
def connect_open():
    form = bottle.request.forms
    if "security_type" in form and "ssid" in form:
        ssid = form["ssid"]
        if form["security_type"] == "open":
            timer = threading.Timer(5, pify.connect_open, (_nm, ssid))
            timer.start()
            return bottle.template(load_tpl("web/views/post_connect.tpl"), pify_server_title=_conf.pify_server_title(),
                                   pify_post_connect_url=_conf.pify_post_connect_url(),
                                   ssid=ssid)
    else:
        return "Invalid connection type"


@bottle.post("/connect/wpa")
def connect_wpa():
    form = bottle.request.forms
    if "security_type" in form and "ssid" in form and "ssid_pass" in form:
        ssid = form["ssid"]
        ssid_pass = form["ssid_pass"]
        if form["security_type"] == "wpa":
            timer = threading.Timer(5, pify.connect_wpa, (_nm, ssid, ssid_pass))
            timer.start()
            return bottle.template(load_tpl("web/views/post_connect.tpl"), pify_server_title=_conf.pify_server_title(),
                                   ssid=ssid)
    else:
        return "Invalid connection type"

    return "<p>" + str(bottle.request.forms) + "</p>"


# Static file routes
@bottle.route("/css/<file>")
def css(file: str):
    return bottle.static_file(file, "web/css")


@bottle.route("/js/<file>")
def js(file: str):
    return bottle.static_file(file, "web/js")


@bottle.route("/img/<file>")
def img(file: str):
    return bottle.static_file(file, "web/img")


def run(config: conf.PifyConfiguration, nm: nmoperations.NM):
    global _nm
    global _conf
    _nm = nm
    _conf = config

    bottle.run(host="0.0.0.0", port=80)


if __name__ == "__main__":
    config = conf.PifyConfiguration()
    nm = nmoperations.NM(config)
    run(config, nm)

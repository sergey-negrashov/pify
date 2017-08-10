import logging
import threading

import bottle
import nmoperations
import pify

_nm = None

def load_tpl(path: str) -> str:
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError:
        logging.error("load_tpl: template not found: {}".format(path))


@bottle.route("/")
def index():
    #nm = nmoperations.NM()
    #print(_nm)
    #print(_nm.get_ssids())
    return bottle.template(load_tpl("web/views/pify.tpl"), networks=_nm.get_ssids())


@bottle.route("/refresh")
def refresh():
    #pify.wait_then_run(5, pify.refresh, [nmoperations.NM()])
    timer = threading.Timer(5, pify.refresh, (_nm,))
    timer.start()
    return bottle.template(load_tpl("web/views/refresh.tpl"))

@bottle.route("/forget")
def forget_devices():
    #nm = nmoperations.NM()
    timer = threading.Timer(5, pify.forget_networks, (_nm,))
    timer.start()
    return bottle.template(load_tpl("web/views/refresh.tpl"))


@bottle.post("/connect/open")
def connect_open():
    #nm = nmoperations.NM()
    form = bottle.request.forms
    if "security_type" in form and "ssid" in form:
        ssid = form["ssid"]
        if form["security_type"] == "open":
            timer = threading.Timer(5, pify.connect_open, (_nm, ssid))
            timer.start()
            return bottle.template(load_tpl("web/views/post_connect.tpl"), ssid=ssid)
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
            return bottle.template(load_tpl("web/views/post_connect.tpl"), ssid=ssid)
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


def run(nm):
    global _nm
    _nm = nm
    bottle.run(host="0.0.0.0", port=80)


if __name__ == "__main__":
    nm = nmoperations.NM()
    run(nm)

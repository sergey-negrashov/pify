import bottle
import nmoperations
import pify


# Application routes
@bottle.route("/")
def index():
    nm = nmoperations.NM()
    with open("web/views/pify.tpl", "r") as f:
        content = f.read()
        return bottle.template(content, networks=nm.get_ssids())


@bottle.route("/refresh")
def refresh():
    with open("web/views/refresh.tpl", "r") as f:
        content = f.read()
        pify.wait_then_run(5, pify.refresh, [nmoperations.NM()])
        return bottle.template(content)


@bottle.post("/connect/open")
def connect_open():
    nm = nmoperations.NM()
    form = bottle.request.forms
    if "security_type" in form and "ssid" in form:
        ssid = form["ssid"]
        if form["security_type"] == "open":
            pify.wait_then_run(5, pify.connect_open, [nm, ssid])
            return "Please check TODO FILL ME IN to make sure your device is working."
    else:
        return "Invalid connection type"

@bottle.post("/connect/wpa")
def connect_wpa():
    nm = nmoperations.NM()
    form = bottle.request.forms
    if "security_type" in form and "ssid" in form and "ssid_pass" in form:
        ssid = form["ssid"]
        ssid_pass = form["ssid_pass"]
        if form["security_type"] == "wpa":
            pify.wait_then_run(5, pify.connect_wpa, [nm, ssid, ssid_pass])
            return "Please check TODO FILL ME IN to make sure your device is working."
    else:
        return "Invalid connection type"

    return "<p>" + str(bottle.request.forms) + "</p>"


# Static file routes
@bottle.route("/css/<file>")
def css(file):
    return bottle.static_file(file, "web/css")


@bottle.route("/js/<file>")
def js(file):
    return bottle.static_file(file, "web/js")


@bottle.route("/img/<file>")
def img(file):
    return bottle.static_file(file, "web/img")


def run():
    bottle.run(host="0.0.0.0", port=80)


if __name__ == "__main__":
    run()

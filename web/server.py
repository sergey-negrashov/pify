import bottle
import nmoperations

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
        return bottle.template(content)


@bottle.post("/connect/open")
def connect_open():
    nm = nmoperations.NM()
    form = bottle.request.forms
    if "security_type" in form and "ssid" in form:
        ssid = form["ssid"]
        if form["security_type"] == "open":
            if nm.is_in_AP_mode():
                nm.disable_AP_mode()
            nm.add_connection_open(ssid)
            nm.activate_connection(ssid)
    else:
        return "Invalid connection type"

    return "<p>" + str(bottle.request.forms) + "</p>"


@bottle.post("/connect/wpa")
def connect_wpa():
    nm = nmoperations.NM()
    form = bottle.request.forms
    if "security_type" in form and "ssid" in form and "ssid_pass" in form:
        ssid = form["ssid"]
        ssid_pass = form["ssid_pass"]
        if form["security_type"] == "wpa":
            if nm.is_in_AP_mode():
                nm.disable_AP_mode()
            nm.add_connection_wpa(ssid, ssid_pass)
            nm.activate_connection(ssid)
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


def _run():
    bottle.run(host="0.0.0.0", port=80)


if __name__ == "__main__":
    _run()

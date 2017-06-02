import bottle
import nmoperations
import os

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
    return "<p>" + str(bottle.request.forms) + "</p>"


@bottle.post("/connect/wpa")
def connect_wpa():
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

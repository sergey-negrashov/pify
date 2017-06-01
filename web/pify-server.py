import bottle


# Application routes
@bottle.route("/")
def index():
    with open("views/pify.tpl", "r") as f:
        content = f.read()
        return bottle.template(content, networks=[["Test0", 0, 24],
                                                  ["Test1", 1, 49],
                                                  ["Test2", 1, 67],
                                                  ["Test3", 1, 88]])


@bottle.route("/test")
def test():
    with open("./views/pify.html", "r") as f:
        content = f.read()
        return bottle.template(content)


# Static file routes
@bottle.route("/css/<file>")
def css(file):
    return bottle.static_file(file, "./css")


@bottle.route("/js/<file>")
def js(file):
    return bottle.static_file(file, "./js")


@bottle.route("/img/<file>")
def img(file):
    return bottle.static_file(file, "./img")


def _run():
    bottle.run(host="0.0.0.0", port=80)


if __name__ == "__main__":
    _run()

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
    bottle.run(host="localhost", port=8000)

if __name__ == "__main__":
    _run()
import json
import sys


class PifyConfiguration():
    def __init__(self, path: str = None):
        self.conf = {}

        if path is not None:
            with(open(path, "r")) as f:
                self.conf = json.load(f)

    def get(self, key: str, default: str = None) -> str:
        if key in self.conf:
            return self.conf[key]
        else:
            return default

    def pify_server_title(self) -> str:
        return self.get("pify_server_title", "pify wireless agent")

    def pify_ap_ssid(self) -> str:
        return self.get("pify_ap_ssid", "pify")

    def pify_post_connect_url(self) -> str:
        return self.get("pify_post_connect_url", "#")

    def __str__(self):
        return "pify_server_title:{}\npify_api_ssid:{}\npify_post_connect_url:{}".format(self.pify_server_title(),
                                                                                         self.pify_ap_ssid(),
                                                                                         self.pify_post_connect_url())


if __name__ == "__main__":
    conf = PifyConfiguration("opq.pify.json")
    print(len(sys.argv))

import NetworkManager as nm
import dbus.mainloop.glib
import uuid


class NM:
    OPQ_AP_NAME = "OPQ"
    NM_DEVICE_STATE_DISCONNECTED = 30
    NM_DEVICE_STATE_ACTIVATED = 100

    def __init__(self):
        dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)

    def is_wifi_connected(self):
        for conn in nm.NetworkManager.ActiveConnections:
            settings = conn.Connection.GetSettings()['connection']
            if settings['type'] == "802-11-wireless":
                if settings['uuid'] != str(uuid.uuid3(uuid.NAMESPACE_DNS, self.OPQ_AP_NAME)):
                    return True
        return False

    def is_wifi_connecting(self):
        devices = nm.NetworkManager.GetDevices()
        for dev in devices:
            if dev.State > self.NM_DEVICE_STATE_DISCONNECTED and dev.State < self.NM_DEVICE_STATE_ACTIVATED:
                return True
        return False

    def is_in_AP_mode(self):
        for conn in nm.NetworkManager.ActiveConnections:
            settings = conn.Connection.GetSettings()['connection']
            if settings['uuid'] == str(uuid.uuid3(uuid.NAMESPACE_DNS, self.OPQ_AP_NAME)):
                return True
        return False


    def add_connection_wpa(self, SSID, password):
        connections = nm.Settings.ListConnections()
        connections = dict([(x.GetSettings()['connection']['id'], x) for x in connections])
        if SSID in  connections:
            connections[SSID].Delete()

        new_connection = {
            '802-11-wireless': {'mode': 'infrastructure',
                                'security': '802-11-wireless-security',
                                'ssid': SSID},
            '802-11-wireless-security': {
                'key-mgmt': 'wpa-psk',
                'psk' : password},
            'connection': {'id': SSID,
                           'type': '802-11-wireless',
                           'uuid': str(uuid.uuid3(uuid.NAMESPACE_DNS, SSID))},
            'ipv4': {'method': 'auto'},
            'ipv6': {'method': 'auto'}
        }
        nm.Settings.AddConnection(new_connection)

    def add_connection_open(self, SSID):
        connections = nm.Settings.ListConnections()
        connections = dict([(x.GetSettings()['connection']['id'], x) for x in connections])
        if SSID in  connections:
            connections[SSID].Delete()
        new_connection = {
            '802-11-wireless': {'mode': 'infrastructure',
                                #'security': '802-11-wireless-security',
                                'ssid': SSID},

            'connection': {'id': SSID,
                           'type': '802-11-wireless',
                           'uuid': str(uuid.uuid3(uuid.NAMESPACE_DNS, SSID))},
            'ipv4': {'method': 'auto'},
            'ipv6': {'method': 'auto'}
        }
        nm.Settings.AddConnection(new_connection)

    def create_AP(self):
        self.disable_AP_mode()
        new_connection = {
            '802-11-wireless': {'mode': 'ap',
                                'hidden': False,
                                'ssid': self.OPQ_AP_NAME},

            'connection': {'id': self.OPQ_AP_NAME,
                           'type': '802-11-wireless',
                           'uuid': str(uuid.uuid3(uuid.NAMESPACE_DNS, self.OPQ_AP_NAME)),
                           'autoconnect': False},
            'ipv4': {'method': 'auto'},
            'ipv6': {'method': 'auto'}
        }
        nm.Settings.AddConnection(new_connection)
        self.activate_connection(self.OPQ_AP_NAME)

    def disable_AP_mode(self):
        connections = nm.Settings.ListConnections()
        connections = dict([(x.GetSettings()['connection']['id'], x) for x in connections])
        if self.OPQ_AP_NAME in  connections:
            connections[self.OPQ_AP_NAME].Delete()


    def activate_connection(self, SSID):
        connections = nm.Settings.ListConnections()
        connections = dict([(x.GetSettings()['connection']['id'], x) for x in connections])
        if not SSID in connections:
            return False
        conn = connections[SSID]

        devices = nm.NetworkManager.GetDevices()
        for dev in devices:
            if dev.DeviceType == nm.NM_DEVICE_TYPE_WIFI:
                nm.NetworkManager.ActivateConnection(conn, dev, "/")
                return True
        print("No wifi device found")
        return False

    def activate_any_connection(self):
        nm.NetworkManager.Enable(False)
        nm.NetworkManager.Enable(True)

    def get_ssids(self):
        out = []
        self.disable_AP_mode()
        for dev in nm.NetworkManager.GetDevices():
            if dev.DeviceType != nm.NM_DEVICE_TYPE_WIFI:
                continue
            for ap in dev.GetAccessPoints():
                out.append([ap.Ssid, ap.Flags | ap.WpaFlags , ap.Strength])
        return out


if __name__ == '__main__':
    import time
    netman = NM()
    print("Connecting to test_network:")
    netman.add_connection_open("test_network")
    netman.activate_connection("test_network")
    while(netman.is_wifi_connecting()):
        print('.', end='', flush=True)
        time.sleep(0.1)
    print()
    print("Did we connect?")
    print(netman.is_wifi_connected())
    networks = netman.get_ssids()
    for network in networks:
        print ("Name: "  + network[0])
        print ("Encrypted: " + str(network[1] != 0))
        print ("Strength: " + str(network[2]))
    print("Going into AP mode:")
    netman.create_AP()
    time.sleep(1)
    print("Are we in AP mode?")
    print(netman.is_in_AP_mode())
    print("Turning off the AP mode?")
    netman.disable_AP_mode()
    print("Are we in AP mode?")
    print(netman.is_in_AP_mode())
    networks = netman.get_ssids()
    for network in networks:
        print ("Name: " + network[0])
        print ("Encrypted: " + str(network[1] != 0))
        print ("Strength: " + str(network[2]))
    netman.activate_any_connection()
    time.sleep(5)
    while(netman.is_wifi_connecting()):
        print('.', end='', flush=True)
        time.sleep(0.1)
    print()
    print("Did we connect?")
    print(netman.is_wifi_connected())
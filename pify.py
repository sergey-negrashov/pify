import logging
import sched
import time
import threading
import typing

import nmoperations
import web.server

logging.basicConfig(level=logging.DEBUG)


def wait_then_run(sec: int, fn: typing.Callable, args: typing.List, blocking: bool = False):
    s = sched.scheduler()
    s.enter(sec, 1, fn, tuple(args))
    s.run(blocking=blocking)


def disable_ap(nm: nmoperations.NM):
    while nm.is_in_AP_mode():
        print("Disabling AP mode")
        nm.disable_AP_mode()
        time.sleep(1)
    print("AP mode disabled")


def start_fsm(nm: nmoperations.NM):
    disable_ap(nm)
    is_conn_a(nm)


def is_conn_a(nm: nmoperations.NM):
    if nm.is_connected_to_internet():
        print("is_conn_a: connected to internet, monitoring connection")
        monitor_connection(nm)
    else:
        print("is_conn_a: not connected to internet, going into AP mode")
        connect_any(nm)


def is_conn_b(nm: nmoperations.NM):
    if nm.is_connected_to_internet():
        print("is_conn_b: connected to internet, monitoring connection")
        monitor_connection(nm)
    else:
        print("is_conn_b: not connected to internet, going into AP mode")
        enable_ap(nm)


def connect_any(nm: nmoperations.NM):
    disable_ap(nm)
    print("Attempting to connect to any open or previously connected networks")
    nm.activate_any_connection()
    wait_then_run(10, is_conn_b, [nm])


def monitor_connection(nm: nmoperations.NM):
    if nm.is_connected_to_internet():
        print("monitor_connection: connected to internet")
        wait_then_run(60 * 10, monitor_connection, [nm], blocking=True)
    else:
        print("monitor_connection: not connected to internet")
        enable_ap(nm)


def monitor_ap(nm: nmoperations.NM):
    print("monitor_ap")
    disable_ap(nm)
    is_conn_a(nm)


def enable_ap(nm: nmoperations.NM):
    while not nm.is_in_AP_mode():
        print("Attempting to go into AP mode")
        nm.create_AP()
        time.sleep(1)

    wait_then_run(60 * 10, monitor_ap, [nm])


def connect_open(nm: nmoperations.NM, ssid: str):
    print("connect_open")
    disable_ap(nm)
    nm.add_connection_open(ssid)
    nm.activate_connection(ssid)
    wait_then_run(5, monitor_connection, [nm])


def connect_wpa(nm: nmoperations.NM, ssid: str, passwd: str):
    print("connect_wpa")
    disable_ap(nm)
    nm.add_connection_wpa(ssid, passwd)
    nm.activate_connection(ssid)
    wait_then_run(5, monitor_connection, [nm])


def refresh(nm: nmoperations.NM):
    print("refresh")
    disable_ap(nm)
    time.sleep(5)
    enable_ap(nm)
    print("refresh done")

class PifyFsmThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.nm = nmoperations.NM()

    def run(self):
        start_fsm(self.nm)


if __name__ == "__main__":
    print("Starting pify")

    print("Starting pify FSM")
    fsm_thread = PifyFsmThread()
    fsm_thread.start()

    print("Starting bottle server")
    web.server.run()



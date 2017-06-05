import logging
import sched
import time

import nmoperations
import web.server


def wait_then_run(sec, fn, args):
    s = sched.scheduler()
    s.enter(sec, 1, fn, tuple(args))
    s.run(blocking=False)


def disable_ap(nm):
    while nm.is_in_AP_mode():
        logging.info("Disabling AP mode")
        nm.disable_AP_mode()
        time.sleep(1)
    logging.info("AP mode disabled")

def start_fsm(nm):
    connect_any(nm)


def connect_any(nm):
    disable_ap(nm)
    logging.info("Attempting to connect to any open or previously connected networks")
    nm.activate_any_connection()
    wait_then_run(10, is_connected, [nm])

def is_connected(nm):
    if nm.is_connected_to_internet():
        logging.info("is_connected: connected to internet, monitoring connection")
        monitor_connection(nm)
    else:
        logging.info("is_connected: not connected to internet, going into AP mode")
        connect_ap(nm)


def monitor_connection(nm):
    if nm.is_connected_to_internet():
        logging.info("monitor_connection: connected to internet")
        wait_then_run(60 * 10, monitor_connection, [nm])
    else:
        logging.info("monitor_connection: not connected to internet")
        connect_ap(nm)


def connect_ap(nm):
    while not nm.is_in_AP_mode():
        logging.info("Attempting to go into AP mode")
        nm.create_AP()
        time.sleep(1)

    wait_then_run(60 * 10, is_connected, [nm])



if __name__ == "__main__":
    logging.info("Starting pify")

    logging.info("Starting bottle server")
    web.server._run()

    logging.info("Starting pify FSM")
    nm = nmoperations.NM()
    start_fsm(nm)

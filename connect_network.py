import network
import secrets
import time

connect_timeout = 30

def connect_network():
    wlan = network.WLAN(network.STA_IF)  # create station interface
    wlan.active(True)  # activate the interface
    wlan.config(dhcp_hostname="datalogger_node1")
    wlan.connect(secrets.network, secrets.password)  # connect to an AP
    print("Connecting to wifi '{}'".format(secrets.network), end="...")
    connect_start = time.time()
    while not wlan.isconnected():
        if connect_start+connection_timeout>time.time():
            print("!!!Timeout!!!")
        print(".", end="")
        time.sleep(1)
    print("... Done!")
    print(wlan.ifconfig())  # get the interface's IP/netmask/gw/DNS addresses
connect_network()

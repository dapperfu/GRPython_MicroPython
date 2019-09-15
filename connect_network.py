import network
import secrets
def connect_network():
    wlan = network.WLAN(network.STA_IF)  # create station interface
    wlan.active(True)  # activate the interface
    wlan.connect(secrets.network, secrets.password)  # connect to an AP
    print("Connecting to wifi '{}'".format(secrets.network), end="...")
    while not wlan.isconnected():
        print(".", end="")
        time.sleep(1)
    print("... Done!")
    print(wlan.ifconfig())  # get the interface's IP/netmask/gw/DNS addresses
connect_network()

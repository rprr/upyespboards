from configwifi import wificreds
from time import sleep

# Start WiFi
def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(wificreds[0],wificreds[1])
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())

def start_network_services():
    try:
        #Start Telnet
        import utelnetserver
        utelnetserver.start()

        #Start ftp
        import uftpd

        # Start ntptime
        from ntptime import settime
        settime()
    except OSError:
        pass

do_connect()

start_network_services()

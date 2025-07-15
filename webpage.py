import network
import socket
import ure

# Load HTML page from file
def load_html():
    with open('index.html', 'r') as f:
        return f.read()

# HTTP server
def start_http():
    html = load_html()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 80))
    s.listen(5)
    while True:
        conn, addr = s.accept()
        req = conn.recv(1024)
        req_str = req.decode('utf-8')
        print('Request from:', addr)
        if 'favicon.ico' in req_str:
            conn.close()
            continue

        conn.send('HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n')
        conn.send(html)
        conn.close()

def start():
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid='Szolnoki Gamer', authmode=network.AUTH_OPEN)
    ap.ifconfig(('1.1.1.1', '255.255.255.0', '1.1.1.1', '1.1.1.1'))
    while ap.active() == False:
        pass
    print('AP started:', ap.ifconfig())
    start_http()

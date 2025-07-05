# blynklib.py - Blynk library for MicroPython
import socket
import struct
import time

class Blynk:
    def __init__(self, auth, server='blynk.cloud', port=80):
        self.auth = auth
        self.server = server
        self.port = port
        self.handlers = {}
        self.connect()

    def connect(self):
        ai = socket.getaddrinfo(self.server, self.port)
        addr = ai[0][-1]
        self.sock = socket.socket()
        self.sock.connect(addr)
        self._send(2, self.auth)

    def _send(self, cmd, data=''):
        d = self.auth if cmd == 2 else data
        self.sock.send(struct.pack("!BHH", cmd, 1, len(d)) + d.encode())

    def virtual_write(self, pin, val):
        self._send(20, f'{pin}\0{val}\0')

    def handle_event(self, evt_pin):
        def decorator(f):
            self.handlers[evt_pin] = f
            return f
        return decorator

    def run(self):
        self.sock.settimeout(0.05)
        try:
            data = self.sock.recv(1024)
            if len(data) > 0 and data[0] == 20:
                d = data[5:].decode().split('\0')
                pin = f'write {d[0]}'
                if pin in self.handlers:
                    self.handlers[pin](int(d[0]), d[1:])
        except:
            pass

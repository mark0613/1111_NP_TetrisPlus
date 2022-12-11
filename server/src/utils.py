import bcrypt
import random
import string
import socket
import struct

LOWER = string.ascii_lowercase
UPPER = string.ascii_uppercase
DIGITS = string.digits

def get_random_string(length: int=1):
    sequence = LOWER + UPPER + DIGITS
    result = ""
    if length < 1:
        length = 1
    for i in range(length):
        result += random.choice(sequence)
    return result

class UdpSocket:
    def __init__(self):
        self.buf_size = 1024
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    def bind(self, port):
        self.socket.bind(('', port))

    def send_to(self, data: str, address: tuple):
        ip, port = address
        port = int(port)
        self.socket.sendto(data.encode('utf-8'), (ip, port))

    def receive_from(self):
        data, (ip, port) = self.socket.recvfrom(self.buf_size)
        return data.decode("utf-8"), (ip, port)
    
    def close(self):
        self.socket.close()

class MulticastSender(UdpSocket):
    def __init__(self):
        super().__init__()
        ttl = struct.pack('b', 1)
        self.socket.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

class MulticastReceiver(UdpSocket):
    def __init__(self, port):
        super().__init__()
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(('', port))
    
    def join_group(self, group_ip):
        group = socket.inet_aton(group_ip)
        mreq = struct.pack('4sL', group, socket.INADDR_ANY)
        self.socket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    def drop_group(self, group_ip):
        group = socket.inet_aton(group_ip)
        mreq = struct.pack('4sL', group, socket.INADDR_ANY)
        self.socket.setsockopt(socket.IPPROTO_IP, socket.IP_DROP_MEMBERSHIP, mreq)

class PasswordEncoder:
    def encode(self, password: str) -> str:
        password = password.encode('utf-8')
        hash = bcrypt.hashpw(password, bcrypt.gensalt(10))
        return hash.decode('utf-8')

    def verify(self, password: str, hash: str) -> str:
        password = password.encode('utf-8')
        hash = hash.encode('utf-8')
        return bcrypt.checkpw(password, hash)

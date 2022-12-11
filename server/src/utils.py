import binascii
import hashlib
import random
import string
import select
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
    def encode(password, salt=None):
        if salt is None:
            salt = get_random_string(4)
        password_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), 100000)
        salt_str = binascii.hexlify(salt).decode()
        password_hash_str = binascii.hexlify(password_hash).decode()
        return salt_str, password_hash_str

    def verify(password, salt, password_hash):
        my_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), 100000)
        return my_hash == password_hash
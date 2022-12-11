import socket
import struct


class TcpSocket:
    def __init__(self, type="s"):
        self.backlog = 5
        self.buf_size = 1024
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if type == "s":
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
    def send(self, data: str):
        self.socket.send(data.encode("utf-8"))
    
    def receive(self):
        return self.socket.recv(self.buf_size).decode("utf-8")
    
    def close(self) -> str:
        self.socket.close()

class TcpServer(TcpSocket):
    def __init__(self):
        super().__init__("s")
    
    def accept(self, port: int):
        self.socket.bind(('', port))
        self.socket.listen(self.backlog)
        self.client, (remote_ip, remote_port) = self.socket.accept()
    
    def send(self, data: str):
        self.client.send(data.encode("utf-8"))
    
    def receive(self) -> str:
        return self.client.recv(self.buf_size).decode("utf-8")

class TcpClient(TcpSocket):
    def __init__(self):
        super().__init__("c")
    
    def connect(self, address: tuple):
        ip, port = address
        port = int(port)
        self.socket.connect((ip, port))

class UdpSocket:
    def __init__(self):
        self.buf_size = 1024
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    def bind(self, port):
        self.socket.bind(('localhost', port))

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

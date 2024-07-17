import socket
import threading
from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls 
import time
import random # import randint
from hashlib import sha256 
import os 

import datetime
from ryu.ofproto import ofproto_v1_3
import numpy as np
import json
from datetime import datetime
import ast

class MyController_auth(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]

    def __init__(self, *args, **kwargs):
        super(MyController_auth, self).__init__(*args, **kwargs)
        self.sockets = []
        self.lock = threading.Lock()

    def start(self):
        sdn_neigh1 = "10.13.3.19" 
        host = "10.13.4.78" # socket.gethostname()
        port1 = 8881  # socket server port number
        port2 = 8882
        port3 = 8883
        port4 = 8884
        port5 = 8885
        port6 = 8886
        port7 = 8887
        port8 = 8888
        port9 = 8889
        port10 = 8880

        self.ryu_scket = [None] * 10

        self.ryu_scket[0] = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # instantiate
        self.ryu_scket[0].bind((host, port1))  # bind host address and port together
        #self.ryu_scket[0].listen(20) 

        self.ryu_scket[1] = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # instantiate
        self.ryu_scket[1].bind((host, port2))  # bind host address and port together
        #self.ryu_scket[1].listen(20) 

        self.ryu_scket[2] = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # instantiate
        self.ryu_scket[2].bind((host, port3))  # bind host address and port together
        #self.ryu_scket[2].listen(20) 

        self.ryu_scket[3] = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # instantiate
        self.ryu_scket[3].bind((host, port4))  # bind host address and port together
        #self.ryu_scket[3].listen(20) 

        self.ryu_scket[4] = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # instantiate
        self.ryu_scket[4].bind((host, port5))  # bind host address and port together
        #self.ryu_scket[4].listen(20) 

        self.ryu_scket[5] = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # instantiate
        self.ryu_scket[5].bind((host, port6))  # bind host address and port together
        self.ryu_scket[5].listen(20) 

        self.ryu_scket[6] = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # instantiate
        self.ryu_scket[6].bind((host, port7))  # bind host address and port together
        self.ryu_scket[6].listen(20) 

        self.ryu_scket[7] = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # instantiate
        self.ryu_scket[7].bind((host, port8))  # bind host address and port together
        self.ryu_scket[7].listen(20) 

        self.ryu_scket[8] = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # instantiate
        self.ryu_scket[8].bind((host, port9))  # bind host address and port together
        self.ryu_scket[8].listen(20) 

        self.ryu_scket[9] = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # instantiate
        self.ryu_scket[9].bind((host, port10))  # bind host address and port together
        self.ryu_scket[9].listen(20) 
        '''
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((host, port1)) 
        self.sock.listen(10)
        '''
        self.logger.info('Waiting for Mininet RSU-Veh to connect...')
        self.logger.info('=============================')

        i = 0
        while True:
            if i == 0 : 
                print ("sdn_neigh1 IP is ", sdn_neigh1 )
                print ("sdn_neigh1 port  is ", type(port1)) 
                result = self.ryu_scket[i].connect((sdn_neigh1, port1))
                print(result)
                self.logger.info('Ryu Neigh1 connected:')
                ryu1_thread = threading.Thread(target=self.handle_ryus, args=(self.ryu_scket[i],))
                ryu1_thread.start()   
                i = i+1 

                
            else:
                connection, client_address = self.ryu_scket[i].accept()
                self.logger.info('Mininet AP connected: %s:%s', *client_address)
                veh_thread = threading.Thread(target=self.handle_client, args=(connection,))
                i = i + 1
                veh_thread.start()


    def stop(self):
        self.sock.close()
        self.logger.info('Socket closed')

    def send_to_all_mininet_aps(self, data):
        with self.lock:
            for sock in self.sockets:
                sock.sendall(data.encode())
                self.logger.debug('Sent data to Mininet AP: %s', data)

    def handle_client(self, rsu_conn):

        while True:
            data = rsu_conn.recv(1024).decode()
            #print("Topo recvd from RSU1 is ", data, "and type is ", type(data), "\n")

            # Convert JSON-formatted string to dictionary
            received_dict = json.loads(data)
            print("Topo recvd from RSU2 is ", received_dict, "and type is ", type(data), "\n")

            print("\n--------------------------------\n")

            sdn2_file = "sdn2.txt"
            with open(sdn2_file, 'w+') as file:
                received_dict = json.dumps(received_dict)
                json.dump(received_dict, file)
                print("RSU2 Topo is ", received_dict, "and type is ", type(received_dict))

                print ("\n-----------------------------\n")

    def handle_ryus(self, ryu_conn):
        sdn2_file = "sdn2.txt"
        sdn2_topo = "sdn2_topo.txt"
        sdn1_topo = "sdn1_topo.txt"
        timeinstance = 0
        while True:
            if os.path.exists(sdn2_file) == False:
                print("file doesn't exist")
                time.sleep(8)
            else:
                with open(sdn2_file, 'r') as file:
                    topo_rsu1 = file.read()
                    print("Topo sent from SDN 2 is ", topo_rsu1, "and type is ", type(topo_rsu1), "\n")
                    print("========================================")

                with open(sdn2_topo, "a") as topofile:
                    topofile.write("Topo at time \n")
                    topofile.write(str(timeinstance))
                    topofile.write("\n") 
                    Timestamp = str(datetime.now())
                    print(Timestamp)
                    topofile.write(Timestamp)
                    topofile.write("----\n") 
                    topofile.write(topo_rsu1)
                    print("TOPO stored.===================================")
         

                '''with open(sdn2_topo, "r") as Topo:
                    ctopo = Topo.read()
                    print("The current data on TOPO2 file ", ctopo, "\n" )
                    print("========================================")
                '''    
                timeinstance = timeinstance + 8
                JFdata = json.dumps(topo_rsu1)
                ryu_conn.send(JFdata.encode())
                    #time.sleep(8)
 	        #print("HANDLER YURUNNIN****************************************")
            data = ryu_conn.recv(1024).decode()
            #print("Topo recvd from RSU1 is ", data, "and type is ", type(data), "\n")

            # Convert JSON-formatted string to dictionary
            received_dict = ast.literal_eval(data)
            time.sleep(8)
            print("Topo recvd from SDN 1 is ", received_dict, "and type is ", type(data), "\n")
            with open(sdn1_topo, 'a') as sdn1topo:
                sdn1topo.write("Topo at time \n")
                sdn1topo.write(str(timeinstance))
                sdn1topo.write("\n") 
                Timestamp = str(datetime.now())
                sdn1topo.write("\n")
                sdn1topo.write(received_dict)
                sdn1topo.write("\n")
                print("SDN1 TOPO stored.===================================")
            
            with open(sdn1_topo, "r") as sdn1topo:
                    ctopo = sdn1topo.read()
                    print("The current data on SDN1 topo file ", ctopo, "\n" )
                    print("========================================")
            print("\n--------------------------------\n")
            print("\n--------------------------------\n")

            #data = ryu_conn.recv(1024).decode()  # sdn2 - sdn1
            #ryu_conn.send(JFdata.encode())
            #print("Topo recvd from RSU1 is ", data, "and type is ", type(data), "\n")

            # Convert JSON-formatted string to dictionary
            #received_dict = json.loads(JFdata)
            #print("Topo sent from SDN is ", received_dict, "and type is ", type(data), "\n")

            #print("\n--------------------------------\n")
            #time.sleep(15)

            # read sdn1.txt and send to sdn2
            

            #if sdn1_file exits :
            #    wait(

	    
    @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
    def packet_in_handler(self, ev):
        pkt = packet.Packet(ev.msg.data)
        # Process the packet and generate some data to send to the Mininet APs
        data = 'Some data to send to Mininet APs'
        self.send_to_all_mininet_aps(data)

if __name__ == '__main__':
    from ryu import cfg
    from ryu import utils

    cfg.CONF.register_opts([
        cfg.IntOpt('controller1_port', default=6633,
                   help='OpenFlow controller port for App1'),
    ])

    utils.load_modules(['MyController_auth'])
    app_manager.run()

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
import ast
from datetime import datetime

class MyController_auth(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]

    def __init__(self, *args, **kwargs):
        super(MyController_auth, self).__init__(*args, **kwargs)
        self.sockets = []
        self.lock = threading.Lock()

    def start(self):

        sdn_neigh1 = "10.13.4.78"
        host = "10.13.3.19" # socket.gethostname()
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
        self.ryu_scket[0].listen(20) 

        self.ryu_scket[1] = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # instantiate
        self.ryu_scket[1].bind((host, port2))  # bind host address and port together
        self.ryu_scket[1].listen(20) 

        self.ryu_scket[2] = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # instantiate
        self.ryu_scket[2].bind((host, port3))  # bind host address and port together
        self.ryu_scket[2].listen(20) 

        self.ryu_scket[3] = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # instantiate
        self.ryu_scket[3].bind((host, port4))  # bind host address and port together
        self.ryu_scket[3].listen(20) 

        self.ryu_scket[4] = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # instantiate
        self.ryu_scket[4].bind((host, port5))  # bind host address and port together
        self.ryu_scket[4].listen(20) 

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
            if i ==0 : 
                print("connection pending 1111111")
                ryu_conn, ryu_client1  = self.ryu_scket[i].accept()
                #if ryu_client1 == sdn_neigh1:

                self.logger.info('Ryu Neigh1 connected: %s:%s', *ryu_client1)
                ryu1_thread = threading.Thread(target=self.handle_ryus, args=(ryu_conn,))
                ryu1_thread.start()    
                
                i = i + 1

        
            else :
                connection, client_address = self.ryu_scket[i].accept()
                self.logger.info('Mininet AP connected: %s:%s', *client_address)
                veh_thread = threading.Thread(target=self.handle_client, args=(connection,))
                veh_thread.start()
                i = i + 1
        '''while True:
            if i ==0 : 
                ryu_conn, ryu_client1  = self.ryu_scket[i].accept()
                if ryu_client1[0] == sdn_neigh1:
                    i = i + 1
                    self.logger.info('Ryu Neigh1 connected: %s:%s', *ryu_client1)
            connection, client_address = self.ryu_scket[i].accept()
            self.logger.info('Mininet AP connected: %s:%s', *client_address)
            veh_thread = threading.Thread(target=self.handle_client, args=(connection,))
            i = i+1
            data = self.Ret_handler(connection)
            ryu1_thread = threading.Thread(target=self.handle_ryus, args=(ryu_conn, data))
            ryu1_thread.start()
            veh_thread.start()    
            #i = i + 1
            '''
        '''connection, client_address = self.ryu_scket[i].accept()
            self.logger.info('Mininet AP connected: %s:%s', *client_address)
            veh_thread = threading.Thread(target=self.handle_client, args=(connection,))
            
            veh_thread.start()
            '''
            #data =self.Ret_handler(connection)
            #ryu11_thread = threading.Thread(target= self., args=(connection))
            #ryu11_thread.start()
        '''else :
                connection, client_address = self.ryu_scket[i].accept()
                self.logger.info('Mininet AP connected: %s:%s', *client_address)
                veh_thread = threading.Thread(target=self.handle_client, args=(connection,))

                i = i + 1

                veh_thread.start()
            '''

    def stop(self):
        self.sock.close()
        self.logger.info('Socket closed')

    def send_to_all_mininet_aps(self, data):
        with self.lock:
            for sock in self.sockets:
                sock.sendall(data.encode())
                self.logger.debug('Sent data to Mininet AP: %s', data)

    def handle_ryus(self, ryu_conn,):

        sdn1_file = "sdn1.txt"
        sdn2_topo = "sdn2_topo.txt"
        sdn1_topo = "sdn1_topo.txt"
        timeinstance = 0
        while True:
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
            if os.path.exists(sdn1_file) == False :
                print("file doesn't exist")
                time.sleep(8)
            else:
                with open(sdn1_file, 'r') as file:
                    topo_rsu1 = file.read()
                    print("Topo sent from SDN 1 is ", topo_rsu1, "and type is ", type(topo_rsu1), "\n")

                    # open sdn1_file = "sdn1_topo.txt" and append the periodic topology
                with open(sdn1_topo, "a") as topofile:
                    topofile.write("Topo at time \n")
                    topofile.write(str(timeinstance))
                    topofile.write("\n") 
                    Timestamp = str(datetime.now())
                    print(Timestamp)
                    topofile.write(Timestamp)
                    topofile.write("----\n") 
                    topofile.write(topo_rsu1)
                    topofile.write("\n")
                    print("SDN1 TOPO stored.===================================")

                '''with open(combined_topo, "a") as topofile:
                    topofile.write("Topo at time \n")
                    topofile.write(str(timeinstance))
                    topofile.write("\n") 
                    topofile.write(topo_rsu1)
                    topofile.write("\n")'''    
                '''with open(sdn1_topo, "r") as Topo:
                    ctopo = Topo.read()
                    print("The current data on TOPO1 file ", ctopo, "\n" )
                    print("========================================")'''
                timeinstance = timeinstance + 8
                JFdata = json.dumps(topo_rsu1)
                ryu_conn.send(JFdata.encode())

                #time.sleep(8)

        
            #print("HANDLER YURUNNIN****************************************")
            data = ryu_conn.recv(1024).decode()                               #New code starts
            #print("Topo recvd from RSU1 is ", data, "and type is ", type(data), "\n")
            
            #Convert JSON-formatted string to dictionary
            received_dict = ast.literal_eval(data)
            #received_dict = [json.loads(line) for line in open(data, "r") ]
            #time.sleep(8)
            print("Topo recvd from SDN 2 is ", received_dict, "and type is ", type(data), "\n")

            # open sdn2_file = "sdn2_topo.txt" and append the periodic
            with open(sdn2_topo, 'a') as sdn2topo:
                sdn2topo.write("Topo at time \n")
                sdn2topo.write(str(timeinstance))
                sdn2topo.write("\n") 
                Timestamp = str(datetime.now())
                sdn2topo.write("\n")
                sdn2topo.write(received_dict)
                sdn2topo.write("\n")
                print("SDN2 TOPO stored.===================================")
            
            with open(sdn2_topo, "r") as sdn2topo:
                    ctopo = sdn2topo.read()
                    print("The current data on SDN2 topo file ", ctopo, "\n" )
                    print("========================================")
            print("\n--------------------------------\n")
                
    def handle_client(self, rsu_conn,):

        while True:
            '''
            numi = rsu_conn.recv(1024).decode()
            print("Value of NUMI variable:",numi)
            #data = rsu_conn.recv(1024).decode()
            numi =int(numi)
            i = 0
            received_dict = ""
            while i<numi:
                data = rsu_conn.recv(1024).decode()
                received_dict = received_dict + data
                i = i+1
            '''
            #print("Topo recvd from RSU1 is ", data, "and type is ", type(data), "\n")

            # Convert JSON-formatted string to dictionary
            data = rsu_conn.recv(1024).decode()
            received_dict = ast.literal_eval(data)
            print("Topo recvd from RSU1 is ", received_dict, "and type is ", type(data), "\n")
            print("\n--------------------------------\n")

            # store in sdn1.txt
            sdn1_file = "sdn1.txt"
            with open(sdn1_file, 'w+') as file:
                received_dict = json.dumps(received_dict)
                json.dump(received_dict, file)
                print("RSU1 Topo is ", received_dict, "and type is ", type(received_dict))

                print ("\n-----------------------------\n")
            
            

                # Convert dictionary to JSON-formatted string

                
    '''def Ret_handler(self, rsu_conn, ryu_conn):
        data = rsu_conn.recv(1024).decode()
        recieved_data = json.loads(data)

        return recieved_data
    '''
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

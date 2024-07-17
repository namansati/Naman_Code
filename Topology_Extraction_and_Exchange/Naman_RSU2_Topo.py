import socket
import sys, os, json
import time

ryu_host = "10.13.4.78" # ryu ctrler gethostname()
ryu_port = 8882
ryu_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # instantiate
print ('===========111==================')
ryu_socket.connect((ryu_host, ryu_port))  # connect to the serve
print ('============2222=================')

file_path = 'rsu2.txt'

print ("Ryu connect Done")

lofd = 200
while True:
    with open(file_path, 'r') as file:
        topo_rsu2 = json.load(file)
        print("RSU2 Topo is ", topo_rsu2, "and type is ", type(topo_rsu2))

        print ("\n-----------------------------\n")

        # Convert dictionary to JSON-formatted string
        topo_rsu2_str = json.dumps(topo_rsu2)
        '''
        if len(topo_rsu2_str) > lofd:
            i = 0
            numi = len(topo_rsu2_str)/lofd + 1  
            numi = int(numi)
            numi = str(numi)          
            ryu_socket.send(numi.encode())
            #numi = len(topo_rsu2_str)/lofd + 1 
        else:
            numi = "1"
            ryu_socket.send(numi.encode())
        while i<len(topo_rsu2_str):
            x = i
            y = x + lofd - 1
            ryu_socket.send(topo_rsu2_str[x:y].encode())
            i = i+lofd
        '''
        ryu_socket.send(topo_rsu2_str.encode())  # Send the encoded JSON string
        time.sleep(8)




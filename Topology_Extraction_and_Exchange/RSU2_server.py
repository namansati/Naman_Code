import socket
import sys, os, json
import time
import subprocess
import threading 
reqconter1 = 0
ryu_host = "10.13.3.93" # ryu ctrler gethostname()
ryu_port = 8882 
print ('========111=====================')
ryu_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # instantiate

ryu_socket.connect((ryu_host, ryu_port))  # connect to the serve
print ('========2222=====================')

file_path = 'rsu1.txt'

print ("Ryu connect Done")


host = "10.0.0.200"
cport1 = 8901
#cport2 = 8902
#cport3 = 8903
#cport4 = 8904


req1 = "ls"
req2 = "ifconfig"
req3 = "pwd"
req4 = "echo req4"
req5 = "iwconfig"
req6 = "echo req 6"

'''
a = 10
b=20
c=30
d =40
'''

RSU_skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
RSU_skt.bind((host, cport1))
RSU_skt.listen(20)
'''
sock_serv = [None] * 10 

sock_serv[0] = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_serv[0].bind((host, cport1))
sock_serv[0].listen(20)

sock_serv[1] = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_serv[1].bind((host, cport1))
sock_serv[1].listen(20)

sock_serv[2] = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_serv[2].bind((host, cport3))
sock_serv[2].listen(20)

sock_serv[3] = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_serv[3].bind((host, cport4))
sock_serv[3].listen(20)
'''
print("thissssssssssssssssssss executesssssssssssssssssssssssssss")

def client_handler(connect):
    global reqconter1
    while True:
        data = connect.recv(1024).decode()
        start = time.time()
        reqconter1 = reqconter1 + 1
        print ("Data number from sta: ", data, )

        if data == "1":
            #result = str(a + b)
            res = subprocess.run(req1, shell=True, capture_output=True, text=True)
            result = str(res.stdout)
            print(result)
            end = time.time()
            rt = end - start
            print("response Time: ", rt)
            #reqconter1 = reqconter1 + 1
            connect.send(result.encode())
        elif data == "2":
            #result = str(d-a)
            res = subprocess.run(req2, shell=True, capture_output=True, text=True)
            result = str(res.stdout)
            print(result)
            end = time.time()
            rt = end - start
            #reqconter1 = reqconter1 + 1
            print("response Time: ", rt)
            connect.send(result.encode())
        elif data == "3":
            #result = str(b-a)
            res = subprocess.run(req3, shell=True, capture_output=True, text=True)
            result = str(res.stdout)
            print(result)
            end = time.time()
            rt = end - start
            #reqconter1 = reqconter1 + 1
            print("response Time: ", rt)
            connect.send(result.encode())
        elif data == "4":
            #result = str(a+c)
            res = subprocess.run(req4, shell=True, capture_output=True, text=True)
            result = str(res.stdout)
            print(result)
            end = time.time()
            rt = end - start
            print("response Time: ", rt)
            #reqconter1 = reqconter1 + 1
            connect.send(result.encode())
            rt = end - start
            print("response Time: ", rt)                
            connect.send(result.encode())
        elif data == "6":
            #result = str(c-a)
            res = subprocess.run(req6, shell=True, capture_output=True, text=True)
            result = str(res.stdout)
            print(result)
            end = time.time()
            rt = end - start
            print("response Time: ", rt)
            connect.send(result.encode())
            #reqconter1 = reqconter1 + 1
            rt = str(rt)
        else:
            result = "Invalid req"
            connect.send(result.encode())
        
        connect.send(str(reqconter1).encode())    
        print("re2:",reqconter1)
        time.sleep(0.500)
        #connect.send(rt.encode())                                   #Sending_The_Total_ResponseTime_To_vehicle
        #print(reqconter1)                                            #Number of reqs processed by RSU1 i.e. Eq10
        #lb.send(reqconter1)
        

print("Checkin for vehicle conns:............")
i = 0
while True :
    conn1, client1 = RSU_skt.accept()
    veh_thread1 = threading.Thread(target=client_handler, args=(conn1,))
    veh_thread1.start()
    print("Vehicle is Connected.")
    print("Next Car waiting to connect")
    i = i + 1
    #if i == 3 :
     #   break

'''
conn2, client2 = sock_serv[1].accept()
veh_thread2 = threading.Thread(target=client_handler, args=(conn2,))
veh_thread2.start()
print("Vehicle is Connected.")
print("car 3 waiting to connect")
conn3, client3 = sock_serv[2].accept()
veh_thread3 = threading.Thread(target=client_handler, args=(conn3,))
veh_thread3.start()
print("Vehicle is Connected.")

print ("Loggggggggg 1")
'''
while True:
    with open(file_path, 'r') as file:
        #conn, car[i] = sock_serv[i].accept()
        #lbf = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        #lbf.connect((ryu_host, lbport1))

        print("Vehicle is Connected.")
        topo_rsu1 = json.load(file)
        print("RSU1 Topo is ", topo_rsu1, "and type is ", type(topo_rsu1))

        print ("\n-----------------------------\n")

        # Convert dictionary to JSON-formatted string
        topo_rsu1_str = json.dumps(topo_rsu1)
        ryu_socket.send(topo_rsu1_str.encode())  # Send the encoded JSON string
        time.sleep(5)


        #client_thread = threading.Thread (target=client_handler, args= (lbf, conn, reqconter, ))
        #client_thread.start()
        #i =i+1

        



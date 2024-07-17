from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi
from mn_wifi.node import OVSKernelAP
from mn_wifi.wmediumdConnector import interference
from mininet.log import setLogLevel, info
from mininet.term import makeTerm
from mininet.node import RemoteController

import time
from mn_wifi.link import wmediumd, ITSLink
import sys
import xml.etree.ElementTree as ET
import sched
import json
import threading

def print_json_network_info(net, rsu1_file_name, rsu2_file_name):

    net_dict1 = {'RSU1': []}
    net_dict2 = {'RSU2': []}

    for each_sta in net.stations:

        if each_sta.wintfs[0].associatedTo is not None :
            if str(each_sta.wintfs[0].associatedTo.node) == "RSU1":
                net_dict1['RSU1'].append({'Station Name':str(each_sta),'IP Address':each_sta.IP(),'MAC Address':each_sta.MAC()})
            else :
                if str(each_sta.wintfs[0].associatedTo.node) == 'RSU2':
                    net_dict2['RSU2'].append({'Station Name':str(each_sta),'IP Address':each_sta.IP(),'MAC Address':each_sta.MAC()})
                    
    # Assuming net_dict is a dictionary
    #net_dict_str = json.dumps(net_dict)
    #print ("Dump is ", net_dict_str)
    

    # Write the JSON string to the file
    with open(rsu1_file_name, 'w+') as file:
        json.dump(net_dict1, file)

    with open(rsu2_file_name, 'w+') as file:
        json.dump(net_dict2, file)
    
    '''
    with open(rsu1_file_name, 'r') as file:
        topo_rsu1 = json.load(rsu1_file_name)
        print ("Old RSU1 Topo is ", topo_rsu1)
    '''
    print ("RSU1 Topo is \n", net_dict1, "\n \n")
    print ("RSU2 Topo is \n", net_dict2, "\n ----------------------\n")
    #makeTerm(RSU1, cmd=f"bash -c 'python3 Naman_RSU1_topo.py \"{net_dict_str}\" ;'")


def topology():
    
    def save_periodically(sc, net, rsu1_file_name, rsu2_file_name):
        print_json_network_info(net, rsu1_file_name, rsu2_file_name)
        sc.enter(interval_seconds, 1, save_periodically, (sc, net, rsu1_file_name, rsu2_file_name))

    net = Mininet_wifi (allAutoAssociation=True, controller= RemoteController, accessPoint=OVSKernelAP, link=wmediumd, wmediumd_mode=interference) #accessPoint= UserAP) # TCLink

    info ("Creating nodes ---- \n")

    sta1 = net.addStation ("sta1", wlans=1, mac="00:00:00:00:00:01", ip="10.0.0.1/8", max_x=10, max_y=10, min_v=1.0, max_v=1.1, range=4) # position="45,105,0", 192.168.0.3/24
    
    sta2 = net.addStation('sta2', wlans=1, mac='00:00:00:00:00:02', ip='10.0.0.2/8', position='90,60,0', min_v=5.0, max_v=10.0, range=5)
    
    sta3 = net.addStation('sta3', mac='00:00:00:00:00:03', ip='10.0.0.3/8', position='90,60,0', min_v=5.0, max_v=10.0, range=5)
    
    sta4 = net.addStation('sta4', mac='00:00:00:00:00:04', ip='10.0.0.4/8', position='90,60,0', min_v=5.0, max_v=10.0, range=5)
    
    sta5 = net.addStation('sta5', mac='00:00:00:00:00:05', ip='10.0.0.5/8', position='90,60,0', min_v=5.0, max_v=10.0, range=5)
    
    sta6 = net.addStation('sta6', mac='00:00:00:00:00:06', ip='10.0.0.6/8', position='90,60,0', min_v=5.0, max_v=10.0, range=5)
    
    sta7 = net.addStation('sta7', mac='00:00:00:00:00:07', ip='10.0.0.7/8', position='90,60,0', min_v=5.0, max_v=10.0, range=5)
    
    sta8 = net.addStation('sta8', mac='00:00:00:00:00:08', ip='10.0.0.8/8', position='90,60,0', min_v=5.0, max_v=10.0, range=5)
    
    sta9 = net.addStation('sta9', mac='00:00:00:00:00:09', ip='10.0.0.9/8', position='90,60,0', min_v=5.0, max_v=10.0, range=5)
    '''
    sta10 = net.addStation('sta10', mac='00:00:00:00:00:10', ip='10.0.0.10/8', position='90,60,0', min_v=5.0, max_v=10.0, range=5)
    
    sta11 = net.addStation('sta11', mac='00:00:00:00:00:11', ip='10.0.0.11/8', position='90,60,0', min_v=5.0, max_v=10.0, range=5)

    sta12 = net.addStation('sta12', mac='00:00:00:00:00:12', ip='10.0.0.12/8', position='90,60,0', min_v=5.0, max_v=10.0, range=5)
    
    sta13 = net.addStation('sta13', mac='00:00:00:00:00:13', ip='10.0.0.13/8', position='90,60,0', min_v=5.0, max_v=10.0, range=5)
    
    sta14 = net.addStation('sta14', mac='00:00:00:00:00:14', ip='10.0.0.14/8', position='90,60,0', min_v=5.0, max_v=10.0, range=5)
 
    sta15 = net.addStation('sta15', mac='00:00:00:00:00:15', ip='10.0.0.15/8', position='90,60,0', min_v=5.0, max_v=10.0, range=5)
    
    sta16 = net.addStation('sta16', mac='00:00:00:00:00:16', ip='10.0.0.16/8', position='90,60,0', min_v=5.0, max_v=10.0, range=5)
    
    sta17 = net.addStation('sta17', mac='00:00:00:00:00:17', ip='10.0.0.17/8', position='90,60,0', min_v=5.0, max_v=10.0, range=5)
   
    sta18 = net.addStation('sta18', mac='00:00:00:00:00:18', ip='10.0.0.18/8', position='90,60,0', min_v=5.0, max_v=10.0, range=5)
    
    sta19 = net.addStation('sta19', mac='00:00:00:00:00:19', ip='10.0.0.19/8', position='90,60,0', min_v=5.0, max_v=10.0, range=5)
    
    sta20 = net.addStation('sta20', mac='00:00:00:00:00:20', ip='10.0.0.20/8', position='90,60,0', min_v=5.0, max_v=10.0, range=5)
    
    sta21 = net.addStation('sta21', mac='00:00:00:00:00:21', ip='10.0.0.21/8', position='90,60,0', min_v=5.0, max_v=10.0, range=5)

    sta22 = net.addStation('sta22', mac='00:00:00:00:00:22', ip='10.0.0.22/8', position='90,60,0', min_v=5.0, max_v=10.0, range=5)
    
    sta23 = net.addStation('sta23', mac='00:00:00:00:00:23', ip='10.0.0.23/8', position='90,60,0', min_v=5.0, max_v=10.0, range=5)
    
    sta24 = net.addStation('sta24', mac='00:00:00:00:00:24', ip='10.0.0.24/8', position='90,60,0', min_v=5.0, max_v=10.0, range=5)
 
    sta25 = net.addStation('sta25', mac='00:00:00:00:00:25', ip='10.0.0.25/8', position='90,60,0', min_v=5.0, max_v=10.0, range=5)
    
    sta26 = net.addStation('sta26', mac='00:00:00:00:00:26', ip='10.0.0.26/8', position='90,60,0', min_v=5.0, max_v=10.0, range=5)
    10,105
    sta27 = net.addStation('sta27', mac='00:00:00:00:00:27', ip='10.0.0.27/8', position='90,60,0', min_v=5.0, max_v=10.0, range=5)
   
    sta28 = net.addStation('sta28', mac='00:00:00:00:00:28', ip='10.0.0.28/8', position='90,60,0', min_v=5.0, max_v=10.0, range=5)
    
    sta29 = net.addStation('sta29', mac='00:00:00:00:00:29', ip='10.0.0.29/8', position='90,60,0', min_v=5.0, max_v=10.0, range=5)
    
    sta30 = net.addStation('sta30', mac='00:00:00:00:00:30', ip='10.0.0.30/8', position='90,60,0', min_v=5.0, max_v=10.0, range=5)
    '''
    #sta31 = net.addStation('sta31', mac='00:00:00:00:00:31', ip='10.0.0.31/8', position='90,60,0', min_v=5.0, max_v=10.0, range=5)

    #sta32 = net.addStation('sta32', mac='00:00:00:00:00:32', ip='10.0.0.32/8', position='90,60,0', min_v=5.0, max_v=10.0, range=5)
    
    #sta33 = net.addStation('sta33', mac='00:00:00:00:00:33', ip='10.0.0.33/8', position='90,60,0', min_v=5.0, max_v=10.0, range=5)
    
    #sta34 = net.addStation('sta34', mac='00:00:00:00:00:34', ip='10.0.0.34/8', position='90,60,0', min_v=5.0, max_v=10.0, range=5)
 
    #sta35 = net.addStation('sta35', mac='00:00:00:00:00:35', ip='10.0.0.35/8', position='90,60,0', min_v=5.0, max_v=10.0, range=5)
    
    #sta36 = net.addStation('sta36', mac='00:00:00:00:00:36', ip='10.0.0.36/8', position='90,60,0', min_v=5.0, max_v=10.0, range=5)
    
    #sta37 = net.addStation('sta37', mac='00:00:00:00:00:37', ip='10.0.0.37/8', position='90,60,0', min_v=5.0, max_v=10.0, range=5)
   
    #sta38 = net.addStation('sta38', mac='00:00:00:00:00:38', ip='10.0.0.38/8', position='90,60,0', min_v=5.0, max_v=10.0, range=5)
    
    #sta39 = net.addStation('sta39', mac='00:00:00:00:00:39', ip='10.0.0.39/8', position='90,60,0', min_v=5.0, max_v=10.0, range=5)
    
    #sta40 = net.addStation('sta40', mac='00:00:00:00:00:40', ip='10.0.0.40/8', position='90,60,0', min_v=5.0, max_v=10.0, range=5)
    #lbfsta = net.addStation ("lbfsta", wlans=1, mac="00:00:00:00:00:90", ip="10.0.0.300/8", max_x=10, max_y=10, min_v=1.0, max_v=1.1, range=4) # position="45,105,0", 192.168.0.3/24

    RSU1 = net.addAccessPoint ('RSU1', ssid='SSID_ap1', dpid='1', cls=OVSKernelAP,  mac="00:00:00:00:00:70", mode='g', failMode='standalone', range= '30', channel=4, position='180,105,0', datapath='user') # cls=OVSKernelAP, inNamespace=False,
    RSU2 = net.addAccessPoint ('RSU2', ssid='SSID_ap2', dpid='2', color='r', cls=OVSKernelAP, mac="00:00:00:00:00:80", mode='g', failMode='standalone', range= '40', channel=4, position='230,105,0', datapath='user')
                                                                                                                                                            #30                                     #100,105,0
    #backbone1 = net.addSwitch('backbone1', mac='00:00:00:00:00:12', dpid='4', datapath='user', inband=True)

    c1 = net.addController('C1', controller=RemoteController, ip='10.13.3.6', port=6633)
    c2 = net.addController('C2', controller=RemoteController, ip='10.13.1.94', port=6644)

    net.setPropagationModel (model="logDistance", exp=4.3)

    info ("**** Configuring Wifi Nodes \n")
    net.configureWifiNodes()
    #net.AssociationControl('ssf')

    info ("**** Associating and Creating links \n")
    net.plotGraph (min_x= 100, max_x=300, min_y=50, max_y=150)
    net.startMobility (time=0, seed=1, model='logDistance', ac_method='ssf') # can also parameter repetitions=2 - to simulate twice
    net.mobility (sta1, 'start', time=5, position="120,105,0") # 150,105,0
    net.mobility (sta1, 'stop', time=120, position="380,105,0") # 150,105,0
    
    net.mobility (sta2, 'start', time=9, position="120,105,0") # 150,105,0
    net.mobility (sta2, 'stop', time=120, position="380,105,0") # 10,105,0

    net.mobility (sta3, 'start', time=15, position="120,105,0") # 150,105,0
    net.mobility (sta3, 'stop', time=140, position="380,105,0") # 10,105,0

    net.mobility (sta4, 'start', time=5, position="120,105,0") # 150,105,0
    net.mobility (sta4, 'stop', time=120, position="380,105,0") # 120,105,0
    
    net.mobility (sta5, 'start', time=9, position="120,105,0") # 150,105,0
    net.mobility (sta5, 'stop', time=120, position="380,105,0")
    
    net.mobility (sta6, 'start', time=5, position="120,105,0") # 150,105,0
    net.mobility (sta6, 'stop', time=120, position="380,105,0") # 120,105,0
    
    net.mobility (sta7, 'start', time=9, position="120,105,0") # 150,105,0
    net.mobility (sta7, 'stop', time=120, position="380,105,0")

    net.mobility (sta9, 'start', time=5, position="120,105,0") # 150,105,0
    net.mobility (sta9, 'stop', time=120, position="380,105,0") # 120,105,0
    
    net.mobility (sta8, 'start', time=9, position="120,105,0") # 150,105,0
    net.mobility (sta8, 'stop', time=120, position="380,105,0")
    '''
    net.mobility (sta10, 'start', time=5, position="120,105,0") # 150,105,0
    net.mobility (sta10, 'stop', time=120, position="380,105,0") # 120,105,0

    net.mobility (sta11, 'start', time=5, position="120,105,0") # 150,105,0
    net.mobility (sta11, 'stop', time=120, position="380,105,0") # 120,105,0

    net.mobility (sta12, 'start', time=5, position="120,105,0") # 150,105,0
    net.mobility (sta12, 'stop', time=120, position="380,105,0") # 120,105,0

    net.mobility (sta13, 'start', time=5, position="120,105,0") # 150,105,0
    net.mobility (sta13, 'stop', time=120, position="380,105,0") # 120,105,0
    
    net.mobility (sta14, 'start', time=5, position="120,105,0") # 150,105,0
    net.mobility (sta14, 'stop', time=120, position="380,105,0") # 120,105,0

    net.mobility (sta15, 'start', time=5, position="120,105,0") # 150,105,0
    net.mobility (sta15, 'stop', time=120, position="380,105,0") # 120,105,0    
    
    net.mobility (sta16, 'start', time=5, position="120,105,0") # 150,105,0
    net.mobility (sta16, 'stop', time=120, position="380,105,0") # 120,105,0    
    
    net.mobility (sta17, 'start', time=5, position="120,105,0") # 150,105,0
    net.mobility (sta17, 'stop', time=120, position="380,105,0") # 120,105,0    
    
    net.mobility (sta18, 'start', time=5, position="120,105,0") # 150,105,0
    net.mobility (sta18, 'stop', time=120, position="380,105,0") # 120,105,0    

    net.mobility (sta19, 'start', time=5, position="120,105,0") # 150,105,0
    net.mobility (sta19, 'stop', time=120, position="380,105,0") # 120,105,0
    
    net.mobility (sta20, 'start', time=5, position="120,105,0") # 150,105,0
    net.mobility (sta20, 'stop', time=120, position="380,105,0") # 120,105,0
    
    #net.mobility (sta10, 'start', time=5, position="120,105,0") # 150,105,0
    #net.mobility (sta10, 'stop', time=120, position="380,105,0") # 120,105,0

    net.mobility (sta21, 'start', time=5, position="120,105,0") # 150,105,0
    net.mobility (sta21, 'stop', time=120, position="380,105,0") # 120,105,0

    net.mobility (sta22, 'start', time=5, position="120,105,0") # 150,105,0
    net.mobility (sta22, 'stop', time=120, position="380,105,0") # 120,105,0

    net.mobility (sta23, 'start', time=5, position="120,105,0") # 150,105,0
    net.mobility (sta23, 'stop', time=120, position="380,105,0") # 120,105,0
    
    net.mobility (sta24, 'start', time=5, position="120,105,0") # 150,105,0
    net.mobility (sta24, 'stop', time=120, position="380,105,0") # 120,105,0

    net.mobility (sta25, 'start', time=5, position="120,105,0") # 150,105,0
    net.mobility (sta25, 'stop', time=120, position="380,105,0") # 120,105,0    
    
    net.mobility (sta26, 'start', time=5, position="120,105,0") # 150,105,0
    net.mobility (sta26, 'stop', time=120, position="380,105,0") # 120,105,0    
    
    net.mobility (sta27, 'start', time=5, position="120,105,0") # 150,105,0
    net.mobility (sta27, 'stop', time=120, position="380,105,0") # 120,105,0    
    
    net.mobility (sta28, 'start', time=5, position="120,105,0") # 150,105,0
    net.mobility (sta28, 'stop', time=120, position="380,105,0") # 120,105,0    

    net.mobility (sta29, 'start', time=5, position="120,105,0") # 150,105,0
    net.mobility (sta29, 'stop', time=120, position="380,105,0") # 120,105,0
    
    net.mobility (sta30, 'start', time=5, position="120,105,0") # 150,105,0
    net.mobility (sta30, 'stop', time=120, position="380,105,0") # 120,105,0
    
    #net.mobility (lbfsta, 'start', time=15, position="40,105,0") # 150,105,0
    #net.mobility (lbfsta, 'stop', time=1500, position="40,105,0")

    '''
    net.stopMobility (time=220)
    RSU1.cmd('ifconfig RSU1-wlan1 10.0.0.100/8')
    RSU2.cmd('ifconfig RSU2-wlan1 10.0.0.200/8')

    info ("**** Starting network \n")
    net.build ()
    
    RSU1.start ([c1])
    RSU2.start ([c2])

    #makeTerm (RSU1)
    
    makeTerm (RSU1, cmd = "bash -c 'python3 RSU1_server.py;'")     #Naman_RSU1_topo.py
    #time.sleep(1)
    makeTerm (RSU2, cmd = "bash -c 'python3 RSU2_server.py;'")   #Naman_RSU2_Topo.py
    #makeTerm(RSU2)
    time.sleep(3)
    '''
    #executing client code on cars
    makeTerm(sta1, cmd = "bash -c 'python3 Simple_SC_C1.py;'")
    makeTerm(sta2, cmd = "bash -c 'python3 Simple_SC_C1.py;'")
    makeTerm(sta3, cmd = "bash -c 'python3 Simple_SC_C1.py;'")
    makeTerm(sta4, cmd = "bash -c 'python3 Simple_SC_C1.py;'")
    makeTerm(sta5, cmd = "bash -c 'python3 Simple_SC_C1.py;'")    
    makeTerm(sta6, cmd = "bash -c 'python3 Simple_SC_C2.py;'")
    makeTerm(sta7, cmd = "bash -c 'python3 Simple_SC_C2.py;'")
    makeTerm(sta8, cmd = "bash -c 'python3 Simple_SC_C2.py;'")   
    makeTerm(sta9, cmd = "bash -c 'python3 Simple_SC_C2.py;'") 
    #makeTerm(sta6)
    #makeTerm(sta7)
    #makeTerm(sta8)
    makeTerm(sta10, cmd = "bash -c 'python3 Simple_SC_C2.py;'")
    makeTerm(sta11, cmd = "bash -c 'python3 Simple_SC_C1.py;'")
    makeTerm(sta12, cmd = "bash -c 'python3 Simple_SC_C1.py;'")
    makeTerm(sta13, cmd = "bash -c 'python3 Simple_SC_C1.py;'")
    makeTerm(sta14, cmd = "bash -c 'python3 Simple_SC_C1.py;'")
    makeTerm(sta15, cmd = "bash -c 'python3 Simple_SC_C1.py;'")    
    makeTerm(sta16, cmd = "bash -c 'python3 Simple_SC_C2.py;'")
    makeTerm(sta17, cmd = "bash -c 'python3 Simple_SC_C2.py;'")
    makeTerm(sta18, cmd = "bash -c 'python3 Simple_SC_C2.py;'")   
    makeTerm(sta19, cmd = "bash -c 'python3 Simple_SC_C2.py;'") 
    makeTerm(sta20, cmd = "bash -c 'python3 Simple_SC_C2.py;'")    
    #makeTerm(sta7)
    #makeTerm(sta8)
    makeTerm(sta20, cmd = "bash -c 'python3 Simple_SC_C2.py;'")
    makeTerm(sta21, cmd = "bash -c 'python3 Simple_SC_C1.py;'")
    makeTerm(sta22, cmd = "bash -c 'python3 Simple_SC_C1.py;'")
    makeTerm(sta23, cmd = "bash -c 'python3 Simple_SC_C1.py;'")
    makeTerm(sta24, cmd = "bash -c 'python3 Simple_SC_C1.py;'")
    makeTerm(sta25, cmd = "bash -c 'python3 Simple_SC_C1.py;'")    
    makeTerm(sta26, cmd = "bash -c 'python3 Simple_SC_C2.py;'")
    makeTerm(sta27, cmd = "bash -c 'python3 Simple_SC_C2.py;'")
    makeTerm(sta28, cmd = "bash -c 'python3 Simple_SC_C2.py;'")  
    makeTerm(sta29, cmd = "bash -c 'python3 Simple_SC_C2.py;'") 
    makeTerm(sta30, cmd = "bash -c 'python3 Simple_SC_C2.py;'")  
    '''
    r1_range = []
    r2_range = []
    
    def Run_stations(net):
        while True:
            for sta in net.stations:
                if sta.wintfs[0].associatedTo is not None:
                    acp = sta.wintfs[0].associatedTo.node
                    acp = str(acp)
                    if acp == "RSU1" and str(sta) not in r1_range:
                        r1_range.append(str(sta))
                        makeTerm(sta, cmd = "bash -c 'python3 Simple_SC_C1.py;'")

                    if acp == "RSU2" and str(sta) not in r2_range:
                        r2_range.append(str(sta))
                        makeTerm(sta, cmd = "bash -c 'python3 Simple_SC_C2.py;'")
                else:
                    if str(sta) in r1_range:
                        r1_range.remove(str(sta))
                        sta.cmd(exit)
                    if str(sta) in r2_range:
                        r2_range.remove(str(sta))
                        sta.cmd(exit)

    #Run_stations(net)   
    runthread = threading.Thread(target=Run_stations, args=(net,))
    runthread.start()

    s = sched.scheduler(time.time, time.sleep)
    interval_seconds = 6
    rsu1_file_name = "rsu1.txt"
    rsu2_file_name = "rsu2.txt"
    s.enter(interval_seconds, 1, save_periodically, (s, net, rsu1_file_name, rsu2_file_name))
    s.run()
    '''
    r1_range = []
    r2_range = []
    
    def Run_stations(net):
        makeTerm(sta30)
        while True:
            for sta in net.stations:
                if sta.wintfs[0].associatedTo is not None:
                    acp = sta.wintfs[0].associatedTo.node
                    acp = str(acp)
                    if acp == "RSU1" and str(sta) not in r1_range:
                        r1_range.append(str(sta))
                        makeTerm(sta, cmd = "bash -c 'python3 Simple_SC_C1.py;'")
                    if acp == "RSU2" and str(sta) not in r2_range:
                        r2_range.append(str(sta))
                        makeTerm(sta, cmd = "bash -c 'python3 Simple_SC_C2.py;'")
                else:
                    if str(sta) in r1_range:
                        sta.cmd(exit)
                    if str(sta) in r2_range:
                        sta.cmd(exit)
        
    runthread = threading.Thread(target=Run_stations, args=(net))
    runthread().start()
    '''


    info ("**** Running CLI \n")
    CLI(net)

    info ("**** Stopping network \n")
    net.stop ()
    
    
if __name__ == '__main__' :
    setLogLevel ('info')
    topology()


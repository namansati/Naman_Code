import socket

print("Sock_11000011created")
import logging
import random
import time
import subprocess
import re
import numpy as np
from scipy.stats import norm
import random

host = "10.0.0.100"
host2 = "10.0.0.200"
port = 8901
command = "iwconfig sta1-wlan0"         #Calculation_of_Tx_Power_of_vehicle

def Load_Bal():                                                                                     #New_Code
    class LSHFamily:
        def __init__(self, dim, num_functions, p):
            self.dim = dim
            self.num_functions = num_functions
            self.functions = [self._generate_function(p) for _ in range(num_functions)]

        def _generate_function(self, p):
            a = np.random.normal(0, 1, self.dim)
            b = np.random.uniform(0, p)
            return lambda x: int((np.dot(a, x) + b) / p)

    dim = 100  # Dimensionality of the input space
    num_functions = 10  # Number of hash functions in the family
    p = 2  # p-stable parameter
    lsh_family = LSHFamily(dim, num_functions, p)
    num_buckets = 1000

'''def set_transmission_power(interface, power_level):
    """
    Set the transmission power of a network interface.
    
    Args:
    - interface: Name of the network interface (e.g., 'wlan0', 'eth0').
    - power_level: Desired power level in dBm.
    
    Returns:
    - True if the power level was successfully set, False otherwise.
    """
        # Execute the command to set transmission power
    subprocess.run(['iw', 'dev', interface, 'set', 'txpower', 'fixed', str(power_level)], check=True)


res = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
print(res)

result = res.stdout 
tx_power = [line for line in result.split('\n') if "Tx-Power" in line][0]
print("tx_power:",tx_power)
pattern = r"tx_Power= /w+"
sub_match = re.search(pattern,tx_power)
'''
#if sub_match:
#trans_power = sub_match.group()

    #print("Transmission Power:",trans_power)                                        #calculation_of_Tx_Power_of_vehicle

#We_can_alternatively_Set_the_Tx_power_manually_by using_command_iwconfig sta1-wlan0 txpower (value) dBm

print("Sock_1111created")


csocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Sock_522222 created, flag")
flag = 0 
while flag == 0:
    try: 
        csocket.connect((host, port))
        flag = 1
    except:
        print("connection failed.")
#csocket.connect((host, port))


print("connection established.")

while True:
    st = time.time()
    print("in the loop.")
    rand = str(random.randrange(1,7)) #Choosing_a_Service_to_send_to_RSU_from_Vehicle
    csocket.send(rand.encode())
    en = time.time()
    SendReqTime = en - st
    SendReqTime = float(SendReqTime)
    print("Time to send a service request to RSU: ", SendReqTime)                      #Time_to_send_a_service_request_from vehicle
    print("num sent: ", rand)

    command = csocket.recv(1024).decode("utf-8")
    print ("Cmd is ", command)
    #time.sleep(2)
    #tc = csocket.recv(1024).decode("utf-8")                         #Propagation_Time_calculation
    #print("TC is: ",tc)
    #print(type(tc))

    #pt = float(tc) + SendReqTime                              #Eq6_in_Load_Balancing_Paper  
    #print("Total Time:",pt)                                         #Total_offloading_Time_of_Service_Req_from_vehicle

    #total_propagation_time = float(tc) + SendReqTime
    '''
    interface =  "sta1-wlan0"
    power = 20              #setting desired Transmission Power

    command = "sudo ifcofig sta1-wlan0 txpower 20"          #Changing the transmission power

    txp = subprocess.run(command, shell=True, capture_output=True, text=True)
    print("Trans Power changed")
    print(txp)

    #propagation_energy = power * total_propagation_time         #Eq7    
    #print(propagation_energy)
    #Propagation_Energy_Consumption= PropagationTime . Transmission_power
    
    Fm = 200        #Initializing the processing power of RSU (instructions per second)

    #exec_time = float(tc) - SendReqTime #Execution_TIme for RSU

    #exec_energy = Fm * exec_time    #Eq8

    #Total_Energy_Consumption = exec_energy + propagation_energy         #Eq9

    #print(Total_Energy_Consumption)
    '''    
    #Load_Balance_Model
    
    re1 = csocket.recv(1024).decode("utf-8")
    #re1 = int(re1)
    print("No. of Requests processed by RSU:",re1)
    #time.sleep(1)

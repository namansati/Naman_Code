import psutil
import socket
import time

import pyexcel as pe

cpu_mem = pe.get_sheet(file_name = "cpu_mem.xlsx", name_column_by_row = 0)

def get_process_for_port(port):
    # Iterate over all running processes
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            # Get the list of open connections for the process
            connections = proc.connections()
        except psutil.AccessDenied:
            continue

        # Iterate over the connections
        for conn in connections:
            # Check if the connection is TCP and matches the specified port
            if conn.type == socket.SOCK_STREAM and conn.laddr.port == port:
                # Return the process ID and name
                return proc.info

    # If no process is found for the specified port
    return None

# Function to get CPU and memory utilization for a process
def get_cpu_memory_utilization(pid):
    # Get process object
    process = psutil.Process(pid)
    # Get CPU utilization
    cpu_utilization = process.cpu_percent(interval=1)
    # Get memory utilization
    memory_utilization = process.memory_percent()
    return cpu_utilization, memory_utilization

# Specify the TCP port number
port_number = 8901  # Replace with your port number

# Get the process information for the specified port
process_info = get_process_for_port(port_number)

#echo "USER PID  %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND"
#ps aux | grep 50001 

print ("Process Info : ", process_info)

while True:
    if process_info:
        pid = process_info['pid']
        print(f"Process ID: {pid}")
        print(f"Process Name: {process_info['name']}")

        # Get CPU and memory utilization
        cpu_utilization, memory_utilization = get_cpu_memory_utilization(pid)
        print(f"CPU Utilization: {cpu_utilization}%")
        print(f"Memory Utilization: {memory_utilization}%")
        if(cpu_utilization > 0):
            cpu_mem.row += ["40cars", cpu_utilization, memory_utilization]
            cpu_mem.save_as("cpu_mem.xlsx")
    else:
        print(f"No process found running on port {port_number}")

    

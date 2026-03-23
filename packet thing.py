# Basic packet sniffer sim#
#Programmer: Azrael#
#Date: 3/22/2026#

#Get user name. This is optional and can be removed.#
name = input("Please enter your name: ")

#There should be a space between welcome and the name variable to ensure proper formatting of the output. This is also option and can be removed as well.#   
print("Welcome " + name + ", would you like to get started?")

#Verify user input to ensure it's functioning appropriately#
while True:
    choice = input("Press Y to continue or N to terminate the program: ").strip().upper()
    if choice == 'Y':
        print("Great! Let's start with a basic packet sniffer.")
        break
    elif choice == 'N':
        print("Goodbye!")
        exit()
    else:
        print("Invalid input. Please enter Y or N.")

# Import necessary libraries
from scapy.all import sniff, IP, TCP, UDP

# Define a callback function to process packets
def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = "Other"
        if TCP in packet:
            protocol = "TCP"
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
        elif UDP in packet:
            protocol = "UDP"
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
        print(f"Packet: {ip_src}:{src_port if 'src_port' in locals() else ''} -> {ip_dst}:{dst_port if 'dst_port' in locals() else ''} Protocol: {protocol}")

# Sniff packets (note: may require admin privileges on Windows)
print("Sniffing packets... Press Ctrl+C to stop.")
try:
    sniff(prn=packet_callback, count=10)  # Sniff 10 packets
    print("Sniffing complete.")
except PermissionError:
    print("Permission denied. Please run as administrator for packet sniffing.")
except KeyboardInterrupt:
    print("Sniffing stopped.")



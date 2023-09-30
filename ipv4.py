import socket

def is_valid_ipv4(ip):
    try:
        # Use the inet_aton function from the socket library to parse the IP address
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

# Input IPv4 address
ip_address = input("Enter an IPv4 address: ")

if is_valid_ipv4(ip_address):
    print(f"{ip_address} is a valid IPv4 address.")
else:
    print(f"{ip_address} is not a valid IPv4 address.")


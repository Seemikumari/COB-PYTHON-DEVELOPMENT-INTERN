import re


def validate_ipv4_address(ip):
    # Here i have defines regular expression pattern for IPv4 address
    pattern = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'

    # Use the re.match() function to match the pattern against the input
    if re.match(pattern, ip):
        return True
    else:
        return False


# Example usage
ip_address = input("Enter an IPv4 address: ")

if validate_ipv4_address(ip_address):
    print(f"The IP address {ip_address} is valid.")
else:
    print(f"The IP address {ip_address} is not valid.")

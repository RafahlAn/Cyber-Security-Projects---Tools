import socket
print ("*"*50)
print ("Port Scanner By RaFaHl")
print ("*"*50, end="\n\n")

target = input ("Input Target ip ")
print ("-"*50)
print (f"\n Scanning {target} ... \n")
print ("-"*50)
open_ports = []
try :
	for port in range (1, 200):

		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(1.0)

		result = s.connect_ex((target, port))

		if result == 0 :
			try:
				service = socket.getservbyport(port)
			except : 
				service = "unknown"
			open_ports.append((port, service))
		s.close()

except KeyboardInterrupt : 
	print ("\n Scan stopped by the user ")
except socket.error : 
	print ("\n Server not responding")
if open_ports:
	print (f"Found {len(open_ports)} open ports")
	# tuple unpacking
	for port, service  in open_ports:
		print (f"[+] Port {port} open ({service})")
else :
	print ("No open ports found ")

print ("-"*50)
print ("Scan Initialized Successfully")


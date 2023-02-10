print('hi this is kp , i am here to learn')
print('\nsensors with reading can be exported to email')
import socket
ipaddress=""
try:
  ipaddress='10.0.0.5'
except socket.error:
  print("Error in resolving hostname")
bmc.alerts.configure(smtp=ipaddress)
bmc.alerts.sendmail('arjuncr@amiindia.co.in', 'sensors', 'test mail from krithika and sri')
print('mail sent')

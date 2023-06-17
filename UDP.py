import socket 

target_host = "127.0.0.1"
target_port = 80

#Creation de l'objet socket 
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Envoie de la data
client.sendto(b"DATAAAAA",(target_host, target_port))

#Reception de la data
data, addr = client.recvfrom(4096)

print(data.decode())
client.close()
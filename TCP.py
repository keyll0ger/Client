import socket 

target_host = "www.google.com"
target_port = 80

#Création de l'objet socket 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connexion au client
client.connect(target_host, target_port)

#Envoi de la data
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

#Reception de la data
response = client.recv[4096]

print(response.decode())
client.close()
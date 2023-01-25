import socket
import json

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host, port = "127.0.0.1", 2222

client_socket.connect((host, port))


nom_fichier = "infos_livreur.json"

ID = input("Veuillez renseigner votre identifiant : ")    
if ID == nom_fichier["livreurs"]["identifiant"] :
    password = input("Taper votre mot de passe : ")
    print("SUUUUUU !!!!")
    # if password == nom_fichier["livreurs"]["password"] :
else :
    print("Erreur : Identifiant Incorrect")



if __name__ == "__main__" :
    while True :
        message = input(f"{ID} > ")
        client_socket.send(f"{ID} > {message}".encode("utf-8"))
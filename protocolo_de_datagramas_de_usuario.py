import socket
from cifrar import *
import asyncio
import datetime

Direcciones={"El_Ocho":("127.0.0.1",5005),"Profesor":("127.0.0.1",5004)}

def dispara_y_olvida(f):
    def envuelto(*args, **kwargs):
        return asyncio.get_event_loop().run_in_executor(None, f, *args, *kwargs)
    return envuelto

def enviar_al_equipo(MENSAJE,DESTINO):
    MENSAJE = encriptar(MENSAJE).encode()
    # print(DESTINO)
    # print("mensaje: %s" % MENSAJE)
    enchufe = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
    # print(type((UDP_IP, UDP_PORT)))
    # print(MENSAJE)
    enchufe.sendto(MENSAJE, DESTINO)

@dispara_y_olvida
def escucha(ESCUCHAR_DIRECCION):
    if ESCUCHAR_DIRECCION == Direcciones['Profesor']:
        desde='El Ocho'
    else:
        desde='Profesor'
    enchufe = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
    enchufe.bind(ESCUCHAR_DIRECCION)
    while True:
        datos, addr = enchufe.recvfrom(1024) # buffer size is 1024 bytes
        datos=descifrar(datos.decode())
        hora=datetime.datetime.now().strftime("%H:%M:%S")
        print(f"\n[{hora}] Mensaje de {desde}: {datos}")
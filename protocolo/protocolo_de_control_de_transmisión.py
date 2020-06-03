import socket
from cifrar import *
import asyncio
import datetime

Direcciones={"Policia":("127.0.0.1",5006),"Profesor":("127.0.0.1",5003)}

def dispara_y_olvida(f):
    def envuelto(*args, **kwargs):
        return asyncio.get_event_loop().run_in_executor(None, f, *args, *kwargs)
    return envuelto

def enviar_al_equipo(MENSAJE,DESTINO):
    MENSAJE = str.encode(MENSAJE)
    # print(DESTINO)
    # print("mensaje: %s" % MENSAJE)
    enchufe = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_STREAM) # UDP
    # print(type((UDP_IP, UDP_PORT)))
    enchufe.connect(DESTINO)
    enchufe.send(MENSAJE)

@dispara_y_olvida
def envolver_escucha(ESCUCHAR_DIRECCION):
    while 1:
        escucha(ESCUCHAR_DIRECCION)

def escucha(ESCUCHAR_DIRECCION):
    # print("wrking")
    if ESCUCHAR_DIRECCION == Direcciones['Profesor']:
        desde='Policia'
    else:
        desde='Profesor'
    enchufe = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_STREAM) # UDP
    enchufe.bind(ESCUCHAR_DIRECCION)
    enchufe.listen(1)
    conn, addr = enchufe.accept()
    # print(addr)
    while True:
        datos = conn.recv(1024) # buffer size is 1024 bytes
        # datos=descifrar(str(datos))
        # time=
        if not datos: break
        hora=datetime.datetime.now().strftime("%H:%M:%S")
        print(f"\n[{hora}] Mensaje de {desde}: {datos.decode()}")
    enchufe.close()
from protocolo_de_datagramas_de_usuario import *
from os import system,getpid
# from pancartas import El_Ocho

Profesor_Destino=("127.0.0.1",5004)
Escuchar_Direccion=("127.0.0.1",5005)

def main():
    # El_Ocho()
    escucha(Escuchar_Direccion)
    print("En cualquier punto, ingrese /exit para salir")
    while(1):
        mensaje=input('Enviar: ')
        if mensaje == '/exit' or mensaje == '/salida':
            break
        enviar_al_equipo(mensaje,Profesor_Destino)
    system(f'kill {getpid()}')

if __name__ == "__main__":
    main()
from protocolo.protocolo_de_control_de_transmisión import *
from os import system,getpid
# from pancartas import El_Policia

Escuchar_Direccion=("127.0.0.1",5006)
Profesor_Destino=("127.0.0.1",5003)
def main():
    # El_Policia()
    envolver_escucha(Escuchar_Direccion)
    print("En cualquier punto, ingrese /exit para salir")
    while(1):
        mensaje=input('Enviar: ')
        if mensaje == '/exit' or mensaje == '/salida':
            break
        enviar_al_equipo(mensaje,Profesor_Destino)
    system(f'kill {getpid()}')

if __name__ == "__main__":
    main()
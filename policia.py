from protocolo_de_control_de_transmisión import *

Escuchar_Direccion=("127.0.0.1",5006)
Profesor_Destino=("127.0.0.1",5003)
def main():
    envolver_escucha(Escuchar_Direccion)
    while(1):
        mensaje=input('Send: ')
        enviar_al_equipo(mensaje,Profesor_Destino)

if __name__ == "__main__":
    main()
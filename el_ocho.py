from protocolo_de_datagrama_uniforme import *

Profesor_Destino=("127.0.0.1",5004)
Escuchar_Direccion=("127.0.0.1",5005)

def main():
    escucha(Escuchar_Direccion)
    while(1):
        mensaje=input('Send: ')
        enviar_al_equipo(mensaje,Profesor_Destino)

if __name__ == "__main__":
    main()
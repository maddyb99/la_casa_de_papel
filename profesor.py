import protocolo_de_datagramas_de_usuario as UDP
import protocolo_de_control_de_transmisión as TCP
from os import system,getpid
import termios
import sys, tty
# from pancartas import El_Profesor

Destino={"El_Ocho":("127.0.0.1",5005),"Policia":("127.0.0.1",5006),"Yo_UDP":("127.0.0.1",5004),"Yo_TCP":("127.0.0.1",5003)}

def main():
    UDP.escucha(Destino["Yo_UDP"])
    TCP.envolver_escucha(Destino["Yo_TCP"])
    eleccion=0
    # El_Profesor()
    print("En cualquier momento presione\n1. Para hablar con los ocho\n2. Para hablar con la policía\n3. Salir\n") 
    while 1:
        eleccion=input()
        # fd = sys.stdin.fileno()
        # old_settings = termios.tcgetattr(fd)
        try:
            # tty.setraw(fd)
            # eleccion=sys.stdin.read(1)
            eleccion=int(eleccion)
        except:
            print("¡No es una opción válida!")
        # finally:
        #     termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        if eleccion == 1:
            mensaje=input('Enviar a los ocho: ')
            UDP.enviar_al_equipo(mensaje,Destino["El_Ocho"])
        elif eleccion == 2:
            mensaje=input('Enviar a la policia: ')
            TCP.enviar_al_equipo(mensaje,Destino["Policia"])
        elif eleccion==3:
            break
        else:
            print("¡No es una opción válida!")
    system(f'kill {getpid()}')

        
if __name__ == "__main__":
    main()

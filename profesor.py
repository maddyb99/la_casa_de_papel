import protocolo_de_datagrama_uniforme as UDP
import protocolo_de_control_de_transmisión as TCP

Destino={"El_Ocho":("127.0.0.1",5005),"Policia":("127.0.0.1",5006),"Yo_UDP":("127.0.0.1",5004),"Yo_TCP":("127.0.0.1",5003)}

def main():
    UDP.escucha(Destino["Yo_UDP"])
    TCP.envolver_escucha(Destino["Yo_TCP"])
    eleccion=0
    while not eleccion == 3:
        print("En cualquier momento presione\n1. Para hablar con los ocho\n2. Para hablar con la policía\n3. Salir\n") 
        eleccion=int(input())
        if eleccion == 1:
            mensaje=input('Ingresar mensaje: ')
            UDP.enviar_al_equipo(mensaje,Destino["El_Ocho"])
        if eleccion == 2:
            mensaje=input('Ingresar mensaje: ')
            TCP.enviar_al_equipo(mensaje,Destino["Policia"])

        
if __name__ == "__main__":
    main()

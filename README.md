# The Problem: La casa de papel

“The Professor” is planning a heist at Royal Mint of Spain. He recruits a group of eight people (Berlin,
Tokyo, Nairobi, Rio, Moscow, Denver, Helsinki, and Oslo) to carry out the heist. The plan is to capture
the Mint for 11 days, so his team can print the money as they deal with elite police force. The Professor
will head the heist from an external location. To prevent the elite police force to break in the Mint and
give his team time to continue the heist, Professor will negotiate with the police headed by inspector
Raquel Murillo. Now, Professor is in need to establish two kinds of separate networks: A reliable
persistent network for negotiating dialogues with inspector Raquel Murillo and an unreliable but
secured network to communicate with his team at the Royal Mint.

![Image](./image.png)

The Professor recruits a brilliant engineer from India ( **You** – A Double Agent) to help him setup his
communication requirement. Design the working prototype for Professor to fulfil his needs for the heist.

Later, you are asked by elite police force to help them by capturing the secured communications
between The Professor and his Dali team. You capture the secured communication packets and provide
as much of the details about captured secured communication to police.

**I, am being your communicator, need the followings by 2 nd June 2020, in documented form for “the
red boxes”**

1. The working prototype for “Professor” communication requirements.
2. The secured communication packet captures with their meanings/details (as much you can) for
   Raquel/Elite Police Force.

# The Solution: Basics

## The Parties

Professor = Profesor

Police = Policia

The Eight= El Ocho

## The Protocols

Protocolo = Protocol

User Datagram Protocol = Protocolo de datagramas de usuario

Transmission Control Protocol = Protocolo de Control de Transmisión

Cipher = Cifrar

## Usage

run `profesor.py`, `el_ocho.py` and `policia.py` to initiate the three parties involved.

The Professor's Panel will be something like:

```
En cualquier momento presione
1. Para hablar con los ocho
2. Para hablar con la policía
3. Salir

```

which translates to:

```
At any time enter
1. To talk to The Eight
2. To speak to the Police
3. Exit
```

Type your choice and press enter to communicate.
Enter message when prompt appears.
For Eg. `Enviar a la policia` is `Send to the police`

In the Other two chats you will have this:

```
En cualquier punto, ingrese /salida para salir
Enviar:
```

Which Translates to:

```
At any point, enter /exit to exit
Send:
```

In both these terminals, You can start typing to send message to the Professor.

## Other Useful Translations

enviar : send

dispara_y_olvida : fire_and_forget

enviar_al_equipo : send to team

mensaje : message

enchufe : Socket

escucha : Listen

desde : from

pancartas : banners

eleccion : choice

Direcciones : Addresses

destino : destination

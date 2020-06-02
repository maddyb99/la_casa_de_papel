def encriptar(mensaje):
    new_mensaje=''
    for ch in mensaje:
        new_mensaje=new_mensaje+(chr(ord(ch)+2))
    return new_mensaje

def descifrar(mensaje):
    new_mensaje=''
    # type(mensaje)
    for ch in mensaje:
        new_mensaje=new_mensaje+(chr(ord(ch)-2))
        # print(ch)
        # print(new_mensaje)
    # print(new_mensaje)
    return new_mensaje
def mostrar_nombre(nombre):
    """ Esta función devuelve un texto
        que precede al nombre introducido
        por el usuario. """
    
    return "Tu nombre es ", nombre


# Métodos para ver comentarios en tiempo de ejecución: 
help(mostrar_nombre) # Muestra el comentario con información más detallada
print(mostrar_nombre.__doc__) # Muestra el comentario
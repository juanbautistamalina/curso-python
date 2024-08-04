import doctest

def area_triangulo(base, altura):
    """
        Esta función debe devolver el área de un triángulo ...
        
        A continuación se escribe una prueba de documentación: 
        Primero se coloca >>> y luego la función, finalmente se coloca
        el resultado que debe arrojar, es decir, el resultado que se espera.
        
        
        >>> area_triangulo(2,4)
        4.0
        
    """
    
    return (base*altura)/2


""" Si no muestra nada por consola, significa que la función está funcionando correctamente.
    Mientras que si arroja algo por consola, hay algo que no está funcionando como debería"""
doctest.testmod() 



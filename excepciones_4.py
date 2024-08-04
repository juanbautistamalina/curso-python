def evaluar_edad(edad):   
    
    if edad<=0: 
        # Creando mi propia excepción 
        raise ValueError("No se permiten edades nagativas. ")
    
    elif edad<20: 
        return "Eres muy joven"
    
    elif edad<40:
        return "Eres joven"
    
    elif edad<60:
        return "Eres maduro"
    
    elif edad<100:
        return "Cuídate"

evaluar_edad(-3)
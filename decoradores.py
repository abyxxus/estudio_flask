def decorador(func):
    
    def decor(*args):
        print("inicio de funcion: " , func.__name__)
        func(*args)
        print("fin de la funcion: " , func.__name__)
        
    return decor

@decorador
def saludo (nombre):
    print("hola " , nombre)
    
saludo("arlex")
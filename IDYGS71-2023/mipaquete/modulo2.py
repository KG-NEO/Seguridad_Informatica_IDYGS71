def salida():

    pregunta = input("Quieres salir conmigo? ")
    
    if(pregunta == "no"):
        print("Excelente, ven vamos ")
        
    else:
        if pregunta.lower() == "no":
            print("Descuida no pasa nada.")
       
    sal = input("Te la pasaste increible? ").lower()
    
    if(sal == "si"):
        print("Gracias por una noche magica" )
    else:
        print("No me vuelvas a llamar" )
        
def renta():
    
    carro = input("Hola quiere rentar un carro? ").lower()
    
    if(carro == "si"):
        print("Un momento por favor. ")
       
    else:
        print("Nos vemos hasta luego. ")
      
       
    rent = input("Tenemos entre un BMW o MAZDA, cual elige? ").lower()
    
    if(rent == " "):
        print("Buena eleccion ")
        
    else:
        print("Nos vemos hasta luego. ")
        
    gra = input("Entonces el costo seria de $1,200 por una semana, ¿lo acepta? ").lower()
    
     if(gra == "si"):
        print("Excelente nos vemos en una semana disfrute sus vaciones ")
        
    else:
        print("De acuerdo no pasa nada, hasta luego y buenas vacacioenes ")
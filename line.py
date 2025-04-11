def line():
    coeficiente_A = float(input("Ingrese el coeficiente A: "))
    coeficiente_B = float(input("Ingrese el coeficiente B: "))
    coeficiente_x1 = float(input("Ingrese el coeficiente X1: "))
    coeficiente_x2 = float(input("Ingrese el coeficiente X2: "))

    print(f"El coeficiente A de su ecuación de la recta es: {coeficiente_A}")
    print(f"El coeficiente B de su ecuación de la recta es: {coeficiente_B}")
    print(f"El coeficiente X1 de su ecuación de la recta es: {coeficiente_x1}")
    print(f"El coeficiente X2 de su ecuación de la recta es: {coeficiente_x2}")
    print(f"\nPara la siguiente ecuación:")
    print(f"\tY = {coeficiente_A}X + {coeficiente_B}")
    print(f"\nDados los siguientes puntos:")
    Y1=coeficiente_A*coeficiente_x1+coeficiente_B
    print(f"\t{Y1}")
    
    P1= (50.0, 110.99999999999999)
    P2= (-32.9, -79.66999999999999)
    x1= 50.0
    y1= 110.99999999999999
    x2= -32.9
    y2= -79.66999999999999

	print(f"\nDados los siguientes puntos:\n \tP1 ({x1},{y1})\n\tP2 ({x2},{y2})")
    distancia=float(((y2-y1)**2 + (x2-x1)**2)**0.5)
    print(f"\nLa distancia entre ellos es: {distancia}")

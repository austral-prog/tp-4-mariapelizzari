def line():
    coeficiente_A = float(input("Ingrese el coeficiente A: "))
    coeficiente_B = float(input("Ingrese el coeficiente B: "))
    coeficiente_x1 = float(input("Ingrese el coeficiente X1: "))
    coeficiente_x2 = float(input("Ingrese el coeficiente X2: "))
    coeficiente_y1= (coeficiente_A * coeficiente_x1 + coeficiente_B)
    coeficiente_y2= (coeficiente_A * coeficiente_x2 + coeficiente_B)
    print(f"El coeficiente A de su ecuación de la recta es: {coeficiente_A}")
    print(f"El coeficiente B de su ecuación de la recta es: {coeficiente_B}")
    print(f"El coeficiente X1 de su ecuación de la recta es: {coeficiente_x1}")
    print(f"El coeficiente X2 de su ecuación de la recta es: {coeficiente_x2}")
   
    print(f"\nPara la siguiente ecuación:")
    print(f"\tY = {coeficiente_A}X + {coeficiente_B}")
   
    print(f"\nDados los siguientes puntos:")
    p = [coeficiente_x1, coeficiente_y1]
    q = [coeficiente_x2, coeficiente_y2]

    P1_str = f"P1 ({coeficiente_x1}, {coeficiente_y1})"
    P2_str = f"P2 ({coeficiente_x2}, {coeficiente_y2})"
    print(f"\t{P1_str}")
    print(f"\t{P2_str}")
    distancia = float(((coeficiente_y2-coeficiente_y1)**2+ (coeficiente_x2-coeficiente_x1)**2)**0.5)
    print(f"\nLa distancia entre ellos es: {distancia}")
    

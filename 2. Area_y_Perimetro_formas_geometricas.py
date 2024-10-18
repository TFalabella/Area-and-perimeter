#   Calculadora de área y perímetro de varias Formas Geométricas.

import sys
import time

Pi = 3.14

def preguntar_si_o_no ():
    while True:
                    print ("\n--- ¿Quieres realizar otro calculo? ---")
                    print ("1. Si.") #Volver atras
                    print ("2. No.") #Salir
                    
                    opcion_si_no = input ()

                    if opcion_si_no == "1":
                        print ("Volviendo al menu principal...")
                        break
                    
                    elif opcion_si_no == "2":
                        print ("Saliendo...")
                        time.sleep(2)
                        sys.exit ()

                    else:
                        print ("Opción no válida, por favor selecciona 1 o 2.")

# Aca comienza el codigo visto en Terminal.

while True:
    print ("\n--- ¿Que necesitas calcular? ---")
    print ("1. Área.")
    print ("2. Perímetro.")
    print ("3. Salir.")

    opcion = input ("Selecciona una opción (1-3:)")

    if opcion == "3":
        print ("Saliendo...")
        break

    if opcion == "1":
        print ("Ingresando en Calculadora de área...")

        while True:
            print ("\n--- Calcular el área de: ---")
            print ("1. Cuadrado.")
            print ("2. Rectángulo.")
            print ("3. Círculo.")
            print ("4. Triángulo.")
            print ("5. Trapecio.")
            print ("6. Rombo.")
            print ("7. Volver atras.")
            
            opcion_area = input ("\n Selecciona la forma geométrica correspondiente (1-7:)")

            if opcion_area == "7":
                print ("Volviendo al menu principal...")
                break
            
            if opcion_area == "1":
                print ("\nCalculando el área del cuadrado en centímetros.")
                L = float (input ("Introduce el valor de uno de sus lados:"))
                A = L ** 2

                print ("\n El área del cuadrado es de:", A, "cm.")
                
                if not preguntar_si_o_no():
                    break
     

            elif opcion_area == "2":
                print ("\nCalculando el área del rectángulo en centímetros.")
                L = float (input ("Introduce el valor del largo de la forma:"))
                W = float (input ("Introduce el valor del ancho de la forma:"))
                A = L * W

                print ("\n El área del rectángulo es de:", A, "cm.")

                if not preguntar_si_o_no():
                    break
                

            elif opcion_area == "3":
                print ("\nCalculando el área del círculo en centímetros.")
                r = float (input ("Introduce el radio del círculo:"))
                A = Pi * r**2 

                print ("\n El área del círculo es de:", A, "cm.")

                if not preguntar_si_o_no():
                    break


            elif opcion_area == "4":
                print ("\nCalculando el área del triángulo en centímetros.")
                b = float (input ("Introduce el valor de la base del triángulo:"))
                h = float (input ("Introduce el valor de la altura del triángulo:"))
                A = (b * h) / 2

                print ("\n El área del círculo es de:", A, "cm.")

                if not preguntar_si_o_no():
                    break

           

            elif opcion_area == "5":
                print ("\nCalculando el área del trapecio en centímetros.")
                b1 = float (input ("Introduce el valor de la primer base:"))
                b2 = float (input ("Introduce el valor de la segunda base:"))
                h = float (input ("Introduce el valor de la altura:"))
                A = ((b1 + b2) * h) / 2

                print ("\n El área del trapecio es", A, "cm.")

                if not preguntar_si_o_no():
                    break

            
            elif opcion_area == "6":
                print ("\nCalculando el área del rombo en centímetos.")
                D = float (input ("Introduce el valor de la longitud de la diagonal mayor del rombo:"))
                d = float (input ("Introduce el valor de la longitud de la diagonal menor del rombo:"))
                A = (D * d) / 2

                print ("\n El área del rombo es de:", A, "cm.")

                if not preguntar_si_o_no():
                    break


            
            else:
                print ("Opción no válida.")


    elif opcion == "2":
        print ("Ingresando en Calculadora de perímetro...")

        while True:
            print ("\n--- Calcular el perímetro de: ---")
            print ("1. Cuadrado.")
            print ("2. Rectángulo.")
            print ("3. Círculo.")
            print ("4. Triángulo.")
            print ("5. Trapecio.")
            print ("7. Volver atras.")
            
            opcion_perimetro = input ("\n Selecciona la forma geométrica correspondiente (1-7:)")

            if opcion_perimetro == "7":
                print ("Volviendo al menu principal...")
                break
            
            if opcion_perimetro == "1":
                print ("\nCalculando el perímetro del cuadrado en centímetros.")
                L = float (input ("Introduce el valor de uno de sus lados:"))
                P = 4 * L

                print ("\n El perímetro del cuadrado es de:", P, "cm.")

                if not preguntar_si_o_no():
                    break

            
            elif opcion_perimetro == "2":
                print ("\nCalculando el perímetro del rectángulo en centímetros.")
                L = float (input ("Introduce el valor del largo de la forma:"))
                W = float (input ("Introduce el valor del ancho de la forma:"))
                P = 2 * (L + W)

                print ("\n El perímetro del rectángulo es de:", P, "cm.")

                if not preguntar_si_o_no():
                    break

            
            elif opcion_perimetro == "3":
                print ("\nCalculando el perímetro del círculo en centímetros.")
                r = float (input ("Introduce el radio del círculo:"))
                P = 2 * Pi * r

                print ("\n El perímetro del círculo es de:", P, "cm.")

                if not preguntar_si_o_no():
                    break

            
            elif opcion_perimetro == "4":
                print ("\nCalculando el perímetro del triángulo en centímetros.")
                a = float (input ("Introduce la longitud de uno de los lados del triángulo:"))
                b = float (input ("Introduce la longitud de otro lado del triángulo:"))
                c = float (input ("Introduce la longitud del tercer lado del tríangulo:"))
                P = a + b + c

                print ("\n El perímetro del tríangulo es de:", P, "cm.")

                if not preguntar_si_o_no():
                    break


            elif opcion_perimetro == "5":
                print ("\nCalculando el perímetro del trapecio en centímetros.")
                b1 = float (input ("Introduce el valor de la primer base:"))
                b2 = float (input ("Introduce el valor de la segunda base:"))
                L1 = float (input ("Introduce la longitud de uno de los lados no paralelos:"))
                L2 = float (input ("Introduce la longitud del otro lado no paralelo:"))
                P = b1 + b2 + L1 + L2
               
                print ("\n El perímetroa del trapecio es", P, "cm.")

                if not preguntar_si_o_no():
                    break

        
            elif opcion_perimetro == "6":
                print ("\nCalculando el perímetro del rombo en centímetos.")
                L = float (input ("Introduce la longitud de uno de sus lados:"))
                P = 4 * L

                print ("\n El perímetro del rombo es de:", P, "cm.")

                if not preguntar_si_o_no():
                    break

            
            else:
                print ("Opción no valida.")
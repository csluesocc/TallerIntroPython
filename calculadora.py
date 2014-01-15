#para ejecutar el programa abra la terminal y escriba:
# python + el nombre del script no olvide escribir la extencion .py
# ejemplo: python caculadora.py (esto debe escribir para ejecutar el script)
print """
****************************************
*                                      *
* COMUNIDAD DE SOFTWARE LIBRE UES-OCC  *
*                                      *
* Taller de python Basico              *
*                                      *
* Impartido por: Eduardo Valencia      *
*                                      *
**************************************** """
def Menu():
 
    print """
     *****************
     *   Calculadora *
     *****************
Menu
------------
1) Suma
2) Resta
3) Multiplicacion
4) Division
5) Salir"""

def Calculadora():
    """Funcion Para Calcular Operaciones Aritmeticas basicas"""
    Menu()
    opc = int(input("Selecione Opcion\n"))
    while (opc >0 and opc <5):
        x = int(input("Ingrese Numero\n"))
        y = int(input("Ingrese Otro Numero\n"))
        if (opc==1):
            print "La Suma es:", x+y
            opc = int(input("Selecione Opcion\n"))
        elif(opc==2):
            print "La Resta es:",x-y
            opc = int(input("Selecione Opcion\n"))
        elif(opc==3):
            print "La Multiplicacion es:",x*y
            opc = int(input("Selecione Opcion\n"))
        elif(opc==4):
            try:
              print "La Division es:", x/y
              opc = int(input("Selecione Opcion\n"))
            except ZeroDivisionError:
              print "No se Permite la Division Entre 0"
              opc = int(input("Selecione Opcion\n"))

Calculadora()









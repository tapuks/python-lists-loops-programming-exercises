my_sample_list = ['Esmeralda','Kiko','Ruth','Lebron','Pedro','Maria','Lou','Fernando','Cesco','Bart','Annie']

#Your code here:

my_sample_list[1]="Steven"
my_sample_list[-1]="Pepe"
print(my_sample_list)
# Define el valor del primer elemento al del 3er elemento concatenado con el valor del 5to elemento.
my_sample_list[2] = my_sample_list[0] +" "+ my_sample_list[4]
print(my_sample_list)

# Invierte el ciclo (desde el final hasta el principio) de toda la lista e imprime todos los elementos.
# LARGO DE LA LISTA
lastList = len(my_sample_list)-1
# FOR IN EMPEZARA DESDE LA ULTINA POSICION HASTA LA POSICION -1( SI PONEMOS 0 NO ENTRA EN LA POSICION 0)
# Y RESTARA 1 CADA VUELTA
for i in range(lastList,-1,-1):
    print(my_sample_list[i])


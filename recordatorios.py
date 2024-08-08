recordatorios = [['2021-01-01', "11:00", "Levantarse y ejercitar"],
 ['2021-05-01', "15:00", "No trabajar"],
 ['2021-07-15', "13:00", "No hacer nada es feriado"],
 ['2021-09-18', "16:00", "Ramadas"],
 ['2021-12-25', "00:00", "Navidad"]]

#Para agregar un evento nuevo
recordatorios.append(["2021-02-02", "06:00", "Empezar el año"])

#Cambiar el día 15 de julio por el 16 de julio
#print(recordatorios[2])
recordatorios[2] = ['2021-07-16', "13:00", "No hacer nada es feriado"]

#Borrar 01 de mayo
del recordatorios[1]

#Agregar cen de Navidad y Año nuevo
recordatorios.append(["2021-12-25", "22:00", "Cena de Navidad"])
recordatorios.append(["2021-12-31", "22:00", "Cena de año nuevo"])

#ordenar
recordatorios.sort()

# Output
print(recordatorios)

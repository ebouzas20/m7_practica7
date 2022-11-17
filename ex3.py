import csv #importem paquet csv
 
myData = [["eric", "bouzas", "20"], ['435345', '345345345', '13123A']] #Passem la informació que volem que surti per pantalla i al arxiu
 
myFile = open('ex3.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(myData)
#aquesta funció escriu el que hi ha dins de myData al nostre arxiu csv que també ha creat     


with open('ex3.csv') as File:
    reader = csv.reader(File, delimiter=',', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        print(row)
#aquesta funció serveix per llegir el que hi ha dins de l'arxiu csv i també ho imprimeix a la consola
import string
import random

#Generar Password aleatorio, numeros letras y caracteres especiales
def generatePassword():


    newPassword = string.digits + string.punctuation + string.ascii_lowercase + string.ascii_uppercase 
    tamanio = random.randint(4, 16)
    
    return ''.join(random.choice(newPassword) for i in range(tamanio))

print (generatePassword())

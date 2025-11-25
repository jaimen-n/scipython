##caesar's cypher, sistema de cifrado que funciona tomando cada letra de un mensaje y sustituyéndola por la que haya x posiciones en el alfabeto después
text = 'Hello Zaira' ## texto a encriptar
shift = 3 ## número de posiciones a adelantar para encriptar

def caesar(message, offset):## creo una función que toma dos argumentos, un texto sobre el que trabajar y un número de posiciones que adelantar en el alfabeto
    alphabet = 'abcdefghijklmnopqrstuvwxyz' ## alfabeto, si quiero que el programa encripte símbolos y números, debería añadirlos aquí
    encrypted_text = '' ## declaro aquí la variable donde se guardará el resultado para que el scope sea de toda la función
    for char in message.lower():## repetir para cada carácter dentro del mensaje:
        if char == ' ': ## este if es para que si hay espacios dentro del mensaje no los cambie
            encrypted_text += char ##añadir el espacio a la variable de resultado
        else:
            index = alphabet.find(char) ##aquí lo que hace es localizar la posición de la letra dada en el alfabeto
            new_index = (index + offset) % len(alphabet) ##aquí toma la posición y la incrementa x veces en función del offset que hayamos dado a la función, el modulo de la longitud del alfabeto es para evitar que pete cuando introducimos la última letra del alfabeto, ya que si suma algo a ese valor y luego lo intenta sacar del alfabeto, no va a encontrar nada, ya que estará buscando x posiciones por delante del último carácter
            encrypted_text += alphabet[new_index] ## aquí suma al texto resultado la letra que esté x posiciones detrás de la letra original, para eso busca en alphabet la letra en la posición que hemos obtenido justo antes
    print('plain text:', message)## aquí imprime el texto original, el mensaje
    print('encrypted text:', encrypted_text)## aquí imprime el texto resultado

caesar(text, shift)##invoco la función con el mensaje que haya dentro de text, y con el offset que haya dentro de shift
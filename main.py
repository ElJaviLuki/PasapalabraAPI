
import json
import requests


def getRosco(nRosco):
    response = requests.get('https://atreslab.com/modulosblancos/'+str(nRosco), headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'TE': 'Trailers',
    })

    if(response.status_code==200):
        return response.json()

abecedario = [ "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "X", "Y", "Z" ]
def printRosco(rosco):
    for cuestion in enumerate(rosco):
        letra = abecedario[cuestion[0]]
        pregunta = cuestion[1]['pregunta']

        respuestas = cuestion[1]['respuesta'].split(', ')
        for respuesta in respuestas:
            if (respuesta.startswith(letra)):
                print("Empieza por " + letra + ": ", end=" ")
            else:
                print("Contiene la " + letra + ": ", end=" ")

            print(pregunta + "\t" + respuesta)







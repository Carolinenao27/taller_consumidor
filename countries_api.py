import requests

def lista_nombre_paises(url):
    paises = requests.get(url)
    paises = paises.json()



    for pais in paises:
        print (f"Nombre Oficial en Español: {pais['translations']['spa']['official']}")
        print(f"La capital es: {pais['capital'][0]}")
        print(f"Su moneda es: {pais['currencies']}")
        print(f"El codigo  es: {pais['idd']['root']}")


url = 'https://restcountries.com/v3.1/independent?status=true&fields=translations,capital,currencies,idd,root'
lista_nombre_paises(url)
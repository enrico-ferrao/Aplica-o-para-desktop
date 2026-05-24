import requests

#API URL
url = f"https://nominatim.openstreetmap.org/search?q={rua}&format=json"

#calculador de frete
def calcular_frete():
    rua = input("Qual o nome da rua? ").replace(" ","+")
    
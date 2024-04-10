import requests

url = "https://camo.githubusercontent.com/f78f4b2c6b2b1769a018c21df3946feeab7f3860f123a77036f5b60047d0e93d/68747470733a2f2f6b6f6d617265762e636f6d2f67687076632f3f757365726e616d653d6c6f7569732d68746d6c637373266c6162656c3d50726f66696c65253230766965777326636f6c6f723d306537356236267374796c653d666c6174"

for _ in range(100000):
    response = requests.get(url)
    if response.status_code == 200:
        print("Requête réussie")
    else:
        print("Requête échouée avec le code d'état:", response.status_code)

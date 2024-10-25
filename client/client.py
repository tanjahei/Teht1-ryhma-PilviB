import time
import requests
import hashlib

# Palvelimen osoite (tässä tapauksessa oletetaan, että palvelimen nimi on "server")
server_url = "http://server:5000"

# Funktio, joka lataa tiedoston palvelimelta ja tarkistaa checksumin
def download_and_verify_file():
    try:
        # Pyydetään palvelinta luomaan uusi tiedosto
        generate_response = requests.get(f"{server_url}/generate")
        print(generate_response.json())
        
        # Ladataan tiedosto palvelimelta
        file_response = requests.get(f"{server_url}/file")
        file_path = "/clientdata/received_file.txt"
        with open(file_path, 'wb') as f:
            f.write(file_response.content)
        print(f"File downloaded and saved to {file_path}")

        # Haetaan checksum palvelimelta
        checksum_response = requests.get(f"{server_url}/checksum").json()
        server_checksum = checksum_response['checksum']
        
        # Lasketaan checksum vastaanotetulle tiedostolle
        with open(file_path, 'rb') as f:
            content = f.read()
            client_checksum = hashlib.md5(content).hexdigest()

        # Varmistetaan, että checksumit täsmäävät
        if server_checksum == client_checksum:
            print("File received successfully and checksum matches.")
        else:
            print("Checksum mismatch! File transfer may have failed.")

    except Exception as e:
        print(f"Error during file download or verification: {e}")

# Jatkuva silmukka, jossa tiedoston lataus ja tarkistus suoritetaan
if __name__ == "__main__":
    while True:
        download_and_verify_file()
        # Odotetaan 5 sekuntia ennen seuraavaa tiedoston latausta
        time.sleep(5)

"""
import requests
import hashlib

# Palvelimen osoite (tässä tapauksessa oletetaan, että palvelimen nimi on "server")
server_url = "http://server:5000"

# Lataa tiedosto palvelimelta ja tallenna /clientdata-kansioon
response = requests.get(f"{server_url}/file")
file_path = "/clientdata/received_file.txt"
with open(file_path, 'wb') as f:
    f.write(response.content)

# Tarkistetaan checksum
checksum_response = requests.get(f"{server_url}/checksum").json()
checksum = checksum_response['checksum']

# Lasketaan checksum vastaanotetulle tiedostolle
with open(file_path, 'rb') as f:
    content = f.read()
    client_checksum = hashlib.md5(content).hexdigest()

# Varmistetaan, että checksumit täsmäävät
if checksum == client_checksum:
    print("File received successfully and checksum matches.")
else:
    print("Checksum mismatch! File transfer may have failed.")
"""

   ____    U _____ u    _      ____    __  __  U _____ u 
U |  _"\ u \| ___"|/U  /"\  u |  _"\ U|' \/ '|u\| ___"|/ 
 \| |_) |/  |  _|"   \/ _ \/ /| | | |\| |\/| |/ |  _|"   
  |  _ <    | |___   / ___ \ U| |_| |\| |  | |  | |___   
  |_| \_\   |_____| /_/   \_\ |____/ u|_|  |_|  |_____|  
  //   \\_  <<   >>  \\    >>  |||_  <<,-,,-.   <<   >>  
 (__)  (__)(__) (__)(__)  (__)(__)_)  (./  \.) (__) (__) 


# Docker-based File Transfer System

## Ympäristön kuvaus
Tämä ympäristö sisältää kaksi Docker-konttia:
- **server**: Ajaa Flask-pohjaista palvelinta, joka luo 1KB kokoisen satunnaisen tiedoston ja tarjoaa sen asiakasohjelmalle.
- **client**: Yhdistää palvelimeen, lataa tiedoston ja tarkistaa checksumin oikeellisuuden.
- Tiedostojen muodostaminen j

## Asennusohjeet

1. Luo tarvittavat voluumit:
    ```bash
    docker volume create servervol
    docker volume create clientvol
    ```

2. Rakenna konttikuvat:
    ```bash
    docker build -t server-image ./server
    docker build -t client-image ./client
    ```

3. Luo Docker-verkko:
    ```bash
    docker network create app-network
    ```

4. Käynnistä palvelin: (anna suoritusoikeudet: sudo chmod +x run_client.sh sudo chmod +x run_server.sh )
    ```bash
    ./run_server.sh
    ```

5. Käynnistä asiakas:
    ```bash
    ./run_client.sh
    ```

## Tarkistus
- Varmista, että tiedosto on vastaanotettu ja tiedoston koko on 1KB asiakkaan puolella komennolla:
    ```bash
    docker exec -it client ls -lh  /clientdata
    ```
- Tulostaa kontin sisällä tapahtuvia tarkistuksia, 10 viimeisintä.
    ```bash
    docker logs --tail 30 client
    ```
- Tulostaa tiedoston sisällön tarkastelua varten.
    ```bash
    docker exec -it client cat /clientdata/received_file.txt
    ```

- Asiakaskontti tulostaa, jos checksum täsmää. Tiedosto uudelleenkirjoitetaan joka samannimiseksi tiedostoksi.

## Huomioitavaa
- Sovellukset ovat konfiguroitu niin, että ne käynnistyvät automaattisesti kontin käynnistyessä.
- Voluumit ja verkko säilyvät myös konttien uudelleenkäynnistyksen jälkeen.

#!/bin/bash

# Luo verkko (jos sitä ei ole jo olemassa)
docker network create app-network || true

# Käynnistä palvelinkontti 
docker run -d --name server --network app-network -v servervol:/serverdata -p 5000:5000 server-image

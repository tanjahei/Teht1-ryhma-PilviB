#!/bin/bash

# Luo verkko (jos sitä ei ole jo olemassa)
docker network create app-network || true

# Käynnistä asiakaskontti 
docker run -d --name client --network app-network -v clientvol:/clientdata client-image
#
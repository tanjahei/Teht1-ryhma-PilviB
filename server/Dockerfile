# Käytetään virallista Python-pohjakuvaa
FROM python:3.9-slim

# Työhakemiston asetus
WORKDIR /app

# Kopioidaan palvelinsovellus ja vaatimukset
COPY server.py /app

# Varmistetaan, että kaikki vaaditut riippuvuudet ovat asennettuina
RUN pip install --no-cache-dir flask

# Mountataan voluumi
VOLUME /serverdata

# Palvelinsovelluksen suoritus, kun kontti käynnistyy
CMD ["python", "server.py"]

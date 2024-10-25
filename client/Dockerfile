# Käytetään virallista Python-pohjakuvaa
FROM python:3.9-slim

# Työhakemiston asetus
WORKDIR /app

# Kopioidaan asiakassovellus ja vaatimukset
COPY client.py /app

# Asennetaan tarvittavat paketit
RUN pip install --no-cache-dir requests

# Mountataan voluumi
VOLUME /clientdata

# Asiakassovelluksen suoritus, kun kontti käynnistyy
CMD ["python", "client.py"]

# Użyj oficjalnego obrazu z Pythona
FROM python:3.12-slim

# Ustaw katalog roboczy w kontenerze
WORKDIR /app

# Skopiuj pliki z repo do kontenera
COPY . .

# Instaluj zależności
RUN pip install --no-cache-dir -r requirements.txt

# Określ domyślne polecenie do uruchomienia aplikacji
CMD ["python", "app.py"]

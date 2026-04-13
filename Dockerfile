
# que version de Sisteme operativo quiero usar: python 
FROM python:3.12-slim

# directorio como se llama
WORKDIR /app

# copiar archivo requerimientos en el directorio /app 
COPY requirements.txt .

# instala los requerimientos 
RUN pip install --no-cache-dir -r requirements.txt


# copiar todo el directorio actual en /app
COPY . .

# expone un puerto
EXPOSE 8080

# Comando para ejecutar el proyecto
CMD ["fastapi", "run", "main.py", "--host", "0.0.0.0", "--port", "8080"]

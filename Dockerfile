FROM python:3.12.2

# Mise en place de l'environnement de travail
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Création du répertoire de travail
WORKDIR /app

# Installation des dépendances Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copie du code source dans le conteneur Docker
COPY . /app/

# Exécution des migrations Django (si nécessaire)
RUN python manage.py migrate

# Exposer le port sur lequel votre application fonctionne (par défaut, port 8000 pour Django)
EXPOSE 8000

# Commande pour démarrer le serveur Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

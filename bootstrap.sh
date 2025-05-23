#!/bin/bash

echo "🔧 Jobless as a Service™ — Inicialización total"
echo "-----------------------------------------------"


# 1. Instalar dependencias
echo "📦 Instalando dependencias..."
pip install -r requirements.txt
# 2. Crear migraciones
echo "🧱 Creando migraciones..."
python manage.py makemigrations
# 3. Aplicar migraciones
echo "🧱 Aplicando migraciones..."
python manage.py migrate

# 4. Crear superusuario y usuarios de prueba
echo "👤 Creando usuarios administrativos y de prueba..."
python manage.py seed_data

# 5. Ficheros estaticos
echo "📂 Recopilando ficheros estáticos..."
python manage.py collectstatic --noinput

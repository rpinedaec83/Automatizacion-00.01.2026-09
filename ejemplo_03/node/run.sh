#!/bin/bash
cd "$(dirname "$0")"

if [ ! -d "node_modules" ]; then
    echo "Instalando dependencias de Node.js..."
    npm install
fi

echo "=========================================================="
echo " Iniciando Servidor Node.js: Ejemplo 03"
echo " Laboratorio de Agentes - OpenAI & DeepSeek en Vivo"
echo "=========================================================="
echo " Abriendo en: http://localhost:3000"
echo "=========================================================="

node server.js

#!/bin/bash
cd "$(dirname "$0")"

# Buscar o crear entorno virtual
if [ ! -d ".venv" ] && [ ! -d "../../.venv" ]; then
    echo "Creando entorno virtual Python..."
    python3 -m venv .venv
    ./.venv/bin/pip install -r requirements.txt
fi

if [ -f "./.venv/bin/python" ]; then
    PYTHON_BIN="./.venv/bin/python"
elif [ -f "../../.venv/bin/python" ]; then
    PYTHON_BIN="../../.venv/bin/python"
else
    PYTHON_BIN="python3"
fi

echo "=========================================================="
echo " Iniciando Servidor Python: Ejemplo 03"
echo " Laboratorio de Agentes - OpenAI & DeepSeek en Vivo"
echo "=========================================================="
echo " Abriendo en: http://localhost:5001"
echo "=========================================================="

$PYTHON_BIN app.py

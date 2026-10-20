#!/bin/bash
cd "$(dirname "$0")"

# Usar el entorno virtual
if [ -f "../../.venv/bin/python" ]; then
    PYTHON_BIN="../../.venv/bin/python"
elif [ -f "./.venv/bin/python" ]; then
    PYTHON_BIN="./.venv/bin/python"
else
    PYTHON_BIN="python3"
fi

echo "=========================================================="
echo " Iniciando Laboratorio Interactivo: Subindicador 4"
echo " Diseño de Prompts Efectivos, R-C-T-R-F y Few-Shot"
echo "=========================================================="
echo " Abriendo en: http://localhost:5002"
echo "=========================================================="

$PYTHON_BIN app.py

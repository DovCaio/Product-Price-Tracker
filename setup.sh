#!/bin/bash

set -e

echo "📦 Criando ambiente virtual..."
python3 -m venv .venv

echo "🐍 Ativando ambiente virtual..."
source .venv/bin/activate

echo "⬆️ Atualizando pip..."
pip install --upgrade pip

echo "📥 Instalando dependências..."
pip install -r requirements.txt

echo "✅ Setup concluído!"
echo "Use: source .venv/bin/activate"
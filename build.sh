#!/usr/bin/env bash
# Script de build para o Render

# Instalar dependências do Node.js
npm install

# Criar diretório src se não existir
mkdir -p src

# Verificar se o script Python existe e está no lugar correto
if [ ! -f "src/instagram_downloader.py" ]; then
    echo "Copiando instagram_downloader.py para src/"
    cp instagram_downloader.py src/ 2>/dev/null || echo "instagram_downloader.py não encontrado"
fi

# Instalar dependências Python
pip install -r requirements.txt

# Construir o frontend
npm run build

# Verificar o ambiente
node check_env.js 
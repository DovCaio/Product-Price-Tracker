#!/bin/bash

export $(cat .env | xargs) #É necessário criar um . env com AMAZON_PRODUCT_URLS="..." por exemplo

set -e

cd /home/caiojhonatanalvespereira/scripts/verify_prices #Coloque o caminho do repositório

echo "Subindo banco de dados"
docker compose up -d

until docker exec product_postgres pg_isready -U scraper > /dev/null 2>&1; do #Overhead
  echo "Verificando estado do banco de dados"
  sleep 1
done

echo "Banco de dados pronto"

echo "Executando Scrapping..."

source .venv/bin/activate

scrapy crawl amazon >> logs.txt 2>&1

docker compose down
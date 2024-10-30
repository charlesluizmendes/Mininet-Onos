#!/bin/bash

if [ -z "$1" ]; then
  echo "Por favor, especifique a topologia (single, linear, tree)"
  exit 1
fi

TOPOLOGY=$1
shift

# Argumentos adicionais para a topologia
EXTRA_ARGS=""

for arg in "$@"; do
  EXTRA_ARGS="$EXTRA_ARGS $arg"
done

echo "Executando a topologia $TOPOLOGY com parâmetros adicionais: $EXTRA_ARGS"

# Execute o script de gerenciamento do Mininet com o tipo de topologia e parâmetros adicionais
sudo python3 src/services/network.py $TOPOLOGY $EXTRA_ARGS

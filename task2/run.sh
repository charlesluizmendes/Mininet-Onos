#!/bin/bash

if [ -z "$1" ]; then
  echo "Por favor, especifique a topologia (single, linear, tree)"
  exit 1
fi

TOPOLOGY=$1

echo "Executando a topologia $TOPOLOGY"

# Execute o script de gerenciamento do Mininet com o tipo de topologia especificado
sudo python3 src/services/network.py $TOPOLOGY

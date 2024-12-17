#!/usr/bin/python

import sys
import configparser
import os
from mininet.log import setLogLevel, info
from services.topology import SingleSwitchTopology, LinearTopology, TreeTopology
from services.network import MininetNetwork

def get_controller_config():
    config = configparser.ConfigParser()
    config_path = os.path.abspath('config.properties')
    print(f"Tentando carregar o arquivo de configuração de: {config_path}")
    config.read(config_path)

    if 'DEFAULT' in config:
        print("Configurações carregadas:", dict(config['DEFAULT']))
    else:
        return "Erro: A seção 'DEFAULT' não foi encontrada no arquivo config.properties."

    if 'ip' in config['DEFAULT'] and 'port' in config['DEFAULT']:
        controller_ip = config['DEFAULT']['ip']
        controller_port = int(config['DEFAULT']['port'])
        return controller_ip, controller_port
    else:
        return "Erro de configuração: parâmetros 'ip' ou 'port' ausentes."

if __name__ == '__main__':
    setLogLevel('info')

    controller_config = get_controller_config()
    if isinstance(controller_config, str):
        print(controller_config)
        sys.exit(1)

    controller_ip, controller_port = controller_config
    
    topology_type = sys.argv[1] if len(sys.argv) > 1 else "single"

    if topology_type == "single":
        network = MininetNetwork(SingleSwitchTopology, controller_ip, controller_port, num_hosts=13)
    elif topology_type == "linear":
        network = MininetNetwork(LinearTopology, controller_ip, controller_port, num_switches=10, num_hosts=10)
    elif topology_type == "tree":
        network = MininetNetwork(TreeTopology, controller_ip, controller_port, depth=4, fanout=5)
    else:
        raise ValueError("Topologia desconhecida. Escolha entre: single, linear ou tree.")

    network.run()

#!/usr/bin/python

import sys
import configparser
from mininet.log import setLogLevel, info
from services.topology import SingleSwitchTopology, LinearTopology, TreeTopology
from services.network import MininetNetwork

def get_controller_config():
    config = configparser.ConfigParser()
    config.read('config.properties')
    try:
        controller_ip = config['ONOS']['ip']
        controller_port = int(config['ONOS']['port'])
        return controller_ip, controller_port
    except KeyError as e:
        return f"Erro: Parâmetro {e} de configuração do ONOS não encontrado."

def get_network_from_args(controller_ip, controller_port):
    topology_type = sys.argv[1] if len(sys.argv) > 1 else None
    if not topology_type:
        return "Erro: Por favor, especifique a topologia (single, linear, tree)"

    topo_args = {}
    if len(sys.argv) > 2:
        for arg in sys.argv[2:]:
            try:
                key, value = arg.split('=')
                topo_args[key] = int(value)
            except ValueError:
                return "Erro: Argumento inválido. Use o formato key=value."

    if topology_type == "single":
        if 'hosts' not in topo_args:
            return "Erro: O parâmetro 'hosts' é necessário para a topologia 'single'"
        return MininetNetwork(SingleSwitchTopology, controller_ip, controller_port, hosts=topo_args['hosts'])

    elif topology_type == "linear":
        if 'switches' not in topo_args or 'hosts' not in topo_args:
            return "Erro: Os parâmetros 'switches' e 'hosts' são necessários para a topologia 'linear'"
        return MininetNetwork(LinearTopology, controller_ip, controller_port, switches=topo_args['switches'], hosts=topo_args['hosts'])

    elif topology_type == "tree":
        if 'depth' not in topo_args or 'fanout' not in topo_args:
            return "Erro: Os parâmetros 'depth' e 'fanout' são necessários para a topologia 'tree'"
        return MininetNetwork(TreeTopology, controller_ip, controller_port, depth=topo_args['depth'], fanout=topo_args['fanout'])

    else:
        return "Erro: Topologia desconhecida. Escolha entre: single, linear ou tree."

if __name__ == '__main__':
    setLogLevel('info')

    controller_config = get_controller_config()
    if isinstance(controller_config, str):
        print(controller_config)
    else:
        controller_ip, controller_port = controller_config
        result = get_network_from_args(controller_ip, controller_port)
        if isinstance(result, str): 
            print(result)
        else:
            result.run()

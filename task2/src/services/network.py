#!/usr/bin/python

import sys
import configparser
import os
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.log import setLogLevel, info
from topology import SingleSwitchTopology, LinearTopology, TreeTopology

class MininetNetwork:
    def __init__(self, topo_class, controller_ip, controller_port, **topo_args):
        self.topo = topo_class(**topo_args)
        self.controller_ip = controller_ip
        self.controller_port = controller_port

    def create_network(self):
        info("*** Inicializando a rede com controlador remoto ONOS\n")
        onos_controller = RemoteController('c0', ip=self.controller_ip, port=self.controller_port)
        net = Mininet(topo=self.topo, controller=onos_controller)
        return net

    def run(self):
        net = self.create_network()
        info("*** Iniciando a rede\n")
        net.start()
        info("*** Testando Conexão entre Hosts\n")
        net.pingAll()
        info("*** Parando a rede\n")
        net.stop()

def get_controller_config():
    config = configparser.ConfigParser()
    config_path = os.path.abspath('config.properties')
    print(f"Tentando carregar o arquivo de configuração de: {config_path}")
    config.read(config_path)

    # Verifica se a seção DEFAULT existe e imprime configurações carregadas
    if 'DEFAULT' in config:
        print("Configurações carregadas:", dict(config['DEFAULT']))
    else:
        return "Erro: A seção 'DEFAULT' não foi encontrada no arquivo config.properties."

    # Verifica se as chaves ip e port estão presentes
    if 'ip' in config['DEFAULT'] and 'port' in config['DEFAULT']:
        controller_ip = config['DEFAULT']['ip']
        controller_port = int(config['DEFAULT']['port'])
        return controller_ip, controller_port
    else:
        return "Erro de configuração: parâmetros 'ip' ou 'port' ausentes."

if __name__ == '__main__':
    setLogLevel('info')

    # Carregar configuração do controlador
    controller_config = get_controller_config()
    if isinstance(controller_config, str):
        print(controller_config)
        sys.exit(1)  # Sai se houver um erro de configuração

    controller_ip, controller_port = controller_config
    
    # Define a topologia com base nos argumentos da linha de comando
    topology_type = sys.argv[1] if len(sys.argv) > 1 else "single"

    if topology_type == "single":
        network = MininetNetwork(SingleSwitchTopology, controller_ip, controller_port, num_hosts=13)
    elif topology_type == "linear":
        network = MininetNetwork(LinearTopology, controller_ip, controller_port, num_switches=10, num_hosts=10)
    elif topology_type == "tree":
        network = MininetNetwork(TreeTopology, controller_ip, controller_port, depth=3, fanout=2)
    else:
        raise ValueError("Topologia desconhecida. Escolha entre: single, linear ou tree.")

    network.run()

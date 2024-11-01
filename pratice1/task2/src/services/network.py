#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.log import info

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

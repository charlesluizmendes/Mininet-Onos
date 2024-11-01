from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.topo import Topo

class CustomTopology(Topo):
    def __init__(self):
        super().__init__()
        info("*** Criando topologia com 4 switches e 7 hosts distribuídos\n")

        # Adiciona switches
        s1 = self.addSwitch('s1', protocols="OpenFlow13")
        s2 = self.addSwitch('s2', protocols="OpenFlow13")
        s3 = self.addSwitch('s3', protocols="OpenFlow13")
        s4 = self.addSwitch('s4', protocols="OpenFlow13")  # Switch sem hosts

        # Adiciona hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        h6 = self.addHost('h6')
        h7 = self.addHost('h7')

        # Conecta hosts aos switches
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s2)
        self.addLink(h4, s2)
        self.addLink(h5, s4)
        self.addLink(h6, s4)
        self.addLink(h7, s4)

        # Conecta switches entre si
        self.addLink(s1, s2)
        self.addLink(s2, s3)
        self.addLink(s3, s4)

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
        info("*** Abrindo CLI para interação\n")
        CLI(net)
        info("*** Parando a rede\n")
        net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    # Configura e executa a rede usando a topologia e o controlador ONOS
    network = MininetNetwork(CustomTopology, '192.168.64.2', 6653)
    network.run()

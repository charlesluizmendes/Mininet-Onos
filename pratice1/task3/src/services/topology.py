#!/usr/bin/python

from mininet.topo import Topo
from mininet.log import info

class SingleSwitchTopology(Topo):
    def __init__(self, hosts):
        super().__init__()
        info(f"*** Criando topologia única com um switch e {hosts} hosts\n")

        switch = self.addSwitch('s1', protocols="OpenFlow13")

        for i in range(1, hosts + 1):
            host = self.addHost(f'h{i}')
            self.addLink(host, switch)

class LinearTopology(Topo):
    def __init__(self, switches, hosts):
        super().__init__()
        info(f"*** Criando topologia linear com {switches} switch(es) e {hosts} host(s)\n")
        
        previous_switch = None
        switches_list = []
        
        for i in range(1, switches + 1):
            switch = self.addSwitch(f's{i}', protocols="OpenFlow13")
            switches_list.append(switch)
            if previous_switch:
                self.addLink(previous_switch, switch)
            previous_switch = switch
        
        for i in range(1, min(hosts, switches) + 1):
            host = self.addHost(f'h{i}')
            self.addLink(host, switches_list[i - 1])

class TreeTopology(Topo):
    def __init__(self, depth, fanout):
        super().__init__()
        info(f"*** Criando topologia em árvore com depth {depth} e fanout {fanout}\n")
        
        # Inicializa contadores para switches e hosts
        self.switch_count = 1
        self.host_count = 1
        
        # Adiciona o switch raiz
        root_switch = self.addSwitch(f's{self.switch_count}', protocols="OpenFlow13")
        self.switch_count += 1
        
        # Cria a árvore a partir do switch raiz
        self.create_tree(root_switch, depth, fanout)

    def create_tree(self, parent_switch, depth, fanout):
        """Função recursiva para criar a topologia de árvore."""
        if depth == 1:
            # Último nível, conectar hosts ao switch atual
            for _ in range(fanout):
                host = self.addHost(f'h{self.host_count}')
                self.addLink(parent_switch, host)
                self.host_count += 1
        else:
            # Cria switches filhos e conecta-os ao switch atual
            for _ in range(fanout):
                child_switch = self.addSwitch(f's{self.switch_count}', protocols="OpenFlow13")
                self.addLink(parent_switch, child_switch)
                self.switch_count += 1
                
                # Chama recursivamente para o próximo nível
                self.create_tree(child_switch, depth - 1, fanout)

# Comandos para executar 

- Uma topologia única com 10 hosts. Observe que único significa um switch conectado a todos os hosts;
- Uma topologia linear de 5 switches e 5 hosts;
- Uma topologia de árvore com profundidade 3 fanout 2

## Comandos para Mininet:

```
sudo mn --topo single,10 --controller=ref --test pingall
sudo mn --topo linear,5 --controller=ref --test pingall
sudo mn --topo tree,depth=3,fanout=2 --controller=ref --test pingall
```

## Comandos para Onos:

```
sudo mn --topo single,10 --controller remote,ip=192.168.0.48,port=6653 --switch ovs,protocols=OpenFlow13 --test pingall
sudo mn --topo linear,5 --controller remote,ip=192.168.0.48,port=6653 --switch ovs,protocols=OpenFlow13 --test pingall
sudo mn --topo tree,depth=3,fanout=2 --controller remote,ip=192.168.0.48,port=6653 --switch ovs,protocols=OpenFlow13 --test pingall
```
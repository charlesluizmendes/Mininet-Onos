# Comandos para executar 

- Uma topologia única com 10 hosts. Observe que único significa um switch conectado a todos os hosts;
- Uma topologia linear de 5 switches e 5 hosts;
- Uma topologia de árvore com profundidade 3 fanout 2

## Comandos para Mininet:

```
sudo mn --topo single,10 --controller=ref --test pingall
```

```
*** Creating network
*** Adding controller
*** Adding hosts:
h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 
*** Adding switches:
s1 
*** Adding links:
(h1, s1) (h2, s1) (h3, s1) (h4, s1) (h5, s1) (h6, s1) (h7, s1) (h8, s1) (h9, s1) (h10, s1) 
*** Configuring hosts
h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 
*** Starting controller
c0 
*** Starting 1 switches
s1 ...
*** Waiting for switches to connect
s1 
*** Ping: testing ping reachability
h1 -> h2 h3 h4 h5 h6 h7 h8 h9 h10 
h2 -> h1 h3 h4 h5 h6 h7 h8 h9 h10 
h3 -> h1 h2 h4 h5 h6 h7 h8 h9 h10 
h4 -> h1 h2 h3 h5 h6 h7 h8 h9 h10 
h5 -> h1 h2 h3 h4 h6 h7 h8 h9 h10 
h6 -> h1 h2 h3 h4 h5 h7 h8 h9 h10 
h7 -> h1 h2 h3 h4 h5 h6 h8 h9 h10 
h8 -> h1 h2 h3 h4 h5 h6 h7 h9 h10 
h9 -> h1 h2 h3 h4 h5 h6 h7 h8 h10 
h10 -> h1 h2 h3 h4 h5 h6 h7 h8 h9 
*** Results: 0% dropped (90/90 received)
*** Stopping 1 controllers
c0 
*** Stopping 10 links
..........
*** Stopping 1 switches
s1 
*** Stopping 10 hosts
h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 
*** Done
completed in 5.785 seconds
```

```
sudo mn --topo linear,5 --controller=ref --test pingall
```

```
*** Creating network
*** Adding controller
*** Adding hosts:
h1 h2 h3 h4 h5 
*** Adding switches:
s1 s2 s3 s4 s5 
*** Adding links:
(h1, s1) (h2, s2) (h3, s3) (h4, s4) (h5, s5) (s2, s1) (s3, s2) (s4, s3) (s5, s4) 
*** Configuring hosts
h1 h2 h3 h4 h5 
*** Starting controller
c0 
*** Starting 5 switches
s1 s2 s3 s4 s5 ...
*** Waiting for switches to connect
s1 s2 s3 s4 s5 
*** Ping: testing ping reachability
h1 -> h2 h3 h4 h5 
h2 -> h1 h3 h4 h5 
h3 -> h1 h2 h4 h5 
h4 -> h1 h2 h3 h5 
h5 -> h1 h2 h3 h4 
*** Results: 0% dropped (20/20 received)
*** Stopping 1 controllers
c0 
*** Stopping 9 links
.........
*** Stopping 5 switches
s1 s2 s3 s4 s5 
*** Stopping 5 hosts
h1 h2 h3 h4 h5 
*** Done
completed in 5.806 seconds
```

```
sudo mn --topo tree,depth=3,fanout=2 --controller=ref --test pingall
```

```
*** Creating network
*** Adding controller
*** Adding hosts:
h1 h2 h3 h4 h5 h6 h7 h8 
*** Adding switches:
s1 s2 s3 s4 s5 s6 s7 
*** Adding links:
(s1, s2) (s1, s5) (s2, s3) (s2, s4) (s3, h1) (s3, h2) (s4, h3) (s4, h4) (s5, s6) (s5, s7) (s6, h5) (s6, h6) (s7, h7) (s7, h8) 
*** Configuring hosts
h1 h2 h3 h4 h5 h6 h7 h8 
*** Starting controller
c0 
*** Starting 7 switches
s1 s2 s3 s4 s5 s6 s7 ...
*** Waiting for switches to connect
s7 s1 s2 s3 s4 s5 s6 
*** Ping: testing ping reachability
h1 -> h2 h3 h4 h5 h6 h7 h8 
h2 -> h1 h3 h4 h5 h6 h7 h8 
h3 -> h1 h2 h4 h5 h6 h7 h8 
h4 -> h1 h2 h3 h5 h6 h7 h8 
h5 -> h1 h2 h3 h4 h6 h7 h8 
h6 -> h1 h2 h3 h4 h5 h7 h8 
h7 -> h1 h2 h3 h4 h5 h6 h8 
h8 -> h1 h2 h3 h4 h5 h6 h7 
*** Results: 0% dropped (56/56 received)
*** Stopping 1 controllers
c0 
*** Stopping 14 links
..............
*** Stopping 7 switches
s1 s2 s3 s4 s5 s6 s7 
*** Stopping 8 hosts
h1 h2 h3 h4 h5 h6 h7 h8 
*** Done
completed in 6.523 seconds
```

## Comandos para Onos:

```
sudo mn --topo single,10 --controller remote,ip=192.168.0.48,port=6653 --switch ovs,protocols=OpenFlow13 --test pingall
sudo mn --topo linear,5 --controller remote,ip=192.168.0.48,port=6653 --switch ovs,protocols=OpenFlow13 --test pingall
sudo mn --topo tree,depth=3,fanout=2 --controller remote,ip=192.168.0.48,port=6653 --switch ovs,protocols=OpenFlow13 --test pingall
```
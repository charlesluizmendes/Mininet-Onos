
## ovs-vsctl

```
sh> sudo ovs-vsctl list-br
s1
s2
s3
s4
```

### Após executar o comando "onos> app deactivate org.onosproject.fwd":

```
sh> sudo ovs-ofctl -O OpenFlow13 dump-flows s1
 cookie=0x100007a585b6f, duration=28.259s, table=0, n_packets=10, n_bytes=1390, send_flow_rem priority=40000,dl_type=0x8942 actions=CONTROLLER:65535,clear_actions
 cookie=0x100009465555a, duration=28.257s, table=0, n_packets=10, n_bytes=1390, send_flow_rem priority=40000,dl_type=0x88cc actions=CONTROLLER:65535,clear_actions
 cookie=0x10000ea6f4b8e, duration=28.218s, table=0, n_packets=0, n_bytes=0, send_flow_rem priority=40000,arp actions=CONTROLLER:65535,clear_actions
```

```
sh> sudo ovs-ofctl -O OpenFlow13 dump-flows s2
 cookie=0x1000002bbd8d4, duration=51.896s, table=0, n_packets=34, n_bytes=4726, send_flow_rem priority=40000,dl_type=0x88cc actions=CONTROLLER:65535,clear_actions
 cookie=0x10000dc56d70b, duration=51.894s, table=0, n_packets=34, n_bytes=4726, send_flow_rem priority=40000,dl_type=0x8942 actions=CONTROLLER:65535,clear_actions
 cookie=0x10000c70edd85, duration=51.843s, table=0, n_packets=0, n_bytes=0, send_flow_rem priority=40000,arp actions=CONTROLLER:65535,clear_actions
```

```
sh> sudo ovs-ofctl -O OpenFlow13 dump-flows s3
 cookie=0x10000464e5575, duration=71.690s, table=0, n_packets=47, n_bytes=6533, send_flow_rem priority=40000,dl_type=0x8942 actions=CONTROLLER:65535,clear_actions
 cookie=0x10000646f55aa, duration=71.690s, table=0, n_packets=47, n_bytes=6533, send_flow_rem priority=40000,dl_type=0x88cc actions=CONTROLLER:65535,clear_actions
 cookie=0x10000a6288ee9, duration=71.654s, table=0, n_packets=0, n_bytes=0, send_flow_rem priority=40000,arp actions=CONTROLLER:65535,clear_actions
```

```
sh> sudo ovs-ofctl -O OpenFlow13 dump-flows s4
 cookie=0x10000687421fe, duration=95.128s, table=0, n_packets=30, n_bytes=4170, send_flow_rem priority=40000,dl_type=0x8942 actions=CONTROLLER:65535,clear_actions
 cookie=0x10000261e0911, duration=95.121s, table=0, n_packets=30, n_bytes=4170, send_flow_rem priority=40000,dl_type=0x88cc actions=CONTROLLER:65535,clear_actions
 cookie=0x1000011326ce6, duration=95.101s, table=0, n_packets=0, n_bytes=0, send_flow_rem priority=40000,arp actions=CONTROLLER:65535,clear_actions
```

### Após executar o comando "onos> app activate org.onosproject.fwd":

```
sh> sudo ovs-ofctl -O OpenFlow13 dump-flows s1
 cookie=0x100007a585b6f, duration=286.083s, table=0, n_packets=93, n_bytes=12927, send_flow_rem priority=40000,dl_type=0x8942 actions=CONTROLLER:65535,clear_actions
 cookie=0x100009465555a, duration=286.081s, table=0, n_packets=93, n_bytes=12927, send_flow_rem priority=40000,dl_type=0x88cc actions=CONTROLLER:65535,clear_actions
 cookie=0x10000ea6f4b8e, duration=286.042s, table=0, n_packets=3, n_bytes=126, send_flow_rem priority=40000,arp actions=CONTROLLER:65535,clear_actions
 cookie=0x10000021b41dc, duration=9.571s, table=0, n_packets=0, n_bytes=0, send_flow_rem priority=5,ip actions=CONTROLLER:65535,clear_actions
```

``` 
sh> sudo ovs-ofctl -O OpenFlow13 dump-flows s2
 cookie=0x1000002bbd8d4, duration=388.901s, table=0, n_packets=252, n_bytes=35028, send_flow_rem priority=40000,dl_type=0x88cc actions=CONTROLLER:65535,clear_actions
 cookie=0x10000dc56d70b, duration=388.899s, table=0, n_packets=252, n_bytes=35028, send_flow_rem priority=40000,dl_type=0x8942 actions=CONTROLLER:65535,clear_actions
 cookie=0x10000c70edd85, duration=388.848s, table=0, n_packets=0, n_bytes=0, send_flow_rem priority=40000,arp actions=CONTROLLER:65535,clear_actions
 cookie=0x100002341485c, duration=112.368s, table=0, n_packets=0, n_bytes=0, send_flow_rem priority=5,ip actions=CONTROLLER:65535,clear_actions
```

```
sh> sudo ovs-ofctl -O OpenFlow13 dump-flows s3
 cookie=0x10000464e5575, duration=404.162s, table=0, n_packets=261, n_bytes=36279, send_flow_rem priority=40000,dl_type=0x8942 actions=CONTROLLER:65535,clear_actions
 cookie=0x10000646f55aa, duration=404.162s, table=0, n_packets=261, n_bytes=36279, send_flow_rem priority=40000,dl_type=0x88cc actions=CONTROLLER:65535,clear_actions
 cookie=0x10000a6288ee9, duration=404.126s, table=0, n_packets=0, n_bytes=0, send_flow_rem priority=40000,arp actions=CONTROLLER:65535,clear_actions
 cookie=0x10000be641e06, duration=127.654s, table=0, n_packets=0, n_bytes=0, send_flow_rem priority=5,ip actions=CONTROLLER:65535,clear_actions
```
 
```
sh> sudo ovs-ofctl -O OpenFlow13 dump-flows s4
 cookie=0x10000687421fe, duration=417.721s, table=0, n_packets=134, n_bytes=18626, send_flow_rem priority=40000,dl_type=0x8942 actions=CONTROLLER:65535,clear_actions
 cookie=0x10000261e0911, duration=417.714s, table=0, n_packets=134, n_bytes=18626, send_flow_rem priority=40000,dl_type=0x88cc actions=CONTROLLER:65535,clear_actions
 cookie=0x1000011326ce6, duration=417.694s, table=0, n_packets=0, n_bytes=0, send_flow_rem priority=40000,arp actions=CONTROLLER:65535,clear_actions
 cookie=0x10000810531f2, duration=141.199s, table=0, n_packets=0, n_bytes=0, send_flow_rem priority=5,ip actions=CONTROLLER:65535,clear_actions
```

### Após executar o ping "h1 -c4 h2":

Essas regras confirmam que o ONOS configurou corretamente o switch para permitir a comunicação bidirecional entre os hosts conectados às portas s1-eth1 e s1-eth2. Esses fluxos específicos permitem o encaminhamento dos pacotes em ambas as direções, garantindo que o tráfego possa fluir de um host para o outro.

```
sh> sudo ovs-ofctl -O OpenFlow13 dump-flows s1
  cookie=0x100009465555a, duration=39.982s, table=0, n_packets=12, n_bytes=1668, send_flow_rem priority=40000,dl_type=0x88cc actions=CONTROLLER:65535,clear_actions
 cookie=0x10000021b41dc, duration=39.982s, table=0, n_packets=2, n_bytes=196, send_flow_rem priority=5,ip actions=CONTROLLER:65535,clear_actions
 cookie=0x100007a585b6f, duration=39.982s, table=0, n_packets=12, n_bytes=1668, send_flow_rem priority=40000,dl_type=0x8942 actions=CONTROLLER:65535,clear_actions
 cookie=0x10000ea6f4b8e, duration=39.977s, table=0, n_packets=2, n_bytes=84, send_flow_rem priority=40000,arp actions=CONTROLLER:65535,clear_actions
 cookie=0xaa000099b2e63e, duration=4.929s, table=0, n_packets=3, n_bytes=294, send_flow_rem priority=10,in_port="s1-eth1",dl_src=d2:de:fe:5c:62:73,dl_dst=fe:f1:87:ea:18:2d actions=output:"s1-eth2"
 cookie=0xaa00009464dedd, duration=4.928s, table=0, n_packets=3, n_bytes=294, send_flow_rem priority=10,in_port="s1-eth2",dl_src=fe:f1:87:ea:18:2d,dl_dst=d2:de:fe:5c:62:73 actions=output:"s1-eth1"

```
 
### Após executar o ping "h1 -c4 h5":

Essas regras mostram que o ONOS configurou o switch s1 para permitir a comunicação bidirecional entre vários pares de hosts:

O primeiro par está entre as portas s1-eth1 e s1-eth2.
O segundo par está entre as portas s1-eth1 e s1-eth3.

```
sh> sudo ovs-ofctl -O OpenFlow13 dump-flows s1
cookie=0x100007a585b6f, duration=198.555s, table=0, n_packets=63, n_bytes=8757, send_flow_rem priority=40000,dl_type=0x8942 actions=CONTROLLER:65535,clear_actions
 cookie=0x100009465555a, duration=198.547s, table=0, n_packets=63, n_bytes=8757, send_flow_rem priority=40000,dl_type=0x88cc actions=CONTROLLER:65535,clear_actions
 cookie=0x10000ea6f4b8e, duration=198.536s, table=0, n_packets=4, n_bytes=168, send_flow_rem priority=40000,arp actions=CONTROLLER:65535,clear_actions
 cookie=0x10000021b41dc, duration=53.860s, table=0, n_packets=4, n_bytes=392, send_flow_rem priority=5,ip actions=CONTROLLER:65535,clear_actions
 cookie=0xaa0000a7a26d9a, duration=10.845s, table=0, n_packets=3, n_bytes=294, send_flow_rem priority=10,in_port="s1-eth2",dl_src=ce:eb:74:e9:bf:05,dl_dst=82:04:4f:d6:8b:6f actions=output:"s1-eth1"
 cookie=0xaa00009649e3f2, duration=9.858s, table=0, n_packets=3, n_bytes=294, send_flow_rem priority=10,in_port="s1-eth1",dl_src=82:04:4f:d6:8b:6f,dl_dst=ce:eb:74:e9:bf:05 actions=output:"s1-eth2"
 cookie=0xaa0000c4fc9993, duration=5.892s, table=0, n_packets=3, n_bytes=294, send_flow_rem priority=10,in_port="s1-eth1",dl_src=82:04:4f:d6:8b:6f,dl_dst=b2:c2:cf:6b:02:a3 actions=output:"s1-eth3"
 cookie=0xaa0000ad45d091, duration=5.887s, table=0, n_packets=3, n_bytes=294, send_flow_rem priority=10,in_port="s1-eth3",dl_src=b2:c2:cf:6b:02:a3,dl_dst=82:04:4f:d6:8b:6f actions=output:"s1-eth1"
```


## add-host-intent

### h1-h2

```
sh> sudo ovs-ofctl -O OpenFlow13 dump-flows s1
 cookie=0x100009465555a, duration=428.175s, table=0, n_packets=138, n_bytes=19182, send_flow_rem priority=40000,dl_type=0x88cc actions=CONTROLLER:65535,clear_actions
 cookie=0x100007a585b6f, duration=428.175s, table=0, n_packets=138, n_bytes=19182, send_flow_rem priority=40000,dl_type=0x8942 actions=CONTROLLER:65535,clear_actions
 cookie=0x10000ea6f4b8e, duration=428.170s, table=0, n_packets=6, n_bytes=252, send_flow_rem priority=40000,arp actions=CONTROLLER:65535,clear_actions
 cookie=0x2400004263d1a4, duration=24.230s, table=0, n_packets=4, n_bytes=392, send_flow_rem priority=100,in_port="s1-eth2",dl_src=fe:f1:87:ea:18:2d,dl_dst=d2:de:fe:5c:62:73 actions=output:"s1-eth1"
 cookie=0x240000e42994e6, duration=24.230s, table=0, n_packets=4, n_bytes=392, send_flow_rem priority=100,in_port="s1-eth1",dl_src=d2:de:fe:5c:62:73,dl_dst=fe:f1:87:ea:18:2d actions=output:"s1-eth2"
```
 
## h1-h5

```
sh> sudo ovs-ofctl -O OpenFlow13 dump-flows s1
 cookie=0x100009465555a, duration=746.256s, table=0, n_packets=240, n_bytes=33360, send_flow_rem priority=40000,dl_type=0x88cc actions=CONTROLLER:65535,clear_actions
 cookie=0x100007a585b6f, duration=746.256s, table=0, n_packets=240, n_bytes=33360, send_flow_rem priority=40000,dl_type=0x8942 actions=CONTROLLER:65535,clear_actions
 cookie=0x10000ea6f4b8e, duration=746.251s, table=0, n_packets=7, n_bytes=294, send_flow_rem priority=40000,arp actions=CONTROLLER:65535,clear_actions
 cookie=0x2400004263d1a4, duration=342.311s, table=0, n_packets=4, n_bytes=392, send_flow_rem priority=100,in_port="s1-eth2",dl_src=fe:f1:87:ea:18:2d,dl_dst=d2:de:fe:5c:62:73 actions=output:"s1-eth1"
 cookie=0x240000e42994e6, duration=342.311s, table=0, n_packets=4, n_bytes=392, send_flow_rem priority=100,in_port="s1-eth1",dl_src=d2:de:fe:5c:62:73,dl_dst=fe:f1:87:ea:18:2d actions=output:"s1-eth2"
 cookie=0x2400003984d771, duration=14.813s, table=0, n_packets=0, n_bytes=0, send_flow_rem priority=100,in_port="s1-eth3",dl_src=06:39:a0:06:e6:a4,dl_dst=d2:de:fe:5c:62:73 actions=output:"s1-eth1"
 cookie=0x240000d4fdff41, duration=14.813s, table=0, n_packets=0, n_bytes=0, send_flow_rem priority=100,in_port="s1-eth1",dl_src=d2:de:fe:5c:62:73,dl_dst=06:39:a0:06:e6:a4 actions=output:"s1-eth3"
 ```
 

## add-point-intent
 
### h1-h2

```
sh> sudo ovs-ofctl -O OpenFlow13 dump-flows s1
  cookie=0x100009465555a, duration=1157.259s, table=0, n_packets=373, n_bytes=51847, send_flow_rem priority=40000,dl_type=0x88cc actions=CONTROLLER:65535,clear_actions
 cookie=0x100007a585b6f, duration=1157.259s, table=0, n_packets=373, n_bytes=51847, send_flow_rem priority=40000,dl_type=0x8942 actions=CONTROLLER:65535,clear_actions
 cookie=0x10000ea6f4b8e, duration=1157.254s, table=0, n_packets=8, n_bytes=336, send_flow_rem priority=40000,arp actions=CONTROLLER:65535,clear_actions
 cookie=0x24000056c9eee0, duration=10.370s, table=0, n_packets=0, n_bytes=0, send_flow_rem priority=100,in_port="s1-eth1" actions=output:"s1-eth2"
```

### h2-h1

```
sh> sudo ovs-ofctl -O OpenFlow13 dump-flows s1
  cookie=0x100009465555a, duration=1184.257s, table=0, n_packets=382, n_bytes=53098, send_flow_rem priority=40000,dl_type=0x88cc actions=CONTROLLER:65535,clear_actions
 cookie=0x100007a585b6f, duration=1184.257s, table=0, n_packets=382, n_bytes=53098, send_flow_rem priority=40000,dl_type=0x8942 actions=CONTROLLER:65535,clear_actions
 cookie=0x10000ea6f4b8e, duration=1184.252s, table=0, n_packets=8, n_bytes=336, send_flow_rem priority=40000,arp actions=CONTROLLER:65535,clear_actions
 cookie=0x24000056c9eee0, duration=37.368s, table=0, n_packets=0, n_bytes=0, send_flow_rem priority=100,in_port="s1-eth1" actions=output:"s1-eth2"
 cookie=0x24000041c14f20, duration=4.067s, table=0, n_packets=0, n_bytes=0, send_flow_rem priority=100,in_port="s1-eth2" actions=output:"s1-eth1"
```

### h1-h5

``` 
sh> sudo ovs-ofctl -O OpenFlow13 dump-flows s1
 cookie=0x100009465555a, duration=1835.030s, table=0, n_packets=591, n_bytes=82149, send_flow_rem priority=40000,dl_type=0x88cc actions=CONTROLLER:65535,clear_actions
 cookie=0x100007a585b6f, duration=1835.030s, table=0, n_packets=591, n_bytes=82149, send_flow_rem priority=40000,dl_type=0x8942 actions=CONTROLLER:65535,clear_actions
 cookie=0x10000ea6f4b8e, duration=1835.025s, table=0, n_packets=8, n_bytes=336, send_flow_rem priority=40000,arp actions=CONTROLLER:65535,clear_actions
 cookie=0x24000056c9eee0, duration=5.230s, table=0, n_packets=0, n_bytes=0, send_flow_rem priority=100,in_port="s1-eth1" actions=output:"s1-eth3"

sh> sudo ovs-ofctl -O OpenFlow13 dump-flows s2
 cookie=0x1000002bbd8d4, duration=1853.037s, table=0, n_packets=1198, n_bytes=166522, send_flow_rem priority=40000,dl_type=0x88cc actions=CONTROLLER:65535,clear_actions
 cookie=0x10000dc56d70b, duration=1853.037s, table=0, n_packets=1198, n_bytes=166522, send_flow_rem priority=40000,dl_type=0x8942 actions=CONTROLLER:65535,clear_actions
 cookie=0x10000c70edd85, duration=1853.015s, table=0, n_packets=0, n_bytes=0, send_flow_rem priority=40000,arp actions=CONTROLLER:65535,clear_actions
 cookie=0x2400009609fe12, duration=23.178s, table=0, n_packets=0, n_bytes=0, send_flow_rem priority=100,in_port="s2-eth3" actions=output:"s2-eth4"

sh> sudo ovs-ofctl -O OpenFlow13 dump-flows s3
 cookie=0x10000464e5575, duration=1868.957s, table=0, n_packets=1204, n_bytes=167356, send_flow_rem priority=40000,dl_type=0x8942 actions=CONTROLLER:65535,clear_actions
 cookie=0x10000646f55aa, duration=1868.957s, table=0, n_packets=1204, n_bytes=167356, send_flow_rem priority=40000,dl_type=0x88cc actions=CONTROLLER:65535,clear_actions
 cookie=0x10000a6288ee9, duration=1868.955s, table=0, n_packets=0, n_bytes=0, send_flow_rem priority=40000,arp actions=CONTROLLER:65535,clear_actions
 cookie=0x240000125fe92b, duration=39.132s, table=0, n_packets=2, n_bytes=214, send_flow_rem priority=100,in_port="s3-eth1" actions=output:"s3-eth2"

sh> sudo ovs-ofctl -O OpenFlow13 dump-flows s4
 cookie=0x10000687421fe, duration=1878.316s, table=0, n_packets=606, n_bytes=84234, send_flow_rem priority=40000,dl_type=0x8942 actions=CONTROLLER:65535,clear_actions
 cookie=0x10000261e0911, duration=1878.316s, table=0, n_packets=606, n_bytes=84234, send_flow_rem priority=40000,dl_type=0x88cc actions=CONTROLLER:65535,clear_actions
 cookie=0x1000011326ce6, duration=1878.308s, table=0, n_packets=3, n_bytes=126, send_flow_rem priority=40000,arp actions=CONTROLLER:65535,clear_actions
 cookie=0x240000196cfd83, duration=48.482s, table=0, n_packets=3, n_bytes=321, send_flow_rem priority=100,in_port="s4-eth4" actions=output:"s4-eth1"
```

### h5-h1

```
sh> sudo ovs-ofctl -O OpenFlow13 dump-flows s1
 cookie=0x100009465555a, duration=1417.681s, table=0, n_packets=457, n_bytes=63523, send_flow_rem priority=40000,dl_type=0x88cc actions=CONTROLLER:65535,clear_actions
 cookie=0x100007a585b6f, duration=1417.681s, table=0, n_packets=457, n_bytes=63523, send_flow_rem priority=40000,dl_type=0x8942 actions=CONTROLLER:65535,clear_actions
 cookie=0x10000ea6f4b8e, duration=1417.676s, table=0, n_packets=8, n_bytes=336, send_flow_rem priority=40000,arp actions=CONTROLLER:65535,clear_actions
 cookie=0x24000056c9eee0, duration=25.504s, table=0, n_packets=0, n_bytes=0, send_flow_rem priority=100,in_port="s1-eth1" actions=output:"s1-eth3"
 cookie=0x2400003765d2e1, duration=7.351s, table=0, n_packets=0, n_bytes=0, send_flow_rem priority=100,in_port="s1-eth3" actions=output:"s1-eth1"
 
sh> sudo ovs-ofctl -O OpenFlow13 dump-flows s2
 cookie=0x1000002bbd8d4, duration=1432.727s, table=0, n_packets=928, n_bytes=128992, send_flow_rem priority=40000,dl_type=0x88cc actions=CONTROLLER:65535,clear_actions
 cookie=0x10000dc56d70b, duration=1432.727s, table=0, n_packets=928, n_bytes=128992, send_flow_rem priority=40000,dl_type=0x8942 actions=CONTROLLER:65535,clear_actions
 cookie=0x10000c70edd85, duration=1432.705s, table=0, n_packets=0, n_bytes=0, send_flow_rem priority=40000,arp actions=CONTROLLER:65535,clear_actions
 cookie=0x2400009609fe12, duration=40.491s, table=0, n_packets=0, n_bytes=0, send_flow_rem priority=100,in_port="s2-eth3" actions=output:"s2-eth4"
 cookie=0x2400008c26a64c, duration=22.338s, table=0, n_packets=0, n_bytes=0, send_flow_rem priority=100,in_port="s2-eth4" actions=output:"s2-eth3"
 
sh> sudo ovs-ofctl -O OpenFlow13 dump-flows s3
 cookie=0x10000464e5575, duration=1436.992s, table=0, n_packets=926, n_bytes=128714, send_flow_rem priority=40000,dl_type=0x8942 actions=CONTROLLER:65535,clear_actions
 cookie=0x10000646f55aa, duration=1436.992s, table=0, n_packets=926, n_bytes=128714, send_flow_rem priority=40000,dl_type=0x88cc actions=CONTROLLER:65535,clear_actions
 cookie=0x10000a6288ee9, duration=1436.990s, table=0, n_packets=0, n_bytes=0, send_flow_rem priority=40000,arp actions=CONTROLLER:65535,clear_actions
 cookie=0x240000125fe92b, duration=44.790s, table=0, n_packets=0, n_bytes=0, send_flow_rem priority=100,in_port="s3-eth1" actions=output:"s3-eth2"
 cookie=0x2400008fd05f07, duration=26.637s, table=0, n_packets=0, n_bytes=0, send_flow_rem priority=100,in_port="s3-eth2" actions=output:"s3-eth1"
 
sh> sudo ovs-ofctl -O OpenFlow13 dump-flows s4
 cookie=0x10000687421fe, duration=1439.352s, table=0, n_packets=465, n_bytes=64635, send_flow_rem priority=40000,dl_type=0x8942 actions=CONTROLLER:65535,clear_actions
 cookie=0x10000261e0911, duration=1439.352s, table=0, n_packets=465, n_bytes=64635, send_flow_rem priority=40000,dl_type=0x88cc actions=CONTROLLER:65535,clear_actions
 cookie=0x1000011326ce6, duration=1439.344s, table=0, n_packets=3, n_bytes=126, send_flow_rem priority=40000,arp actions=CONTROLLER:65535,clear_actions
 cookie=0x240000196cfd83, duration=47.141s, table=0, n_packets=0, n_bytes=0, send_flow_rem priority=100,in_port="s4-eth4" actions=output:"s4-eth1"
 cookie=0x2400003540fcd7, duration=28.988s, table=0, n_packets=0, n_bytes=0, send_flow_rem priority=100,in_port="s4-eth1" actions=output:"s4-eth4"
```

## ip netns list

```
sh> sudo ip netns list
```
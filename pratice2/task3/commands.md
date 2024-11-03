
## ovs-vsctl

```
sh> sudo ovs-vsctl list-br
s1
s2
s3
s4
```

## Após executar o comando "onos> app deactivate org.onosproject.fwd":

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

As duas últimas regras, com priority=10, foram adicionadas para encaminhar pacotes entre os hosts conectados às portas s1-eth1 e s1-eth2 no switch s1. Aqui está o que elas fazem:

Regra 1 (in_port="s1-eth2", dl_src=22:18:8c:ae:a0:eb, dl_dst=66:92:91:f3:fd:06)

Esta regra captura pacotes que chegam pela porta s1-eth2 com o endereço MAC de origem 22:18:8c:ae:a0:eb (um host) e destino 66:92:91:f3:fd:06 (outro host).
Ação: output:"s1-eth1" — os pacotes são encaminhados para a porta s1-eth1, que conecta ao host de destino.
Regra 2 (in_port="s1-eth1", dl_src=66:92:91:f3:fd:06, dl_dst=22:18:8c:ae:a0:eb)

Esta regra corresponde ao tráfego no caminho oposto: captura pacotes que chegam pela porta s1-eth1 com origem 66:92:91:f3:fd:06 e destino 22:18:8c:ae:a0:eb.
Ação: output:"s1-eth2" — os pacotes são encaminhados para a porta s1-eth2, permitindo a comunicação bidirecional entre os dois hosts.

```
sh> sudo ovs-ofctl -O OpenFlow13 dump-flows s1
 cookie=0x100007a585b6f, duration=113.404s, table=0, n_packets=36, n_bytes=5004, send_flow_rem priority=40000,dl_type=0x8942 actions=CONTROLLER:65535,clear_actions
 cookie=0x100009465555a, duration=113.401s, table=0, n_packets=36, n_bytes=5004, send_flow_rem priority=40000,dl_type=0x88cc actions=CONTROLLER:65535,clear_actions
 cookie=0x10000021b41dc, duration=113.390s, table=0, n_packets=2, n_bytes=196, send_flow_rem priority=5,ip actions=CONTROLLER:65535,clear_actions
 cookie=0x10000ea6f4b8e, duration=113.378s, table=0, n_packets=3, n_bytes=126, send_flow_rem priority=40000,arp actions=CONTROLLER:65535,clear_actions
 cookie=0xaa00002fb8e708, duration=5.925s, table=0, n_packets=3, n_bytes=294, send_flow_rem priority=10,in_port="s1-eth2",dl_src=22:18:8c:ae:a0:eb,dl_dst=66:92:91:f3:fd:06 actions=output:"s1-eth1"
 cookie=0xaa0000cc393c54, duration=4.938s, table=0, n_packets=3, n_bytes=294, send_flow_rem priority=10,in_port="s1-eth1",dl_src=66:92:91:f3:fd:06,dl_dst=22:18:8c:ae:a0:eb actions=output:"s1-eth2"
```
 
### Após executar o ping "h1 -c4 h5":

As duas últimas regras de fluxo com priority=10 foram criadas para permitir a comunicação entre os hosts h1 e h5:

Regra 1 (in_port="s1-eth1", dl_src=66:92:91:f3:fd:06, dl_dst=06:c4:5a:52:49:3b):

Esta regra corresponde aos pacotes recebidos na porta s1-eth1 com o endereço MAC de origem 66:92:91:f3:fd:06 (provavelmente h1) e destino 06:c4:5a:52:49:3b (provavelmente h5).
A ação output:"s1-eth3" indica que esses pacotes devem ser enviados para a porta s1-eth3, que conecta o switch s1 ao próximo switch ou ao host h5.
Regra 2 (in_port="s1-eth3", dl_src=06:c4:5a:52:49:3b, dl_dst=66:92:91:f3:fd:06):

Esta regra trata dos pacotes no caminho inverso, com origem h5 (06:c4:5a:52:49:3b) e destino h1 (66:92:91:f3:fd:06).
A ação output:"s1-eth1" instrui o switch a encaminhar esses pacotes para a porta s1-eth1, permitindo a comunicação bidirecional entre h1 e h5.

```
sh> sudo ovs-ofctl -O OpenFlow13 dump-flows s1
 cookie=0x100007a585b6f, duration=145.682s, table=0, n_packets=47, n_bytes=6533, send_flow_rem priority=40000,dl_type=0x8942 actions=CONTROLLER:65535,clear_actions
 cookie=0x100009465555a, duration=145.679s, table=0, n_packets=47, n_bytes=6533, send_flow_rem priority=40000,dl_type=0x88cc actions=CONTROLLER:65535,clear_actions
 cookie=0x10000021b41dc, duration=145.668s, table=0, n_packets=4, n_bytes=392, send_flow_rem priority=5,ip actions=CONTROLLER:65535,clear_actions
 cookie=0x10000ea6f4b8e, duration=145.656s, table=0, n_packets=4, n_bytes=168, send_flow_rem priority=40000,arp actions=CONTROLLER:65535,clear_actions
 cookie=0xaa00009be16676, duration=5.055s, table=0, n_packets=3, n_bytes=294, send_flow_rem priority=10,in_port="s1-eth1",dl_src=66:92:91:f3:fd:06,dl_dst=06:c4:5a:52:49:3b actions=output:"s1-eth3"
 cookie=0xaa000092360ef3, duration=5.048s, table=0, n_packets=3, n_bytes=294, send_flow_rem priority=10,in_port="s1-eth3",dl_src=06:c4:5a:52:49:3b,dl_dst=66:92:91:f3:fd:06 actions=output:"s1-eth1"
```

## ip netns list

sh> sudo ip netns list
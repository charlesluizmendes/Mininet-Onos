# Criando topologia:

```
sudo python3 custom_topology.py
```



# Sem suporte ao encaminhamento reativo:

```
onos> app deactivate org.onosproject.fwd
```

### Intents Resultados:

```
onos> intents
```

### Flows Resultados:

```
onos> flows
deviceId=of:0000000000000001, flowRuleCount=3
    id=100007a585b6f, state=ADDED, bytes=1946, packets=14, duration=45, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:bddp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=100009465555a, state=ADDED, bytes=1946, packets=14, duration=45, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:lldp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=10000ea6f4b8e, state=ADDED, bytes=0, packets=0, duration=45, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:arp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
deviceId=of:0000000000000002, flowRuleCount=3
    id=1000002bbd8d4, state=ADDED, bytes=3892, packets=28, duration=45, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:lldp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=10000c70edd85, state=ADDED, bytes=0, packets=0, duration=45, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:arp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=10000dc56d70b, state=ADDED, bytes=3892, packets=28, duration=45, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:bddp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
deviceId=of:0000000000000003, flowRuleCount=3
    id=10000464e5575, state=ADDED, bytes=3892, packets=28, duration=45, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:bddp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=10000646f55aa, state=ADDED, bytes=3892, packets=28, duration=45, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:lldp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=10000a6288ee9, state=ADDED, bytes=0, packets=0, duration=45, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:arp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
deviceId=of:0000000000000004, flowRuleCount=3
    id=1000011326ce6, state=ADDED, bytes=0, packets=0, duration=45, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:arp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=10000261e0911, state=ADDED, bytes=1946, packets=14, duration=45, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:lldp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=10000687421fe, state=ADDED, bytes=1946, packets=14, duration=45, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:bddp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
```

### Ping Resultados:

```
mininet> h1 ping -c 4 h2  # Ping entre hosts no mesmo switch
PING 10.0.0.2 (10.0.0.2) 56(84) bytes of data.

--- 10.0.0.2 ping statistics ---
4 packets transmitted, 0 received, 100% packet loss, time 3066ms

mininet> h1 ping -c 4 h5  # Ping entre hosts em switches diferentes
PING 10.0.0.5 (10.0.0.5) 56(84) bytes of data.

--- 10.0.0.5 ping statistics ---
4 packets transmitted, 0 received, 100% packet loss, time 3081ms
```



# Com suporte de encaminhamento Reactevice:

```
onos> app activate org.onosproject.fwd
```

### Intents Resultados:

```
onos> intents
```

### Flows Resultados:

```
onos> flows
deviceId=of:0000000000000001, flowRuleCount=4
    id=100007a585b6f, state=ADDED, bytes=9869, packets=71, duration=220, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:bddp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=100009465555a, state=ADDED, bytes=9869, packets=71, duration=220, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:lldp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=10000ea6f4b8e, state=ADDED, bytes=126, packets=3, duration=220, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:arp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=10000021b41dc, state=ADDED, bytes=0, packets=0, duration=10, liveType=UNKNOWN, priority=5, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:ipv4], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
deviceId=of:0000000000000002, flowRuleCount=4
    id=1000002bbd8d4, state=ADDED, bytes=19738, packets=142, duration=220, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:lldp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=10000c70edd85, state=ADDED, bytes=0, packets=0, duration=220, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:arp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=10000dc56d70b, state=ADDED, bytes=19738, packets=142, duration=220, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:bddp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=100002341485c, state=ADDED, bytes=0, packets=0, duration=10, liveType=UNKNOWN, priority=5, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:ipv4], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
deviceId=of:0000000000000003, flowRuleCount=4
    id=10000464e5575, state=ADDED, bytes=19738, packets=142, duration=220, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:bddp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=10000646f55aa, state=ADDED, bytes=19738, packets=142, duration=220, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:lldp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=10000a6288ee9, state=ADDED, bytes=0, packets=0, duration=220, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:arp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=10000be641e06, state=ADDED, bytes=0, packets=0, duration=10, liveType=UNKNOWN, priority=5, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:ipv4], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
deviceId=of:0000000000000004, flowRuleCount=4
    id=1000011326ce6, state=ADDED, bytes=42, packets=1, duration=220, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:arp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=10000261e0911, state=ADDED, bytes=9869, packets=71, duration=220, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:lldp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=10000687421fe, state=ADDED, bytes=9869, packets=71, duration=220, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:bddp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=10000810531f2, state=ADDED, bytes=0, packets=0, duration=10, liveType=UNKNOWN, priority=5, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:ipv4], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
```

### Ping Resultados:

```
mininet> h1 ping -c 4 h2  # Ping entre hosts no mesmo switch
PING 10.0.0.2 (10.0.0.2) 56(84) bytes of data.
64 bytes from 10.0.0.2: icmp_seq=1 ttl=64 time=5.10 ms
64 bytes from 10.0.0.2: icmp_seq=2 ttl=64 time=0.281 ms
64 bytes from 10.0.0.2: icmp_seq=3 ttl=64 time=0.095 ms
64 bytes from 10.0.0.2: icmp_seq=4 ttl=64 time=0.118 ms

--- 10.0.0.2 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3066ms
rtt min/avg/max/mdev = 0.095/1.397/5.097/2.136 ms

mininet> h1 ping -c 4 h5  # Ping entre hosts em switches diferentes
PING 10.0.0.5 (10.0.0.5) 56(84) bytes of data.
64 bytes from 10.0.0.5: icmp_seq=1 ttl=64 time=9.18 ms
64 bytes from 10.0.0.5: icmp_seq=2 ttl=64 time=1.81 ms
64 bytes from 10.0.0.5: icmp_seq=3 ttl=64 time=0.114 ms
64 bytes from 10.0.0.5: icmp_seq=4 ttl=64 time=0.054 ms

--- 10.0.0.5 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3038ms
rtt min/avg/max/mdev = 0.054/2.788/9.177/3.755 m
```



# Intents definidos pelo usuário sem suporte a encaminhamento do Reactevice:

```
onos> app deactivate org.onosproject.fwd
```

### Listando Hosts:

```
onos> hosts
id=AA:70:F6:40:E0:F0/None, mac=AA:70:F6:40:E0:F0, locations=[of:0000000000000001/1], vlan=None, ip(s)=[10.0.0.1], innerVlan=None, outerTPID=unknown, provider=of:org.onosproject.provider.host, configured=false
id=EE:04:2E:5A:DF:D0/None, mac=EE:04:2E:5A:DF:D0, locations=[of:0000000000000004/1], vlan=None, ip(s)=[10.0.0.5], innerVlan=None, outerTPID=unknown, provider=of:org.onosproject.provider.host, configured=false
id=F2:19:21:AE:91:42/None, mac=F2:19:21:AE:91:42, locations=[of:0000000000000001/2], vlan=None, ip(s)=[10.0.0.2], innerVlan=None, outerTPID=unknown, provider=of:org.onosproject.provider.host, configured=false
```


### Adicionando Host To Host Intent:

```
onos> add-host-intent AA:70:F6:40:E0:F0/None F2:19:21:AE:91:42/None
Host to Host intent submitted:
HostToHostIntent{id=0x200000, key=0x200000, appId=DefaultApplicationId{id=2, name=org.onosproject.cli}, priority=100, resources=[AA:70:F6:40:E0:F0/None, F2:19:21:AE:91:42/None], selector=DefaultTrafficSelector{criteria=[]}, treatment=DefaultTrafficTreatment{immediate=[NOACTION], deferred=[], transition=None, meter=[], cleared=false, StatTrigger=null, metadata=null}, constraints=[LinkTypeConstraint{inclusive=false, types=[OPTICAL]}], resourceGroup=null, one=AA:70:F6:40:E0:F0/None, two=F2:19:21:AE:91:42/None}

onos> add-host-intent AA:70:F6:40:E0:F0/None EE:04:2E:5A:DF:D0/None
Host to Host intent submitted:
HostToHostIntent{id=0x200005, key=0x200005, appId=DefaultApplicationId{id=2, name=org.onosproject.cli}, priority=100, resources=[AA:70:F6:40:E0:F0/None, EE:04:2E:5A:DF:D0/None], selector=DefaultTrafficSelector{criteria=[]}, treatment=DefaultTrafficTreatment{immediate=[NOACTION], deferred=[], transition=None, meter=[], cleared=false, StatTrigger=null, metadata=null}, constraints=[LinkTypeConstraint{inclusive=false, types=[OPTICAL]}], resourceGroup=null, one=AA:70:F6:40:E0:F0/None, two=EE:04:2E:5A:DF:D0/None}              
```

### Flows (Host To Host Intent) Resultados:

```
onos> flows
deviceId=of:0000000000000001, flowRuleCount=7
    id=100007a585b6f, state=ADDED, bytes=20572, packets=148, duration=460, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:bddp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=100009465555a, state=ADDED, bytes=20572, packets=148, duration=460, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:lldp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=10000ea6f4b8e, state=ADDED, bytes=252, packets=6, duration=460, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:arp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=240000a03b90e5, state=ADDED, bytes=0, packets=0, duration=25, liveType=UNKNOWN, priority=100, tableId=0, appId=org.onosproject.net.intent, payLoad=null, selector=[IN_PORT:1, ETH_DST:F2:19:21:AE:91:42, ETH_SRC:AA:70:F6:40:E0:F0], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:2], deferred=[], transition=None, meter=[], cleared=false, StatTrigger=null, metadata=null}
    id=240000d430d4da, state=ADDED, bytes=0, packets=0, duration=11, liveType=UNKNOWN, priority=100, tableId=0, appId=org.onosproject.net.intent, payLoad=null, selector=[IN_PORT:3, ETH_DST:AA:70:F6:40:E0:F0, ETH_SRC:EE:04:2E:5A:DF:D0], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:1], deferred=[], transition=None, meter=[], cleared=false, StatTrigger=null, metadata=null}
    id=240000e7bcb0a9, state=ADDED, bytes=0, packets=0, duration=25, liveType=UNKNOWN, priority=100, tableId=0, appId=org.onosproject.net.intent, payLoad=null, selector=[IN_PORT:2, ETH_DST:AA:70:F6:40:E0:F0, ETH_SRC:F2:19:21:AE:91:42], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:1], deferred=[], transition=None, meter=[], cleared=false, StatTrigger=null, metadata=null}
    id=240000f68d9658, state=ADDED, bytes=0, packets=0, duration=11, liveType=UNKNOWN, priority=100, tableId=0, appId=org.onosproject.net.intent, payLoad=null, selector=[IN_PORT:1, ETH_DST:EE:04:2E:5A:DF:D0, ETH_SRC:AA:70:F6:40:E0:F0], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:3], deferred=[], transition=None, meter=[], cleared=false, StatTrigger=null, metadata=null}
deviceId=of:0000000000000002, flowRuleCount=5
    id=1000002bbd8d4, state=ADDED, bytes=41144, packets=296, duration=460, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:lldp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=10000c70edd85, state=ADDED, bytes=0, packets=0, duration=460, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:arp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=10000dc56d70b, state=ADDED, bytes=41144, packets=296, duration=460, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:bddp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=2400007db77bae, state=ADDED, bytes=0, packets=0, duration=11, liveType=UNKNOWN, priority=100, tableId=0, appId=org.onosproject.net.intent, payLoad=null, selector=[IN_PORT:4, ETH_DST:AA:70:F6:40:E0:F0, ETH_SRC:EE:04:2E:5A:DF:D0], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:3], deferred=[], transition=None, meter=[], cleared=false, StatTrigger=null, metadata=null}
    id=2400009bf78eb7, state=ADDED, bytes=0, packets=0, duration=11, liveType=UNKNOWN, priority=100, tableId=0, appId=org.onosproject.net.intent, payLoad=null, selector=[IN_PORT:3, ETH_DST:EE:04:2E:5A:DF:D0, ETH_SRC:AA:70:F6:40:E0:F0], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:4], deferred=[], transition=None, meter=[], cleared=false, StatTrigger=null, metadata=null}
deviceId=of:0000000000000003, flowRuleCount=5
    id=10000464e5575, state=ADDED, bytes=41144, packets=296, duration=460, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:bddp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=10000646f55aa, state=ADDED, bytes=41144, packets=296, duration=460, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:lldp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=10000a6288ee9, state=ADDED, bytes=0, packets=0, duration=460, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:arp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=240000d2f183d2, state=ADDED, bytes=0, packets=0, duration=11, liveType=UNKNOWN, priority=100, tableId=0, appId=org.onosproject.net.intent, payLoad=null, selector=[IN_PORT:2, ETH_DST:AA:70:F6:40:E0:F0, ETH_SRC:EE:04:2E:5A:DF:D0], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:1], deferred=[], transition=None, meter=[], cleared=false, StatTrigger=null, metadata=null}
    id=240000f5c541a8, state=ADDED, bytes=0, packets=0, duration=11, liveType=UNKNOWN, priority=100, tableId=0, appId=org.onosproject.net.intent, payLoad=null, selector=[IN_PORT:1, ETH_DST:EE:04:2E:5A:DF:D0, ETH_SRC:AA:70:F6:40:E0:F0], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:2], deferred=[], transition=None, meter=[], cleared=false, StatTrigger=null, metadata=null}
deviceId=of:0000000000000004, flowRuleCount=5
    id=1000011326ce6, state=ADDED, bytes=84, packets=2, duration=460, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:arp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=10000261e0911, state=ADDED, bytes=20572, packets=148, duration=460, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:lldp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=10000687421fe, state=ADDED, bytes=20572, packets=148, duration=460, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:bddp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=24000022c2dd9f, state=ADDED, bytes=0, packets=0, duration=11, liveType=UNKNOWN, priority=100, tableId=0, appId=org.onosproject.net.intent, payLoad=null, selector=[IN_PORT:1, ETH_DST:AA:70:F6:40:E0:F0, ETH_SRC:EE:04:2E:5A:DF:D0], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:4], deferred=[], transition=None, meter=[], cleared=false, StatTrigger=null, metadata=null}
    id=2400005c6bae39, state=ADDED, bytes=0, packets=0, duration=11, liveType=UNKNOWN, priority=100, tableId=0, appId=org.onosproject.net.intent, payLoad=null, selector=[IN_PORT:4, ETH_DST:EE:04:2E:5A:DF:D0, ETH_SRC:AA:70:F6:40:E0:F0], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:1], deferred=[], transition=None, meter=[], cleared=false, StatTrigger=null, metadata=null}
```

### Intents (Host To Host Intent) Resultados:

```
onos> intents
Id: 0x200005
State: INSTALLED
Key: 0x200005
Intent type: HostToHostIntent
Application Id: org.onosproject.cli
Leader Id: 192.168.0.48
Resources: [AA:70:F6:40:E0:F0/None, EE:04:2E:5A:DF:D0/None]
Treatment: [NOACTION]
Constraints: [LinkTypeConstraint{inclusive=false, types=[OPTICAL]}]
Source host: AA:70:F6:40:E0:F0/None
Destination host: EE:04:2E:5A:DF:D0/None

Id: 0x200000
State: INSTALLED
Key: 0x200000
Intent type: HostToHostIntent
Application Id: org.onosproject.cli
Leader Id: 192.168.0.48
Resources: [AA:70:F6:40:E0:F0/None, F2:19:21:AE:91:42/None]
Treatment: [NOACTION]
Constraints: [LinkTypeConstraint{inclusive=false, types=[OPTICAL]}]
Source host: AA:70:F6:40:E0:F0/None
Destination host: F2:19:21:AE:91:42/None
```

### Ping (Host To Host Intent) Resultados:

```
mininet> h1 ping -c 4 h2  # Ping entre hosts no mesmo switch
4 packets transmitted, 4 received, 0% packet loss, time 3089ms
rtt min/avg/max/mdev = 0.036/1.499/5.547/2.340 ms
mininet> h1 ping -c 4 h2
PING 10.0.0.2 (10.0.0.2) 56(84) bytes of data.
64 bytes from 10.0.0.2: icmp_seq=1 ttl=64 time=0.205 ms
64 bytes from 10.0.0.2: icmp_seq=2 ttl=64 time=0.039 ms
64 bytes from 10.0.0.2: icmp_seq=3 ttl=64 time=0.036 ms
64 bytes from 10.0.0.2: icmp_seq=4 ttl=64 time=0.033 ms

--- 10.0.0.2 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3075ms
rtt min/avg/max/mdev = 0.033/0.078/0.205/0.073 ms

mininet> h1 ping -c 4 h5  # Ping entre hosts em switches diferentes
PING 10.0.0.5 (10.0.0.5) 56(84) bytes of data.
64 bytes from 10.0.0.5: icmp_seq=1 ttl=64 time=0.319 ms
64 bytes from 10.0.0.5: icmp_seq=2 ttl=64 time=0.052 ms
64 bytes from 10.0.0.5: icmp_seq=3 ttl=64 time=0.048 ms
64 bytes from 10.0.0.5: icmp_seq=4 ttl=64 time=0.042 ms

--- 10.0.0.5 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3056ms
rtt min/avg/max/mdev = 0.042/0.115/0.319/0.117 ms
```



# Adicionando Point To Point Intent [h1 para h2]:

```
onos> add-point-intent of:0000000000000001/1 of:0000000000000001/2
Point to point intent submitted:
PointToPointIntent{id=0x300031, key=0x300031, appId=DefaultApplicationId{id=2, name=org.onosproject.cli}, priority=100, resources=[], selector=DefaultTrafficSelector{criteria=[]}, treatment=DefaultTrafficTreatment{immediate=[NOACTION], deferred=[], transition=None, meter=[], cleared=false, StatTrigger=null, metadata=null}, ingress=FilteredConnectPoint{connectPoint=of:0000000000000001/1, trafficSelector=DefaultTrafficSelector{criteria=[]}}, egress=FilteredConnectPoint{connectPoint=of:0000000000000001/2, trafficSelector=DefaultTrafficSelector{criteria=[]}}, constraints=[], links=null, resourceGroup=null}

onos> add-point-intent of:0000000000000001/2 of:0000000000000001/1
Point to point intent submitted:
PointToPointIntent{id=0x300034, key=0x300034, appId=DefaultApplicationId{id=2, name=org.onosproject.cli}, priority=100, resources=[], selector=DefaultTrafficSelector{criteria=[]}, treatment=DefaultTrafficTreatment{immediate=[NOACTION], deferred=[], transition=None, meter=[], cleared=false, StatTrigger=null, metadata=null}, ingress=FilteredConnectPoint{connectPoint=of:0000000000000001/2, trafficSelector=DefaultTrafficSelector{criteria=[]}}, egress=FilteredConnectPoint{connectPoint=of:0000000000000001/1, trafficSelector=DefaultTrafficSelector{criteria=[]}}, constraints=[], links=null, resourceGroup=null}
```

## Flows (Point To Point Intent [h1 para h2]) Resultados:

```
onos> flows
deviceId=of:0000000000000001, flowRuleCount=5
    id=100007a585b6f, state=ADDED, bytes=358898, packets=2582, duration=3490, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:bddp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=100009465555a, state=ADDED, bytes=358898, packets=2582, duration=3490, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:lldp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=10000ea6f4b8e, state=ADDED, bytes=1890, packets=45, duration=3490, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:arp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=24000041c14f20, state=ADDED, bytes=0, packets=0, duration=61, liveType=UNKNOWN, priority=100, tableId=0, appId=org.onosproject.net.intent, payLoad=null, selector=[IN_PORT:2], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:1], deferred=[], transition=None, meter=[], cleared=false, StatTrigger=null, metadata=null}
    id=24000056c9eee0, state=ADDED, bytes=0, packets=0, duration=68, liveType=UNKNOWN, priority=100, tableId=0, appId=org.onosproject.net.intent, payLoad=null, selector=[IN_PORT:1], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:2], deferred=[], transition=None, meter=[], cleared=false, StatTrigger=null, metadata=null}
deviceId=of:0000000000000002, flowRuleCount=3
    id=1000002bbd8d4, state=ADDED, bytes=717796, packets=5164, duration=3490, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:lldp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=10000c70edd85, state=ADDED, bytes=0, packets=0, duration=3490, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:arp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=10000dc56d70b, state=ADDED, bytes=717796, packets=5164, duration=3490, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:bddp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
deviceId=of:0000000000000003, flowRuleCount=3
    id=10000464e5575, state=ADDED, bytes=717796, packets=5164, duration=3490, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:bddp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=10000646f55aa, state=ADDED, bytes=717796, packets=5164, duration=3490, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:lldp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=10000a6288ee9, state=ADDED, bytes=0, packets=0, duration=3490, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:arp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
deviceId=of:0000000000000004, flowRuleCount=3
    id=1000011326ce6, state=ADDED, bytes=252, packets=6, duration=3490, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:arp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=10000261e0911, state=ADDED, bytes=358898, packets=2582, duration=3490, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:lldp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=10000687421fe, state=ADDED, bytes=358898, packets=2582, duration=3490, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:bddp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
```

## Intents (Point To Point Intent [h1 para h2]) Resultados:

```
onos> intents
Id: 0x300031
State: INSTALLED
Key: 0x300031
Intent type: PointToPointIntent
Application Id: org.onosproject.cli
Leader Id: 192.168.0.48
Treatment: [NOACTION]
Ingress connect points and individual selectors
 -> Connect Point: of:0000000000000001/1   Selector: Inherited
Egress connect points and individual selectors
 -> Connect Point: of:0000000000000001/2   Selector: Inherited

Id: 0x300034
State: INSTALLED
Key: 0x300034
Intent type: PointToPointIntent
Application Id: org.onosproject.cli
Leader Id: 192.168.0.48
Treatment: [NOACTION]
Ingress connect points and individual selectors
 -> Connect Point: of:0000000000000001/2   Selector: Inherited
Egress connect points and individual selectors
 -> Connect Point: of:0000000000000001/1   Selector: Inherited
```

## Ping (Point To Point Intent [h1 para h2]) Resultados:

```
mininet> h1 ping -c 4 h2  # Ping entre hosts no mesmo switch
PING 10.0.0.2 (10.0.0.2) 56(84) bytes of data.
64 bytes from 10.0.0.2: icmp_seq=1 ttl=64 time=0.213 ms
64 bytes from 10.0.0.2: icmp_seq=2 ttl=64 time=0.037 ms
64 bytes from 10.0.0.2: icmp_seq=3 ttl=64 time=0.024 ms
64 bytes from 10.0.0.2: icmp_seq=4 ttl=64 time=0.033 ms

--- 10.0.0.2 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3070ms
rtt min/avg/max/mdev = 0.024/0.076/0.213/0.078 ms
```


### *OBS:

Aqui devemos excluir todos os Intents criando de [h1 para h2], pois a porta de [of:0000000000000001/1] estará aberta e não poderá ser utilizada para realizar um ping em [of:0000000000000004/1].

Com isso devemos excluir os Intents anteriores:

```
onos> remove-intent org.onosproject.cli 0x300031
onos> remove-intent org.onosproject.cli 0x300034
```


# Adicionando Point To Point Intent [h1 para h5]:

```
onos> add-point-intent of:0000000000000001/1 of:0000000000000004/1
Point to point intent submitted:
PointToPointIntent{id=0x300037, key=0x300037, appId=DefaultApplicationId{id=2, name=org.onosproject.cli}, priority=100, resources=[], selector=DefaultTrafficSelector{criteria=[]}, treatment=DefaultTrafficTreatment{immediate=[NOACTION], deferred=[], transition=None, meter=[], cleared=false, StatTrigger=null, metadata=null}, ingress=FilteredConnectPoint{connectPoint=of:0000000000000001/1, trafficSelector=DefaultTrafficSelector{criteria=[]}}, egress=FilteredConnectPoint{connectPoint=of:0000000000000004/1, trafficSelector=DefaultTrafficSelector{criteria=[]}}, constraints=[], links=null, resourceGroup=null}

onos> add-point-intent of:0000000000000004/1 of:0000000000000001/1
Point to point intent submitted:
PointToPointIntent{id=0x30003a, key=0x30003a, appId=DefaultApplicationId{id=2, name=org.onosproject.cli}, priority=100, resources=[], selector=DefaultTrafficSelector{criteria=[]}, treatment=DefaultTrafficTreatment{immediate=[NOACTION], deferred=[], transition=None, meter=[], cleared=false, StatTrigger=null, metadata=null}, ingress=FilteredConnectPoint{connectPoint=of:0000000000000004/1, trafficSelector=DefaultTrafficSelector{criteria=[]}}, egress=FilteredConnectPoint{connectPoint=of:0000000000000001/1, trafficSelector=DefaultTrafficSelector{criteria=[]}}, constraints=[], links=null, resourceGroup=null}
```

## Flows (Point To Point Intent [h1 para h5]) Resultados:

```
onos> flows
deviceId=of:0000000000000001, flowRuleCount=5
    id=100007a585b6f, state=ADDED, bytes=379609, packets=2731, duration=3950, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:bddp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=100009465555a, state=ADDED, bytes=379609, packets=2731, duration=3950, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:lldp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=10000ea6f4b8e, state=ADDED, bytes=1974, packets=47, duration=3950, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:arp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=2400003765d2e1, state=ADDED, bytes=0, packets=0, duration=52, liveType=UNKNOWN, priority=100, tableId=0, appId=org.onosproject.net.intent, payLoad=null, selector=[IN_PORT:3], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:1], deferred=[], transition=None, meter=[], cleared=false, StatTrigger=null, metadata=null}
    id=24000056c9eee0, state=ADDED, bytes=0, packets=0, duration=66, liveType=UNKNOWN, priority=100, tableId=0, appId=org.onosproject.net.intent, payLoad=null, selector=[IN_PORT:1], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:3], deferred=[], transition=None, meter=[], cleared=false, StatTrigger=null, metadata=null}
deviceId=of:0000000000000002, flowRuleCount=5
    id=1000002bbd8d4, state=ADDED, bytes=759218, packets=5462, duration=3950, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:lldp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=10000c70edd85, state=ADDED, bytes=0, packets=0, duration=3950, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:arp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=10000dc56d70b, state=ADDED, bytes=759218, packets=5462, duration=3950, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:bddp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=2400008c26a64c, state=ADDED, bytes=0, packets=0, duration=52, liveType=UNKNOWN, priority=100, tableId=0, appId=org.onosproject.net.intent, payLoad=null, selector=[IN_PORT:4], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:3], deferred=[], transition=None, meter=[], cleared=false, StatTrigger=null, metadata=null}
    id=2400009609fe12, state=ADDED, bytes=0, packets=0, duration=66, liveType=UNKNOWN, priority=100, tableId=0, appId=org.onosproject.net.intent, payLoad=null, selector=[IN_PORT:3], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:4], deferred=[], transition=None, meter=[], cleared=false, StatTrigger=null, metadata=null}
deviceId=of:0000000000000003, flowRuleCount=5
    id=10000464e5575, state=ADDED, bytes=759218, packets=5462, duration=3950, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:bddp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=10000646f55aa, state=ADDED, bytes=759218, packets=5462, duration=3950, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:lldp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=10000a6288ee9, state=ADDED, bytes=0, packets=0, duration=3950, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:arp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=240000125fe92b, state=ADDED, bytes=0, packets=0, duration=66, liveType=UNKNOWN, priority=100, tableId=0, appId=org.onosproject.net.intent, payLoad=null, selector=[IN_PORT:1], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:2], deferred=[], transition=None, meter=[], cleared=false, StatTrigger=null, metadata=null}
    id=2400008fd05f07, state=ADDED, bytes=0, packets=0, duration=52, liveType=UNKNOWN, priority=100, tableId=0, appId=org.onosproject.net.intent, payLoad=null, selector=[IN_PORT:2], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:1], deferred=[], transition=None, meter=[], cleared=false, StatTrigger=null, metadata=null}
deviceId=of:0000000000000004, flowRuleCount=5
    id=1000011326ce6, state=ADDED, bytes=252, packets=6, duration=3950, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:arp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=10000261e0911, state=ADDED, bytes=379609, packets=2731, duration=3950, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:lldp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=10000687421fe, state=ADDED, bytes=379609, packets=2731, duration=3950, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:bddp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=240000196cfd83, state=ADDED, bytes=0, packets=0, duration=66, liveType=UNKNOWN, priority=100, tableId=0, appId=org.onosproject.net.intent, payLoad=null, selector=[IN_PORT:4], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:1], deferred=[], transition=None, meter=[], cleared=false, StatTrigger=null, metadata=null}
    id=2400003540fcd7, state=ADDED, bytes=0, packets=0, duration=52, liveType=UNKNOWN, priority=100, tableId=0, appId=org.onosproject.net.intent, payLoad=null, selector=[IN_PORT:1], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:4], deferred=[], transition=None, meter=[], cleared=false, StatTrigger=null, metadata=null}
```


## Intents (Point To Point Intent [h1 para h5]) Resultados:

```
onos> intents
Id: 0x30003a
State: INSTALLED
Key: 0x30003a
Intent type: PointToPointIntent
Application Id: org.onosproject.cli
Leader Id: 192.168.0.48
Treatment: [NOACTION]
Ingress connect points and individual selectors
 -> Connect Point: of:0000000000000004/1   Selector: Inherited
Egress connect points and individual selectors
 -> Connect Point: of:0000000000000001/1   Selector: Inherited

Id: 0x300037
State: INSTALLED
Key: 0x300037
Intent type: PointToPointIntent
Application Id: org.onosproject.cli
Leader Id: 192.168.0.48
Treatment: [NOACTION]
Ingress connect points and individual selectors
 -> Connect Point: of:0000000000000001/1   Selector: Inherited
Egress connect points and individual selectors
 -> Connect Point: of:0000000000000004/1   Selector: Inherited
```

## Ping (Point To Point Intent [h1 para h5]) Resultados:

```
mininet> h1 ping -c 4 h5  # Ping entre hosts em switches diferentes
PING 10.0.0.5 (10.0.0.5) 56(84) bytes of data.
64 bytes from 10.0.0.5: icmp_seq=1 ttl=64 time=0.289 ms
64 bytes from 10.0.0.5: icmp_seq=2 ttl=64 time=0.040 ms
64 bytes from 10.0.0.5: icmp_seq=3 ttl=64 time=0.039 ms
64 bytes from 10.0.0.5: icmp_seq=4 ttl=64 time=0.039 ms

--- 10.0.0.5 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3070ms
rtt min/avg/max/mdev = 0.039/0.101/0.289/0.108 ms
```
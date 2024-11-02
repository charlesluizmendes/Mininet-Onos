# Comandos para executar 

Crie uma topologia com pelo menos 4 switches, sendo que um deles não deve ter nenhum host, e distribua pelo menos 7 clientes entre esses switches.

```
sudo python custom_topology.py
```

## Sem suporte ao encaminhamento reativo:

```
onos> app deactivate org.onosproject.fwd
```

### Resultado de Testes:

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

### Intents Instalados:

```
onos> intents
```

### Fluxos Instalados:

```
onos> flows
deviceId=of:0000000000000001, flowRuleCount=3
    id=100007a585b6f, state=ADDED, bytes=33082, packets=238, duration=740, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:bddp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=100009465555a, state=ADDED, bytes=33082, packets=238, duration=740, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:lldp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=10000ea6f4b8e, state=ADDED, bytes=425418, packets=10129, duration=740, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:arp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
deviceId=of:0000000000000002, flowRuleCount=3
    id=1000002bbd8d4, state=ADDED, bytes=66164, packets=476, duration=740, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:lldp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=10000c70edd85, state=ADDED, bytes=1003506, packets=23893, duration=740, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:arp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=10000dc56d70b, state=ADDED, bytes=66164, packets=476, duration=740, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:bddp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
deviceId=of:0000000000000003, flowRuleCount=3
    id=10000464e5575, state=ADDED, bytes=66164, packets=476, duration=740, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:bddp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=10000646f55aa, state=ADDED, bytes=66164, packets=476, duration=740, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:lldp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=10000a6288ee9, state=ADDED, bytes=462210, packets=11005, duration=740, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:arp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
deviceId=of:0000000000000004, flowRuleCount=3
    id=1000011326ce6, state=ADDED, bytes=417018, packets=9929, duration=740, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:arp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=10000261e0911, state=ADDED, bytes=33082, packets=238, duration=740, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:lldp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=10000687421fe, state=ADDED, bytes=33082, packets=238, duration=740, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:bddp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
```

### Listando Hosts:

```
onos> hosts
id=06:F0:EE:AC:DB:3F/None, mac=06:F0:EE:AC:DB:3F, locations=[of:0000000000000002/2], vlan=None, ip(s)=[10.0.0.4], innerVlan=None, outerTPID=unknown, provider=of:org.onosproject.provider.host, configured=false
id=32:AA:7A:67:C2:B8/None, mac=32:AA:7A:67:C2:B8, locations=[of:0000000000000001/1], vlan=None, ip(s)=[10.0.0.1], innerVlan=None, outerTPID=unknown, provider=of:org.onosproject.provider.host, configured=false
id=56:67:FB:2E:0A:CD/None, mac=56:67:FB:2E:0A:CD, locations=[of:0000000000000002/1], vlan=None, ip(s)=[10.0.0.3], innerVlan=None, outerTPID=unknown, provider=of:org.onosproject.provider.host, configured=false
id=6A:FF:48:30:E2:C0/None, mac=6A:FF:48:30:E2:C0, locations=[of:0000000000000001/2], vlan=None, ip(s)=[10.0.0.2], innerVlan=None, outerTPID=unknown, provider=of:org.onosproject.provider.host, configured=false
id=CA:00:10:06:E8:CF/None, mac=CA:00:10:06:E8:CF, locations=[of:0000000000000004/1], vlan=None, ip(s)=[10.0.0.5], innerVlan=None, outerTPID=unknown, provider=of:org.onosproject.provider.host, configured=false
id=D6:4C:2B:BD:98:88/None, mac=D6:4C:2B:BD:98:88, locations=[of:0000000000000004/2], vlan=None, ip(s)=[10.0.0.6], innerVlan=None, outerTPID=unknown, provider=of:org.onosproject.provider.host, configured=false
id=E2:39:13:FC:D5:BB/None, mac=E2:39:13:FC:D5:BB, locations=[of:0000000000000004/3], vlan=None, ip(s)=[10.0.0.7], innerVlan=None, outerTPID=unknown, provider=of:org.onosproject.provider.host, configured=false

```

### Adicionando Intents:

```
onos> add-host-intent 32:AA:7A:67:C2:B8/None 6A:FF:48:30:E2:C0/None
Host to Host intent submitted:
HostToHostIntent{id=0x0, key=0x0, appId=DefaultApplicationId{id=2, name=org.onosproject.cli}, priority=100, resources=[32:AA:7A:67:C2:B8/None, 6A:FF:48:30:E2:C0/None], selector=DefaultTrafficSelector{criteria=[]}, treatment=DefaultTrafficTreatment{immediate=[NOACTION], deferred=[], transition=None, meter=[], cleared=false, StatTrigger=null, metadata=null}, constraints=[LinkTypeConstraint{inclusive=false, types=[OPTICAL]}], resourceGroup=null, one=32:AA:7A:67:C2:B8/None, two=6A:FF:48:30:E2:C0/None}

onos> add-host-intent 32:AA:7A:67:C2:B8/None CA:00:10:06:E8:CF/None
Host to Host intent submitted:
HostToHostIntent{id=0x5, key=0x5, appId=DefaultApplicationId{id=2, name=org.onosproject.cli}, priority=100, resources=[32:AA:7A:67:C2:B8/None, CA:00:10:06:E8:CF/None], selector=DefaultTrafficSelector{criteria=[]}, treatment=DefaultTrafficTreatment{immediate=[NOACTION], deferred=[], transition=None, meter=[], cleared=false, StatTrigger=null, metadata=null}, constraints=[LinkTypeConstraint{inclusive=false, types=[OPTICAL]}], resourceGroup=null, one=32:AA:7A:67:C2:B8/None, two=CA:00:10:06:E8:CF/None}
onos@root >                           
```

### Intents Instalados:

```
onos> intents
Id: 0x0
State: INSTALLED
Key: 0x0
Intent type: HostToHostIntent
Application Id: org.onosproject.cli
Leader Id: 192.168.0.48
Resources: [32:AA:7A:67:C2:B8/None, 6A:FF:48:30:E2:C0/None]
Treatment: [NOACTION]
Constraints: [LinkTypeConstraint{inclusive=false, types=[OPTICAL]}]
Source host: 32:AA:7A:67:C2:B8/None
Destination host: 6A:FF:48:30:E2:C0/None

Id: 0x5
State: INSTALLED
Key: 0x5
Intent type: HostToHostIntent
Application Id: org.onosproject.cli
Leader Id: 192.168.0.48
Resources: [32:AA:7A:67:C2:B8/None, CA:00:10:06:E8:CF/None]
Treatment: [NOACTION]
Constraints: [LinkTypeConstraint{inclusive=false, types=[OPTICAL]}]
Source host: 32:AA:7A:67:C2:B8/None
Destination host: CA:00:10:06:E8:CF/None
```

### Resultado de Testes:

```
mininet> h1 ping -c 4 h2  # Ping entre hosts no mesmo switch
PING 10.0.0.2 (10.0.0.2) 56(84) bytes of data.
64 bytes from 10.0.0.2: icmp_seq=1 ttl=64 time=1.03 ms
64 bytes from 10.0.0.2: icmp_seq=2 ttl=64 time=0.087 ms
64 bytes from 10.0.0.2: icmp_seq=3 ttl=64 time=0.093 ms
64 bytes from 10.0.0.2: icmp_seq=4 ttl=64 time=0.091 ms

--- 10.0.0.2 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3026ms
rtt min/avg/max/mdev = 0.087/0.325/1.032/0.407 ms

mininet> h1 ping -c 4 h5  # Ping entre hosts em switches diferentes
PING 10.0.0.5 (10.0.0.5) 56(84) bytes of data.
64 bytes from 10.0.0.5: icmp_seq=1 ttl=64 time=0.340 ms
64 bytes from 10.0.0.5: icmp_seq=2 ttl=64 time=0.115 ms
64 bytes from 10.0.0.5: icmp_seq=3 ttl=64 time=0.108 ms
64 bytes from 10.0.0.5: icmp_seq=4 ttl=64 time=0.108 ms

--- 10.0.0.5 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3102ms
rtt min/avg/max/mdev = 0.108/0.167/0.340/0.099 ms

```


## Com suporte de encaminhamento Reactevice:

Como o aplicativo de encaminhamento reativo (Reactive Forwarding) ativo, o Onos realiza o envio dos pacotes de maneira automatica:

```
onos> app activate org.onosproject.fwd
```

### Resultado de Testes:

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

### Intents Instalados:

```
onos> intents
```

### Fluxos Instalados:

```
onos> flows
deviceId=of:0000000000000001, flowRuleCount=4
    id=100007a585b6f, state=ADDED, bytes=9174, packets=66, duration=205, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:bddp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=100009465555a, state=ADDED, bytes=9174, packets=66, duration=205, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:lldp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=10000ea6f4b8e, state=ADDED, bytes=425208, packets=10124, duration=205, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:arp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=10000021b41dc, state=ADDED, bytes=6272, packets=64, duration=205, liveType=UNKNOWN, priority=5, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:ipv4], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
deviceId=of:0000000000000002, flowRuleCount=4
    id=1000002bbd8d4, state=ADDED, bytes=18348, packets=132, duration=205, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:lldp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=10000c70edd85, state=ADDED, bytes=1003506, packets=23893, duration=205, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:arp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=10000dc56d70b, state=ADDED, bytes=18348, packets=132, duration=205, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:bddp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=100002341485c, state=ADDED, bytes=6566, packets=67, duration=205, liveType=UNKNOWN, priority=5, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:ipv4], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
deviceId=of:0000000000000003, flowRuleCount=4
    id=10000464e5575, state=ADDED, bytes=18348, packets=132, duration=205, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:bddp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=10000646f55aa, state=ADDED, bytes=18348, packets=132, duration=205, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:lldp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=10000a6288ee9, state=ADDED, bytes=462210, packets=11005, duration=205, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:arp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=10000be641e06, state=ADDED, bytes=5880, packets=60, duration=205, liveType=UNKNOWN, priority=5, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:ipv4], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
deviceId=of:0000000000000004, flowRuleCount=4
    id=1000011326ce6, state=ADDED, bytes=416976, packets=9928, duration=205, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:arp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=10000261e0911, state=ADDED, bytes=9174, packets=66, duration=205, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:lldp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=10000687421fe, state=ADDED, bytes=9174, packets=66, duration=205, liveType=UNKNOWN, priority=40000, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:bddp], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
    id=10000810531f2, state=ADDED, bytes=5880, packets=60, duration=205, liveType=UNKNOWN, priority=5, tableId=0, appId=org.onosproject.core, payLoad=null, selector=[ETH_TYPE:ipv4], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:CONTROLLER], deferred=[], transition=None, meter=[], cleared=true, StatTrigger=null, metadata=null}
```
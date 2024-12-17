# cURL's utilizados para realizar as operações pela API do Onos:

## add-host-intent

### h1-h2:

```
curl --location 'http://localhost:8181/onos/v1/intents' \
--header 'Authorization: Basic b25vczpyb2Nrcw==' \
--header 'Content-Type: application/json' \
--data '{
    "type": "HostToHostIntent",
    "appId": "org.onosproject.cli",
    "one": "AA:70:F6:40:E0:F0/-1",
    "two": "F2:19:21:AE:91:42/-1",
    "priority": 100
}'
```

### h1-h5:

```
curl --location 'http://localhost:8181/onos/v1/intents' \
--header 'Authorization: Basic b25vczpyb2Nrcw==' \
--header 'Content-Type: application/json' \
--data '{
    "type": "HostToHostIntent",
    "appId": "org.onosproject.cli",
    "one": "AA:70:F6:40:E0:F0/-1",
    "two": "EE:04:2E:5A:DF:D0/-1",
    "priority": 100
}'
```

## del-host-intent

### h1-h2:

```
curl --location --request DELETE 'http://localhost:8181/onos/v1/intents/org.onosproject.cli/0x200005' \
--header 'Authorization: Basic b25vczpyb2Nrcw=='
```

### h1-h5:

```
curl --location --request DELETE 'http://localhost:8181/onos/v1/intents/org.onosproject.cli/0x200000' \
--header 'Authorization: Basic b25vczpyb2Nrcw=='
```

## add-point-intent

### h1-h2:

```
curl --location 'http://localhost:8181/onos/v1/intents' \
--header 'Authorization: Basic b25vczpyb2Nrcw==' \
--header 'Content-Type: application/json' \
--data '{
    "type": "PointToPointIntent",
    "appId": "org.onosproject.cli",
    "priority": 100,
    "ingressPoint": {
        "device": "of:0000000000000001",
        "port": "1"
    },
    "egressPoint": {
        "device": "of:0000000000000001",
        "port": "2"
    }
}'
```

### h2-h1:

```
curl --location 'http://localhost:8181/onos/v1/intents' \
--header 'Authorization: Basic b25vczpyb2Nrcw==' \
--header 'Content-Type: application/json' \
--data '{
    "type": "PointToPointIntent",
    "appId": "org.onosproject.cli",
    "priority": 100,
    "ingressPoint": {
        "device": "of:0000000000000001",
        "port": "2"
    },
    "egressPoint": {
        "device": "of:0000000000000001",
        "port": "1"
    }
}'
```

### h1-h5:

```
curl --location 'http://localhost:8181/onos/v1/intents' \
--header 'Authorization: Basic b25vczpyb2Nrcw==' \
--header 'Content-Type: application/json' \
--data '{
    "type": "PointToPointIntent",
    "appId": "org.onosproject.cli",
    "priority": 100,
    "ingressPoint": {
        "device": "of:0000000000000001",
        "port": "1"
    },
    "egressPoint": {
        "device": "of:0000000000000004",
        "port": "1"
    }
}'
```

### h5-h1:

```
curl --location 'http://localhost:8181/onos/v1/intents' \
--header 'Authorization: Basic b25vczpyb2Nrcw==' \
--header 'Content-Type: application/json' \
--data '{
    "type": "PointToPointIntent",
    "appId": "org.onosproject.cli",
    "priority": 100,
    "ingressPoint": {
        "device": "of:0000000000000004",
        "port": "1"
    },
    "egressPoint": {
        "device": "of:0000000000000001",
        "port": "1"
    }
}'
```

## del-point-intent

### h1-h2:

```
curl --location --request DELETE 'http://localhost:8181/onos/v1/intents/org.onosproject.cli/0x300031' \
--header 'Authorization: Basic b25vczpyb2Nrcw=='
```

### h2-h1:

```
curl --location --request DELETE 'http://localhost:8181/onos/v1/intents/org.onosproject.cli/0x300034' \
--header 'Authorization: Basic b25vczpyb2Nrcw=='
```

### h1-h5:

```
curl --location --request DELETE 'http://localhost:8181/onos/v1/intents/org.onosproject.cli/0x30003a' \
--header 'Authorization: Basic b25vczpyb2Nrcw=='
```

### h5-h1:

```
curl --location --request DELETE 'http://localhost:8181/onos/v1/intents/org.onosproject.cli/0x300037' \
--header 'Authorization: Basic b25vczpyb2Nrcw=='
```

## aps:

```
curl --location 'http://localhost:8181/onos/v1/applications' \
--header 'Authorization: Basic b25vczpyb2Nrcw=='
```

## fwd-activate:

```
curl --location --request POST 'http://localhost:8181/onos/v1/applications/org.onosproject.fwd/active' \
--header 'Authorization: Basic b25vczpyb2Nrcw=='
```

## fwd-deactivate:

```
curl --location --request DELETE 'http://localhost:8181/onos/v1/applications/org.onosproject.fwd/active' \
--header 'Authorization: Basic b25vczpyb2Nrcw=='
```

## intents:

```
curl --location 'http://localhost:8181/onos/v1/intents' \
--header 'Authorization: Basic b25vczpyb2Nrcw=='
```
```
{
    "intents": [
        {
            "type": "PointToPointIntent",
            "id": "0x6",
            "key": "0x6",
            "appId": "org.onosproject.cli",
            "resources": [],
            "state": "FAILED"
        },
        {
            "type": "HostToHostIntent",
            "id": "0x1",
            "key": "0x1",
            "appId": "org.onosproject.cli",
            "resources": [
                "AA:70:F6:40:E0:F0/None",
                "EE:04:2E:5A:DF:D0/None"
            ],
            "state": "FAILED"
        },
        {
            "type": "PointToPointIntent",
            "id": "0x7",
            "key": "0x7",
            "appId": "org.onosproject.cli",
            "resources": [],
            "state": "FAILED"
        },
        {
            "type": "HostToHostIntent",
            "id": "0x0",
            "key": "0x0",
            "appId": "org.onosproject.cli",
            "resources": [
                "AA:70:F6:40:E0:F0/None",
                "F2:19:21:AE:91:42/None"
            ],
            "state": "FAILED"
        },
        {
            "type": "PointToPointIntent",
            "id": "0x4",
            "key": "0x4",
            "appId": "org.onosproject.cli",
            "resources": [],
            "state": "INSTALLING"
        },
        {
            "type": "PointToPointIntent",
            "id": "0x2",
            "key": "0x2",
            "appId": "org.onosproject.cli",
            "resources": [],
            "state": "INSTALLING"
        }
    ]
}
```

## flows:

```
curl --location 'http://localhost:8181/onos/v1/flows' \
--header 'Authorization: Basic b25vczpyb2Nrcw=='
```

## hosts:

```
curl --location 'http://localhost:8181/onos/v1/hosts' \
--header 'Authorization: Basic b25vczpyb2Nrcw=='
```
```
{
    "hosts": [
        {
            "id": "02:6A:F8:E8:14:9A/None",
            "mac": "02:6A:F8:E8:14:9A",
            "vlan": "None",
            "innerVlan": "None",
            "outerTpid": "unknown",
            "configured": false,
            "ipAddresses": [
                "10.0.0.2"
            ],
            "locations": [
                {
                    "elementId": "of:0000000000000004",
                    "port": "3"
                }
            ]
        },
        {
            "id": "D2:00:A0:DF:D5:70/None",
            "mac": "D2:00:A0:DF:D5:70",
            "vlan": "None",
            "innerVlan": "None",
            "outerTpid": "unknown",
            "configured": false,
            "ipAddresses": [
                "10.0.0.1"
            ],
            "locations": [
                {
                    "elementId": "of:0000000000000019",
                    "port": "1"
                }
            ]
        }
    ]
}
```
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
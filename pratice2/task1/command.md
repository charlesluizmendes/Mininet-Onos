# Comandos para executar 

Crie uma topologia com pelo menos 4 switches, sendo que um deles não deve ter nenhum host, e distribua pelo menos 7 clientes entre esses switches.

```
sudo python custom_topology.py
```

## Sem suporte ao encaminhamento reativo:

```
onos> app deactivate org.onosproject.fwd
mininet> h1 ping -c 4 h2  # Ping entre hosts no mesmo switch
mininet> h1 ping -c 4 h5  # Ping entre hosts em switches diferentes
onos> intents
onos> flows
```

### Conclusão

O ONOS não cria intents automaticamente por padrão quando o encaminhamento reativo está desativado. O comportamento padrão do ONOS é monitorar a rede e criar intents automaticamente apenas quando o aplicativo de encaminhamento reativo (Reactive Forwarding) está ativo, pois este aplicativo gerencia a instalação automática de regras de fluxo baseadas na demanda de tráfego.

Quando o encaminhamento reativo é desativado, o ONOS espera que o administrador ou um aplicativo customizado adicione intents explicitamente para definir o caminho entre os hosts.

Para criar os Intents:

```
onos> add-host-intent 66:0E:FF:A4:EC:C7/None 72:44:69:1F:C1:0D/None
onos> add-host-intent 66:0E:FF:A4:EC:C7/None D2:75:91:EA:84:F1/None
```

Agora ao repetir os testes de trasnferencia de pacotes entre os hosts, tudo ocorre normalmente:

```
mininet> h1 ping -c 4 h2  # Ping entre hosts no mesmo switch
mininet> h1 ping -c 4 h5  # Ping entre hosts em switches diferentes
```
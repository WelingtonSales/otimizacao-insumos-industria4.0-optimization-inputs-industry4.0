# Especificações Técnicas do Sistema

## Hardware de Borda
- **Gateway:** ICP DAS tGW-700
- **Processador:** ARM Cortex-A8
- **RAM:** 512MB
- **Armazenamento:** 4GB

## Protocolos
- **Máquina → Gateway:** Modbus TCP/OPC UA
- **Gateway → Nuvem:** MQTT com Sparkplug B sobre TLS 1.2+

## Stack Tecnológica
- **Gateway:** Python 3.9+, TensorFlow Lite, Docker
- **Nuvem:** HiveMQ Cloud, InfluxDB Cloud, Grafana Cloud

## Variáveis Monitoradas (10 Hz)
- Códigos de erro
- Sensores de posição
- Sensor de cola (pressão/temperatura)
- Contador de ciclos
- Tempo de ciclo
- Torque do motor
- Leitor de código

## Segurança (IEC 62443)
- Criptografia TLS 1.2+
- Autenticação multifator (MFA)
- Segmentação de rede
- MLSecOps para ciclo de vida da IA

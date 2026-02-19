**otimizacao-insumos-industria4.0-optimization-inputs-industry4.0**

Artefatos complementares do projeto de otimização de insumos com Edge AI


**Autor:** Welington dos Santos Sales

**Ano:** 2026


**📋 Sobre o Projeto**

Este repositório contém os artefatos complementares do projeto "Otimização de Insumos na Indústria 4.0", que propõe um sistema baseado em Edge AI para cálculo do Custo Real por Embalagem Efetiva (CRPE) na indústria cerâmica.

**🎯 Problema**

A Empresa Alfa decide compra de embalagens baseada apenas em custo unitário e defeitos iniciais, ignorando perdas no processo (atolamentos, falhas de colagem, rasgos).

**🎯 Objetivo**

Fornecer todos os artefatos técnicos necessários para compreensão e implementação da solução proposta, incluindo diagramas de arquitetura, especificações técnicas, código de simulação e mockups de interface.

**💡 Solução Proposta**

•	Gateway industrial coleta dados da máquina (10 Hz)
•	Modelo de IA leve (DSLM) classifica falhas em tempo real
•	Dados enviados à nuvem para dashboard
•	Cálculo automático do CRPE por fornecedor

**📁 Estrutura do Repositório**

-- diagramas/ # Diagramas de arquitetura (C4 model) 
-- script-simulacao/ # Código Python para simulação do CRPE 
-- especificacoes/ # Especificações técnicas detalhadas

**Como Referenciar Este Projeto**

SALES, W. S. **Otimização de Insumos na Indústria 4.0: Artefatos Complementares**. GitHub, 2026. Disponível em: [https://github.com/WelingtonSales/otimizacao-insumos-industria4.0-optimization-inputs-industry4.0.git]

**🛠️ Como Executar a Simulação**

cd script-simulacao
pip install -r requirements.txt
python crpe_simulacao.py


# Otimização de Insumos na Indústria 4.0
Artefatos complementares do projeto otimização de insumos com Edge AI

**Autor:** Welington dos Santos Sales  
**Ano:** 2026

## 📋 Sobre o Projeto
Projeto de extensão conceitual que propõe um sistema baseado em **Edge AI** para otimização de custos na indústria cerâmica, calculando o **Custo Real por Embalagem Efetiva (CRPE)**

## 🎯 Objetivo do Projeto
Calcular o **Custo Real por Embalagem Efetiva (CRPE)** para otimizar a decisão de compra entre fornecedores, considerando não apenas o custo unitário, mas também as perdas no processo produtivo (atolamentos, falhas de colagem, rasgos)..

## 🎯 Problema
A Empresa Alfa decide compra de embalagens baseada apenas em custo unitário e defeitos iniciais, ignorando perdas no processo (atolamentos, falhas de colagem, rasgos).

## 💡 Solução Proposta
- Gateway industrial coleta dados da máquina (10 Hz)
- Modelo de IA leve (DSLM) classifica falhas em tempo real
- Dados enviados à nuvem para dashboard
- Cálculo automático do CRPE por fornecedor

## 📁 Estrutura do Repositório
-- diagramas/ # Diagramas de arquitetura (C4 model)
-- script-simulacao/ # Código Python para simulação do CRPE
-- especificacoes/ # Especificações técnicas detalhadas

## 📚 Referência
SALES, W. S. **Otimização de Insumos na Indústria 4.0: Artefatos Complementares**. GitHub, 2026. Disponível em: https://github.com/WelingtonSales/otimizacao-insumos-industria4.0-optimization-inputs-industry4.0.git

## 🛠️ Como Executar a Simulação
```bash
cd script-simulacao
pip install -r requirements.txt
python crpe_simulacao.py

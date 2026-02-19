#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SIMULAÇÃO DO CRPE (Custo Real por Embalagem Efetiva)
Projeto: Otimização de Insumos na Indústria 4.0
Autor: Welington dos Santos Sales
Data: 2026
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate

# =============================================================================
# DADOS DOS FORNECEDORES
# =============================================================================
fornecedores = {
    'A': {'nome': 'Fornecedor A', 'custo_unitario': 2.00, 'defeito_inicial': 0.03},
    'B': {'nome': 'Fornecedor B', 'custo_unitario': 1.80, 'defeito_inicial': 0.06},
    'C': {'nome': 'Fornecedor C', 'custo_unitario': 1.50, 'defeito_inicial': 0.10}
}

# =============================================================================
# CENÁRIOS DE FALHA NO PROCESSO
# =============================================================================
cenarios = {
    'Otimista': {'A': 0.01, 'B': 0.03, 'C': 0.05},
    'Base': {'A': 0.02, 'B': 0.04, 'C': 0.07},
    'Pessimista': {'A': 0.04, 'B': 0.06, 'C': 0.10}
}

# =============================================================================
# FUNÇÃO DE CÁLCULO DO CRPE
# =============================================================================
def calcular_crpe(custo_unitario, defeito_inicial, falha_processo):
    perda_total = defeito_inicial + falha_processo
    crpe = custo_unitario / (1 - perda_total)
    return round(crpe, 2)

# =============================================================================
# EXECUÇÃO DA SIMULAÇÃO
# =============================================================================
print("=" * 70)
print(" CÁLCULO DO CRPE - CUSTO REAL POR EMBALAGEM EFETIVA ".center(70))
print("=" * 70)

resultados = []

for nome_cenario, falhas in cenarios.items():
    print(f"\n>>> CENÁRIO: {nome_cenario}")
    print("-" * 40)
    
    for id_forn, dados in fornecedores.items():
        perda_total = dados['defeito_inicial'] + falhas[id_forn]
        crpe = calcular_crpe(dados['custo_unitario'], dados['defeito_inicial'], falhas[id_forn])
        
        resultados.append({
            'Cenário': nome_cenario,
            'Fornecedor': id_forn,
            'Custo Unitário (R$)': dados['custo_unitario'],
            'Defeito Inicial': f"{dados['defeito_inicial']:.1%}",
            'Falha Processo': f"{falhas[id_forn]:.1%}",
            'Perda Total': f"{perda_total:.1%}",
            'CRPE (R$)': crpe
        })
        
        print(f"Fornecedor {id_forn}: R$ {dados['custo_unitario']:.2f} / "
              f"(1 - {perda_total:.1%}) = R$ {crpe:.2f}")

# =============================================================================
# ANÁLISE DOS RESULTADOS
# =============================================================================
print("\n" + "=" * 70)
print(" ANÁLISE COMPARATIVA ".center(70))
print("=" * 70)

df = pd.DataFrame(resultados)
tabela = df.pivot_table(values='CRPE (R$)', index='Fornecedor', columns='Cenário')
print("\nTabela de CRPE por Fornecedor e Cenário (R$):")
print(tabulate(tabela, headers='keys', tablefmt='grid', floatfmt='.2f'))

# Melhor fornecedor por cenário
print("\n" + "🏆 MELHOR FORNECEDOR POR CENÁRIO:")
print("-" * 40)
for cenario in df['Cenário'].unique():
    df_cenario = df[df['Cenário'] == cenario]
    melhor = df_cenario.loc[df_cenario['CRPE (R$)'].idxmin()]
    print(f"{cenario}: Fornecedor {melhor['Fornecedor']} (CRPE = R$ {melhor['CRPE (R$)']:.2f})")

print("\n" + "=" * 70)
print(" SIMULAÇÃO CONCLUÍDA COM SUCESSO! ".center(70))
print("=" * 70)

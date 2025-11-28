#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import base64
import re

# Lê o arquivo JSON
with open('iPass-canal de atendimento Copia.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Decodifica o base64 dos dialogs
dialogs_base64 = data['builder_version']['dialogs'][0]
dialogs_json = json.loads(base64.b64decode(dialogs_base64))

# Extrai os nós principais
nodes = {}
for cell in dialogs_json['config']['cells']:
    if cell.get('type') == 'altu.DialogNode':
        node_name = cell.get('name', '')
        title = cell.get('title', '')
        entry_point = cell.get('entry_point', '')
        next_steps = cell.get('next_step', [])
        
        input_data = cell.get('input')
        input_type = 'N/A'
        if input_data and input_data.get('default'):
            input_type = input_data.get('default', {}).get('type', 'N/A')
        
        nodes[node_name] = {
            'title': title,
            'entry_point': entry_point,
            'next_steps': next_steps or [],
            'input_type': input_type
        }

# Mapeia os nós esperados do fluxograma
fluxograma_esperado = {
    'Inicio': ['email'],
    'email': ['Menu', 'Tudo certo'],
    'Tudo certo': ['Menu'],
    'Menu': ['Pergunta1', 'Pergunta2', 'Outros'],
    'Pergunta1': ['Reembolso', 'Pagamento Recusado', 'Formas de Pagamento', 'DuvidaResposta'],
    'Pergunta2': ['RedefinicaoSenha', 'Meia Entrada', 'Transferencia', 'OndeIngressos', 'Classificacao', 'DuvidaResposta'],
    'Outros': ['SalvaPergunta'],
    'SalvaPergunta': ['NovaPergunta'],
    'NovaPergunta': ['Avaliacao', 'Menu'],
    'DuvidaResposta': ['NovaPergunta'],
    'Avaliacao': ['ComentarioAvaliacao'],
    'ComentarioAvaliacao': ['Comentario', 'Fim'],
    'Comentario': ['Fim']
}

# Encontra os nós no JSON
print("=" * 80)
print("ANÁLISE DE CONFORMIDADE - JSON vs FLUXOGRAMA")
print("=" * 80)
print("\n1. NÓS ENCONTRADOS NO JSON:")
print("-" * 80)
for node_name, node_info in sorted(nodes.items()):
    print(f"  • {node_name}: '{node_info['title']}' (entry: {node_info['entry_point']})")

print("\n2. COMPARAÇÃO COM FLUXOGRAMA:")
print("-" * 80)

# Verifica nós esperados
nós_encontrados = set(nodes.keys())
nós_esperados = set(fluxograma_esperado.keys())

print("\n✓ Nós presentes no JSON e no fluxograma:")
for node in nós_encontrados & nós_esperados:
    print(f"  • {node}")

print("\n✗ Nós no fluxograma mas não encontrados no JSON:")
for node in nós_esperados - nós_encontrados:
    print(f"  • {node}")

print("\n⚠ Nós no JSON mas não no fluxograma:")
for node in nós_encontrados - nós_esperados:
    print(f"  • {node}")

# Verifica fluxos
print("\n3. VERIFICAÇÃO DE FLUXOS:")
print("-" * 80)

# Mapeia títulos para nomes de nós
title_to_node = {info['title']: name for name, info in nodes.items()}

# Verifica se os fluxos estão corretos
problemas = []

# Verifica fluxo Inicio -> Email
if 'node_130a4c130ea317b3' in nodes:  # Inicio
    next_nodes = [step.get('dialog_node', '') for step in nodes['node_130a4c130ea317b3']['next_steps']]
    if 'node_c4c876491d3003d1' not in next_nodes:  # email
        problemas.append("Inicio não conecta diretamente ao email")

# Verifica fluxo Email -> Menu ou Tudo Certo
if 'node_c4c876491d3003d1' in nodes:  # email
    next_nodes = [step.get('dialog_node', '') for step in nodes['node_c4c876491d3003d1']['next_steps']]
    if 'node_2e834f3fdbb4af1e' in nodes:  # Tudo certo
        if 'node_2e834f3fdbb4af1e' not in next_nodes and 'node_f0569278ef1d6be4' not in next_nodes:
            problemas.append("Email não conecta a 'Tudo certo' ou Menu")

# Verifica Menu
if 'node_f0569278ef1d6be4' in nodes:  # Menu
    next_nodes = [step.get('dialog_node', '') for step in nodes['node_f0569278ef1d6be4']['next_steps']]
    print(f"\n  Menu conecta para: {len(next_nodes)} nós")
    for step in nodes['node_f0569278ef1d6be4']['next_steps']:
        condition = step.get('condition', '')
        target = step.get('dialog_node', '')
        target_title = nodes.get(target, {}).get('title', 'N/A')
        print(f"    - {condition} -> {target_title}")

if problemas:
    print("\n⚠ PROBLEMAS ENCONTRADOS:")
    for problema in problemas:
        print(f"  • {problema}")
else:
    print("\n✓ Fluxos básicos parecem corretos")

print("\n" + "=" * 80)


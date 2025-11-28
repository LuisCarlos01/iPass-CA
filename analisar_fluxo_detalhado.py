#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import base64

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

# Mapeia títulos para IDs de nós
title_to_id = {info['title']: name for name, info in nodes.items()}

# Fluxograma esperado (por títulos)
fluxograma_esperado = {
    'Inicio': ['email'],
    'email': ['Tudo certo'],
    'Tudo certo': ['Menu'],
    'Menu': ['Pergunta1', 'Pergunta2', 'Outros'],
    'Pergunta1': ['Reembolso', 'Pagamento Recusado', 'Formas de Pagamento', 'DuvidaRespondida'],
    'Pergunta2': ['Redifinição de senha', 'Meia Entrada', 'Transferência de titularidade', 
                  'Onde encontro meus ingressos', 'Classificação Indicativa', 'DuvidaRespondida'],
    'Outros': ['salvaPergunta'],
    'salvaPergunta': ['NovaPergunta?'],
    'NovaPergunta?': ['Avaliação', 'Menu'],
    'DuvidaRespondida': ['NovaPergunta?'],
    'Avaliação': ['Comentario Avaliação'],
    'Comentario Avaliação': ['Comentário', 'Fim'],
    'Comentário': ['Fim']
}

print("=" * 80)
print("ANÁLISE DETALHADA - JSON vs FLUXOGRAMA")
print("=" * 80)

print("\n1. MAPEAMENTO DE NÓS (Título -> ID):")
print("-" * 80)
for title, node_id in sorted(title_to_id.items()):
    print(f"  '{title}' -> {node_id}")

print("\n2. VERIFICAÇÃO DE CONFORMIDADE:")
print("-" * 80)

problemas = []
conformes = []

for origem_title, destinos_esperados in fluxograma_esperado.items():
    origem_id = title_to_id.get(origem_title)
    
    if not origem_id:
        problemas.append(f"❌ Nó '{origem_title}' não encontrado no JSON")
        continue
    
    origem_node = nodes.get(origem_id)
    if not origem_node:
        continue
    
    # Pega os IDs dos nós de destino esperados
    destinos_ids_esperados = set()
    for dest_title in destinos_esperados:
        dest_id = title_to_id.get(dest_title)
        if dest_id:
            destinos_ids_esperados.add(dest_id)
        else:
            problemas.append(f"⚠ Nó de destino '{dest_title}' não encontrado no JSON")
    
    # Pega os IDs dos nós de destino reais
    destinos_ids_reais = set()
    for step in origem_node['next_steps']:
        dest_id = step.get('dialog_node', '')
        if dest_id:
            destinos_ids_reais.add(dest_id)
    
    # Compara
    faltando = destinos_ids_esperados - destinos_ids_reais
    extras = destinos_ids_reais - destinos_ids_esperados
    
    if faltando or extras:
        problemas.append(f"❌ '{origem_title}':")
        if faltando:
            faltando_titles = [nodes.get(d, {}).get('title', d) for d in faltando]
            problemas.append(f"   - Faltando conexões para: {faltando_titles}")
        if extras:
            extras_titles = [nodes.get(d, {}).get('title', d) for d in extras]
            problemas.append(f"   - Conexões extras para: {extras_titles}")
    else:
        conformes.append(f"✓ '{origem_title}' -> {[nodes.get(d, {}).get('title', d) for d in destinos_ids_esperados]}")

print("\n✓ FLUXOS CONFORMES:")
for item in conformes:
    print(f"  {item}")

if problemas:
    print("\n❌ PROBLEMAS ENCONTRADOS:")
    for problema in problemas:
        print(f"  {problema}")
else:
    print("\n✅ TODOS OS FLUXOS ESTÃO CONFORMES!")

print("\n3. FLUXO DETALHADO DO JSON:")
print("-" * 80)
for node_id, node_info in sorted(nodes.items()):
    if node_info['next_steps']:
        print(f"\n'{node_info['title']}' ({node_id}):")
        for step in node_info['next_steps']:
            condition = step.get('condition', 'true')
            target_id = step.get('dialog_node', '')
            target_title = nodes.get(target_id, {}).get('title', 'N/A')
            print(f"  [{condition}] -> '{target_title}'")

print("\n" + "=" * 80)


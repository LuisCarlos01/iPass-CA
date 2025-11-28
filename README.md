# iPass - Canal de Atendimento

Repositório contendo a configuração do chatbot de atendimento da iPass, incluindo fluxograma e arquivo de configuração JSON.

## 📋 Estrutura do Projeto

```
iPass-CA/
├── README.md
├── fluxograma_chatbot_ipass.md              # Fluxograma visual do chatbot
├── iPass-canal de atendimento Copia.json    # Configuração do chatbot (AltU)
├── ipass-zenvia-chatbot.json                # Configuração do chatbot (Zenvia)
├── ZENVIA_README.md                         # Documentação Zenvia
├── RELATORIO_CONFORMIDADE.md                # Relatório de validação
├── analisar_fluxo.py                        # Script de análise básica
└── analisar_fluxo_detalhado.py              # Script de análise detalhada
```

## 🎯 Objetivo

Este projeto contém a documentação e configuração do chatbot de atendimento da iPass, que oferece suporte aos clientes através de dois canais principais:

- **Suporte Financeiro**: Reembolsos, pagamentos recusados e formas de pagamento
- **Suporte Técnico**: Recuperação de senha, meia entrada, transferências, localização de ingressos e classificação indicativa

## 🔄 Fluxo do Chatbot

### Fluxo Principal

1. **Início** → Coleta de nome do usuário
2. **E-mail** → Validação do e-mail
3. **Confirmação** → Validação dos dados coletados
4. **Menu Principal** → Escolha do tipo de suporte
5. **Atendimento** → Resolução da dúvida
6. **Avaliação** → Coleta de feedback (NPS)
7. **Fim** → Encerramento

### Canais de Suporte

#### Suporte Financeiro
- Reembolso/Cancelamento
- Pagamento Recusado
- Formas de Pagamento

#### Suporte Técnico
- Recuperação de Senha
- Meia Entrada
- Transferência de Titularidade
- Localização de Ingressos
- Classificação Indicativa

## 📁 Arquivos Principais

### `fluxograma_chatbot_ipass.md`
Fluxograma visual em Mermaid que representa toda a estrutura de conversação do chatbot. Inclui:
- Fluxos de navegação
- Pontos de decisão
- Canais de suporte
- Fluxo de avaliação

### `iPass-canal de atendimento Copia.json`
Arquivo de configuração do chatbot no formato **AltU Builder**. Contém:
- Estrutura de diálogos (codificada em base64)
- Configurações de publicação
- Nós de diálogo e suas conexões
- Variáveis e condições de fluxo

### `ipass-zenvia-chatbot.json`
Arquivo de configuração do chatbot no formato **Zenvia**. Contém:
- Estrutura de nós simplificada
- Configurações de input e validação
- Fluxo de transições
- Integrações via webhook
- Suporte para WhatsApp, Webchat e Instagram

📖 [Ver documentação completa do Zenvia](ZENVIA_README.md)

### `RELATORIO_CONFORMIDADE.md`
Relatório técnico validando a conformidade entre o fluxograma e a implementação JSON.

## 🛠️ Plataformas Suportadas

### AltU Builder
- Plataforma de construção de chatbots
- Arquivo: `iPass-canal de atendimento Copia.json`
- Formato: Diálogos codificados em base64

### Zenvia
- Plataforma omnichannel de conversação
- Arquivo: `ipass-zenvia-chatbot.json`
- Canais: WhatsApp, Webchat, Instagram
- Recursos: NPS, Webhooks, Validações
- [Ver documentação completa](ZENVIA_README.md)

### Outras Tecnologias
- **Mermaid**: Linguagem de diagramação para fluxogramas
- **Python**: Scripts de validação e análise
- **JSON**: Formato de configuração

## 📊 Validação

O projeto inclui scripts Python para validação da conformidade:
- `analisar_fluxo.py`: Análise básica de estrutura
- `analisar_fluxo_detalhado.py`: Análise detalhada de fluxos e conexões

## 🔍 Como Visualizar o Fluxograma

O fluxograma pode ser visualizado em qualquer renderizador de Mermaid:
- GitHub (renderização automática)
- VS Code com extensão Mermaid
- [Mermaid Live Editor](https://mermaid.live/)

## 📝 Notas Técnicas

- O arquivo JSON contém os diálogos codificados em base64
- A estrutura segue o padrão AltU Builder v2
- Todos os nós estão validados e conformes com o fluxograma
- O chatbot utiliza variáveis `contact.extra.*` para controle de fluxo

## 📞 Contato

Para dúvidas sobre o chatbot, entre em contato via: **contato@ipass.com.br**

---

**Última atualização**: 2025


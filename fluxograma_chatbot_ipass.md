# Fluxograma - Chatbot iPass - Canal de Atendimento

```mermaid
flowchart TD
    Start([Início]) --> Inicio[Início<br/>Coleta nome]
    Inicio --> Email[E-mail<br/>Validação]
    Email --> TudoCerto[Confirmação<br/>Dados coletados]
    TudoCerto --> Menu{Menu Principal}
    
    Menu -->|Financeiro| Pergunta1[Assunto?]
    Menu -->|Técnico| Pergunta2[Dúvida técnica?]
    Menu -->|Outros| Outros[Outros]
    
    %% Fluxo Suporte Financeiro
    Pergunta1 -->|Reembolso| Reembolso[Reembolso]
    Pergunta1 -->|Pagamento Recusado| PagamentoRecusado[Pagamento Recusado]
    Pergunta1 -->|Forma Pagamento| FormasPagamento[Formas Pagamento]
    Pergunta1 -->|Outros| DuvidaResposta{Dúvida<br/>Respondida?}
    
    Reembolso --> DuvidaResposta
    PagamentoRecusado --> DuvidaResposta
    FormasPagamento --> DuvidaResposta
    
    %% Fluxo Suporte Técnico
    Pergunta2 -->|Recuperar Senha| RedefinicaoSenha[Recuperar Senha]
    Pergunta2 -->|Meia Entrada| MeiaEntrada[Meia Entrada]
    Pergunta2 -->|Transferência| Transferencia[Transferência]
    Pergunta2 -->|Localizar Ingressos| OndeIngressos[Localizar Ingressos]
    Pergunta2 -->|Classificação| Classificacao[Classificação]
    Pergunta2 -->|Outros| DuvidaResposta
    
    RedefinicaoSenha --> DuvidaResposta
    MeiaEntrada --> DuvidaResposta
    Transferencia --> DuvidaResposta
    OndeIngressos --> DuvidaResposta
    Classificacao --> DuvidaResposta
    
    %% Fluxo Outros
    Outros --> SalvaPergunta[Registra Dúvida]
    SalvaPergunta --> NovaPergunta{Nova<br/>Pergunta?}
    
    NovaPergunta -->|Sim| Avaliacao[Avaliação<br/>NPS 0-10]
    NovaPergunta -->|Não| Menu
    
    %% Fluxo comum após resposta
    DuvidaResposta --> NovaPergunta
    
    %% Fluxo de avaliação
    Avaliacao --> ComentarioAvaliacao{Comentário?}
    ComentarioAvaliacao -->|Sim| Comentario[Comentário]
    ComentarioAvaliacao -->|Não| Fim[Fim]
    Comentario --> Fim
    
    %% Estilos melhorados
    classDef startEnd fill:#4caf50,stroke:#2e7d32,stroke-width:3px,color:#fff
    classDef process fill:#2196f3,stroke:#1565c0,stroke-width:2px,color:#fff
    classDef decision fill:#ff9800,stroke:#e65100,stroke-width:2px,color:#fff
    classDef menu fill:#9c27b0,stroke:#6a1b9a,stroke-width:2px,color:#fff
    classDef suporte fill:#00bcd4,stroke:#0277bd,stroke-width:2px,color:#fff
    
    class Start,Inicio,Email,TudoCerto,Fim startEnd
    class Reembolso,PagamentoRecusado,FormasPagamento,RedefinicaoSenha,MeiaEntrada,Transferencia,OndeIngressos,Classificacao,SalvaPergunta,Comentario,Avaliacao process
    class Menu,Pergunta1,Pergunta2,NovaPergunta,ComentarioAvaliacao,DuvidaResposta decision
    class Outros suporte
```

## Descrição dos Fluxos

### 1. Fluxo Inicial
- **Início**: Saudação e coleta do nome do usuário
- **Email**: Validação do e-mail (formato obrigatório)
- **Tudo Certo**: Confirmação dos dados coletados

### 2. Menu Principal
O usuário escolhe entre três opções:
- **Suporte Financeiro**: Questões sobre pagamentos, reembolsos e formas de pagamento
- **Suporte Técnico**: Dúvidas sobre senha, ingressos, transferências, etc.
- **Outros**: Para dúvidas não categorizadas

### 3. Suporte Financeiro
- Reembolso/Cancelamento
- Pagamento Recusado
- Formas de Pagamento (Cartão de Crédito e PIX)

### 4. Suporte Técnico
- Recuperação de senha
- Meia Entrada
- Transferência de titularidade
- Onde encontro meus ingressos
- Classificação Indicativa

### 5. Fluxo de Avaliação
Após responder a dúvida:
- Pergunta se a dúvida foi respondida
- Se sim, solicita avaliação NPS (0-10)
- Opcionalmente coleta comentário
- Encerra a conversa

### 6. Fluxo de Outros
- Registra a dúvida
- Orienta contato via e-mail: contato@ipass.com.br
- Retorna ao menu para nova tentativa

## Legenda de Cores

- **🟢 Verde**: Início e fim do fluxo
- **🔵 Azul**: Processos de informação/resposta
- **🟠 Laranja**: Pontos de decisão e menus
- **🔷 Azul claro**: Fluxos de suporte técnico


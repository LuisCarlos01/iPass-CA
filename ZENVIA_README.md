# iPass Chatbot - Zenvia

Este documento explica como importar e configurar o chatbot iPass na plataforma Zenvia.

## 📁 Arquivo

- **Nome**: `ipass-zenvia-chatbot.json`
- **Versão**: 1.0.0
- **Plataforma**: Zenvia
- **Canais suportados**: WhatsApp, Webchat, Instagram

## 🚀 Como Importar no Zenvia

### Passo 1: Acessar a Plataforma Zenvia

1. Acesse [https://app.zenvia.com](https://app.zenvia.com)
2. Faça login com suas credenciais
3. Navegue até **"Chatbots"** ou **"Flows"**

### Passo 2: Importar o Fluxo

1. Clique em **"Criar Novo Bot"** ou **"Importar Fluxo"**
2. Selecione **"Importar de arquivo JSON"**
3. Faça upload do arquivo `ipass-zenvia-chatbot.json`
4. Aguarde o processamento

### Passo 3: Configurar Variáveis

O chatbot utiliza as seguintes variáveis que podem precisar de configuração:

```json
{
  "user_name": "",        // Nome do usuário
  "user_email": "",       // Email do usuário
  "support_type": "",     // Tipo de suporte (Financeiro/Técnico)
  "question_type": "",    // Tipo de pergunta
  "nps_score": 0,         // Pontuação NPS (0-10)
  "user_feedback": ""     // Comentário do usuário
}
```

### Passo 4: Configurar Webhooks (Opcional)

Se você deseja salvar as perguntas e feedbacks dos usuários, configure os webhooks:

#### Webhook para Salvar Perguntas

- **URL**: `{{seu_dominio}}/api/save_question`
- **Método**: POST
- **Payload**:
```json
{
  "name": "{{user_name}}",
  "email": "{{user_email}}",
  "question": "{{user_question}}",
  "timestamp": "{{timestamp}}"
}
```

#### Webhook para Salvar Feedback

- **URL**: `{{seu_dominio}}/api/save_feedback`
- **Método**: POST
- **Payload**:
```json
{
  "name": "{{user_name}}",
  "email": "{{user_email}}",
  "nps_score": "{{nps_score}}",
  "feedback": "{{user_feedback}}",
  "timestamp": "{{timestamp}}"
}
```

### Passo 5: Testar o Fluxo

1. Use o **Simulador** do Zenvia para testar o fluxo
2. Verifique todos os caminhos:
   - Fluxo de Suporte Financeiro
   - Fluxo de Suporte Técnico
   - Fluxo de Avaliação NPS
3. Teste validações de email
4. Teste todas as opções de menu

## 🔄 Estrutura do Fluxo

### Fluxo Principal

```
Início (Coleta Nome)
    ↓
Coleta Email
    ↓
Confirmação de Dados
    ↓
Menu Principal
    ├─→ Suporte Financeiro
    │   ├─→ Reembolso
    │   ├─→ Pagamento Recusado
    │   ├─→ Formas de Pagamento
    │   └─→ Outros
    │
    ├─→ Suporte Técnico
    │   ├─→ Recuperar Senha
    │   ├─→ Meia Entrada
    │   ├─→ Transferir Ingresso
    │   ├─→ Localizar Ingressos
    │   ├─→ Classificação Indicativa
    │   └─→ Outros
    │
    └─→ Outros
        ↓
Dúvida Respondida?
    ├─→ Sim → Nova Pergunta?
    └─→ Não → Outros
        ↓
Avaliação NPS
    ↓
Comentário (Opcional)
    ↓
Fim
```

## 📊 Tipos de Nós

| Tipo | Descrição | Exemplo |
|------|-----------|---------|
| `text_input` | Coleta de texto livre | Nome, Email, Comentários |
| `menu` | Opções de múltipla escolha (lista) | Menu Principal, Suporte Financeiro |
| `quick_reply` | Botões de resposta rápida | Sim/Não, Opções Técnicas |
| `message` | Apenas mensagem (sem input) | Informações, Respostas |
| `nps` | Avaliação de 0 a 10 | Avaliação de Satisfação |

## ⚙️ Configurações Importantes

### Timeout

- **Padrão**: 300 segundos (5 minutos)
- **Localização**: `settings.timeout`
- **Ajustar se necessário** para eventos com alto volume

### Validação de Email

- **Regex**: `^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$`
- **Tentativas máximas**: 2
- **Mensagens de erro**: Configuradas no nó `coleta_email`

### Mensagens de Fallback

Configure mensagens para casos de erro:

- `fallback_message`: Quando o bot não entende a entrada
- `error_message`: Quando ocorre um erro técnico
- `end_session_message`: Quando a sessão expira

## 🎨 Personalização

### Alterar Mensagens

Para alterar mensagens, edite o campo `content` dentro de cada nó:

```json
{
  "id": "inicio",
  "messages": [
    {
      "type": "text",
      "content": "Sua mensagem personalizada aqui"
    }
  ]
}
```

### Adicionar Novos Nós

1. Copie a estrutura de um nó existente
2. Altere o `id` para um único identificador
3. Configure `messages`, `input` e `transitions`
4. Adicione o novo nó ao array `nodes`

### Alterar Opções de Menu

Edite o campo `input.options` do nó desejado:

```json
{
  "options": [
    {
      "id": "opcao1",
      "label": "📌 Texto Visível",
      "value": "Valor Salvo",
      "description": "Descrição opcional"
    }
  ]
}
```

## 🐛 Troubleshooting

### Problema: Fluxo não avança após input

**Solução**: Verifique se as condições em `transitions` estão corretas:
```json
{
  "condition": "{{variavel}} == 'valor'",
  "target": "proximo_no"
}
```

### Problema: Email não valida corretamente

**Solução**: Verifique a regex de validação no nó `coleta_email` e ajuste se necessário.

### Problema: Webhook não funciona

**Solução**: 
1. Verifique se a URL está acessível
2. Confirme que o método HTTP está correto (POST)
3. Verifique os logs do Zenvia para erros

### Problema: NPS não salva

**Solução**: Certifique-se de que o webhook de feedback está configurado e ativo.

## 📝 Notas Importantes

1. **Teste Completo**: Sempre teste todo o fluxo antes de colocar em produção
2. **Backup**: Mantenha um backup do JSON original
3. **Versionamento**: Use controle de versão para mudanças
4. **Monitoramento**: Configure alertas para erros críticos
5. **Analytics**: Ative analytics do Zenvia para acompanhar métricas

## 🔗 Links Úteis

- [Documentação Zenvia](https://zenvia.com/docs)
- [API Reference](https://zenvia.com/api)
- [Community Forum](https://community.zenvia.com)
- [Support](https://support.zenvia.com)

## 📞 Suporte

Para dúvidas sobre o chatbot iPass:
- **Email**: suporte@ipass.com.br
- **Website**: https://ipass.com.br

Para dúvidas sobre a plataforma Zenvia:
- **Suporte Zenvia**: https://support.zenvia.com
- **Email**: support@zenvia.com

---

**Última atualização**: 28/11/2025  
**Versão do chatbot**: 1.0.0  
**Plataforma**: Zenvia 2.0


# 🤖 AI Project Architect - Agente de P&D

Este projeto consiste em um **Arquiteto de Agentes de IA Sênior** desenvolvido com a biblioteca [Agno](https://github.com/agno-ai/agno). O agente é especializado em pesquisa e desenvolvimento, capaz de conceber projetos detalhados para novos sistemas autônomos utilizando dados reais e verificados da internet.

## 🚀 Diferenciais Técnicos

Diferente de LLMs comuns, este agente utiliza um pipeline de pesquisa rigoroso para evitar alucinações:

- **Busca Híbrida:** Integração com **DuckDuckGo Tools** para tendências de mercado e bibliotecas recentes.
- **Alta Fidelidade:** Uso do **ValyuTools** para priorizar artigos científicos, documentações oficiais e referências robustas.
- **Zero Alucinação:** Protocolo de sistema que proíbe terminantemente a invenção de links ou capacidades técnicas inexistentes.
- **Stack Otimizada:** Baseado no modelo `llama-3.3-70b` via **Groq**, configurado com temperatura 0 para máxima precisão factual.

## 🛠️ Tecnologias Utilizadas

- **Framework:** [Agno (AgentOS)](https://agno.com/)
- **LLM:** Llama 3.3 70B (via Groq)
- **Ferramentas:** DuckDuckGo Search & Valyu Research
- **Ambiente:** Python 3.11+

## 📋 Pré-requisitos

Antes de começar, você precisará de:

- Uma chave de API da [Groq](https://console.groq.com/).
- Uma chave de API do [Valyu](https://valyu.ai/).

## 🔧 Instalação

1. **Clone o repositório:**

   ```bash
   git clone [https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git](https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git)
   cd NOME_DO_REPOSITORIO

   ```

2. **Crie e ative o ambiente virtual**
   ```bash
   python -m venv venv
    # No Windows:
    .\venv\Scripts\activate
    # No Linux/Mac:
    source venv/bin/activate
   ```
3. **Instale as dependências**

   ```bash
   pip install agno groq python-dotenv duckduckgo-search

   ```

4. **Como usar**
   ```bash
   fastapi dev main.py
   ```

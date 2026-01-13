import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.valyu import ValyuTools
from agno.os import AgentOS

load_dotenv()

# Configuração do Agente
agent = Agent(
    id="ai-project-architect",
    name="Arquiteto de Projetos IA",
    role="Especialista em P&D para concepção de sistemas de agentes autônomos.",
    model=Groq(id="llama-3.3-70b-versatile", temperature=0),
    tools=[DuckDuckGoTools(), ValyuTools()],
    instructions=[
        "Sempre inicie consultando o ValyuTools para encontrar fontes acadêmicas ou oficiais.",
        "Use o DuckDuckGoTools apenas para complementar com ferramentas de mercado recentes.",
        "PROIBIÇÃO CRÍTICA: Não invente URLs. Forneça apenas links verificados.",
        "ESTRUTURA: 1. Conceito, 2. Stack Técnica, 3. RAG/Memória, 4. Viabilidade, 5. Fontes."
    ],
    # Removido 'show_tool_calls' daqui para evitar o TypeError
    markdown=True
)

# Se quiser rodar via terminal para teste rápido, descomente a linha abaixo:
# agent.print_response("Ideia para agente de saúde", show_tool_calls=True)

# Configuração para o App/FastAPI
agent_os = AgentOS(agents=[agent])
app = agent_os.get_app() 
🇧🇷 Versão em português:
[README.pt-br.md](README.pt-br.md)

# 🚀 DataPilot

Copiloto inteligente para auditoria e limpeza de dados com IA assistiva.

O DataPilot foi desenvolvido para simplificar tarefas repetitivas de qualidade de dados através de auditorias automáticas, insights inteligentes e futuras interações em linguagem natural.

---

## 📌 Sobre o projeto

Analistas de dados frequentemente gastam tempo com tarefas repetitivas como:

- verificar valores nulos
- identificar duplicados
- validar tipos de dados
- encontrar inconsistências
- analisar qualidade do dataset

O objetivo do DataPilot é automatizar esse processo e transformar tarefas técnicas em uma experiência simples e assistida.

---

## ✨ Funcionalidades atuais

### ✅ Upload de CSV
Envio de datasets diretamente pela interface.

### ✅ Auditoria automática
O sistema identifica automaticamente:

- valores ausentes
- linhas duplicadas
- tipos de dados
- cardinalidade
- estrutura do dataset

### ✅ Data Quality Score
Geração automática de score de qualidade do dataset.

### ✅ Smart Insights
Geração de insights automáticos baseados em regras heurísticas e métricas estatísticas.

Exemplos:
- colunas com muitos valores ausentes
- presença de duplicados
- colunas com alta cardinalidade
- avaliação geral da qualidade dos dados

---

## 🛡️ Arquitetura focada em privacidade

O DataPilot foi pensado com foco em arquitetura enterprise e compatibilidade com ambientes sensíveis à LGPD.

### 🔒 Processamento local
As auditorias são realizadas localmente utilizando:
- pandas
- regras estatísticas
- heurísticas

Sem necessidade de envio do dataset bruto para APIs externas.

### 🤖 IA como camada assistiva
A IA será utilizada como camada de interpretação e automação, e não como motor principal do sistema.

Isso reduz:
- riscos de privacidade
- exposição de dados sensíveis
- custos com tokens/API
- dependência de provedores externos

---

## 🛠️ Tecnologias utilizadas

- Python
- Pandas
- NumPy
- Streamlit

---

## 📂 Estrutura do projeto

```txt
DataPilot/
│
├── app/
│   ├── ai/
│   ├── audit/
│   ├── cleaning/
│   ├── ui/
│   ├── utils/
│   └── main.py
│
├── data/
├── outputs/
├── tests/
├── requirements.txt
└── README.md

🚀 Roadmap
✅ V1 — AI Data Auditor
Upload de CSV
Auditoria automática
Score de qualidade
Smart insights
🔥 V2 — AI Data Cleaner
Remoção de duplicados
Tratamento de nulos
Conversão de tipos
Normalização de dados
Comandos em linguagem natural
🚀 V3 — AI Analyst
KPIs automáticos
Métricas de retenção
Cohort analysis
Análise exploratória
🧠 V4 — AI Insights Engine
Detecção automática de padrões
Identificação de anomalias
Sugestão de hipóteses
Storytelling de dados
🎯 Objetivo do projeto

O DataPilot busca unir:

automação
engenharia de dados
análise de dados
IA assistiva
experiência do usuário

em uma única plataforma de produtividade para analistas.

📌 Status do projeto

🚧 Em desenvolvimento ativo.

👨‍💻 Autor

Gabriel Schmidel

GitHub:
https://github.com/gschmidel19
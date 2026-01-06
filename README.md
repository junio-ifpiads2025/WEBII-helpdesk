# 🎧 Helpdesk MVP

Um sistema de chamados simples e intuitivo desenvolvido com **Django**, focado na resolução rápida de problemas através de uma interface baseada em chat.

O objetivo deste MVP (Minimum Viable Product) é oferecer um fluxo de suporte eficiente sem a complexidade de ferramentas corporativas pesadas.

---

## 🚀 Funcionalidades

- **Autenticação por E-mail:** Login e Cadastro simplificados usando E-mail e Senha.
- **Perfis de Acesso:**
  - **Cliente:** Abre chamados, visualiza apenas os seus tickets e interage via chat.
  - **Técnico (Staff):** Visualiza todos os chamados, altera status e prioridades.
- **Interface Intuitiva:**
  - **Dashboard:** Visualização rápida com indicadores de cor para prioridades (Alta/Média/Baixa).
- **Gestão de Status:** Fluxo simples: `Aberto` → `Em Andamento` → `Concluído`.

---

## 🛠️ Tecnologias Utilizadas

- **Backend:** Python 3 + Django
- **Frontend:** HTML5 + Bootstrap 5 (CDN)
- **Banco de Dados:** SQLite (Padrão para desenvolvimento)
- **Ícones:** Bootstrap Icons

---

## 📦 Como Rodar o Projeto

Siga os passos abaixo para executar o sistema em sua máquina local.

### 1. Pré-requisitos
Certifique-se de ter o **Python 3** e o **Git** instalados.

### 2. Instalação

```bash
# Clone este repositório
git clone https://github.com/junio-ifpiads2025/WEBII-ChamadaTecnicaHelpDesk.git

# Entre na pasta do projeto
cd helpdesk_root

# Crie um ambiente virtual
python3 -m venv venv

# Ative o ambiente virtual
# No Linux/Mac:
source venv/bin/activate
# No Windows:
# venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

# Catarina Quest  
Um quiz interativo desenvolvido para testar e aprimorar os conhecimentos sobre o estado de Santa Catarina.  

## 📋 Descrição  
O Catarina Quest é uma aplicação web que oferece aos usuários um quiz com perguntas relacionadas à história, cultura, geografia e outros aspectos do estado de Santa Catarina. O projeto foi desenvolvido utilizando o framework Django para o backend e Vue.js para o frontend, proporcionando uma experiência dinâmica e responsiva.  

## 🚀 Funcionalidades  
- **Perguntas Diversificadas**: Inclui uma variedade de perguntas sobre Santa Catarina.  
- **Feedback Imediato**: Os usuários recebem feedback instantâneo sobre suas respostas.  
- **Pontuação**: Sistema de pontuação para acompanhar o desempenho do usuário.  
- **Interface Responsiva**: Design adaptável para diferentes dispositivos.  

## 🛠️ Tecnologias Utilizadas  
- **Backend**: [Django](https://www.djangoproject.com/) (Python)  
- **Frontend**: [Vue.js](https://vuejs.org/)  
- **Banco de Dados**: SQLite (padrão do Django)  
- **Gerenciamento de Pacotes**: [pip](https://pip.pypa.io/en/stable/) e [npm](https://www.npmjs.com/)  

## 📦 Instalação  
Siga os passos abaixo para configurar o ambiente de desenvolvimento do Catarina Quest.  

### 1️⃣ Clonar o Repositório  

```git clone https://github.com/hencostan/catarina_quest.git```

```cd catarina_quest```

## ⚙️ Configuração do Backend (Django)
Criar e ativar o ambiente virtual:

```python3 -m venv venv```

```source venv/bin/activate  # No Windows, use venv\Scripts\activate```

Instalar as dependências do Python:

```pip install -r requirements.txt```

Realizar as migrações do banco de dados:

```python manage.py migrate```

Iniciar o servidor Django:

```python manage.py runserver```

## 🎨 Configuração do Frontend (Vue.js)

Navegar até o diretório do frontend:

```cd frontend```

Instalar as dependências do Node.js:

```npm install```

Compilar e iniciar o servidor de desenvolvimento do Vue.js:

```npm run server```

## 🖥️ Uso
Após seguir os passos de instalação:

Acesse o frontend do Vue.js em http://localhost:8080 para interagir com o quiz.

O backend do Django estará disponível em http://127.0.0.1:8000.

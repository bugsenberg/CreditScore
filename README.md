# Previsão de Score de Crédito com Flask e Machine Learning

Este projeto é uma aplicação web desenvolvida com **Flask** que utiliza um modelo de **machine learning** para prever o **score de crédito** de clientes com base em informações como profissão, mix de crédito e comportamento de pagamento.

## 💡 Funcionalidades

- Interface web para inserção de dados.
- Previsão de score de crédito usando modelo treinado com `RandomForestClassifier`.
- Encoders para variáveis categóricas.
- Resultado da previsão exibido na mesma página, com visual moderno e responsivo.

## 🧠 Tecnologias Utilizadas

- Python
- Flask
- Pandas
- Scikit-learn
- HTML + CSS

## 🚀 Como executar o projeto

1. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
Navegue até o diretório do projeto:

bash
Copiar
Editar
cd nome-do-repositorio
Instale as dependências (recomenda-se uso de ambiente virtual):

bash
Copiar
Editar
pip install -r requirements.txt
Execute o aplicativo:

bash
Copiar
Editar
python app.py
Acesse no navegador:

cpp
Copiar
Editar
http://127.0.0.1:5000

📁 Estrutura do Projeto
csharp
Copiar
Editar
├── app.py                  # Arquivo principal Flask
├── modelo.pkl              # Modelo treinado
├── encoder_profissao.pkl   # Encoder de profissão
├── encoder_mix.pkl         # Encoder de mix de crédito
├── encoder_pagamento.pkl   # Encoder de comportamento de pagamento
├── templates/
│   └── formulario.html     # Interface web (HTML)
├── static/
│   └── style.css           # Estilos CSS
└── clientes.csv            # Base de dados (opcional)
📝 Licença
Este projeto está licenciado sob a MIT License.

Desenvolvido com 💻 por Seu Nome.
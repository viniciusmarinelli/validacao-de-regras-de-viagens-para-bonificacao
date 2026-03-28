# Validação de Regras de Viagens para Bonificação

## 📌 Descrição do Projeto

Este projeto tem como objetivo automatizar a validação de regras operacionais para identificar se motoristas devem ser bonificados com base em dados de viagens.

A solução foi desenvolvida para substituir um processo manual de auditoria, que exigia análise individual de viagens, tornando o processo mais rápido, confiável e escalável.

---

## 🎯 Problema de Negócio

Em operações logísticas, a validação de bonificação de motoristas pode ser complexa e sujeita a erros quando feita manualmente.

Principais desafios:

- Alto volume de viagens para análise
- Necessidade de validar múltiplas regras operacionais
- Risco de erro humano
- Tempo elevado para auditoria

---

## 💡 Solução

Foi desenvolvido um pipeline de dados em Python que:

- Processa dados de viagens a partir de arquivos CSV
- Realiza o cruzamento com dados de motoristas
- Aplica regras de negócio para validação de bonificação
- Gera relatórios automatizados com os resultados

---

## ⚙️ Regras Implementadas

### 🚛 3ª Perna

- Identifica motoristas que realizaram duas ou mais viagens no mesmo dia
- Verifica o status dos registros
- Classifica como:
  - BONIFICAR
  - NÃO BONIFICAR
  - JUSTIFICAR

---

### 🐄 Gado Magro no Sábado

- Identifica viagens realizadas aos sábados
- Filtra viagens do tipo específico (gado magro)
- Aplica regras de validação com base no status do registro

---

## 🔄 Pipeline do Projeto
Dados de viagens (CSV)
↓
Processamento e limpeza
↓
Cruzamento com base de motoristas
↓
Aplicação das regras de negócio
↓
Geração de relatório final (Excel)

---

## 🛠️ Tecnologias Utilizadas

- Python
- Pandas
- Excel

---

## 📂 Estrutura do Projeto
data/
trips_sample.csv
drivers_sample.xlsx

src/
data_processing.py
bonus_rules.py
report.py

main.py
requirements.txt

---

## ▶️ Como Executar

1. Clone o repositório:


git clone https://github.com/viniciusmarinelli/validacao-de-regras-de-viagens-para-bonificacao


2. Acesse a pasta do projeto:


cd validacao-de-regras-de-viagens-para-bonificacao


3. Instale as dependências:


pip install -r requirements.txt


4. Execute o projeto:


python main.py


---

## ⚠️ Observação

Os dados utilizados neste projeto são fictícios e foram criados apenas para fins de demonstração, sem qualquer relação com dados reais.

---

## 📊 Possíveis Melhorias

- Criação de dashboard para visualização dos resultados
- Integração com banco de dados (SQL)
- Automatização do processo (execução agendada)
- Inclusão de testes automatizados

---

## 👨‍💻 Autor

Vinícius de Souza Marinelli  

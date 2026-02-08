Sistema de Empréstimo em Python 

Este projeto é um sistema simples de simulação de empréstimos**, desenvolvido em Python, que analisa a renda do cliente, define o tipo de empréstimo e calcula parcelas fixas com juros


Funcionalidades

- Cadastro de dados do cliente
- Análise de renda para aprovação ou reprovação do empréstimo
- Classificação automática do tipo de empréstimo:
  - Empréstimo pessoal
  - Empréstimo consignado
  - Empréstimo com garantia
- Cálculo de:
  - Valor da parcela fixa
  - Total pago
  - Juros totais

 Regras do sistema

- Renda menor que R$ 1.500 -> empréstimo reprovado
- Tipos de empréstimo:
  - Renda até R$ 2.499 -> Empréstimo pessoal (5% ao mês)
  - Renda até R$ 4.999 -> Empréstimo consignado (3% ao mês)
  - Renda acima de R$ 5.000 -> Empréstimo com garantia (2% ao mês)

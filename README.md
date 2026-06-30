# Aula 17 – Integração Contínua, Qualidade Automatizada, Métricas e Gestão de Defeitos

## Integrantes

- Angelo Fonseca
---

## 1. Repositório da Atividade

| Item | Descrição |
| --- | --- |
| Nome do repositório | LocalEats-17 |
| Link do repositório | https://github.com/angelofonseca/LocalEats-17|

### Estrutura de Diretórios

```
tests/
│   ├── test_search.py
│   ├── test_busca_nome_bdd.py
│   └── features/
│       └── busca_nome.feature
.github/
│  └── workflows/
│        └── quality.yml
├── search.py
└── requirements.txt
```

---

## 2. Planejamento da Funcionalidade

| Item | Descrição |
| --- | --- |
| Título da Issue | Busca por nome do restaurante |
| Objetivo da funcionalidade | Buscar restaurante pelo nome. |
| Link da Issue | https://github.com/angelofonseca/LocalEats-17/issues/1 |


---

## 3. Teste Automatizado

| Item | Descrição |
| --- | --- |
| Tipo de teste | Unitário e BDD |
| Objetivo do teste | Garantir que o sistema encontre corretamente um restaurante a partir do nome buscado |
| Link para o arquivo do teste (TDD) | https://github.com/angelofonseca/LocalEats-17/blob/main/tests/test_search.py |
| Link para o arquivo do teste (BDD) | https://github.com/angelofonseca/LocalEats-17/blob/main/tests/test_busca_nome_bdd.py |

---

## 4. Pipeline de Integração Contínua

| Item | Descrição |
| --- | --- |
| Nome do workflow | Quality Check |
| Evento que dispara a execução | PUSH e PR |
| Link para o arquivo do workflow | <https://github.com/angelofonseca/LocalEats-17/blob/main/.github/workflows/quality.yml> |
| Link de uma execução do workflow | <https://github.com/angelofonseca/LocalEats-17/actions> |

---

## 5. Indicadores de Qualidade

| Indicador | Valor |
|------------|---------|
| Quantidade de testes executados | 3 |
| Quantidade de testes aprovados | 3 |
| Quantidade de testes com falha | 1 |
| Status final do pipeline | Sucesso |

Cobertura de search.py: 100%.

---

## 6. Registro de Defeito

| Item | Descrição |
|--------|--------|
| Título do defeito | Quando busca por nome com espaços extras nao encontra o restaurante
| Severidade | Média |
| Link da Issue | https://github.com/angelofonseca/LocalEats-17/issues/3 |
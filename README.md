
# Casos de Teste

O programa é responsável para validar ou não um triângulo. O triângulo é válido caso não possua todos os lados com tamanho zero,
nenhum lado pode ter comprimento igual a zero, cada lado deve ser menor que a soma de todos os lados divididos por 2.


Com isso, realizamos os testes:

| id | módulo | descrição | resultado|
|----|--------|-----------|----------|
| 1| Triângulo | Inserção de dados "(0, 0, 0)"| Inválido|
| 2| Triângulo |Inserção de lados "(0, 4, 4)" | Inválido|
| 3| Triângulo |Inserção de lados "(2, 3, 4)" | Válido|

1. O primeiro teste, realizamos caso todos os lados fossem zero, com isso não seria um triângulo e retornaria false;
2. O segundo teste, realizamos com um lados sendo zero, com isso não seria um triângulo por ter esse comprimento e retornaria false;
3. O terceiro teste, realizamos com comprimentos válidos e cumprindo todos os requisitos de ser um triângulo e retornaria true



O prompt abaixo foi enviado **sem nenhuma alteração** ao Gemini, ao DeepSeek e ao ChatGPT. À esquerda está o texto na íntegra, dividido em blocos na ordem em que aparece; à direita, o instrumento de aula que cada bloco carrega e o efeito que eu esperava dele. Juntando os blocos da esquerda, de cima para baixo, tem-se o prompt completo, que também pode ser [baixado em texto puro](assets/prompt-mestre.txt).

::: {.caixa}
**A ideia geral.** Um prompt comum pede oportunidades e aceita o que vier. Este chega com a régua pronta: diz o que conta como oportunidade (Aula 4), que evidência aceitar (Aula 4), o que corta uma candidata (Aula 5), em que campos responder (Aulas 4, 5 e 6) e o que rejeitar (Aula 6). O trabalho analítico que eu faria depois, à mão, foi transferido para a instrução.
:::

::: {.tabela .media}
| Decisão que o prompt precisava tomar | Onde ela está |
|---|---|
| Recorte (setor, região, porte, capital, horizonte) | Bloco 2 |
| Critério de corte e destino de quem não passa | Blocos 6 e 11, seções 2 e 3 do formato |
| Padrão de evidência e o que fazer sem dado confiável | Bloco 9 e campo Evidências |
| Formato de saída em campos fixos | Bloco 12 |
| Quantidade de oportunidades | Bloco 4 |
:::

## Bloco 1 · Papel e contexto

::: {.bloco}
::: {.bloco-prompt}
{{PROMPT:8-13}}
:::
::: {.bloco-just}
[Estrutura-base]{.tag}

Estrutura herdada da Atividade 1: define um papel exigente para a IA e pede que as variáveis sejam lidas antes de qualquer resposta. Não carrega instrumento das Aulas 4 a 6.

**Efeito esperado:** uma resposta de consultor crítico, que questiona a ideia, e não de entusiasta do setor. As variáveis ficam delimitadas pela tag `<variaveis>`, separadas das instruções de processo e de formato.
:::
:::

## Bloco 2 · Recorte

::: {.bloco}
::: {.bloco-prompt}
{{PROMPT:14-19}}
:::
::: {.bloco-just}
[Recorte · Leitura crítica de dado (Aula 4) · 3Ms (Aula 5)]{.tag}

Prompt sem recorte devolve lugar-comum. Aqui ficam fixados setor, região, porte, capital e horizonte.

- **Região:** exigir a RA de cada oportunidade, justificada com dados, prepara o terreno para a [leitura crítica de dado](index.html#leitura-critica): o erro provável é usar número nacional da panificação como se valesse para uma RA.
- **Capital de R\$ 500 mil:** é o limite que torna decisivos o 3º M (margem e ponto de equilíbrio) e o capital inicial nos [critérios de potencial](index.html#timmons).
- **Horizonte:** abertura entre 2026 e 2030 e operação desenhada para funcionar sem os donos em até 10 anos, o que vira um campo próprio do formato.

**Efeito esperado:** oportunidades comparáveis entre si, todas no mesmo território e com a mesma restrição de capital.
:::
:::

## Bloco 3 · Definição de oportunidade

::: {.bloco}
::: {.bloco-prompt}
{{PROMPT:20-20}}
:::
::: {.bloco-just}
[Tendência × oportunidade (Aula 4)]{.tag}

Padaria é um ramo tradicional, com demanda conhecida e muita concorrência. Sem essa distinção, a tendência acaba apresentada como se fosse oportunidade, e as três IAs devolveriam a mesma resposta genérica: "abra uma padaria artesanal".

**Efeito esperado:** exigir um cliente identificável, que pagaria para resolver o problema e que o negócio atende melhor do que quem já o atende, força cada resposta a sair do geral para o específico. A tendência fica rebaixada a "lugar onde procurar". [Justificativa completa](index.html#tendencia).
:::
:::

## Bloco 4 · Quantidade

::: {.bloco}
::: {.bloco-prompt}
{{PROMPT:21-21}}
:::
::: {.bloco-just}
[Quantidade]{.tag}

Pedir muitas oportunidades favorece a lista genérica; pedir poucas força a seleção. O limite é de até três, ordenadas da mais à menos defensável.

**Efeito esperado:** a instrução "se menos de 3 passarem nos critérios de corte, entregue menos e diga isso" dá à IA uma saída honesta e impede que ela complete a lista para cumprir a cota. É o que liga a quantidade ao filtro de corte do bloco 6.
:::
:::

## Bloco 5 · Objetivo, público e profundidade

::: {.bloco}
::: {.bloco-prompt}
{{PROMPT:22-24}}
:::
::: {.bloco-just}
[Estrutura-base]{.tag}

Define o entregável (um resumo executivo por oportunidade aprovada, com dados e referências reais), quem vai lê-lo e para que serve: decidir em qual oportunidade focar antes de montar o plano de negócios.

**Efeito esperado:** profundidade intermediária, suficiente para comparar e decidir, sem virar plano de negócios completo.
:::
:::

## Bloco 6 · Critérios de corte

::: {.bloco}
::: {.bloco-prompt}
{{PROMPT:25-31}}
:::
::: {.bloco-just}
[Checklist final de Dornelas (Aula 5)]{.tag}

É o critério de corte do prompt. A oportunidade que falha em qualquer das cinco perguntas não entra e vai para a lista de descartadas.

**Efeito esperado:** por ser binário, deixa as três respostas comparáveis. Exigir justificativa para cada SIM impede o checklist preenchido no automático, e a lista de descartadas permite ver o filtro funcionando. É também o teste que aplico, por conta própria, às finalistas na [aplicação da régua](auditoria-regua.html). [Justificativa completa](index.html#checklist).
:::
:::

## Bloco 7 · Critérios de potencial

::: {.bloco}
::: {.bloco-prompt}
{{PROMPT:32-32}}
:::
::: {.bloco-just}
[Alto e baixo potencial, Timmons (Aula 5) · usado em parte]{.tag}

Mantive os critérios de lógica (necessidade do cliente, estrutura do mercado, barreiras de entrada e capital inicial), que valem para qualquer negócio.

Deixei de fora os patamares numéricos (30% a 50% de crescimento ao ano e ponto de equilíbrio em menos de dois anos): vêm do capital de risco, foram pensados para startups e reprovariam qualquer padaria saudável num mercado maduro.

**Efeito esperado:** a proibição explícita impede que alguma IA use esses números como corte e descarte tudo. [Justificativa completa](index.html#timmons).
:::
:::

## Bloco 8 · Tom e linguagem

::: {.bloco}
::: {.bloco-prompt}
{{PROMPT:33-33}}
:::
::: {.bloco-just}
[Estrutura-base · apoio à leitura crítica]{.tag}

O tom didático pede que a resposta explique as fontes e os dados que levaram a cada oportunidade.

**Efeito esperado:** o raciocínio fica exposto, o que facilita a auditoria: um número explicado é mais fácil de rastrear e de conferir do que um número solto.
:::
:::

## Bloco 9 · Restrições absolutas

::: {.bloco}
::: {.bloco-prompt}
{{PROMPT:34-40}}
:::
::: {.bloco-just}
[Leitura crítica de dado (Aula 4) · Métrica de atenção × métrica de negócio (Aula 6)]{.tag}

**Leitura crítica de dado.** As três primeiras linhas tornam os dados verificáveis. Cada número precisa de fonte, ano, recorte geográfico e do que mede, com atenção aos dois erros prováveis neste recorte: dado nacional usado como se valesse para uma RA, e faturamento nominal lido como crescimento de vendas. A lista de fontes aceitas exclui notícia sem fonte original. Sem dado confiável, a IA deve escrever "SEM DADO" em vez de estimar.

**Métrica de atenção × métrica de negócio.** Em alimentação é comum justificar potencial pelo Instagram. A quarta linha proíbe esse argumento e só aceita receita, margem, ticket médio, frequência de compra ou clientes pagantes. Se alguma IA o usasse, seria registrado como achado.

**Efeito esperado:** números auditáveis e uma saída honesta para a falta de dado, em vez de invenção. [Justificativas completas](index.html#leitura-critica).
:::
:::

## Bloco 10 · Processo de pensamento crítico

::: {.bloco}
::: {.bloco-prompt}
{{PROMPT:42-50}}
:::
::: {.bloco-just}
[Tendência × oportunidade (Aula 4) · Leitura crítica de dado (Aula 4)]{.tag}

- **Passo 3:** a separação entre fatos, hipóteses e opiniões remete ao mesmo padrão de evidência das Restrições Absolutas.
- **Passo 4:** obriga a listar as tendências primeiro e só depois derivar delas as oportunidades. Nenhuma tendência pode aparecer como oportunidade.
- **Passo 5:** pede a data de corte do conhecimento e se a IA consultou a internet. Como o horizonte é 2026–2030 e os modelos têm data de corte, essa informação ajuda a explicar a divergência entre as respostas e entra no [protocolo](protocolo.html).

**Efeito esperado:** uma análise prévia visível, na tag `<analise_previa>`, que mostra as lacunas e as premissas antes da resposta final.
:::
:::

## Bloco 11 · Diretrizes da tarefa

::: {.bloco}
::: {.bloco-prompt}
{{PROMPT:52-60}}
:::
::: {.bloco-just}
[Checklist final de Dornelas (Aula 5)]{.tag}

Os itens 1 a 4 são estrutura-base: foco no objetivo, nada de achismo, riscos explícitos e respeito às restrições.

O **item 5** repete o filtro do bloco 6 como instrução de processo: aplicar o checklist a cada candidata antes de incluí-la e mostrar as descartadas.

**Efeito esperado:** o filtro deixa de ser só um critério e passa a ser um passo obrigatório, com rastro visível na seção de descartadas.
:::
:::

## Bloco 12 · Formato da resposta

::: {.bloco}
::: {.bloco-prompt}
{{PROMPT:62-67}}
:::
::: {.bloco-just}
[Tendência × oportunidade (Aula 4)]{.tag}

A seção 1 isola as tendências, limitadas a cinco linhas e declaradas como "não são oportunidades". Com isso, a confusão entre as duas, se acontecer, fica visível.
:::
:::

::: {.bloco}
::: {.bloco-prompt}
{{PROMPT:68-85}}
:::
::: {.bloco-just}
[Cinco perguntas (Aula 4) · 3Ms (Aula 5) · Modelo de negócio, modelos na web (Aula 6) · Checklist (Aula 5) · Leitura crítica (Aula 4)]{.tag}

Campos fixos, na mesma ordem, para que as três respostas fiquem comparáveis. Cada campo carrega um instrumento:

- **Cinco perguntas de triagem**, com a mesma redação: "Quem exatamente tem esse problema?", "Quanto dói?", "Por que você, e não o incumbente?", "Por que agora?"; e "quem paga, com que dinheiro" dentro do Modelo de negócio.
- **3Ms**: três campos identificados como 1º, 2º e 3º M; o 2º pede o tamanho na RA, e não no país.
- **Modelo de negócio**: quem paga, por quê e a que custo, dentro dos R\$ 500 mil.
- **Canal digital**: enquadramento nos cinco modelos na web, assinatura ou "não se aplica", com comissão e quem fica com o cliente.
- **Checklist de corte**: as cinco perguntas, cada uma com SIM e justificativa.
- **Evidências**: tabela com número, fonte, ano, recorte geográfico e o que mede.
:::
:::

::: {.bloco}
::: {.bloco-prompt}
{{PROMPT:87-94}}
:::
::: {.bloco-just}
[Checklist final de Dornelas (Aula 5)]{.tag}

A seção 3 mostra as descartadas, com a pergunta do checklist em que falharam: é onde se vê o filtro funcionando.

As seções 4 e 5 pedem riscos (incluindo os campos que ficaram SEM DADO) e próximos passos, começando pela oportunidade priorizada e por quê.
:::
:::

## Mapa dos instrumentos no prompt

::: {.tabela .larga}
| Instrumento | Aula | Onde entra no prompt |
|---|---|---|
| Tendência × oportunidade | 4 | Bloco 3 (definição de oportunidade), bloco 10 (passo 4), bloco 12 (seção 1 do formato) |
| Cinco perguntas de triagem | 4 | Bloco 12: campos fixos de cada oportunidade, com a mesma redação |
| Leitura crítica de dado de mercado | 4 | Bloco 9 (Restrições Absolutas) e campo Evidências do bloco 12 |
| Checklist final de Dornelas | 5 | Bloco 6 (critérios de corte), bloco 11 (item 5), bloco 12 (seções 2 e 3) |
| 3Ms | 5 | Bloco 12: campos 1º, 2º e 3º M |
| Critérios de alto e baixo potencial (em parte) | 5 | Bloco 7 (critérios de potencial, com proibição dos patamares numéricos) |
| Modelo de negócio | 6 | Bloco 12: campo Modelo de negócio |
| Cinco modelos de negócio na web | 6 | Bloco 12: campo Canal digital |
| Métrica de atenção × métrica de negócio | 6 | Bloco 9: uma linha das Restrições Absolutas |
:::

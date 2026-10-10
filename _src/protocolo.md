## Ferramentas e condições de uso

O mesmo prompt-mestre foi aplicado em três IAs generativas. As três respostas foram depois enviadas, juntas, a uma quarta IA, diferente das anteriores, encarregada apenas de sintetizá-las. Nas tabelas de auditoria, as origens aparecem como **A = Gemini**, **B = DeepSeek** e **C = ChatGPT**.

::: {.tabela .larga}
| | Ferramenta | Versão do modelo | Data e hora do teste | Busca na web | Plano |
|---|---|---|---|---|---|
| A | Gemini | [PREENCHER: versão] | [PREENCHER: data e hora] | [PREENCHER: ativada ou não] | [PREENCHER: gratuito ou pago] |
| B | DeepSeek | [PREENCHER: versão] | [PREENCHER: data e hora] | [PREENCHER: ativada ou não] | [PREENCHER: gratuito ou pago] |
| C | ChatGPT | [PREENCHER: versão] | [PREENCHER: data e hora] | [PREENCHER: ativada ou não] | [PREENCHER: gratuito ou pago] |
| 4ª | [PREENCHER: nome da quarta IA] | [PREENCHER: versão] | [PREENCHER: data e hora] | [PREENCHER: ativada ou não] | [PREENCHER: gratuito ou pago] |
:::

### Condições aplicadas às três IAs

- **Mesmo prompt, sem adaptação.** O texto da [página 2](prompt-mestre.html) foi colado igual nas três ferramentas, sem ajuste para nenhuma delas.
- **Primeira resposta.** Foi registrada a primeira resposta de cada IA, sem refinamento em conversa nem pedido de complemento.
- **Resposta na íntegra.** As três respostas foram copiadas inteiras para dentro do prompt de síntese e estão nos [anexos A, B e C](anexos.html), sem edição.
- **Conversa nova.** [PREENCHER: confirmar se cada teste foi feito em conversa nova, sem histórico nem instruções personalizadas]

### O que cada IA declarou sobre si

O passo 5 do processo de pensamento crítico pedia que cada IA informasse sua data de corte de conhecimento e se consultou a internet. As declarações abaixo são da própria resposta, e não verificação minha.

::: {.tabela .media}
| | Data de corte declarada | Uso de internet declarado | Onde declarou |
|---|---|---|---|
| A · Gemini | Não informada | "Não foi realizada busca ao vivo na internet para esta resposta"; diz basear-se em relatórios históricos do IBGE, IPEDF e ABIP | `<analise_previa>`, item 5 |
| B · DeepSeek | "Conhecimento até outubro de 2026" | "Consultei a internet para esta resposta" | `<analise_previa>`, item 5 |
| C · ChatGPT | "9 de outubro de 2026" | "Pesquisa na internet realizada" em 9 de outubro de 2026 | Linha de abertura e seção "Data de corte e fontes" (C não usou a tag `<analise_previa>`) |
:::

Esse campo ajuda a ler a divergência entre as respostas. A, que declarou não ter feito busca, aprovou duas oportunidades; B e C, que declararam ter pesquisado, chegaram a resultados opostos: B aprovou três e C, nenhuma. A busca na web não garantiu dado correto: na [verificação em fonte primária](auditoria-verificacao.html), os dados por RA de B e de C também têm edição, ano ou RA trocados.

### Observação sobre a resposta C

O texto do ChatGPT contém a linha "Pensou por 12s", resíduo da interface que veio junto com o texto copiado. Ela foi mantida no anexo, porque a regra é não editar as respostas, e foi registrada pela própria síntese na seção de conformidade.

## Prompt de síntese

A quarta IA recebeu um prompt próprio, que é o segundo artefato de engenharia de prompt deste trabalho. O texto completo, com o prompt-mestre e as três respostas coladas entre tags, tem cerca de 500 linhas e pode ser [baixado na íntegra em texto puro](assets/prompt-de-sintese.txt). Abaixo estão as instruções, sem cortes; só o material colado (prompt-mestre e respostas) foi recolhido, porque já aparece na [página 2](prompt-mestre.html) e nos [anexos](anexos.html).

### O problema que o prompt de síntese precisava resolver

Quando uma IA resume o que outras disseram, perde-se a pista de qual afirmação veio de onde e do que foi acrescentado no caminho. Cada regra do prompt de síntese ataca um modo de falha específico, e cada uma deixa um rastro que pode ser conferido depois, na auditoria.

::: {.tabela .larga}
| Exigência | Onde está | Modo de falha que ataca | Como confiro na auditoria |
|---|---|---|---|
| Papel restrito: sintetizador, não analista; não avalia, recomenda, completa nem corrige | PAPEL | IA que "melhora" o material e mistura opinião própria | Afirmações órfãs |
| Prompt-mestre entra só como referência de estrutura, com a ordem de não responder a ele | MATERIAL | IA que responde ao prompt-mestre em vez de sintetizar | Conteúdo sem origem em A, B ou C |
| Respostas delimitadas por tags com o nome de cada IA | MATERIAL | Perda da origem de cada trecho | Atribuição por origem |
| Nenhuma informação nova; erro na origem não se corrige, registra-se na seção 7 | Regra 1 | Acréscimo de informação durante a síntese | Afirmações órfãs |
| Atribuição obrigatória [A], [B], [C] em toda afirmação | Regra 2 | Rastreabilidade perdida | Tabela de rastreabilidade |
| Números intactos, com fonte e ano da origem; números diferentes mostrados lado a lado | Regra 3 | Distorção numérica, arredondamento, média | Distorção de número |
| Grau de certeza preservado: hipótese continua hipótese, "SEM DADO" continua "SEM DADO" | Regra 4 | "Pode" virar "vai"; estimativa virar fato | Distorção de certeza |
| Divergência não se resolve: posições lado a lado | Regra 5 | Síntese que busca consenso e apaga discordâncias | Afirmações suprimidas |
| Nada se perde por ser minoria; o exclusivo é marcado como tal | Regra 6 | Supressão do que só uma IA disse | Afirmações suprimidas |
| Sem juízo próprio; ordem por número de IAs que trouxeram a oportunidade, não por mérito | Regra 7 | Ranking disfarçado de síntese | Ordem da seção 2 |
| Critério de equivalência: mesmo cliente e mesmo problema; na dúvida, separar e explicar | Critério de equivalência | Fusão indevida de oportunidades diferentes | Mapa de convergência |
| Formato em 8 seções, com tabela de todos os números, lacunas e conformidade | Formato | Síntese em prosa, impossível de conferir | Tabelas da síntese |
| Declaração de integridade: listar o que não tem origem direta nas três | Seção 8 do formato | Órfãs escondidas | Confronto da declaração com as órfãs que encontrei |
:::

O critério de equivalência reaproveita a definição de oportunidade da Aula 4: se uma oportunidade é um problema concreto de um cliente identificável, duas oportunidades são a mesma quando têm o mesmo cliente e o mesmo problema, ainda que com nomes ou RAs diferentes. A [auditoria de rastreabilidade](auditoria-rastreabilidade.html) mostra o efeito colateral desse critério estrito.

### Texto das instruções

{{PROMPT:1-6}}

::: {.caixa}
**Material colado entre as instruções** (linhas 7 a 478 do arquivo), sem edição:

- `<prompt_mestre>` … `</prompt_mestre>`: o prompt-mestre completo da [página 2](prompt-mestre.html).
- `<resposta_GEMINI>` … `</resposta_GEMINI>`: a resposta do [Anexo A](anexo-a-gemini.html).
- `<resposta_DEEPSEEK>` … `</resposta_DEEPSEEK>`: a resposta do [Anexo B](anexo-b-deepseek.html).
- `<resposta_CHATGPT>` … `</resposta_CHATGPT>`: a resposta do [Anexo C](anexo-c-chatgpt.html).
:::

{{PROMPT:480-516}}

A saída da quarta IA está no [Anexo D](anexo-d-sintese.html), na íntegra.

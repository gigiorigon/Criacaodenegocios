<p class="lede">Das 16 afirmações auditadas, 7 se sustentam, 4 foram distorcidas, 2 são órfãs e 3 conteúdos relevantes foram suprimidos. As quatro distorções são de grau de certeza ou de sentido, não de número: um "pode" ou um "deve" que sumiu. O que se perdeu foram justamente as ressalvas que as próprias IAs fizeram sobre suas melhores oportunidades.</p>

::: {.numeros}
::: {.ok}
7

sustentadas
:::
::: {.warn}
4

distorcidas (certeza ou sentido)
:::
::: {.bad}
2

órfãs
:::
::: {.info}
3

suprimidas
:::
:::

## Como classifiquei

Peguei as afirmações relevantes da síntese e localizei cada uma nas três respostas originais ([anexos A, B e C](anexos.html)). Cada afirmação recebeu uma de quatro classificações:

- <span class="selo ok">Sustentada</span> aparece em uma ou mais das três respostas, sem distorção.
- <span class="selo warn">Distorcida</span> existe na origem, mas mudou de sentido, de número ou de grau de certeza no caminho.
- <span class="selo bad">Órfã</span> não aparece em nenhuma das três: a quarta IA a produziu sozinha, numa tarefa em que não deveria produzir nada novo.
- <span class="selo info">Suprimida</span> estava em uma das três, era relevante e desapareceu da síntese.

As linhas 14 a 16 não têm afirmação da síntese para citar: registram o que faltou nela. A síntese completa está no [Anexo D](anexo-d-sintese.html).

## Tabela de rastreabilidade

A = Gemini, B = DeepSeek, C = ChatGPT.

::: {.tabela .larga}
| \#  | Afirmação da síntese                                                                                                                                                      | Onde aparece | Fidelidade               | Comentário                                                                                                                                                                                                                                                                                                                          |
|-----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1   | Só a oportunidade sem glúten se repete entre IAs; as demais aparecem em uma única resposta (seção 1)                                                                      | A, B         | <span class="selo ok">Sustentada</span> | Correta pelo critério do prompt (mesmo cliente e mesmo problema). Efeito colateral: o critério partiu em três linhas isoladas a produção central para revenda, tema que as três tocam (A aprova, B aprova, C prioriza para teste). O mapa sugere menos convergência do que existe; só a tabela de divergências mostra o tema comum. |
| 2   | Prevalência de doença celíaca: 1% a 2% (FENACELBRA, 2021, Brasil) em A; 1 a cada 681 (Correio Braziliense/UnB, 2023, DF) em B                                             | A, B         | <span class="selo ok">Sustentada</span> | Números, fontes e recortes intactos; divergência mantida lado a lado. A conferência na fonte primária está em 5.2.                                                                                                                                                                                                                  |
| 3   | Padaria convencional não consegue evitar contaminação cruzada, e só uma instalação exclusiva atende esse cliente \[A, B\]                                                 | A, B         | <span class="selo warn">Distorcida</span> (certeza) | A é absoluta ("apenas uma instalação que nasce 100% estéril"). B diz que "a maioria das padarias" não tem estrutura. Ao fundir as duas numa convergência, a síntese elevou a certeza de B.                                                                                                                                          |
| 4   | "Operação gerida por gerente de operações" (condomínios) e "gestão por gerente de operações" (café da manhã) \[B\]                                                        | B            | <span class="selo warn">Distorcida</span> (certeza) | B escreveu "pode ser gerida" e "pode ser gerido". A síntese transformou possibilidade em fato. No sem glúten o "pode" foi mantido, o que mostra a inconsistência.                                                                                                                                                                   |
| 5   | Crescimento do mercado brasileiro sem glúten de 7,2% ao ano até 2033 \[B\] (seção 2)                                                                                      | B            | <span class="selo warn">Distorcida</span> (leve) | B escreveu "deve crescer". A seção 2 tirou o marcador de projeção; a seção 4 da própria síntese registra o número corretamente como projeção.                                                                                                                                                                                       |
| 6   | Os R\$ 500 mil vão para fornos, utilitários leves e um galpão de baixo custo no Guará \[A\]                                                                               | A            | <span class="selo warn">Distorcida</span> (sentido) | A aloca o capital em fornos e utilitários "em um galpão de baixo custo": o galpão é a localização, não um item do investimento. A síntese o pôs na lista de gastos.                                                                                                                                                                 |
| 7   | As duas usam médicos como canal de indicação \[A, B\]                                                                                                                     | A, B         | <span class="selo ok">Sustentada</span> com ressalva | A cita gastropediatras e nutricionistas; B cita médicos. O núcleo (indicação por profissional de saúde) converge, mas "médicos" estreita o que A disse.                                                                                                                                                                             |
| 8   | Recuperação do custo de captação no B2B: duas primeiras semanas (A), primeiro contrato (B), SEM DADO (C)                                                                  | A, B, C      | <span class="selo ok">Sustentada</span> | Três posições lado a lado, sem meio-termo.                                                                                                                                                                                                                                                                                          |
| 9   | Taguatinga: "renda média-baixa" (Codeplan, 2024) em B; renda domiciliar média de R\$ 5.425 (sem ano) em C                                                                 | B, C         | <span class="selo ok">Sustentada</span> | Divergência preservada sem desempate. A checagem em 5.2 mostra qual das duas a fonte primária apoia.                                                                                                                                                                                                                                |
| 10  | C recomenda não abrir padaria agora e testar B2B em Ceilândia como investigação, não como oportunidade validada                                                           | C            | <span class="selo ok">Sustentada</span> | Fiel ao texto e ao grau de certeza de C.                                                                                                                                                                                                                                                                                            |
| 11  | Mão de obra qualificada escassa \[A, B\]                                                                                                                                  | A, B         | <span class="selo ok">Sustentada</span> | A fala em "apagão de mão de obra técnica"; B, em dificuldade de achar mão de obra qualificada. C não trata.                                                                                                                                                                                                                         |
| 12  | Nenhuma das três apresentou tendência como oportunidade \[A, B, C\] (seção 7)                                                                                             | Nenhuma      | <span class="selo bad">Órfã</span> e contestável | Juízo da síntese, exigido pelo formato, mas discutível. A oportunidade de café da manhã de B reescreve sua tendência (iv), "expansão de refeições dentro das padarias", sem cliente nomeável nem dado de demanda. B também responde (e) do sem glúten com "mercado em crescimento", que é tendência.                                |
| 13  | Cafeterias (A), condomínios (B) e congelados (C) são oportunidades distintas (seção 1)                                                                                    | Nenhuma      | <span class="selo bad">Órfã</span> (declarada) | Decisão da síntese, aplicando o critério do prompt, e declarada na seção 8. Legítima, mas é a causa do efeito descrito na linha 1.                                                                                                                                                                                                  |
| 14  | (Ausente na síntese) "É hipótese que os donos de cafeterias terceirizam por vontade e não por contingência"                                                               | A            | <span class="selo info">Suprimida</span> | Estava na análise prévia de A e é a fragilidade central da Oportunidade 1 de A. A síntese levou o checklist de A com SIM nas cinco e perdeu a ressalva que a própria A fez.                                                                                                                                                         |
| 15  | (Ausente na síntese) Hipóteses de B: "que o café da manhã é um diferencial competitivo" e "que há demanda reprimida por produtos sem glúten"                              | B            | <span class="selo info">Suprimida</span> | B rotulou como hipótese o diferencial da sua Op. 3 e a demanda da Op. 2. A síntese registrou só as premissas frágeis da seção 4 de B; o café da manhã aparece com SIM nas cinco e sem a ressalva.                                                                                                                                   |
| 16  | (Ausente na síntese) "Critério final de decisão" de C, com a evidência mínima para cada pergunta do checklist, e o aviso de que interesse verbal não é demanda comprovada | C            | <span class="selo info">Suprimida</span> | Aparece só como "seção fora do formato" na conformidade. Sumiu o conteúdo que define o que contaria como SIM, que é a contribuição metodológica mais útil de C.                                                                                                                                                                     |
:::

Os números da tabela 4 da síntese foram reconferidos contra as três respostas e nenhum foi alterado. O problema da síntese não está nos dados, e sim no tom: ela preservou as divergências explícitas, mas apagou dúvidas que as IAs tinham sobre si mesmas.

::: {.caixa}
**Onde a síntese errou e onde acertou.** As regras de números intactos (regra 3) e de divergência lado a lado (regra 5) funcionaram: nenhum número da tabela 4 da síntese foi alterado, e as divergências explícitas foram preservadas sem desempate (linhas 2, 8 e 9). A regra de grau de certeza (regra 4) foi a mais violada: três das quatro distorções são de certeza (linhas 3 a 5) e a quarta, de sentido (linha 6). As duas órfãs nasceram onde o próprio prompt de síntese pedia uma decisão (critério de equivalência e seção de conformidade), e as três supressões atingiram ressalvas que as IAs fizeram sobre si mesmas.
:::

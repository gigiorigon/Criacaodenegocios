<p class="lede">Das sete afirmações checadas, uma se confirmou, duas têm o número certo com fonte ou edição errada, e quatro não se confirmaram. Os erros aparecem nas três IAs e se concentram nos dados por RA, justamente os que o prompt-mestre exigia para justificar a escolha do local. A síntese reproduziu esses números com fidelidade, como mandava a regra; fidelidade à origem não protege de erro na origem.</p>

::: {.numeros}
::: {.ok}
1

confirmada por inteiro
:::
::: {.warn}
2

número certo, com fonte ou edição errada
:::
::: {.bad}
4

não confirmadas
:::
:::

## Método

Escolhi sete afirmações factuais relevantes do conjunto, priorizando as que sustentam a escolha da RA e o "por que agora" das oportunidades aprovadas, e confrontei cada uma com fonte primária ou institucional: IPEDF/Codeplan (PDAD), Anvisa, literatura clínica indexada e a divulgação dos dados setoriais pela Agência Brasil. Para cada uma, registro se confirmou, não confirmou ou confirmou só em parte, e a referência completa. Quando a fonte não abriu por inteiro, isso está dito na própria linha. A letra entre parênteses indica a IA de origem (A = Gemini, B = DeepSeek, C = ChatGPT).

## Tabela de verificação

::: {.tabela .larga}
| \#  | Afirmação (origem)                                                                                                                       | Resultado                                       | O que a fonte mostra                                                                                                                                                                                                                                                                                                                                                                                                                      | Referência                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-----|------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1   | Faturamento da panificação de R\$ 153,3 bi em 2024 (+10,9%) e fluxo de clientes +4,57% em 2024 (B)                                       | <span class="selo ok">Confirmado</span> | Números e ano batem. O dado de faturamento é do Instituto Ideal e foi divulgado com a ABIP; B não nomeou fonte. Um veículo que reproduziu a notícia atribuiu os 4,57% a 2023, mas o texto da Agência Brasil fala no ano anterior à publicação (abr/2025). Verificado em agência pública que cita a fonte original; o relatório do Ideal não foi aberto.                                                                                   | Agência Brasil (EBC), "Faturamento do setor de panificação cresce 11% em 2024", abr/2025 ([reprodução](https://www.acessa.com/economia/2025/04/237002-faturamento-do-setor-de-panificacao-cresce-11-em-2024.html))                                                                                                                                                                                                                                           |
| 2   | Crescimento setorial superior a 10% no ano, ABIP, 2023 (A)                                                                               | <span class="selo bad">Não confirmado</span> | Segundo a ABIP, o crescimento de 2024 foi quase quatro vezes maior que o de 2023. Os mais de 10% são de 2024; 2023 ficou bem abaixo disso. A trocou o ano.                                                                                                                                                                                                                                                                                | Mesma reportagem da linha 1                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 3   | Prevalência de doença celíaca de 1 a cada 681 no DF (Correio Braziliense/UnB, 2023) (B)                                                  | <span class="selo warn">Parcial</span> número confirmado; fonte, ano e recorte errados | O número vem de estudo da UnB publicado em 2000: 2.045 doadores de sangue do Hemocentro de Brasília, medindo doença celíaca não diagnosticada. Não é de 2023 nem é prevalência da população do DF. Outros estudos brasileiros com doadores acharam de 1:214 a 1:417; o de Brasília é a menor estimativa.                                                                                                                                  | Gandolfi L, Pratesi R, Cordoba JC et al. Prevalence of celiac disease among blood donors in Brazil. Am J Gastroenterol. 2000;95(3):689-92 ([BVS](https://busqueda.bvsalud.org/portal/resource/pt/mdl-10710058)); faixa nacional em São Paulo Med J ([SciELO](https://scielo.br/j/spmj/a/kCtzc7HW3g9zd5YyvvhXzth/?lang=en))                                                                                                                                   |
| 4   | Águas Claras tem 120.107 habitantes (PDAD-A 2024) (B)                                                                                    | <span class="selo warn">Parcial</span> número confirmado; edição errada | 120.107 é a população urbana da PDAD 2021 (Codeplan, publicada em 06/07/2022), com renda domiciliar média de R\$ 14.056,73; nessa edição Águas Claras está no grupo de renda alta. Na cobertura da PDAD-A 2024, a RA aparece com 141.872 moradores (dado secundário).                                                                                                                                                                     | Codeplan, PDAD 2021 – UPT Central Adjacente 2 ([PDF](https://www.ipe.df.gov.br/documents/9915964/10216206/PDAD_2021-Apresentacao_Central_Adj_II.pdf)); PDAD 2021 – DF, grupos de renda ([PDF](https://ipe.df.gov.br/documents/d/ipedf/apresentacao_pdad-df_2021-pdf)); Jornal de Brasília sobre a PDAD-A 2024 ([link](https://jornaldebrasilia.com.br/brasilia/ceilandia-continua-sendo-a-cidade-com-maior-numero-de-moradores-segundo-nova-pdad-ampliada/)) |
| 5   | Renda per capita de R\$ 11.603,22 no Sudoeste/Octogonal e de R\$ 959,90 em Planaltina (PDAD-A 2024) (B)                                  | <span class="selo bad">Não confirmado</span> | O Informe Distrital de Rendimentos da PDAD-A 2024 diz que o cálculo para Sudoeste e Octogonal não teve significância estatística. Na cobertura do informe, R\$ 11.603,22 é o per capita do Lago Norte e R\$ 959,90, o da Fercal. Tudo indica que B atribuiu números reais às RAs erradas. O PDF do informe não abriu por inteiro: a nota de significância foi lida no trecho indexado do próprio PDF, e a atribuição por RA, na imprensa. | IPEDF, Informe Distrital de Rendimentos, PDAD-A 2024, jan/2026 ([PDF](https://agenciabrasilia.df.gov.br/documents/d/guest/2026-01-16_informe-distrital-de-rendimentos-pdf)); Correio da Manhã, 27/01/2026 ([PDF](https://digital.correiodamanha.com.br/jornalcorreiodamanha/2026/01/27/2150d9/pdf/2701df_cmanha20.pdf))                                                                                                                                      |
| 6   | Taguatinga é RA de "renda média-baixa" (Codeplan, 2024) (B); Taguatinga tem 205.689 habitantes e renda domiciliar média de R\$ 5.425 (C) | <span class="selo bad">Não confirmado</span> (as duas) | Na PDAD 2021, Taguatinga está no grupo de renda média-alta, com 210.498 moradores e renda domiciliar média de R\$ 5.816,33. Os números de C não batem com a PDAD 2021 em nenhuma RA da sua tabela (Ceilândia 350.347; Samambaia 247.629; Brazlândia 55.879) nem com a cobertura da PDAD-A 2024. A edição usada por C não pôde ser identificada.                                                                                           | Codeplan, PDAD 2021 – UPT Oeste ([PDF](https://www.ipe.df.gov.br/documents/9915964/10216206/PDAD_2021-Apresentacao_Oeste.pdf)); PDAD 2021 – DF ([PDF](https://ipe.df.gov.br/documents/d/ipedf/apresentacao_pdad-df_2021-pdf))                                                                                                                                                                                                                                |
| 7   | A Anvisa endureceu a rotulagem de alérgenos com a RDC 727/2022 (A)                                                                       | <span class="selo bad">Não confirmado</span> | A RDC 727/2022 existe e exige declarar alérgenos, inclusive por contaminação cruzada. Mas, segundo a própria Anvisa, ela consolidou a RDC 26/2015 "sem alteração de mérito": não houve endurecimento em 2022. Dado novo que nenhuma IA trouxe: em 2025 a Anvisa abriu processo próprio para as alegações "contém" e "não contém glúten", porque a comunidade celíaca defende limites mais restritivos que os do Codex.                    | Anvisa, RDC nº 727/2022 ([PDF](https://antigo.anvisa.gov.br/documents/10181/6503668/(1)RDC_727_2022_COMP.pdf/8167fbac-395a-4189-ab43-024e4d3aa667)); Anvisa, Voto nº 154/2025/SEI/DIRE2 ([PDF](https://www.gov.br/anvisa/pt-br/composicao/diretoria-colegiada/reunioes-da-diretoria/votos/2025/rop-10.2025/2-6.pdf/@@display-file/file))                                                                                                                     |
:::

A FENACELBRA (1% a 2% da população, citada por A) não foi verificada; a literatura clínica consultada fala em média de cerca de 1% na Europa e nos EUA.

## Fontes consultadas

Abertas por inteiro: PDAD 2021 – UPT Oeste e Voto Anvisa nº 154/2025. As demais foram lidas no trecho indexado pela busca; o informe de rendimentos da PDAD-A 2024 não abriu.

- Agência Brasil (EBC), "Faturamento do setor de panificação cresce 11% em 2024", abr/2025 — [reprodução em acessa.com](https://www.acessa.com/economia/2025/04/237002-faturamento-do-setor-de-panificacao-cresce-11-em-2024.html)

- Gandolfi L et al., Am J Gastroenterol 2000;95(3):689-92 — [BVS](https://busqueda.bvsalud.org/portal/resource/pt/mdl-10710058)

- São Paulo Medical Journal, prevalência em doadores no Brasil — [SciELO](https://scielo.br/j/spmj/a/kCtzc7HW3g9zd5YyvvhXzth/?lang=en)

- Codeplan, PDAD 2021 – UPT Central Adjacente 2 — [PDF](https://www.ipe.df.gov.br/documents/9915964/10216206/PDAD_2021-Apresentacao_Central_Adj_II.pdf)

- Codeplan, PDAD 2021 – UPT Oeste — [PDF](https://www.ipe.df.gov.br/documents/9915964/10216206/PDAD_2021-Apresentacao_Oeste.pdf)

- Codeplan, PDAD 2021 – Distrito Federal (grupos de renda) — [PDF](https://ipe.df.gov.br/documents/d/ipedf/apresentacao_pdad-df_2021-pdf)

- IPEDF, apresentação da PDAD-A 2024 (população do DF) — [PDF](https://seduh.df.gov.br/documents/d/seduh/226a-ro_3-apresentacao-pdad_ipedf-pdf)

- IPEDF, Informe Distrital de Rendimentos, PDAD-A 2024 — [PDF](https://agenciabrasilia.df.gov.br/documents/d/guest/2026-01-16_informe-distrital-de-rendimentos-pdf)

- Correio da Manhã, cobertura do informe de rendimentos, 27/01/2026 — [PDF](https://digital.correiodamanha.com.br/jornalcorreiodamanha/2026/01/27/2150d9/pdf/2701df_cmanha20.pdf)

- Jornal de Brasília, população por RA na PDAD-A 2024 — [link](https://jornaldebrasilia.com.br/brasilia/ceilandia-continua-sendo-a-cidade-com-maior-numero-de-moradores-segundo-nova-pdad-ampliada/)

- Anvisa, RDC nº 727/2022 — [PDF](https://antigo.anvisa.gov.br/documents/10181/6503668/(1)RDC_727_2022_COMP.pdf/8167fbac-395a-4189-ab43-024e4d3aa667)

- Anvisa, Voto nº 154/2025/SEI/DIRE2 — [PDF](https://www.gov.br/anvisa/pt-br/composicao/diretoria-colegiada/reunioes-da-diretoria/votos/2025/rop-10.2025/2-6.pdf/@@display-file/file)

- Sou Brasília, "Pão Box leva padaria a minimercados de prédios", 20/07/2026 — [link](https://soubrasilia.com/?p=8817)

- Atly, diretório colaborativo de locais sem glúten — [link](https://atly.com/best/gluten-free/allergen-friendly-brazil)

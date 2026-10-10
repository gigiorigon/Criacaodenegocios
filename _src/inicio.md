::: {.ident}
<p><span>Aluno</span><strong>Giovani Machado Rigon</strong></p>
<p><span>Matrícula</span><strong>16/0070686</strong></p>
<p><span>Disciplina</span><strong>Criação de Negócios (ADM0150)</strong></p>
<p><span>Semestre</span><strong>2026/2</strong></p>
:::

Universidade de Brasília · Faculdade de Economia, Administração, Contabilidade e Gestão de Políticas Públicas · Departamento de Administração · Atividade 2, estudo de caso individual.

## Objetivo do estudo

Este estudo testa um método de detecção de oportunidades de negócio em que quatro inteligências artificiais trabalham em cadeia, e examina onde essa cadeia falha.

O recorte é o mercado de **panificação (padarias) no Distrito Federal**, em regiões administrativas no entorno do Plano Piloto com custo de operação menor, para um negócio de pequeno ou médio porte, com capital de até **R\$ 500 mil** e abertura entre **2026 e 2030**.

O caminho seguido tem quatro passos:

1. **Prompt-mestre.** Escrevi um único prompt que carrega os instrumentos de avaliação de oportunidade das Aulas 4, 5 e 6 ([página 2](prompt-mestre.html)).
2. **Três IAs.** Enviei o mesmo prompt, sem adaptação, ao Gemini, ao DeepSeek e ao ChatGPT ([página 3](protocolo.html)).
3. **Quarta IA.** Submeti as três respostas a uma quarta IA, encarregada apenas de sintetizá-las, com um prompt de síntese próprio ([página 3](protocolo.html#prompt-de-síntese)).
4. **Auditoria.** Tratei a síntese como objeto de investigação: rastreei suas afirmações até as respostas originais, confrontei dados com fontes primárias e apliquei a régua por conta própria ([páginas 4.1 a 4.3](auditoria-rastreabilidade.html)).

## Resultado em uma frase

::: {.caixa .destaque}
A síntese manteve os números, mas perdeu as dúvidas: das 16 afirmações auditadas, 4 foram distorcidas em certeza ou sentido, 2 são órfãs e 3 ressalvas das próprias IAs sumiram. Na fonte primária, só 1 de 7 afirmações se confirmou por inteiro, e os dados por RA das três IAs têm edição, ano ou RA trocados. Pela régua das Aulas 5 e 6, nenhuma oportunidade passa nas cinco perguntas hoje; a única que eu defenderia é a panificação sem glúten dedicada, vendida primeiro a cafeterias e restaurantes.
:::

## A régua analítica

Antes de escrever o prompt, selecionei os instrumentos das Aulas 4, 5 e 6 que ele deveria carregar. Usei os nove instrumentos disponíveis; de um deles, os critérios de alto e baixo potencial, aproveitei só uma parte.

::: {.tabela .media}
| Aula | Instrumento | Uso | Por que entrou |
|------|-------------|-----|----------------|
| 4 | Tendência × oportunidade | <span class="selo ok">Usado</span> | Em ramo tradicional e concorrido, sem essa distinção as três IAs devolveriam a mesma resposta genérica ("abra uma padaria artesanal"); exigir cliente nomeável força o específico. |
| 4 | Cinco perguntas de triagem | <span class="selo ok">Usado</span> | O maior risco em ramo tradicional é entrar num mercado saturado sem diferencial, e a quarta pergunta ataca isso; respondidas uma a uma, impedem que a oportunidade seja só descrita. |
| 4 | Leitura crítica de dado de mercado | <span class="selo ok">Usado</span> | Torna verificáveis os dados que o prompt exige e previne dois erros prováveis: dado nacional usado como se valesse para a RA e faturamento nominal lido como volume. |
| 5 | Checklist final (Dornelas) | <span class="selo ok">Filtro de corte</span> | Por ser binário, funciona como corte e deixa as três respostas comparáveis; é também o teste que aplico às finalistas na análise própria. |
| 5 | 3Ms | <span class="selo ok">Usado</span> | Com capital de R\$ 500 mil, margem e tempo até o equilíbrio decidem se a padaria se sustenta; o 2º M obriga a olhar a concorrência da RA, e não do país. |
| 5 | Critérios de alto e baixo potencial (Timmons) | <span class="selo warn">Em parte</span> | Os critérios de lógica valem para qualquer negócio; os patamares numéricos vêm do capital de risco e reprovariam qualquer padaria saudável. |
| 6 | Modelo de negócio | <span class="selo ok">Usado</span> | Em padaria, quem paga muda conforme a oportunidade (balcão, café ou hotel, órgão público), e cada caso tem custo, ticket e prazo de recebimento diferentes. |
| 6 | Cinco modelos de negócio na web | <span class="selo ok">Usado, em um campo</span> | O canal digital da padaria costuma ser do modelo empresarial; vender em plataforma alheia custa comissão e o cliente fica com ela. Incluí a assinatura. |
| 6 | Métrica de atenção × métrica de negócio | <span class="selo ok">Usado</span> | Em alimentação é comum justificar potencial pelo Instagram; o prompt só aceita receita, margem, ticket médio, frequência de compra ou clientes pagantes. |
:::

### O que ficou de fora

Só um elemento ficou de fora: **os patamares numéricos dos critérios de alto e baixo potencial** (crescimento de 30% a 50% ao ano e ponto de equilíbrio em menos de dois anos). Eles vêm do capital de risco e foram pensados para startups de crescimento acelerado. Panificação é um mercado maduro, que cresce bem abaixo disso; aplicados aqui, reprovariam qualquer padaria, inclusive uma perfeitamente saudável. O prompt proíbe expressamente seu uso como corte.

### Justificativa completa de cada instrumento

Clique em cada instrumento para ver o que ele é, por que o usei e em que trecho do prompt ele entra. A correspondência com o texto do prompt está, bloco a bloco, na [página do prompt-mestre](prompt-mestre.html).

#### Aula 4 · Oportunidades no mercado brasileiro

<details class="instr" id="tendencia">
<summary>Tendência × oportunidade <small>usado</small></summary>
<div>

**O que é.** Tendência é uma direção geral do mercado, conhecida por todos e sem dono, como "cresce o consumo de pão artesanal". Oportunidade é um problema concreto de um cliente identificável, que ele pagaria para resolver e que o negócio resolve melhor do que quem já o atende.

**Por que usei.** Padaria é um ramo tradicional, com demanda conhecida e muita concorrência. Sem essa distinção, a tendência acaba apresentada como se fosse oportunidade, e as três IAs devolveriam a mesma resposta genérica: "abra uma padaria artesanal". Exigir um cliente nomeável força cada resposta a sair do geral para o específico.

**Onde entra.** Na variável "Definição de oportunidade", no passo 4 do processo de pensamento crítico e na seção 1 do formato, que separa as tendências das oportunidades.

</div>
</details>

<details class="instr" id="cinco-perguntas">
<summary>Cinco perguntas de triagem <small>usado</small></summary>
<div>

**O que é.** Cinco perguntas para testar qualquer ideia:

1. Quem exatamente tem o problema?
2. Quanto ele dói?
3. Quem paga, e com que dinheiro?
4. Por que você, e não o concorrente já estabelecido?
5. Por que agora?

**Por que usei.** Em ramo tradicional, o maior risco é entrar num mercado saturado sem nada que diferencie o negócio, e a quarta pergunta ataca isso diretamente. Respondidas uma a uma, as perguntas também impedem que a oportunidade seja apenas descrita.

**Onde entra.** Cada pergunta virou um campo fixo de cada oportunidade, com a mesma redação.

</div>
</details>

<details class="instr" id="leitura-critica">
<summary>Leitura crítica de dado de mercado <small>usado</small></summary>
<div>

**O que é.** O hábito de perguntar, diante de qualquer número, de onde ele veio, de quando é e o que exatamente mede.

**Por que usei.** O prompt pede dados reais, e esse critério os torna verificáveis. Neste recorte há dois erros prováveis:

- usar um dado nacional da panificação como se valesse para uma região administrativa específica do DF;
- ler crescimento de faturamento em reais como crescimento de vendas, sem descontar a inflação.

Incluí também uma saída para quando não houver dado confiável: a IA deve escrever "SEM DADO" em vez de estimar.

**Onde entra.** Nas Restrições Absolutas e no campo Evidências, cuja tabela exige fonte, ano, recorte geográfico e o que o número mede.

</div>
</details>

#### Aula 5 · Identificando oportunidades (Dornelas, cap. 3)

<details class="instr" id="checklist">
<summary>Checklist final <small>usado como filtro de corte</small></summary>
<div>

**O que é.** Cinco perguntas de sim ou não:

1. Existe um problema a resolver?
2. Existe produto ou serviço que o resolva?
3. Os clientes são identificáveis com clareza?
4. Há estratégia de vendas viável em custo e retorno?
5. A janela da oportunidade está aberta?

**Por que usei.** É o critério de corte do prompt. A oportunidade que falha em qualquer pergunta não entra. Por ser binário, deixa as três respostas comparáveis. É também o teste que aplico, por conta própria, às oportunidades finalistas na análise deste trabalho. A lista de descartadas permite ver o filtro funcionando.

**Onde entra.** Na variável "Critérios de corte", no item 5 das diretrizes e nas seções 2 e 3 do formato.

</div>
</details>

<details class="instr" id="3ms">
<summary>3Ms <small>usado</small></summary>
<div>

**O que é.** Roteiro de análise em três etapas:

1. Demanda de mercado: quem é o cliente e como alcançá-lo.
2. Tamanho e estrutura do mercado: tamanho, crescimento, concorrentes e barreiras de entrada.
3. Análise de margem: quanto sobra de cada venda e quando o negócio se paga.

**Por que usei.** Com capital limitado a R\$ 500 mil para ponto comercial, reforma e equipamentos, a margem e o tempo até o ponto de equilíbrio decidem se a padaria se sustenta. A etapa de tamanho e estrutura obriga a olhar a concorrência na região escolhida, e não no país.

**Onde entra.** Em três campos de cada oportunidade, identificados como 1º, 2º e 3º M.

</div>
</details>

<details class="instr" id="timmons">
<summary>Critérios de alto e baixo potencial <small>usado em parte</small></summary>
<div>

**O que é.** Tabela adaptada de Jeffry Timmons que separa oportunidades de alto e baixo potencial. Combina dois tipos de critério:

- De lógica: cliente identificado, concorrência ainda não consolidada, barreiras de entrada e capital necessário.
- Patamares numéricos: crescimento de 30% a 50% ao ano e ponto de equilíbrio em menos de dois anos.

**Por que usei só uma parte.** Os patamares numéricos vêm do capital de risco e foram pensados para startups de crescimento acelerado. Panificação é um mercado maduro, que cresce bem abaixo disso. Aplicados aqui, reprovariam qualquer padaria, inclusive uma perfeitamente saudável. Mantive os critérios de lógica, que valem para qualquer negócio. Os patamares numéricos são o único elemento que deixei de fora, e o prompt proíbe expressamente seu uso como corte.

**Onde entra.** Na variável "Critérios de potencial".

</div>
</details>

#### Aula 6 · Oportunidades na internet (Dornelas, cap. 4)

<details class="instr" id="modelo-negocio">
<summary>Modelo de negócio <small>usado</small></summary>
<div>

**O que é.** A descrição de como a empresa gera receita e de quais custos e investimentos isso exige.

**Por que usei.** Em padaria, quem paga muda conforme a oportunidade. Pode ser o consumidor no balcão, um café ou hotel que compra para revender (venda entre empresas, ou B2B) ou um órgão público por contrato. Cada caso tem custo, ticket e prazo de recebimento diferentes. Exigir quem paga, por quê e a que custo impede que a oportunidade fique só na ideia.

**Onde entra.** Campo próprio em cada oportunidade.

</div>
</details>

<details class="instr" id="modelos-web">
<summary>Cinco modelos de negócio na web <small>usado, em um único campo</small></summary>
<div>

**O que é.** Classificação das formas de ganhar dinheiro na internet: intermediação, propaganda, mercado virtual, empresarial e redes sociais. No modelo empresarial, um negócio do mundo físico usa a internet para vender mais ou gastar menos, como o restaurante que entra num aplicativo de entrega ou a pequena empresa que vende pelo WhatsApp.

**Por que usei.** Padaria é negócio físico, mas quase sempre tem canal digital, e esse canal costuma ser do modelo empresarial. Vender dentro da plataforma de outra empresa tem dois custos: a comissão sobre cada pedido e o fato de o cliente pertencer à plataforma, não à loja. Por isso o campo pede a comissão e quem fica com o cliente. Incluí também a assinatura como opção, por exemplo entrega recorrente de pão ou café da manhã, por ser um modelo que a classificação original não previa.

**Onde entra.** No campo "Canal digital", que aceita "não se aplica" quando não houver componente digital.

</div>
</details>

<details class="instr" id="metrica">
<summary>Métrica de atenção × métrica de negócio <small>usado</small></summary>
<div>

**O que é.** A diferença entre medir atenção (visitas, seguidores, curtidas) e medir negócio (receita, custo, lucro). A atenção só importa quando se converte em receita.

**Por que usei.** Em alimentação é comum justificar o potencial de um negócio pelo sucesso no Instagram. O prompt proíbe esse argumento e só aceita receita, margem, ticket médio, frequência de compra ou clientes pagantes. Se alguma IA usar o argumento mesmo assim, isso será registrado como achado na auditoria.

**Onde entra.** Em uma linha das Restrições Absolutas.

</div>
</details>

## Como navegar

- **[2. Prompt-mestre](prompt-mestre.html):** o prompt na íntegra, com a justificativa ao lado de cada bloco.
- **[3. Protocolo de teste](protocolo.html):** ferramentas, versões, datas, condições de uso e o prompt de síntese.
- **4. Síntese auditada:** [4.1 Rastreabilidade](auditoria-rastreabilidade.html) · [4.2 Verificação em fonte primária](auditoria-verificacao.html) · [4.3 Aplicação da régua](auditoria-regua.html).
- **[5. Conclusão](conclusao.html):** a oportunidade que defendo e o que aprendi sobre encadear IAs.
- **[Anexos](anexos.html):** as quatro respostas completas, sem edição, também em PDF.

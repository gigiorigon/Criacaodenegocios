#!/usr/bin/env python3
"""Gera as páginas HTML do site a partir dos arquivos em _src/.

Uso (na raiz do repositório):  python3 _src/build.py
Requer pandoc. Os anexos de IA são reproduzidos como texto puro, sem edição.
"""
import html
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "_src"
PROMPT_FILE = ROOT / "assets" / "prompt-de-sintese.txt"
PROMPT_LINES = PROMPT_FILE.read_text(encoding="utf-8").splitlines()

ALUNO = {
    "nome": "Giovani Machado Rigon",
    "matricula": "16/0070686",
    "disciplina": "Criação de Negócios (ADM0150)",
    "semestre": "2026/2",
}

# (arquivo de saída, fonte, título curto do menu, título da página, grupo)
PAGES = [
    ("index.html", "inicio.md", "Abertura", "Abertura e régua analítica", "main"),
    ("prompt-mestre.html", "prompt-mestre.md", "Prompt-mestre", "O prompt-mestre", "main"),
    ("protocolo.html", "protocolo.md", "Protocolo", "Protocolo de teste", "main"),
    ("auditoria-rastreabilidade.html", "auditoria-rastreabilidade.md", "Rastreabilidade",
     "Síntese auditada · 4.1 Rastreabilidade", "audit"),
    ("auditoria-verificacao.html", "auditoria-verificacao.md", "Fontes primárias",
     "Síntese auditada · 4.2 Verificação em fonte primária", "audit"),
    ("auditoria-regua.html", "auditoria-regua.md", "Aplicação da régua",
     "Síntese auditada · 4.3 Aplicação da régua", "audit"),
    ("conclusao.html", "conclusao.md", "Conclusão", "Conclusão", "main"),
    ("anexos.html", "anexos.md", "Anexos", "Anexos", "main"),
    ("anexo-a-gemini.html", "anexos/a-gemini.txt", "Anexo A", "Anexo A · Resposta do Gemini", "annex"),
    ("anexo-b-deepseek.html", "anexos/b-deepseek.txt", "Anexo B", "Anexo B · Resposta do DeepSeek", "annex"),
    ("anexo-c-chatgpt.html", "anexos/c-chatgpt.txt", "Anexo C", "Anexo C · Resposta do ChatGPT", "annex"),
    ("anexo-d-sintese.html", "anexos/d-sintese.docx", "Anexo D", "Anexo D · Síntese da quarta IA", "annex"),
]

# Faixa de abertura de cada página: (sobretítulo, título grande, subtítulo, ilustração)
FAIXA = {
    "index.html": ("Estudo de caso · ADM0150 · 2026/2", "Panificação no DF: oportunidades com uma cadeia de IAs",
                   "Um prompt com a régua das Aulas 4, 5 e 6, três IAs, uma quarta IA que sintetiza e uma auditoria que confere tudo na fonte.",
                   "forno"),
    "prompt-mestre.html": ("2 · A receita", "O prompt-mestre", "O prompt na íntegra, bloco a bloco, com o instrumento de aula que cada parte carrega.", "receita"),
    "protocolo.html": ("3 · O preparo", "Protocolo de teste", "As mesmas instruções em três IAs, as condições de uso e o prompt da quarta IA.", "tigelas"),
    "auditoria-rastreabilidade.html": ("4.1 · Síntese auditada", "Rastreabilidade", "Cada afirmação da síntese rastreada até as respostas originais.", "lupa"),
    "auditoria-verificacao.html": ("4.2 · Síntese auditada", "Verificação em fonte primária", "Sete afirmações confrontadas com IPEDF, Anvisa e literatura clínica.", "lupa"),
    "auditoria-regua.html": ("4.3 · Síntese auditada", "Aplicação da régua", "As três finalistas no checklist de Dornelas e na pergunta do modelo de negócio.", "lupa"),
    "conclusao.html": ("5 · O pão que sai do forno", "Conclusão", "A oportunidade que defendo e o que aprendi sobre encadear IAs.", "pao"),
    "anexos.html": ("Anexos", "As quatro respostas, sem edição", "Gemini, DeepSeek, ChatGPT e a síntese do Claude, no site e em PDF.", "cesta"),
}
ANNEX_SUB = "Reproduzida na íntegra e sem edição, como objeto de estudo."

CTA_INICIO = ('<p class="cta"><a class="btn btn-claro" href="prompt-mestre.html">Ver o prompt-mestre</a>'
              '<a class="btn btn-contorno" href="conclusao.html">Ir para a conclusão</a></p>')

MARQUEE_ITENS = ["Tendência × oportunidade", "Cinco perguntas de triagem", "Leitura crítica de dado",
                 "Checklist de Dornelas", "3Ms", "Alto e baixo potencial", "Modelo de negócio",
                 "Cinco modelos na web", "Atenção × negócio"]


def marquee():
    itens = "".join(f"<li>{i}</li>" for i in MARQUEE_ITENS)
    return ('<div class="marquee" aria-label="Instrumentos das Aulas 4, 5 e 6 usados no prompt">'
            f'<ul>{itens}</ul><ul aria-hidden="true">{itens}</ul></div>')


ANNEX_NOTES = {
    "anexo-a-gemini.html": "Resposta do Gemini (origem A) ao prompt-mestre, reproduzida sem edição a partir do texto enviado à quarta IA.",
    "anexo-b-deepseek.html": "Resposta do DeepSeek (origem B) ao prompt-mestre, reproduzida sem edição a partir do texto enviado à quarta IA. Os marcadores [reference:N] fazem parte da resposta original.",
    "anexo-c-chatgpt.html": "Resposta do ChatGPT (origem C) ao prompt-mestre, reproduzida sem edição a partir do texto enviado à quarta IA. A linha \"Pensou por 12s\" é um resíduo da interface que veio junto com o texto copiado.",
    "anexo-d-sintese.html": "Saída da quarta IA ao prompt de síntese, reproduzida sem edição de conteúdo (convertida do documento original para HTML).",
}


def pandoc(args, text=None):
    return subprocess.run(["pandoc", *args], input=text, capture_output=True,
                          text=True, check=True).stdout


def prompt_block(match):
    """{{PROMPT:a-b}} -> bloco de código com as linhas a..b do arquivo do prompt."""
    a, b = int(match.group(1)), int(match.group(2))
    body = "\n".join(PROMPT_LINES[a - 1:b])
    return "\n``` {.prompt}\n" + body + "\n```\n"


def wrap_tables(fragment):
    fragment = fragment.replace("<table", '<div class="tabela"><table')
    return fragment.replace("</table>", "</table></div>")


def render(src: Path):
    if src.suffix == ".md":
        text = src.read_text(encoding="utf-8")
        text = re.sub(r"\{\{PROMPT:(\d+)-(\d+)\}\}", prompt_block, text)
        frag = pandoc(["-f", "markdown+pipe_tables+fenced_divs", "-t", "html5",
                       "--wrap=none"], text)
        frag = frag.replace("[PREENCHER", '<mark class="pendente">[PREENCHER')
        frag = re.sub(r'(<mark class="pendente">\[PREENCHER[^\]]*\])', r"\1</mark>", frag)
        return wrap_tables(frag)
    if src.suffix == ".txt":
        return '<pre class="anexo-bruto">' + html.escape(src.read_text(encoding="utf-8")) + "</pre>"
    if src.suffix == ".docx":
        frag = pandoc([str(src), "-f", "docx", "-t", "html5", "--wrap=none"])
        return '<div class="anexo-doc">' + wrap_tables(frag) + "</div>"
    raise ValueError(src)


def nav_html(current):
    def link(page):
        out, _, label, _, _ = page
        cls = ' class="ativo" aria-current="page"' if out == current else ""
        return f'<a href="{out}"{cls}>{label}</a>'

    main = [p for p in PAGES if p[4] == "main"]
    audit = [p for p in PAGES if p[4] == "audit"]
    items = []
    for i, p in enumerate(main):
        items.append(f"<li>{link(p)}</li>")
        if p[0] == "protocolo.html":
            audit_active = " ativo" if current in [a[0] for a in audit] else ""
            sub = "".join(f"<li>{link(a)}</li>" for a in audit)
            items.append(f'<li class="grupo{audit_active}"><span>Síntese auditada</span><ul>{sub}</ul></li>')
    return "<ul>" + "".join(items) + "</ul>"


def sequence():
    """Ordem de leitura para os links anterior/próximo."""
    return [p for p in PAGES]


def pager(current):
    seq = sequence()
    idx = [p[0] for p in seq].index(current)
    prev_l = seq[idx - 1] if idx > 0 else None
    next_l = seq[idx + 1] if idx < len(seq) - 1 else None
    parts = []
    parts.append(f'<a class="ant" href="{prev_l[0]}"><small>Anterior</small>{prev_l[3]}</a>' if prev_l else "<span></span>")
    parts.append(f'<a class="prox" href="{next_l[0]}"><small>Próxima</small>{next_l[3]}</a>' if next_l else "<span></span>")
    return '<nav class="pager" aria-label="Paginação">' + "".join(parts) + "</nav>"


TEMPLATE = (SRC / "template.html").read_text(encoding="utf-8")


def build():
    for out, src, _label, title, group in PAGES:
        body = render(SRC / src)
        if group == "annex":
            body = (f'<p class="nota-anexo">{ANNEX_NOTES[out]} '
                    f'<a href="anexos.html">Voltar à lista de anexos</a>.</p>' + body)
        if group == "annex":
            kicker, h1, sub, illu = "Anexos", title.split(" · ", 1)[1], ANNEX_SUB, "cesta"
            kicker = title.split(" · ", 1)[0]
        else:
            kicker, h1, sub, illu = FAIXA[out]
        page = (TEMPLATE
                .replace("{{KICKER}}", html.escape(kicker))
                .replace("{{H1}}", html.escape(h1))
                .replace("{{SUB}}", html.escape(sub))
                .replace("{{ILLU}}", illu)
                .replace("{{CTA}}", CTA_INICIO if out == "index.html" else "")
                .replace("{{EXTRA}}", marquee() if out == "index.html" else "")
                .replace("{{TITLE}}", html.escape(title))
                .replace("{{NAV}}", nav_html(out))
                .replace("{{BODY}}", body)
                .replace("{{PAGER}}", pager(out))
                .replace("{{BODYCLASS}}", group)
                .replace("{{NOME}}", ALUNO["nome"])
                .replace("{{MATRICULA}}", ALUNO["matricula"])
                .replace("{{DISCIPLINA}}", ALUNO["disciplina"])
                .replace("{{SEMESTRE}}", ALUNO["semestre"]))
        (ROOT / out).write_text(page, encoding="utf-8")
        print("ok", out)


if __name__ == "__main__":
    build()

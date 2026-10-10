#!/usr/bin/env python3
"""Gera assets/Anexos_Giovani_Rigon_ADM0150.pdf com os quatro anexos.

Uso (na raiz do repositório):  python3 _src/build_pdf.py && node _src/print_pdf.js
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import build  # noqa: E402

ROOT = build.ROOT
css = (ROOT / "assets" / "estilo.css").read_text(encoding="utf-8")
a = build.ALUNO
parts = [f"""<section class="capa">
<p class="sup">Universidade de Brasília · Departamento de Administração</p>
<h1>Anexos</h1>
<p class="lede">Estudo de caso: oportunidades em panificação no DF com uma cadeia de IAs</p>
<p><strong>{a['nome']}</strong><br>Matrícula {a['matricula']}<br>{a['disciplina']}<br>Semestre {a['semestre']}</p>
<ol>
<li>Anexo A · Resposta do Gemini ao prompt-mestre</li>
<li>Anexo B · Resposta do DeepSeek ao prompt-mestre</li>
<li>Anexo C · Resposta do ChatGPT ao prompt-mestre</li>
<li>Anexo D · Síntese da quarta IA</li>
</ol>
<p class="nota">Respostas reproduzidas na íntegra e sem edição. As respostas de IA são objeto de estudo, não fonte.</p>
</section>"""]
for out, src, _l, title, group in build.PAGES:
    if group != "annex":
        continue
    parts.append(f'<section class="anexo"><h1>{title}</h1><p class="nota-anexo">{build.ANNEX_NOTES[out]}</p>'
                 + build.render(build.SRC / src) + "</section>")
html = f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Anexos</title>
<style>{css}
:root {{ color-scheme: light; }}
body {{ background:#fff; font-size: 10.5pt; }}
section {{ page-break-before: always; }}
section.capa {{ page-break-before: avoid; padding-top: 6cm; }}
.capa h1 {{ font-family: var(--serif); font-size: 32pt; margin: .2em 0; }}
.capa .sup, .capa .nota {{ color: var(--muted); }}
.anexo h1 {{ font-family: var(--serif); font-size: 18pt; }}
pre.anexo-bruto {{ font-size: 8.6pt; border: 0; padding: 0; }}
.anexo-doc {{ border: 0; padding: 0; }}
.tabela {{ overflow: visible; }}
table {{ font-size: 8pt; }}
</style></head><body><main style="max-width:none;padding:0">{''.join(parts)}</main></body></html>"""
out = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "_src" / "_anexos_pdf.html"
out.write_text(html, encoding="utf-8")
print(out)

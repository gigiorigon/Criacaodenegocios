# Panificação no DF: oportunidades com uma cadeia de IAs

Site do estudo de caso da Atividade 2 de Criação de Negócios (ADM0150, UnB, 2026/2).
Giovani Machado Rigon · Matrícula 16/0070686.

## Estrutura

| Página | Arquivo |
|---|---|
| 1. Abertura e régua analítica | `index.html` |
| 2. Prompt-mestre | `prompt-mestre.html` |
| 3. Protocolo de teste e prompt de síntese | `protocolo.html` |
| 4.1 Rastreabilidade | `auditoria-rastreabilidade.html` |
| 4.2 Verificação em fonte primária | `auditoria-verificacao.html` |
| 4.3 Aplicação da régua | `auditoria-regua.html` |
| 5. Conclusão | `conclusao.html` |
| Anexos (A a D) e PDF | `anexos.html`, `anexo-*.html`, `assets/Anexos_Giovani_Rigon_ADM0150.pdf` |

Os HTML são gerados a partir de `_src/`. Para editar o texto, altere o `.md` correspondente em `_src/` e rode:

```bash
python3 _src/build.py                      # páginas HTML (requer pandoc)
python3 _src/build_pdf.py && node _src/print_pdf.js   # PDF dos anexos (requer playwright)
```

## Publicação (GitHub Pages)

Settings → Pages → Build and deployment → Source: "Deploy from a branch" → escolha o branch e a pasta `/ (root)`.
O site fica em `https://<usuário>.github.io/<repositório>/`.

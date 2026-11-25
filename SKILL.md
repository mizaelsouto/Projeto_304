---
name: projeto
description: Gera o relatório final de um projeto de software em PDF e Word no padrão do Relatório Final do Grupo 05: capa, sumário ABNT, critérios da Feira Integrada, telas, tecnologias e anexo de fotos.
---

# Relatório final de projeto (padrão Grupo 05)

Esta skill produz o relatório final de um projeto de software lendo o material do projeto (pasta local ou repositório no GitHub) e os dados informados pelo usuário. O resultado segue exatamente a estrutura do Relatório Final do Grupo 05 (Cognitus PDI), com os acréscimos pedidos para a Feira Integrada: introdução com repositório e endereço publicado, linguagens e tecnologias, telas da aplicação, conclusão do grupo pelos seis critérios da ficha de avaliação, referências e anexo com prints, fotos dos integrantes e link de vídeo.

Entregáveis: `relatorio.pdf` (versão de entrega), `relatorio.md` (fonte editável) e, se pedido, `relatorio.docx`. Tudo fica em uma pasta `Relatorio_Final/` dentro do projeto; versões anteriores vão para `Relatorio_Final/old/`, nunca são apagadas.

## 1. Perguntar antes de escrever

Pergunte de uma vez (com AskUserQuestion quando houver, ou em texto) e não invente o que faltar:

1. **Instituição**: nome completo, instituto/campus/departamento, curso, disciplina ou evento (ex.: "Feira Integrada 2026") e período. Essas linhas vão no bloco superior esquerdo da capa, em maiúsculas.
2. **Logo** da instituição (arquivo de imagem). Sem logo, a capa sai sem ele.
3. **Tema/título** do projeto (ex.: "NOME DO APP: subtítulo descritivo").
4. **Cidade e UF** e **data**: mês/ano para a capa (ex.: NOVEMBRO/2026) e data de entrega completa para a folha de identificação.
5. **Integrantes**: nome completo de cada um (matrícula opcional), número do grupo, docente/orientador(a) com o nome exato que deve aparecer.
6. **Endereços**: repositório no GitHub, endereço onde a aplicação está hospedada e vídeo (YouTube ou TikTok), se houver.
7. **Imagens**: pasta com os prints das telas e as fotos dos integrantes.
8. **O que cada integrante fez** e **quais ferramentas de IA** foram usadas e para quê (para as Declarações).
9. Limite de páginas, se houver (o padrão é até 20 páginas sem contar capa, referências e anexos).

Se faltarem prints e houver endereço publicado e ferramenta de navegador disponível, ofereça capturar as telas; caso contrário, peça os prints.

## 2. Ler o projeto

Leia README, documentação, `package.json`, `requirements.txt`, `pom.xml`, `composer.json`, `Dockerfile`, arquivos de configuração e a árvore de pastas. Levante: problema e público, funcionalidades (rotas, telas, componentes), linguagens (contagem por extensão de arquivo), frameworks e bibliotecas com versões, banco de dados, hospedagem, testes e forma de publicação. Use só o que estiver no projeto ou for dito pelo usuário. O que não puder ser comprovado entra como hipótese ou fica de fora; nunca preencha lacunas com números ou fatos inventados.

## 3. Estrutura obrigatória do `relatorio.md`

Mantenha esta ordem e estes títulos (podem ser adaptados ao produto, mas todas as partes existem). Seções primárias em maiúsculas e numeradas ("## 1 INTRODUÇÃO ..."), subseções "### 1.1 Título". O sumário é montado automaticamente a partir desses títulos. Há um exemplo completo e testado em `exemplo/`.

```
# NOME DA INSTITUIÇÃO
**CURSO | DISCIPLINA OU EVENTO (PERÍODO)**

# RELATÓRIO FINAL DO PROJETO: NOME DO PROJETO

| Campo | Preenchimento / Identificação do Grupo |
| :--- | :--- |
| **Instituição:** | ... |
| **Curso:** | ... |
| **Disciplina / Evento:** | ... |
| **Docente / Orientador(a):** | nome exato informado pelo usuário |
| **Grupo:** | ... |
| **Integrantes / Autores:** | ... |
| **Projeto:** | ... |
| **Repositório no GitHub:** | URL |
| **Aplicação publicada:** | URL |
| **Vídeo de apresentação:** | URL ou "não há" |
| **Data de Entrega:** | dia de mês de ano |

<!-- quebra -->

## SUMÁRIO

@@TOC@@

<!-- quebra -->

## RESUMO
## 1 INTRODUÇÃO E VISÃO DO PRODUTO
### 1.1 Apresentação do projeto
### 1.2 Contexto e problema
### 1.3 Justificativa e recorte
### 1.4 Visão do produto
### 1.5 Escopo e exclusões
## 2 EMBASAMENTO
### 2.1 Fundamentação adotada
### 2.2 Tipo de software e de ambiente
### 2.3 O que a fundamentação determina no produto
### 2.4 Limites
## 3 OBJETIVOS, PERSONAS E CENÁRIOS
## 4 RECURSOS E BACKLOG DO PRODUTO
## 5 REQUISITOS DO AMBIENTE
## 6 EQUIPE, TECNOLOGIAS E ARQUITETURA
### 6.1 Equipe e papéis
### 6.2 Linguagens e tecnologias
### 6.3 Arquitetura e serviços
### 6.4 Implantação e hospedagem
### 6.5 Telas da aplicação
## 7 CRONOGRAMA E DEVOPS
## 8 QUADRO DE COERÊNCIA
## 9 CONSIDERAÇÕES FINAIS
### 9.1 Como saber se o produto cumpre o objetivo
### 9.2 Limitações e riscos
### 9.3 Próximo passo
## 10 CONCLUSÃO DO GRUPO
### 10.1 Processo investigativo e registros
### 10.2 Integração curricular e domínio do conteúdo
### 10.3 Desenvolvimento e qualidade do trabalho
### 10.4 Impacto social, ética e sustentabilidade
### 10.5 Apresentação e comunicação
### 10.6 Colaboração e autoavaliação
## 11 HISTÓRICO DE REVISÕES
## REFERÊNCIAS
## DECLARAÇÕES
## GLOSSÁRIO              (opcional)
<!-- quebra -->
## ANEXO A – TELAS DA APLICAÇÃO E FOTOS DOS INTEGRANTES
```

### O que vai em cada parte

**Resumo**: um parágrafo de até 200 palavras com problema, público, fundamentação, o que o produto faz e como foi construído.

**1.1 Apresentação do projeto**: logo no início, uma introdução breve (3 a 5 frases) e, em linhas próprias, o endereço do repositório no GitHub e o endereço onde a aplicação está hospedada. **1.2 a 1.5**: contexto, problema, justificativa, visão do produto (três perguntas: qual é o produto, quem são os usuários, por que usar; e a frase no modelo de Moore) e o que fica fora do escopo.

**2 Embasamento**: em projetos educacionais, a concepção de aprendizagem e o tipo de software; nos demais, a fundamentação técnica ou do domínio. A seção mostra o que essa fundamentação decide no produto.

**3 Objetivos, personas e cenários**: objetivo geral, objetivos específicos codificados (OE1, OE2...), personas codificadas (P1, P2...), declaradas como perfis fictícios, e cenários de uso.

**4 Recursos e backlog**: histórias de usuário (US01...), recursos (R01...) e o backlog por sprint, em tabelas.

**5 Requisitos**: requisitos funcionais (RF01...), com área, serviço e sprint, não funcionais (RNF01...) com forma de verificação, acessibilidade (barreira, resposta e requisito) e privacidade dos dados.

**6 Equipe, tecnologias e arquitetura**: 6.1 tabela de papéis com dono (nomes reais dos integrantes); 6.2 tabela de linguagens e tecnologias (camada, tecnologia e versão, uso no projeto, justificativa, incluindo custo quando houver), baseada no que foi encontrado no projeto; 6.3 figura da arquitetura com as conexões entre as partes e tabela dos serviços ou módulos com a coluna "Conversa com"; 6.4 onde e como está hospedado, com o endereço; 6.5 as telas principais como figuras numeradas, cada uma com uma frase sobre o que o usuário faz nela.

**7 Cronograma e DevOps**: EAP com responsável por pacote, tabela de sprints com período, meta e responsável de cada integrante (carga equilibrada entre eles), gráfico de Gantt (linha de cabeçalho "Atividade" e uma coluna por semana; células com X ficam coloridas), marcos (incluindo publicação ou lançamento), viabilidade do plano e práticas de DevOps (repositório no GitHub, ramos, testes automáticos, ambiente de teste e de homologação, publicação fora do horário de uso). Se o projeto já foi construído, o cronograma registra o que foi feito, com as datas reais.

**8 Quadro de coerência**: uma linha por objetivo, com as colunas objetivo, persona, histórias e recursos, requisitos, serviço ou camada e sprint. Depois da tabela, um parágrafo que segue o fio a partir do item do topo do backlog e explica como a fundamentação aparece nas linhas. Todo código definido no relatório precisa aparecer no quadro ou ter a lacuna explicada em 9.2.

**9 Considerações finais**: até uma página. Responde como verificar se o produto cumpre o objetivo (o que seria observado ou medido), quais as limitações e riscos reais, e qual o próximo passo.

**10 Conclusão do grupo**: uma subseção por critério da ficha individual de avaliação (aba "Feira integrada", se existir na planilha; senão, a aba com os mesmos critérios). Pesos de referência: processo investigativo e registros (3 pontos); integração curricular e domínio do conteúdo (2); desenvolvimento e qualidade do trabalho (2); impacto social, ética e sustentabilidade (1,5); apresentação e comunicação (1); colaboração e autoavaliação (0,5); total 10. Confirme os pesos na planilha do usuário. Cada subseção descreve as evidências do grupo, apontando a seção ou figura do relatório que comprova. Feche com uma tabela "Critério | Peso | Evidência no relatório | Seção" e um parágrafo de conclusão do grupo. O grupo não atribui nota a si mesmo.

**11 Histórico de revisões**: tabela "Etapa ou tarefa | Origem | O que foi apontado | O que mudou | Seção", com devolutivas do professor e decisões do grupo. Se uma devolutiva não chegou, dizer isso na linha.

**Referências**: só o que foi citado no texto, e tudo o que foi citado, em ABNT NBR 6023 e ordem alfabética. Obra sem data aparece sem data (não usar data provável nem "s.d."). Local e editora desconhecidos: "[S. l.: s. n.]". Só use links fornecidos pelo usuário ou presentes no projeto; nunca crie links. Normas legais podem ser citadas pela publicação no Diário Oficial, sem link.

**Declarações**: uma linha por integrante, com o nome do colega por extenso (nunca "o outro integrante"), dizendo o que cada um fez, e a declaração de uso de IA generativa: quais ferramentas (com fabricante) e para quê. Se a IA ajudou a redigir, diga isso; não declare escrita sem IA quando houve.

**Anexo A**: todos os prints das telas, as fotos dos integrantes (grade com nome abaixo de cada foto) e o link do vídeo no YouTube ou TikTok, se houver.

## 4. Regras de escrita

1. Terceira pessoa, linguagem acadêmica simples, sem jargões; termo técnico inevitável é explicado na primeira vez.
2. Texto corrido; listas só quando a estrutura exige. Tabelas para encurtar as seções 4, 5 e 7.
3. O texto é para um leitor que nunca viu as entregas anteriores: nada de "na tarefa anterior" ou "conforme solicitado" no corpo; isso só no histórico.
4. Nomes e códigos iguais do início ao fim (personas, recursos, serviços, requisitos).
5. Nunca inventar dados, números, relatos ou referências. Planos e metas aparecem como propostas, e o que não foi testado não é apresentado como resultado.
6. Use a forma inclusiva "professora(o)" para docentes em geral, com a concordância ajustada; para uma pessoa específica, use o gênero dela.
7. Toda tabela tem título acima (`@CAP|Tabela N – Título`) e fonte abaixo (`@FONTE|Fonte: elaborado pelos autores (ano).`); toda figura, `@CAP|Figura N – Título`. A numeração é sequencial.
8. Diagramas e o Gantt precisam ser legíveis sem ampliar: fonte mínima de 7 pontos na página. Gere diagramas com Graphviz em orientação vertical (`rankdir=TB`) quando ficarem largos.

## 5. Marcadores do `relatorio.md`

| Marcador | Efeito |
| :--- | :--- |
| `<!-- quebra -->` | quebra de página |
| `@@TOC@@` | lugar do sumário (preenchido pelo `montar_sumario.py`) |
| `@CAP|Tabela N – título` | título da tabela ou figura seguinte, preso a ela |
| `@FONTE|Fonte: ...` | fonte abaixo da tabela ou figura |
| `@IMG|caminho.png|largura` | imagem; largura em pontos (máximo 523, padrão 523) |
| `@FOTOS|a.jpg::Nome A;b.jpg::Nome B` | grade de fotos, três por linha, com o nome abaixo |
| tabela com primeira coluna "Campo" | folha de identificação, sem cabeçalho azul |
| tabela com primeira coluna "Atividade" e mais de 10 colunas | gráfico de Gantt; células com X ficam coloridas |

Links `http(s)://` no texto viram links clicáveis no PDF.

## 6. Gerar o PDF

Na pasta `Relatorio_Final/`, crie `config.json` (modelo em `scripts/config_exemplo.json`), copie `scripts/gerar_relatorio.py` e `scripts/montar_sumario.py` (também reproduzidos no fim deste arquivo) e rode `python3 montar_sumario.py config.json`. Ele gera o PDF, preenche o sumário com as páginas reais em duas passadas e avisa se algum título não foi encontrado. Dependências: `reportlab`, `Pillow`, `pdfinfo` e `pdftotext` (Poppler). A fonte é Arial; sem Arial instalada, usa Liberation Sans, que tem as mesmas medidas.

Campos do `config.json`: `md`, `pdf`, `capa` (`instituicao` como lista de linhas, `logo`, `titulo`, `tema`, `grupo`, `integrantes` como lista, `cidade`, `data`), `cabecalho_esq`, `cabecalho_dir` e `rodape`.

Se o usuário pedir Word, gere o `.docx` a partir do mesmo `relatorio.md` com pandoc e um documento de referência em Arial (converta `@CAP` e `@FONTE` em estilos de legenda, `@IMG` e `@FOTOS` em imagens, `<!-- quebra -->` em quebra de página e o sumário em campo TOC do Word, que se atualiza ao abrir). Avise que, com fonte 11 do Word, o número de páginas difere do PDF; a entrega é o PDF.

## 7. Conferência antes de entregar

Renderize as páginas (`pdftoppm -r 60 -png relatorio.pdf p`) e olhe cada uma. Confira:

1. O sumário: o `montar_sumario.py` deve terminar com "títulos não encontrados: nenhum".
2. O limite de páginas, sem contar capa, referências e anexos.
3. Espaços vazios grandes ou títulos sozinhos no pé da página (use `<!-- quebra -->` quando necessário).
4. A numeração e a legenda de todas as tabelas e figuras.
5. Citações e referências, nos dois sentidos: tudo o que é citado está na lista, e tudo o que está na lista é citado.
6. Os links: só os fornecidos pelo usuário ou presentes no projeto.
7. O quadro de coerência, com todos os códigos (OE, US, R, RF, RNF) cobertos ou explicados.
8. A carga de trabalho equilibrada entre os integrantes nas tabelas de sprints e EAP.
9. O corpo do texto, que não pode citar tarefas anteriores.
10. O nome do docente, que deve ser exatamente o informado.

Envie o PDF ao usuário e diga, em poucas linhas, o que precisa de confirmação dele (dados que não estavam no projeto, decisões tomadas por falta de informação).

## Anexo: código dos scripts

`gerar_relatorio.py`:

```python
"""Gera o PDF do relatório a partir do .md e do config.json (padrão Relatório Final Grupo 05)."""
import json, os, re, sys
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import (CondPageBreak, Image as RLImage, KeepTogether, PageBreak, Paragraph,
                                Preformatted, SimpleDocTemplate, Spacer, Table, TableStyle)

HERE = os.path.dirname(os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else "config.json"))
CFG = json.load(open(sys.argv[1] if len(sys.argv) > 1 else "config.json", encoding="utf-8"))
SRC, OUT = os.path.join(HERE, CFG["md"]), os.path.join(HERE, CFG["pdf"])
W = 523  # largura útil em pontos (A4 com margens de 36)

# Fonte: Arial se existir; senão Liberation Sans (mesmas medidas da Arial)
def _font_dir():
    for d in ["/usr/share/fonts/truetype/msttcorefonts/", "/Library/Fonts/", "/System/Library/Fonts/Supplemental/"]:
        if os.path.exists(os.path.join(d, "Arial.ttf")):
            return d, ("Arial.ttf", "Arial Bold.ttf" if os.path.exists(os.path.join(d, "Arial Bold.ttf")) else "Arial_Bold.ttf",
                       "Arial Italic.ttf" if os.path.exists(os.path.join(d, "Arial Italic.ttf")) else "Arial_Italic.ttf",
                       "Arial Bold Italic.ttf" if os.path.exists(os.path.join(d, "Arial Bold Italic.ttf")) else "Arial_Bold_Italic.ttf")
    for d in ["/usr/share/fonts/truetype/liberation/", "/usr/share/fonts/truetype/liberation2/"]:
        if os.path.exists(os.path.join(d, "LiberationSans-Regular.ttf")):
            return d, ("LiberationSans-Regular.ttf", "LiberationSans-Bold.ttf", "LiberationSans-Italic.ttf", "LiberationSans-BoldItalic.ttf")
    raise SystemExit("Instale a fonte Arial ou Liberation Sans")
_d, _f = _font_dir()
for name, file in zip(("LSans", "LSans-Bold", "LSans-Italic", "LSans-BoldItalic"), _f):
    pdfmetrics.registerFont(TTFont(name, os.path.join(_d, file)))
pdfmetrics.registerFontFamily("LSans", normal="LSans", bold="LSans-Bold", italic="LSans-Italic", boldItalic="LSans-BoldItalic")


class NumberedCanvas(canvas.Canvas):
    def __init__(self, *a, **k):
        super().__init__(*a, **k); self._states = []
    def showPage(self):
        self._states.append(dict(self.__dict__)); self._startPage()
    def save(self):
        n = len(self._states)
        for st in self._states:
            self.__dict__.update(st); self.draw_page(n); super().showPage()
        super().save()
    def draw_page(self, total):
        if self._pageNumber == 1:  # capa sem cabeçalho e sem rodapé
            return
        self.saveState(); self.setFont("LSans", 8); self.setFillColor(colors.HexColor("#475569"))
        self.setStrokeColor(colors.HexColor("#CBD5E1")); self.setLineWidth(0.5)
        if self._pageNumber > 2:
            self.drawString(36, 810, CFG.get("cabecalho_esq", "")); self.drawRightString(559, 810, CFG.get("cabecalho_dir", ""))
            self.line(36, 804, 559, 804)
        self.line(36, 40, 559, 40)
        self.drawString(36, 28, CFG.get("rodape", "")); self.drawRightString(559, 28, f"Página {self._pageNumber} de {total}")
        self.restoreState()


S = getSampleStyleSheet()
def PS(name, **k):
    return ParagraphStyle(name, parent=S["Normal"], fontName=k.pop("fontName", "LSans"), **k)
inst_header = PS("Inst", fontName="LSans-Bold", fontSize=9.5, leading=13, alignment=TA_CENTER, textColor=colors.HexColor("#1E3A8A"))
doc_title = PS("DocTitle", fontName="LSans-Bold", fontSize=12, leading=15.5, alignment=TA_CENTER, textColor=colors.HexColor("#0F172A"), spaceAfter=10)
h2 = PS("H2", fontName="LSans-Bold", fontSize=10, leading=14, textColor=colors.HexColor("#1E3A8A"), spaceBefore=9, spaceAfter=3.5, keepWithNext=1)
h3 = PS("H3", fontName="LSans-Bold", fontSize=8.8, leading=12, textColor=colors.HexColor("#1E293B"), spaceBefore=5.5, spaceAfter=2.5, keepWithNext=1)
body = PS("Body", fontSize=8.3, leading=12.2, alignment=TA_JUSTIFY, textColor=colors.HexColor("#1E293B"), spaceAfter=3.8)
bullet = PS("Bullet", fontSize=8.3, leading=12.2, leftIndent=11, spaceAfter=2.8, textColor=colors.HexColor("#1E293B"))
meta_l = PS("MetaL", fontName="LSans-Bold", fontSize=7.8, leading=10.2, textColor=colors.HexColor("#1E293B"))
meta_v = PS("MetaV", fontSize=7.8, leading=10.2, textColor=colors.HexColor("#334155"))
cell = PS("Cell", fontSize=7.2, leading=9.2, textColor=colors.HexColor("#1E293B"))
cell_c = PS("CellC", fontSize=7.2, leading=9.2, alignment=TA_CENTER, textColor=colors.HexColor("#1E293B"))
cell_h = PS("CellH", fontName="LSans-Bold", fontSize=7.2, leading=9.2, alignment=TA_CENTER, textColor=colors.white)
ref = PS("Ref", fontSize=7.6, leading=10.5, alignment=TA_LEFT, textColor=colors.HexColor("#334155"), leftIndent=14, firstLineIndent=-14, spaceAfter=3.2)
cap = PS("Cap", fontName="LSans-Bold", fontSize=7.8, leading=10, alignment=TA_CENTER, spaceBefore=4, spaceAfter=3)
fonte = PS("Fonte", fontSize=7.0, leading=9, alignment=TA_LEFT, spaceBefore=1, spaceAfter=6)
foto_leg = PS("FotoLeg", fontSize=7.2, leading=9, alignment=TA_CENTER)
code_st = ParagraphStyle("Code", parent=S["Normal"], fontName="Courier", fontSize=6.8, leading=8.6)


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
def inline(s):
    s = esc(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<i>\1</i>", s)
    s = re.sub(r"(https?://[^\s<]+?)([.,;)]?)(?=\s|$)", r'<link href="\1" color="#1D4ED8">\1</link>\2', s)
    return s
def split_row(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]
def is_sep(line):
    return bool(re.match(r"^\|\s*:?-{2,}", line.strip()))


def col_widths(rows):
    n = len(rows[0])
    w = [min(max(max(len(r[c]) if c < len(r) else 0 for r in rows), 4), 70) for c in range(n)]
    fixed = {c: 36 for c in range(n) if max(len(r[c]) if c < len(r) else 0 for r in rows) <= 8}
    rest = sum(w[c] for c in range(n) if c not in fixed) or 1
    avail = W - sum(fixed.values())
    out = [fixed.get(c, avail * w[c] / rest) for c in range(n)]
    mins = []
    for c in range(n):
        m = 0
        for i, r in enumerate(rows):
            if c < len(r):
                f, sz = (("LSans-Bold", 7.2) if i == 0 else ("LSans", 7.2))
                m = max(m, max((stringWidth(x, f, sz) for x in re.sub(r"[*`]", "", r[c]).split()), default=0))
        mins.append(m * 1.08 + 12)
    out = [max(o, m) for o, m in zip(out, mins)]
    ex = sum(out) - W
    if ex > 0:
        slack = [max(o - m, 0) for o, m in zip(out, mins)]; ss = sum(slack)
        if ss >= ex:
            out = [o - ex * s / ss if s > 0 else o for o, s in zip(out, slack)]
        else:
            print("AVISO: tabela mais larga que a página; reduza o texto das células")
    return out


def build_table(rows):
    widths = col_widths(rows)
    if rows[0][0].strip() == "Atividade" and len(rows[0]) > 10:  # gráfico de Gantt
        widths = [165] + [(W - 165) / (len(rows[0]) - 1)] * (len(rows[0]) - 1)
    n = len(rows[0])
    short = [all(len(r[c] if c < len(r) else "") <= 8 for r in rows[1:]) for c in range(n)]
    data, gantt = [], []
    for i, row in enumerate(rows):
        line = []
        for c in range(n):
            t = row[c] if c < len(row) else ""
            if i > 0 and t.strip() == "X":
                gantt.append((c, i)); line.append(Paragraph("", cell_c))
            elif i == 0:
                line.append(Paragraph(inline(t), cell_h))
            else:
                line.append(Paragraph(inline(t), cell_c if short[c] and t else cell))
        data.append(line)
    tb = Table(data, colWidths=widths, repeatRows=1)
    st = [("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1E3A8A")), ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E1")),
          ("TOPPADDING", (0, 0), (-1, -1), 2.2), ("BOTTOMPADDING", (0, 0), (-1, -1), 2.2),
          ("LEFTPADDING", (0, 0), (-1, -1), 4), ("RIGHTPADDING", (0, 0), (-1, -1), 4)]
    st += [("BACKGROUND", (0, r), (-1, r), colors.HexColor("#F8FAFC")) for r in range(2, len(rows), 2)]
    st += [("BACKGROUND", (c, r), (c, r), colors.HexColor("#2563EB")) for c, r in gantt]
    tb.setStyle(TableStyle(st))
    return tb


def build_meta(rows):
    tb = Table([[Paragraph(inline(r[0]), meta_l), Paragraph(inline(r[1] if len(r) > 1 else ""), meta_v)] for r in rows], colWidths=[150, 373])
    tb.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F8FAFC")), ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#E2E8F0")),
                            ("TOPPADDING", (0, 0), (-1, -1), 2.2), ("BOTTOMPADDING", (0, 0), (-1, -1), 2.2),
                            ("LEFTPADDING", (0, 0), (-1, -1), 5), ("RIGHTPADDING", (0, 0), (-1, -1), 5)]))
    return tb


def image(path, width):
    from PIL import Image as PI
    p = os.path.join(HERE, path)
    w0, h0 = PI.open(p).size
    h = width * h0 / w0
    if h > 600:  # imagem muito alta: limitar à página
        width, h = width * 600 / h, 600
    return RLImage(p, width=width, height=h)


def photo_grid(spec):
    """@FOTOS|arquivo.jpg::Nome;arquivo2.jpg::Nome 2 -> grade com 3 fotos por linha."""
    items = [x.split("::") for x in spec.split(";") if x.strip()]
    cells = []
    for it in items:
        path, name = it[0].strip(), (it[1].strip() if len(it) > 1 else "")
        img = image(path, 140)
        if img.drawHeight > 170:
            img = RLImage(os.path.join(HERE, path), width=140 * 170 / img.drawHeight, height=170)
        cells.append([img, Paragraph(esc(name), foto_leg)])
    rows = [cells[i:i + 3] for i in range(0, len(cells), 3)]
    rows = [r + [""] * (3 - len(r)) for r in rows]
    tb = Table(rows, colWidths=[W / 3] * 3)
    tb.setStyle(TableStyle([("ALIGN", (0, 0), (-1, -1), "CENTER"), ("VALIGN", (0, 0), (-1, -1), "TOP"),
                            ("BOTTOMPADDING", (0, 0), (-1, -1), 8)]))
    return tb


def build_cover(story):
    c = CFG["capa"]
    inst = PS("CI", fontName="LSans-Bold", fontSize=12, leading=14.5)
    c12 = PS("C12", fontName="LSans-Bold", fontSize=12, leading=15, alignment=TA_CENTER)
    c14 = PS("C14", fontName="LSans-Bold", fontSize=14, leading=19, alignment=TA_CENTER)
    top = Paragraph("<br/>".join(esc(x) for x in c["instituicao"]), inst)
    if c.get("logo") and os.path.exists(os.path.join(HERE, c["logo"])):
        logo = image(c["logo"], 60)
        head = Table([[top, logo]], colWidths=[440, 83])
    else:
        head = Table([[top]], colWidths=[W])
    head.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("ALIGN", (-1, 0), (-1, 0), "RIGHT"),
                              ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0)]))
    extra = max(len(c["integrantes"]) - 3, 0) * 15
    story += [head, Spacer(1, 170 - extra / 3), Paragraph(esc(c["titulo"]), c14), Paragraph(esc(c["tema"]), c14),
              Spacer(1, 150 - extra / 3)]
    if c.get("grupo"):
        story.append(Paragraph(esc(c["grupo"]), c12))
    story += [Paragraph(esc(x), c12) for x in c["integrantes"]]
    story += [Spacer(1, 150 - extra / 3), Paragraph(esc(c["cidade"]), c12), Paragraph(esc(c["data"]), c12), PageBreak()]


def main():
    lines = open(SRC, encoding="utf-8").read().split("\n")
    doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=36, rightMargin=36, topMargin=46, bottomMargin=50, title=CFG["capa"]["tema"])
    story, pending, in_refs, i, head_done = [], None, False, 0, False
    build_cover(story)

    def put(flow):
        nonlocal pending
        if pending is not None:
            story.append(KeepTogether([pending, flow])); pending = None
        else:
            story.append(flow)

    while i < len(lines):
        line = lines[i].rstrip()
        if not head_done and line.startswith("# ") and i + 1 < len(lines) and lines[i + 1].startswith("**"):
            story += [Paragraph(esc(line[2:]) + "<br/>" + esc(lines[i + 1].strip("* ")), inst_header), Spacer(1, 8)]
            head_done = True; i += 2; continue
        if line.strip() == "<!-- quebra -->":
            story.append(PageBreak()); i += 1; continue
        if line.startswith("```"):
            code = []; i += 1
            while i < len(lines) and not lines[i].startswith("```"):
                code.append(lines[i]); i += 1
            i += 1
            box = Table([[Preformatted("\n".join(code), code_st)]], colWidths=[W])
            box.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F8FAFC")), ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E1"))]))
            put(box); story.append(Spacer(1, 4)); continue
        if line.startswith("@CAP|"):
            pending = Paragraph(esc(line[5:].strip()), cap); i += 1; continue
        if line.startswith("@IMG|"):
            parts = line[5:].split("|")
            put(image(parts[0].strip(), float(parts[1]) if len(parts) > 1 and parts[1].strip() else W)); i += 1; continue
        if line.startswith("@FOTOS|"):
            put(photo_grid(line[7:])); i += 1; continue
        if line.startswith("@FONTE|"):
            story.append(Paragraph(esc(line[7:].strip()), fonte)); i += 1; continue
        if line.startswith("@TOC|"):
            _, lvl, ttl, pg = line.split("|", 3)
            f = "LSans-Bold" if lvl == "2" else "LSans"; ind = 0 if lvl == "2" else 18
            dots = max(int((W - ind - stringWidth(pg, f, 8.3) - 16 - stringWidth(ttl, f, 8.3)) / stringWidth(".", f, 8.3)), 3)
            story.append(Paragraph(esc(ttl) + " " + "." * dots + " " + pg, PS("T" + lvl, fontName=f, fontSize=8.3, leftIndent=ind, leading=10, spaceAfter=0.8)))
            i += 1; continue
        if line.startswith("|"):
            block = []
            while i < len(lines) and lines[i].startswith("|"):
                block.append(lines[i]); i += 1
            rows = [split_row(b) for b in block if not is_sep(b)]
            if rows[0][0] == "Campo":
                story.append(build_meta(rows[1:]))
            elif pending is not None and len(rows) > 12:  # tabela longa: pode continuar na página seguinte
                story += [CondPageBreak(90), pending, build_table(rows)]; pending = None
            else:
                put(build_table(rows))
            story.append(Spacer(1, 7)); continue
        if line.startswith("# "):
            story.append(Paragraph(inline(line[2:]), doc_title))
        elif line.startswith("## "):
            t = line[3:].strip(); in_refs = bool(re.match(r"^(\d+\s*)?(REFERÊNCIAS|BIBLIOGRAFIA)", t))
            story.append(Paragraph(inline(t), doc_title if t == "SUMÁRIO" else h2))
        elif line.startswith("### "):
            story.append(Paragraph(inline(line[4:]), h3))
        elif line.startswith("- "):
            story.append(Paragraph("• " + inline(line[2:]), bullet))
        elif line.strip() in ("", "---"):
            pass
        else:
            story.append(Paragraph(inline(line.strip()), ref if in_refs else body))
        i += 1
    doc.build(story, canvasmaker=NumberedCanvas)
    print("PDF gerado:", OUT)


if __name__ == "__main__":
    main()
```

`montar_sumario.py`:

```python
"""Monta o sumário com as páginas reais (duas passadas) e confere cada entrada."""
import json, os, re, subprocess, sys
cfgp = sys.argv[1] if len(sys.argv) > 1 else "config.json"
HERE = os.path.dirname(os.path.abspath(cfgp)); CFG = json.load(open(cfgp, encoding="utf-8"))
MD, PDF = os.path.join(HERE, CFG["md"]), os.path.join(HERE, CFG["pdf"])
norm = lambda t: re.sub(r"\s+", " ", t).strip()

def heads():
    s = open(MD, encoding="utf-8").read(); out = []
    for line in s[s.index("## RESUMO"):].split("\n"):
        m = re.match(r"^(##|###) (.+)$", line)
        if m and m.group(2).strip() != "RESUMO":
            out.append((len(m.group(1)), m.group(2).strip()))
    return out

def write(H, pages):
    s = open(MD, encoding="utf-8").read()
    toc = "\n".join(f"@TOC|{l}|{t}|{pages.get(k, '0')}" for k, (l, t) in enumerate(H)) + "\n"
    s = re.sub(r"(## SUMÁRIO\n\n)(?:@TOC\|[^\n]*\n|@@TOC@@\n)+", lambda m: m.group(1) + toc, s)
    open(MD, "w", encoding="utf-8").write(s)

def build():
    r = subprocess.run([sys.executable, os.path.join(HERE, "gerar_relatorio.py"), cfgp], capture_output=True, text=True)
    if r.returncode:
        print(r.stderr[-3000:]); sys.exit(1)

def find(H):
    n = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", PDF], capture_output=True, text=True).stdout).group(1))
    tx = {p: [norm(l) for l in subprocess.run(["pdftotext", "-f", str(p), "-l", str(p), "-layout", PDF, "-"], capture_output=True, text=True).stdout.split("\n")] for p in range(1, n + 1)}
    start = next(p for p in tx if "RESUMO" in tx[p] and not any("SUMÁRIO" in l for l in tx[p]))
    res = {}
    for k, (l, t) in enumerate(H):
        key = norm(t)
        for p in range(start, n + 1):
            if any(x == key or (x.startswith(key[:45]) and "...." not in x) for x in tx[p]):
                res[k] = p; start = p; break
    return n, res

H = heads()
write(H, {}); build(); n, p1 = find(H)
write(H, p1); build(); n, p2 = find(H)
if p2 != p1:
    write(H, p2); build(); n, p2 = find(H)
miss = [H[k][1] for k in range(len(H)) if k not in p2]
print(f"Páginas: {n} | entradas no sumário: {len(H)} | títulos não encontrados: {miss or 'nenhum'}")
```

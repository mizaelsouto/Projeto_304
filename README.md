# Projeto: skill de relatório final de projeto de software

Skill para o Claude que gera o relatório final de um projeto de software em PDF (e, se pedido, em Word), no mesmo padrão do Relatório Final do Grupo 05 (Cognitus PDI, UFJF 2026.3). A skill lê o material do projeto, como README, código e arquivos de configuração, e pergunta ao usuário os dados que não estão nele. Com isso, monta a capa, a folha de identificação, o sumário com as páginas reais, as seções do relatório, as referências em ABNT e o anexo com telas, fotos dos integrantes e link do vídeo.

## O que o relatório contém

A capa segue o modelo institucional, com as linhas da instituição em negrito à esquerda e o logo à direita. No centro ficam o título e o tema, depois o grupo e os integrantes, e no pé da página a cidade e o mês/ano. Logo no início do texto há uma introdução breve com o endereço do repositório no GitHub e o endereço onde a aplicação está publicada.

O corpo segue a estrutura do Relatório Final do Grupo 05:

1. Introdução e visão.
2. Embasamento.
3. Objetivos, personas e cenários.
4. Recursos e backlog.
5. Requisitos.
6. Equipe, tecnologias e arquitetura, com linguagens e telas da aplicação.
7. Cronograma e DevOps.
8. Quadro de coerência.
9. Considerações finais.

A seção 10, Conclusão do grupo, tem uma subseção para cada critério da ficha individual de avaliação da Feira Integrada:

- Processo investigativo e registros.
- Integração curricular e domínio do conteúdo.
- Desenvolvimento e qualidade do trabalho.
- Impacto social, ética e sustentabilidade.
- Apresentação e comunicação.
- Colaboração e autoavaliação.

Fecham o relatório o histórico de revisões, as referências, as declarações (participação de cada integrante e uso de IA) e o Anexo A, com os prints das telas, as fotos dos integrantes e o link do YouTube ou TikTok.

## Como a Skill Funciona: Fluxo Interativo Passo a Passo

A skill opera de forma **estritamente interativa**. Ela não dispara questionários em bloco: conduz uma conversa guiada em 8 etapas, fazendo uma pergunta por vez e aguardando a resposta digitada pelo usuário antes de prosseguir:

1. **Instituição de Ensino, Curso e Evento** (com opção de informar arquivo de logotipo).
2. **Título, Tema do Projeto e Local/Data**.
3. **Equipe, Integrantes e Docente/Orientador(a)**.
4. **Endereços e Links** (Repositório GitHub, URL de produção e vídeo).
5. **Gestão de Telas e Prints (Com Opção Autônoma da Skill)**:
   - *Opção A:* A skill se oferece para rodar o projeto ou navegar na URL para tirar os prints automaticamente.
   - *Opção B:* O usuário indica o caminho da pasta onde as imagens já estão salvas.
   - *Opção C:* A skill cria a pasta guiada (`anexos/telas/` e `anexos/fotos/`) para a pessoa colocar os arquivos.
6. **Atribuições dos Integrantes e Declaração de Uso de IA**.
7. **Critérios de Avaliação e Limite de Páginas**.
8. **Resumo Geral e Pedido Explícito para Geração**: A skill consolida os dados, exibe um painel de conferência e pede autorização expressa (*"Deseja gerar o relatório agora?"*). Somente após o "Sim", ela gera o `relatorio.md` e compila o `relatorio.pdf`.

## Instalação

Para instalar no Claude (claude.ai ou aplicativo), compacte esta pasta e envie o arquivo .zip em Configurações, na área de Skills. Para usar no Claude Code, copie a pasta para `~/.claude/skills/projeto/`. No Antigravity, ela fica disponível globalmente em `I-A_Skills/projeto-304/.agent/skills/projeto`. Depois disso, basta pedir algo como "gere o relatório final deste projeto" ou ativar a skill `projeto`.

## Uso direto dos scripts

Também é possível gerar o PDF sem o Claude, a partir de um `relatorio.md` já escrito. Os requisitos são Python 3 com `reportlab` e `Pillow`, além do Poppler (`pdfinfo` e `pdftotext`) para montar o sumário. A fonte é Arial; se ela não estiver instalada, o script usa a Liberation Sans, que tem as mesmas medidas.

```bash
pip install reportlab pillow
cp scripts/gerar_relatorio.py scripts/montar_sumario.py scripts/config_exemplo.json minha_pasta/
cd minha_pasta && mv config_exemplo.json config.json   # editar capa, cabeçalho e rodapé
python3 montar_sumario.py config.json                  # gera relatorio.pdf com o sumário paginado
```

O `relatorio.md` usa marcadores próprios, descritos no SKILL.md. Os principais são `@CAP|` para o título de tabela ou figura, `@FONTE|` para a fonte, `@IMG|arquivo|largura` para imagens, `@FOTOS|a.jpg::Nome;b.jpg::Nome` para a grade de fotos e `<!-- quebra -->` para quebra de página.

## Estrutura do repositório

```
SKILL.md                    instruções da skill (estrutura, regras de escrita, conferência)
scripts/gerar_relatorio.py  gera o PDF a partir do relatorio.md e do config.json
scripts/montar_sumario.py   monta o sumário com as páginas reais e confere os títulos
scripts/config_exemplo.json modelo de configuração da capa, cabeçalho e rodapé
exemplo/                    relatório de teste com projeto fictício e o PDF gerado
```

## Regras que a skill segue

O texto é escrito em terceira pessoa, em linguagem acadêmica simples e de preferência em texto corrido. A skill não inventa dados, links nem referências: só usa o que está no projeto ou o que o usuário informa. As referências seguem a ABNT NBR 6023, sem data provável. Docentes em geral são tratados pela forma inclusiva "professora(o)".

## Autoria

Mizael Souto Gomes. Skill elaborada com apoio do Claude (Anthropic) a partir do Relatório Final do Grupo 05, disciplina EADDCC037 Projeto de Software Educacional, UFJF.

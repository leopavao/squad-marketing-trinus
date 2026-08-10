# Trinus Marketing Squad

Repositório operacional do Squad de Marketing da Trinus.

Este repositório é exclusivo da Trinus. Ele concentra contexto de marca, fatos, diretrizes, memória, agentes, playbooks e configurações necessárias para que diferentes assistentes de inteligência artificial trabalhem sobre a mesma fonte oficial.

## Compatibilidade

| Ferramenta | Arquivo de entrada |
|---|---|
| Claude Code | `CLAUDE.md` |
| ChatGPT / Codex | `AGENTS.md` |
| Gemini | `GEMINI.md` |
| Qualquer outro agente | este `README.md` + `squad.yaml` |

Os arquivos de entrada são adaptadores. Eles não devem duplicar contexto, regras de marca ou playbooks. A fonte canônica permanece nos arquivos compartilhados do repositório.

## Inicialização obrigatória

Todo agente deve:

1. Ler `squad.yaml`.
2. Ler `ARQUITETURA-CONTEUDO.md`.
3. Carregar os arquivos listados em `carrega_sempre`.
4. Ler os playbooks de pensamento antes de produzir.
5. Carregar o contexto da Trinus no caminho indicado em `squad.cliente`.
6. Classificar a demanda por camada e ativar somente os agentes necessários.
7. Respeitar os checkpoints, e tratar como cumprido apenas o checkpoint que gerou o arquivo declarado em `squad.yaml`, verificável por `python3 scripts/checar_gates.py <slug-da-peca>`.
8. Tratar a instrução mais recente do humano como prevalente.
8.1. Respeitar a **regra de desvio zero**: a gramática visual se copia do modelo mestre, o conteúdo se cria. O agente não introduz variação de layout, cor, escala ou universo fotográfico. Se achar que a peça pede desvio, ele para antes de produzir e pergunta. Ver `marca/memory/memoria-criativa.md` e `marca/design-system/gramatica-carrossel.md`.
9. Não alterar este repositório sem autorização explícita.
10. Acessar caminhos conhecidos diretamente quando busca ou indexação falhar.

## Escopo

A Trinus é a única marca deste repositório. Tudo que é específico dela vive em `marca/`; o resto (`core/`, `playbooks/`, `sala-de-comando/`) é o motor do squad. Um repositório, uma marca: não há suporte a múltiplos clientes por design.

## Arquivos e entregáveis

O GitHub guarda o cérebro textual e operacional do squad. Não versionar imagens, vídeos, áudios, PDFs, arquivos de design ou outros binários.

Peças finais e ativos visuais devem ser enviados ao Google Drive quando a integração estiver configurada. Até lá, o agente entrega localmente ou no canal solicitado, sem inserir binários no repositório.

Leia `core/politica-ativos.md`.

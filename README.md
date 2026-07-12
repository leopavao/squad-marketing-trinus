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
7. Respeitar os checkpoints.
8. Tratar a instrução mais recente do humano como prevalente.
9. Não alterar este repositório sem autorização explícita.
10. Acessar caminhos conhecidos diretamente quando busca ou indexação falhar.

## Escopo

A Trinus é a única marca deste repositório. O caminho `clients/trinus` é legado da arquitetura original e, enquanto existir, deve ser interpretado como o contexto oficial da Trinus, não como suporte ativo a múltiplos clientes.

## Arquivos e entregáveis

O GitHub guarda o cérebro textual e operacional do squad. Não versionar imagens, vídeos, áudios, PDFs, arquivos de design ou outros binários.

Peças finais e ativos visuais devem ser enviados ao Google Drive quando a integração estiver configurada. Até lá, o agente entrega localmente ou no canal solicitado, sem inserir binários no repositório.

Leia `core/politica-ativos.md`.

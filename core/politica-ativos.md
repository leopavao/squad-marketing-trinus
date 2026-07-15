# Política de ativos e entregáveis

## Princípio

O GitHub é o cérebro textual e operacional do Squad de Marketing da Trinus. O Google Drive é o destino de ativos, peças finais e arquivos binários.

## O que pertence ao GitHub

- Markdown, YAML, JSON e scripts
- contexto, fatos e referências descritas por texto ou link
- agentes, playbooks, memória e decisões
- roteiros, copies, briefings e manifestos de entrega
- metadados e links para arquivos externos
- logos oficiais mínimos da Trinus, conforme a exceção controlada abaixo

## Exceção controlada para logos oficiais

Os logos fundamentais da Trinus podem ser versionados em `marca/design-system/assets/logos/` para que qualquer agente consiga aplicar a marca corretamente.

A exceção é restrita a:

- lockup colorido
- lockup reverso
- ícone dourado
- variações oficiais do monograma

Esses arquivos devem ser fornecidos pela marca, manter nome estável e nunca ser recriados, redesenhados ou recoloridos pelo agente. A exceção não autoriza fotografias, peças finais, referências visuais, PDFs ou outros PNGs no GitHub.

Quando a marca fornecer vetores oficiais, prefira SVG. Enquanto os vetores não existirem, os PNGs transparentes oficiais podem permanecer como ativos operacionais mínimos.

## O que não pertence ao GitHub

- imagens e fotografias, exceto os logos oficiais previstos acima
- vídeos e áudios
- PDFs
- arquivos editáveis de design
- apresentações, planilhas e documentos binários
- pacotes compactados
- qualquer peça final pesada

A lista técnica de extensões bloqueadas e a exceção de logos ficam no `.gitignore`.

## Google Drive

Quando houver integração autorizada:

1. O agente produz ou recebe a peça.
2. Salva a peça na pasta definida no Drive.
3. Registra no entregável textual o nome, a versão e o link do arquivo.
4. Mantém no GitHub somente copy, briefing, decisões, metadados e links.

O pacote completo de identidade, incluindo PDF, arquivos editáveis, fontes e versões de distribuição, permanece no Drive. Nunca inventar um link de Drive. Sem integração disponível, entregar o arquivo pelo canal atual e informar que ele ainda não foi arquivado no Drive.

## Fonte de verdade

- Regras, contexto, copy e memória: GitHub.
- Logos operacionais mínimos: GitHub, no caminho canônico da marca.
- Arquivo visual, pacote-mestre ou binário final: Google Drive.
- Se houver divergência, o texto aprovado mais recente no GitHub governa a próxima produção.

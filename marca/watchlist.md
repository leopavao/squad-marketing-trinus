# Trinus — Watchlist do trend-hunter

> Fontes que o trend-hunter monitora. Definidas com o cliente, refinadas a cada ciclo. Usadas via API do Apify (tier grátis).
> Status: rascunho. Itens com ⛳ a validar/completar no discovery.

## Configuração Apify

- Token: ⛳ gerar conta Apify (grátis, US$5/mês) e colocar o token em variável de ambiente / config segura. Nunca commitar o token.
- Actors: `apify/instagram-scraper` (perfis abaixo) · `apify/google-trends-scraper` (keywords abaixo).
- Limite por run (tier grátis): poucos perfis, poucos posts por perfil, poucas keywords. Cadência mensal/quinzenal.

## Concorrentes / contas de referência (Instagram)

> ⛳ Pedir ao cliente: quem eles admiram, quem é concorrente direto, quem é referência de consórcio premium. Preencher os @ reais.

- ⛳ Concorrentes diretos (consultorias de consórcio premium): @____, @____
- ⛳ Contas de planejamento patrimonial / educação financeira de alta renda: @____, @____
- ⛳ Administradoras (referência de tom institucional, não pra copiar): consórcio Itaú, consórcio Bradesco.

## Palavras-chave (Google Trends)

Seed (refinar com o cliente):

- consórcio imóvel · consórcio contemplado · carta de crédito
- consórcio x financiamento · vale a pena consórcio
- planejamento patrimonial · alavancagem patrimonial
- consórcio de luxo / consórcio alto padrão
- lance consórcio · consórcio imóvel investimento
- ⛳ sazonais a observar: juros (Selic), mercado imobiliário, financiamento imobiliário taxa

## O que NÃO seguir como sinal

Mesmo que esteja bombando: parcelinha, sorteio, "realize seu sonho", contemplação garantida, isca de varejo. É o oposto do posicionamento premium. Serve como contraste, não como pauta.

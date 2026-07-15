# Trinus Consórcios — Sistema de marca

Fonte da verdade visual. Tudo aqui foi **extraído da identidade oficial**
(`ID_TRINUS.pdf` + arquivos de logo), não inventado.

## A marca em uma linha
Consultoria de planejamento patrimonial via consórcio (imóveis, veículos e
bens de alto valor; administradoras Itaú e Bradesco). Público de alta renda.
Posicionamento: premium, técnico, consultivo, estratégico, racional.
**Frase-mãe:** *“Consórcio não começa pela carta. Começa pelo objetivo.”*

## Logo
Arquivos oficiais em `assets/logos/`. **Nunca recriar em fonte parecida.**

| Arquivo | Uso |
|---|---|
| `trinus-lockup-color.png` | Primário. Wordmark navy + ícone dourado, sobre claro. |
| `trinus-lockup-reverse.png` | Wordmark branco + ícone dourado, sobre navy / roxo / petróleo. |
| `trinus-icone-dourado.png` | Ícone isolado (pilha dourada). Favicon, watermark, selo. |
| `trinus-monograma-t-escudo.png` | Monograma “T” em escudo, dourado. Sobre navy/claro. |
| `trinus-monograma-t-navy.png` | Monograma navy, sobre dourado/claro. |
| `trinus-monograma-t-branco.png` | Monograma branco, sobre preto/navy. |

Regras: respiro mínimo ao redor = altura do ícone; nunca aplicar wordmark
navy sobre fundo escuro (usar o reverse); não distorcer, não recolorir fora
das três variações de monograma fornecidas.

## Cor (valores reais)
| Papel | Token | Hex |
|---|---|---|
| Navy institucional — **primária** | `--trinus-navy` | `#1E3C72` |
| Navy profundo | `--trinus-navy-deep` | `#16305C` |
| Dourado — **acento** | `--trinus-gold` | `#F0C850` |
| Roxo — suporte | `--trinus-purple` | `#8A42A8` |
| Petróleo — suporte | `--trinus-azure` | `#2C7BA6` |
| Azul-céu — suporte | `--trinus-sky` | `#60B4E4` |
| Grafite — texto | `--graphite` | `#36404F` |
| Papel — fundo | `--paper` | `#F6F7F9` |
| Preto | `--ink` | `#1A1A1A` |

**Disciplina de acento.** Premium aqui é contido: navy estrutura ~80% dos
pixels; dourado aparece no máximo 1–2 vezes por peça (régua, eyebrow, selo,
numeral, um CTA); roxo/petróleo/céu só codificam pilares, com parcimônia.

**Contraste (regras, não enfeite).**
- Dourado **nunca** vira texto sobre branco (~1.4:1). Texto dourado só sobre
  navy/preto. Sobre claro, dourado é preenchimento / régua / numeral grande.
- Navy sobre claro e branco sobre navy: ~9.6:1, livres para texto.
- Petróleo sobre branco: só ≥18px ou bold.

## Tipografia
- **Fenora** (Latinotype, licenciada) — títulos e destaques.
  Proxy open-source: **Playfair Display** (carregado no `styles.css`).
- **Montserrat** (open-source, Google Fonts — fonte real da marca) — texto
  corrido, labels, chips, botões, dados.
- Três pesos: 400 (ler) · 500–600 (enfatizar) · 700 (anunciar, serif).
- Tracking: display fechado (`-0.02em`); CAIXA ALTA aberta (`0.12em`);
  eyebrow bem aberto (`0.26em`).

## Elementos (`tokens/elements.css`, prefixo `.trn-`)
eyebrow · lockup-line · tagline editorial (uma ideia em itálico) · réguas
(hairline + barra-assinatura dourada) · frames (navy/ouro/inset) · blocos de
cor · selo/pin (monograma em círculo) · cantos de registro · tratamento de
foto (duotone navy + scrim + legenda na borda) · chips de pilar · botões/CTA
· numeral · **número-âncora** (cifra serif + rótulo + leitura de variação,
para comparativos financeiros).

## Princípios de layout
- Muito espaço em branco; hierarquia por tamanho **e** família (serif anuncia,
  sans informa).
- Uma ideia por peça. Um acento por peça.
- Foto sempre tratada (duotone navy) para não competir com o texto.
- Disclaimers e projeções ficam pequenos, na borda, rotulados como ilustrativos.

## Estrutura de arquivos
```
design-system/
  styles.css            ← importe este (fontes + todos os tokens)
  tokens/colors.css
  tokens/typography.css
  tokens/spacing.css
  tokens/elements.css
  assets/logos/*.png
index.html              ← folha de especímen (raiz, renderiza no preview)
demo-carrossel.html     ← composição-exemplo 4:5 em tamanho real
```

# Padrão de Kit de Aprovação — GTM MKT Squad

> Aprovado em jun/2026. É assim que o squad entrega. Toda campanha nova segue este padrão.

---

## O que é o kit

Um arquivo HTML por território (`kit-[produto]-territorio-[letra].html`) que serve como **board de aprovação** antes de qualquer exportação de PNG. Reúne defesa de campanha + criativos prontos para revisar + copy completo.

---

## Estrutura do arquivo

### 1. Header da página (navy)
- Logo do cliente (branca, `design-system/assets/logos/`)
- Eyebrow: `[Produto] · Território [Letra]`
- Barra de accent (cor do cliente)
- Título do território (headline humana, não código)

### 2. Defesa de campanha
Cards horizontais com:
- Por que este território?
- Insight
- Gatilho / mecanismo emocional
- Qualquer compliance ou decisão de copy relevante
- Box com o headline aprovado + CTA

### 3. Feed 4:5 (estático patrocinado)
- Criativo puro: `width:380px; height:475px` — sem mockup, sem chrome
- Barra de accent (7px) no topo como accent de marca
- Gradient escuro sobreposto na parte inferior
- Headline + subtítulo + CTA pill
- Painel de copy ao lado direito: texto na arte + legenda completa

### 4. Stories / Reels 9:16 — **mínimo 3 variantes**
- 3 colunas lado a lado: A · B · C (rótulo acima de cada uma)
- Cada story: `width:240px; height:426px`, border-radius 14px, sem frame de celular
- Chrome do Instagram embarcado dentro do criativo (progress bars + avatar placeholder no topo)
- Copy panel pequeno abaixo de cada story (não ao lado)
- Legenda compartilhada abaixo das 3 colunas
- Variantes típicas: Racional / Produto / Emocional

### 5. Carrossel — todas as fotos/imagens disponíveis
- Grid 4 colunas, cards `220×220px`
- Card 01: hook textual (overlay navy escuro + texto forte, sem subtítulo de lazer)
- Cards 02 a N: todas as fotos do produto com legenda de 1 linha
- Último card: navy sólido + headline de CTA + pill de cor
- Legenda compartilhada + primeira mensagem de canal direto abaixo do grid

---

## Regras visuais do criativo

- **Sem mockup** — o criativo aparece no tamanho certo, limpo, sem chrome externo (sem Mac bar, sem frame de celular, sem engagement row)
- **Sem logo badge sobrepost à foto** — o logo do cliente aparece no header da página e no card CTA
- Fundo da página: tom neutro (ex.: `#dedad5`) com grid de pontos (contextualiza sem distrair)
- Sombra sutil nos criativos
- Fonte: definida pelo design system do cliente (`brand/DESIGN.md`)

---

## Regras de copy

- Texto na arte: um argumento por peça, mínimo absoluto de palavras
- Disclaimers de compliance: sempre na legenda, nunca na arte
- Nenhum número inventado: resultado, prazo, condição — só se confirmado
- CTA coerente com o canal de contato do cliente
- Sem travessões. Sem emoji em feed/carrossel. Emoji aceito em Stories e canal direto

---

## Aprovação antes de exportar

Gate obrigatório:
1. **Território aprovado** (headline + insight + foto hero OK?)
2. **Arte aprovada** (composição, foto, copy na arte OK?)
3. **Copy aprovada** (legenda + primeira mensagem de canal direto OK?)

Só exportar PNG após os 3 gates. Exportação: Chrome headless, PNG 2x.

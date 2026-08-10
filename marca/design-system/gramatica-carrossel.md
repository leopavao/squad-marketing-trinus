# Gramática do carrossel Trinus

Este arquivo descreve, em medidas, o carrossel aprovado da Trinus. Ele existe porque adjetivo não reproduz layout. "Premium editorial navy" já produziu peça errada mais de uma vez.

Referência de origem: carrossel `COMPRAR-A-VISTA-NEM-SEMPRE`, 7 telas, aprovado pelo cliente. Referência mestra vigente.

> **Precedência.** Esta gramática governa peças de carrossel e story. Onde ela divergir de `tokens/typography.css`, ela vence. Os tokens foram escritos para página web e subdimensionam tipografia em canvas 1080.

> **Desvio zero.** A gramática se copia. O conteúdo se cria. Nada aqui é sugestão. O agente que achar que a peça pede algo fora destas medidas para antes de produzir e pergunta ao humano, dizendo qual regra pretende quebrar, por quê e o que muda no resultado. Variação só existe quando o humano pede uma segunda versão de referência ou autoriza um desvio específico, e vale para uma peça só. Ver `marca/memory/memoria-criativa.md`, seção "Regra de desvio zero".

---

## 1. Canvas e grade

- Formato: 4:5, `1080 x 1350`.
- Margem viva: `88px` em todos os lados. Nenhum texto, régua ou logo cruza essa linha.
- Coluna de texto: começa na margem esquerda e ocupa no máximo `56%` da largura.
- A metade direita pertence à fotografia. Quando não há fotografia, ela fica vazia de propósito.

## 2. Escala tipográfica em canvas (sobrescreve os tokens web)

| Papel | Família | Tamanho | Entrelinha | Tracking |
|---|---|---|---|---|
| Eyebrow | Montserrat 600 caps | `22px` | 1.0 | `0.26em` |
| Headline | Fenora / Playfair 700 | `96px` a `112px` | 1.02 | `-0.02em` |
| Subtítulo | Montserrat 400 | `34px` a `38px` | 1.45 | `0` |
| Número-âncora | Fenora / Playfair 700 | `150px` a `190px` | 1.0 | `-0.03em` |
| Label de card | Montserrat 600 caps | `19px` | 1.2 | `0.16em` |
| Corpo de card | Montserrat 400 | `28px` | 1.5 | `0` |

**Regra de ocupação da headline.** A caixa da headline ocupa entre `26%` e `34%` da altura do canvas. Abaixo disso a tela fica tímida e a peça perde a assinatura. Máximo de três linhas.

**Itálico como acento.** Exatamente uma palavra por headline em itálico, quando a frase tiver um pivô conceitual. Nunca duas.

## 3. Cor

| Papel | Valor | Observação |
|---|---|---|
| Fundo claro | creme quente | confirmar amostragem no arquivo-fonte; `--paper` `#F6F7F9` é frio demais e não corresponde à mestra |
| Fundo escuro | `--trinus-navy-deep` `#16305C` | telas de virada |
| Headline sobre claro | `--trinus-navy` `#1E3C72` | |
| Headline sobre escuro | branco | |
| Subtítulo sobre claro | `--graphite` `#36404F` | |
| Acento | `--trinus-gold` `#F0C850` | |

**Disciplina do dourado.** Ele aparece como filete do eyebrow, régua sob a headline, numeração, contorno de ícone, contorno de card, contorno de CTA e no máximo uma palavra em destaque. Nunca preenche área. Nunca vira texto corrido sobre fundo claro.

**Madeira, terracota, bege e verde estão fora.** A Trinus é navy sobre creme, com dourado. Qualquer fotografia que traga marrom ou madeira como cor dominante reprova a tela.

## 4. Ritmo claro e escuro

O carrossel alterna. Não se escolhe uma linha para a peça inteira.

- Entre `25%` e `35%` das telas são navy.
- As telas navy caem nas viradas: onde a tese é cravada e onde o CTA fecha.
- As demais são creme.

Referência de origem: claro, claro, claro, **navy**, claro, claro, **navy**.

## 5. Fotografia

**Uma cena, muitos enquadramentos.** O carrossel usa uma única locação ou objeto arquitetônico, reenquadrado tela a tela. Sete fotografias diferentes quebram a peça, mesmo que cada uma seja boa.

Universo visual: arquitetura monumental e patrimonial. Colunata, escadaria, concreto claro, pedra, vão. Escala institucional, sem pessoas, sem mobiliário, sem decoração.

Tratamento:
- lavada, contraste baixo, quase fantasma;
- ancorada à direita ou ao canto, sangrando nas bordas;
- nunca atrás de texto sem scrim;
- nunca com o logo por cima.

Quando a tela for navy, a mesma cena aparece rebaixada dentro do navy, mantendo a continuidade.

## 6. Anatomia fixa da tela

De cima para baixo, na coluna esquerda:

1. filete dourado curto, `56px` de largura, `3px` de espessura;
2. eyebrow com numeração, separador em traço e rótulo, formato `02 - A TROCA`;
3. headline;
4. régua dourada, `140px` de largura, `3px` de espessura;
5. subtítulo, até duas linhas;
6. conteúdo variável, quando houver;
7. logo lockup, canto inferior esquerdo, largura `185px`.

**Um só sistema de numeração por tela.** A numeração vive no eyebrow. Não existe numeração no canto oposto.

**O logo mora embaixo à esquerda.** Sempre. Mesma escala em todas as telas. Sobre fundo limpo.

**Não existe rodapé recorrente.** Nenhuma frase se repete nas telas. A linha de fecho aparece uma vez, na tela de fecho, em corpo de headline.

## 7. Densidade

Uma ideia por tela. Quando houver cards, no máximo dois lado a lado, com contorno de linha fina e ar interno generoso. Listas de quatro itens usam dois por linha, com numeração serifada em dourado.

Respiro vem de headline grande com vazio em volta. Vazio com tipografia pequena no meio da tela é tela abandonada, e reprova.

## 8. Copy

A headline carrega a tese. O subtítulo carrega a consequência. Pelo menos uma tela do carrossel precisa ancorar em número concreto ou objeto concreto. Carrossel inteiro em abstração consultiva reprova.

## 9. Checklist de reprovação automática

Uma resposta positiva em qualquer item devolve a peça para produção antes de chegar ao humano.

1. A fotografia traz madeira, mobiliário, decoração ou pessoas.
2. Há mais de uma locação fotográfica no conjunto.
3. Alguma headline ocupa menos de 26% da altura da tela.
4. O logo está no topo, sobre fotografia, ou em escalas diferentes entre telas.
5. Existem dois sistemas de numeração na mesma tela.
6. Alguma frase se repete em três ou mais telas.
7. Menos de 25% ou mais de 35% das telas são navy.
8. O dourado preenche área ou aparece como texto corrido sobre fundo claro.
9. O CTA está em contraste baixo, sem borda dourada ou sem fundo navy.
10. Nenhuma tela do conjunto ancora em número ou objeto concreto.
11. A coluna de texto invade a metade direita reservada à fotografia.
12. A composição muda de estrutura entre telas sem função narrativa.

## 10. Pendências de medição

Os valores marcados abaixo foram estimados por observação da peça mestra e precisam ser confirmados contra o arquivo-fonte quando ele estiver acessível ao agente:

- hex exato do creme de fundo;
- tamanho exato da headline em px;
- largura e espessura exatas das réguas;
- escala exata do lockup.

Enquanto a confirmação não acontece, os valores acima valem como especificação vigente.

# Casos de falha nomeados

Reprovações com valor didático. Cada caso descreve o que foi entregue, o que a referência pedia e qual trava passou a existir por causa dele.

Um caso só sai daqui quando a trava correspondente estiver provada em produção.

---

## 2026-08-10 — Carrossel "O preparo estratégico"

**Situação.** Peça de 8 telas produzida tendo como referência mestra o carrossel `COMPRAR-A-VISTA-NEM-SEMPRE`, aprovado pelo cliente. A entrega foi reprovada pelo cliente.

**O que a referência mestra tem.** Uma única arquitetura monumental, colunata com escadaria, reenquadrada nas sete telas. Navy como estrutura, creme como papel, dourado como acento pontual. Headline serifada ocupando cerca de um terço da altura. Logo fixo no canto inferior esquerdo. Ritmo alternando três telas claras, uma navy, duas claras, uma navy. Uma tela ancorando em número concreto.

**O que foi entregue.** Oito fotografias diferentes de decoração de interiores: portais de madeira, sofá, pátio com oliveira, ripado, corredor escuro. Madeira e bege dominando sete das oito telas. Headline em corpo pequeno, com vazio sem tensão em volta. Logo no topo, reduzido, e aplicado por cima da fotografia na tela 05. Dois sistemas de numeração na mesma tela. A linha de fecho repetida como rodapé nas oito telas. CTA em caixa cinza clara sobre fundo claro. Uma única tela navy. Copy inteiramente abstrata, sem nenhum número.

**Causa raiz.** O agente nunca abriu a peça mestra. Ela estava no Google Drive, e não existe ferramenta configurada que abra uma pasta do Drive e devolva imagem. O checkpoint `consultar-memoria-criativa` foi cumprido lendo a descrição textual da peça: "premium, editorial, navy, dourado, muito espaço negativo". A entrega atende cada um desses adjetivos e não se parece com a Trinus.

**Causa secundária.** `tokens/typography.css` fecha `--fs-display` em 68px, escala pensada para página web. Num canvas de 1080x1350 isso produz headline tímida. O designer obediente ao token erra por obediência.

**Causa terciária.** `memoria-criativa.md` mandava "escolher conscientemente entre a linha clara, a linha escura ou uma variação coerente". A peça aprovada usa as duas dentro do mesmo carrossel, como ferramenta de ritmo. A regra empurrava para o carrossel monocromático.

**Travas criadas.**

1. `marca/design-system/gramatica-carrossel.md`, com medidas em vez de adjetivos e checklist de reprovação automática.
2. A escala de canvas passa a sobrescrever os tokens web em peça de social.
3. A regra de escolher uma linha editorial foi substituída pela regra de alternância.
4. `consultar-memoria-criativa` e `comparar-referencias-aprovadas` passam a exigir arquivo de saída. Checkpoint sem artefato é autodeclaração.

**Regra derivada, aplicável a qualquer marca.** Referência visual que o agente não consegue abrir não funciona como referência. Ou o arquivo fica onde o agente lê, ou a gramática dele é transcrita em medidas. Descrição em adjetivo é a terceira via, e ela produz peça genérica.

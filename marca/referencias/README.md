# Biblioteca de referências

Cada peça que o cliente aprovar entra aqui. O HTML fica no GitHub porque é texto, versiona, dá diff e qualquer agente lê e renderiza. A arte final e os arquivos pesados ficam no Drive.

## As três camadas

**Invariante.** Não se mexe sem decisão do humano. Hex dos tokens, famílias e pesos de fonte, escala tipográfica de canvas, grade e margens, regras do logo, disciplina do dourado, universo fotográfico. Tudo isso vive em `marca/design-system/base-carrossel/base.css` e em `marca/design-system/gramatica-carrossel.md`.

**Biblioteca.** Cresce a cada aprovação. É o repertório de composições que o time pode reusar e recombinar.

**Livre.** Tese, copy, dado, narrativa, ordem e função das telas, enquadramento fotográfico. É aqui que a criatividade trabalha.

## Estrutura de uma referência

```
marca/referencias/AAAA-MM-DD-tema-curto/
├── index.html          ← linka ../../design-system/base-carrossel/base.css
├── ficha.md            ← metadados, link do Drive, prompt da locação
└── assets/
    └── locacao-01.jpg  ← a imagem base, reduzida, só para o agente enxergar
```

O HTML de uma peça **não declara cor, fonte nem medida de grade**. Ele linka a base. Se um valor precisa mudar, muda na base, e muda para todas as peças. Hex escrito dentro de uma peça reprova na verificação automática.

## A regra da locação única

Um carrossel usa uma locação fotográfica. Todas as telas apontam para o **mesmo** `src`. O que muda de tela para tela é o `object-position`.

```html
<img class="photo" src="assets/locacao-01.jpg" style="object-position: 78% 50%" alt="">
```

Isso torna a continuidade visual uma consequência do código. Sete telas apontando para o mesmo arquivo não conseguem divergir de universo visual, que foi exatamente o que quebrou a peça reprovada em 2026-08-10.

O tratamento da foto (dessaturação, contraste, brilho, opacidade e scrim) está travado na classe `.photo` da base. Ele não se ajusta por peça.

## Como renderizar e ver

```
python3 scripts/renderizar.py marca/referencias/AAAA-MM-DD-tema-curto
```

Gera o PNG de cada tela em 1080x1350 e uma prancha de conferência. Serve para o agente comparar a peça nova com a referência sem depender do Drive.

## Como registrar uma referência nova

1. O cliente aprova a peça.
2. A arte final vai para o Drive, na pasta da publicação.
3. O HTML vem para cá, numa pasta com a data e o tema.
4. A `ficha.md` registra o link do Drive, a data de aprovação, o território, o prompt que gerou a locação e para que serve esse padrão.
5. O índice em `marca/memory/indice-criativos.md` ganha o registro.

Referência sem HTML aqui não conta como referência, porque nenhum agente consegue abrir uma pasta do Drive.

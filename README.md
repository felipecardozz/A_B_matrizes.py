# A_B_matrizes.py
modelo de futuro código 

Um certo jogo tem um vencedor quando este atinge 3 pontos à frente do oponente. 2 jogadores A e B estão jogando e, num determinado momento, A está 1 ponto à frente de B. Os jogadores têm probabilidades iguais de obter 1 ponto. Qual é a probabilidade de A vencer o jogo?
 (A) 1/2 (B) 2/3 (C) 3/4 (D) 4/5 (E) 5/6

Valor inicial de pontos/vetor estado inicial

D = m(0&0&0&0&1&0&0) 

Onde cada elemento representa a vantagem de A sobre B:
• D11 = -3 (B vence e jogo acaba)
• D12 = -2
• D13 = -1
• D14 = 0 (jogo empatado)
• D15 = +1 (Como jogo começa)
• D16 = +2
• D17 = +3 (A vence e jogo acaba)

A matriz T é usada para modelar a probabilidade de cada jogador ganhar um ponto em uma única rodada, incluindo os estados onde o jogo já terminou (+3 ou -3).

T= ■(1&0&0&0&0&0&0@0.5&0&0.5&0&0&0&0@0&0.5&0&0&0&0&0@0&0&0.5&0&0.5&0&0@0&0&0&0.5&0&0.5&0@0&0&0&0&0.5&0&0.5@0&0&0&0&0&0&1)

• Linhas: estado onde o jogo ocorre (linha 1 A=-3, linha 2 A=-2, linha 3 A=-1, linha 4 A=0, ...)
• Colunas: apresentam para qual dos jogadores o próximo ponto é destinado e a probabilidade de isso ocorrer, junto com a impossibilidade de nova rodada sem pontos se a linha não indicar um dos extremos
Ex.1 extremos não apresentam probabilidade de próximo estado (T11 e T77)
Ex.2 No estado 2, A está com uma desvantagem de -2 pontos (T21), apresentando 50% de perder a partida (T21) e 50% de ganhar 1 ponto (T23)

Dessa forma D apresenta apenas uma única linha que mostra a pontuação que é modificada enquanto ocorre a multiplicação por T.

Para achar a probabilidade de A vencer D’, basta multiplicar a matriz D por T: 
D’ = DT   [cálculo no programa A_B_matrizes.py]

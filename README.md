# S.O. 2025.1 - Atividade 2.02 - Gestão de memória

## Informações gerais

- **Objetivo do repositório**: Repositório para atividade avaliativa dos alunos
- **Assunto**: Gestão de memória
- **Público alvo**: alunos da disciplina de SO (Sistemas Operacionais) do curso de TADS (Superior em Tecnologia em Análise e Desenvolvimento de Sistemas) no CNAT-IFRN (Instituto Federal de Educação, Ciência e Tecnologia do Rio Grande do Norte - Campus Natal-Central).
- disciplina: **SO** [Sistemas Operacionais](https://github.com/sistemas-operacionais/)
- professor: [Leonardo A. Minora](https://github.com/leonardo-minora)
- Repositótio do aluno: [Daniel Braga](https://github.com/DanielBR0612)

## Tarefas do aluno
1. Fork desse repositório e atualizar a linha 10 com o nome e link do github
2. Ler a descrição da atividade
3. Montar a resposta no final deste arqivo, no tópico **Resposta**

---

## 1. Descrição da atividade
### 1.1. Objetivo
Praticar os conceitos de alocação de memória (best-fit), memória virtual e desfragmentação em um sistema com memória limitada.

---

### 1.2. Contexto
Um computador possui apenas **64 KB de RAM** e um **disco rígido para memória virtual**. O sistema operacional deve gerenciar 5 processos com tamanhos diferentes, cuja soma ultrapassa a capacidade da RAM.

#### 1.2.1. Processos iniciais

| Processo | Tamanho (KB) |
|----------|-------------|
| P1       | 20          |
| P2       | 15          |
| P3       | 25          |
| P4       | 10          |
| P5       | 18          |
| **Total**| **88 KB**   |

- **Memória RAM**: 64 KB (contígua, inicialmente vazia).  
- **Memória Virtual (Disco)**: Espaço ilimitado para paginação.

#### 1.2.2. Alocação Inicial com Best-Fit
Os alunos devem simular a alocação dos processos na RAM usando o algoritmo **best-fit**.  
- A memória RAM será representada como um bloco contíguo (ex: `[0KB - 64KB]`).  
- Devem alocar os processos nos menores espaços livres que atendam ao seu tamanho.  

**Alocação inicial**:  
1. P1 (20 KB) → Ocupa [0-20].  
2. P2 (15 KB) → Ocupa [20-15].  
3. _continuar a partir daqui_

#### 1.2.3. Simular Memória Virtual (Paginação)
- Os processos não alocados na RAM devem ser "paginados" no disco.  
- Criar uma tabela de páginas indicando quais partes estão na RAM e quais estão no disco.  

#### 1.2.4. Desfragmentação da RAM
- Desfragmentar a RAM para liberar espaço contíguo.
- Após desfragmentação (compactação), verificar quais processos podem ser alocado.  

### 1.3. Questões para Reflexão
1. Best-fit foi mais eficiente que first-fit ou worst-fit neste cenário?  
2. Como a memória virtual evitou um deadlock?  
3. Qual o impacto da desfragmentação no desempenho do sistema?  

---

## Resposta

### 1. Alocação Inicial com Best-Fit

Após aplicar o algoritmo best-fit, os processos P1, P2 e P3 foram alocados na RAM, ocupando 60 KB. Os processos P4 e P5 não couberam.

Mapa Final da RAM:
| Ocupado por | Tamanho |
| :--- | :--- |
| Processo P1 | 20 KB |
| Processo P2 | 15 KB |
| Processo P3 | 25 KB |
| Livre | 4 KB |

### 2. Simular Memória Virtual (Paginação)

 Na RAM: P1, P2, P3.

 No Disco (Memória Virtual): P4, P5.

### 3. Desfragmentação da RAM

A memória já estava desfragmentada (sem buracos entre os processos). A compactação resultou em um único bloco livre de 4 KB, que ainda era pequeno demais para carregar P4 (10 KB) ou P5 (18 KB) do disco.

### 4. Questões para Reflexão

 Best-fit foi mais eficiente que first-fit ou worst-fit neste cenário?
 Não. Para esta situação específica, os três algoritmos teriam produzido exatamente o mesmo resultado.

 Como a memória virtual evitou um deadlock?
 Ela evitou que o sistema travasse ou rejeitasse os processos P4 e P5 por falta de RAM. Ao colocá-los no disco, o sistema pôde continuar funcionando e executá-los mais tarde.

 Qual o impacto da desfragmentação no desempenho do sistema?
 A desfragmentação é um processo lento que consome recursos e causa pausas no sistema. Embora possa liberar um bloco de memória maior, neste caso não teve benefício prático, pois o espaço liberado foi insuficiente.



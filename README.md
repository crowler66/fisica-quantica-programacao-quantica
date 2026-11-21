# Laboratório de Física Quântica e Programação Quântica

> **Este é um  laboratório computacional para investigar matematicamente a relação entre estados quânticos, números complexos, fase, geometria, interferência, ondas e informação.**

## 1. Apresentação do projeto

Este projeto propõe a construção de um laboratório numérico em Python para estudar conceitos fundamentais da física quântica e da programação quântica.

A investigação parte de uma sequência de conceitos:

**Estado quântico → Amplitude → Número complexo → Fase → Transformação → Interferência → Medição.**

O laboratório utiliza matemática tradicional, álgebra, trigonometria, números complexos, matrizes e programação para representar e investigar esses fenômenos.

São utilizados dois ambientes computacionais complementares:

- **Debian Linux:** sistema operacional utilizado como ambiente de desenvolvimento, execução e experimentação.
- **IBM Qiskit:** ferramenta de programação quântica utilizada para construir circuitos, representar estados e executar simulações.

O objetivo é criar uma base experimental computacional que permita estudar as relações entre informação, fase, geometria e descrição física.

## 2. Fundamentos matemáticos: começando pela álgebra tradicional

Para compreender o comportamento de um qubit, precisamos primeiro compreender como funciona uma combinação de amplitudes.

Um qubit possui dois estados fundamentais, representados por:

- Estado zero: |0⟩
- Estado um: |1⟩

Um estado quântico pode ser representado por:

|ψ⟩ = a|0⟩ + b|1⟩

Onde a e b são amplitudes matemáticas.

Essas amplitudes podem conter números reais e imaginários.

Para que o estado esteja normalizado, precisamos satisfazer:

a² + b² = 1

Essa expressão é a forma simplificada para amplitudes reais. No caso geral, com amplitudes complexas, utilizamos:

|a|² + |b|² = 1

A probabilidade de encontrar o estado zero é o módulo de a elevado ao quadrado.

P(0) = |a|²

A probabilidade de encontrar o estado um é:

P(1) = |b|²

Portanto:

P(0) + P(1) = 1

Essa é a condição de normalização das probabilidades.

## 3. Números complexos e fase

Um número complexo possui duas partes:

z = x + yi

Onde:

- x é a parte real.
- y é a parte imaginária.
- i é a unidade imaginária, definida por i² = -1.

Podemos representar um número complexo utilizando trigonometria:

z = r(cos φ + i sen φ)

Onde r representa o módulo e φ representa o argumento, ou fase, do número complexo.

Pela identidade de Euler:

e^(iφ) = cos φ + i sen φ

Assim:

z = r e^(iφ)

Essa representação é importante porque permite interpretar a multiplicação por um número complexo de módulo 1 como uma rotação no plano complexo.

Por exemplo, para φ = 90 graus:

e^(i90°) = cos 90° + i sen 90°

e^(i90°) = 0 + i

e^(i90°) = i

O resultado corresponde a uma rotação de 90 graus no plano complexo.

## 4. Operador de fase

O operador utilizado no laboratório é:

U(φ) = [ 1       0 ]
       [ 0    e^(iφ) ]

Ele atua sobre o estado:

|ψ⟩ = a|0⟩ + b|1⟩

Aplicando a transformação:

U(φ)|ψ⟩ = a|0⟩ + be^(iφ)|1⟩

Isso significa que a primeira amplitude permanece inalterada, enquanto a segunda recebe uma transformação de fase.

Substituindo a identidade de Euler:

be^(iφ) = b(cos φ + i sen φ)

Podemos escrever:

U(φ)|ψ⟩ = a|0⟩ + b(cos φ + i sen φ)|1⟩

O módulo das amplitudes permanece igual.

Consequentemente, as probabilidades de medição na base computacional não mudam apenas pela aplicação desse operador.

Entretanto, a fase relativa pode produzir diferenças observáveis quando o estado passa por outra transformação.

## 5. Experimento matemático: interferência com portas Hadamard

O laboratório utiliza o circuito:

H → U(φ) → H

A porta Hadamard é representada por:

H = 1/√2 [ 1   1 ]
          [ 1  -1 ]

Considerando o estado inicial:

|ψ⟩ = |0⟩

Aplicando a primeira porta Hadamard:

H|0⟩ = (|0⟩ + |1⟩)/√2

O estado agora possui duas amplitudes iguais.

Aplicando o operador de fase:

U(φ)H|0⟩ = (|0⟩ + e^(iφ)|1⟩)/√2

Aplicando a segunda porta Hadamard:

HU(φ)H|0⟩ = [(1 + e^(iφ))/2]|0⟩ + [(1 - e^(iφ))/2]|1⟩

Agora vamos desenvolver essa expressão utilizando álgebra e trigonometria.

Sabemos que:

e^(iφ) = cos φ + i sen φ

Portanto:

1 + e^(iφ) = 1 + cos φ + i sen φ

E:

1 - e^(iφ) = 1 - cos φ - i sen φ

As amplitudes finais são:

A(0) = (1 + cos φ + i sen φ)/2

A(1) = (1 - cos φ - i sen φ)/2

Para calcular as probabilidades, utilizamos o módulo ao quadrado de cada amplitude.

Para o estado zero:

P(0) = |A(0)|²

P(0) = [(1 + cos φ)² + sen² φ]/4

Desenvolvendo o quadrado:

P(0) = [1 + 2 cos φ + cos² φ + sen² φ]/4

Como:

cos² φ + sen² φ = 1

Obtemos:

P(0) = (2 + 2 cos φ)/4

Simplificando:

**P(0) = (1 + cos φ)/2**

Utilizando a identidade trigonométrica:

cos²(φ/2) = (1 + cos φ)/2

Chegamos a:

**P(0) = cos²(φ/2)**

Agora, para o estado um:

P(1) = |A(1)|²

P(1) = [(1 - cos φ)² + sen² φ]/4

Desenvolvendo:

P(1) = [1 - 2 cos φ + cos² φ + sen² φ]/4

Aplicando a identidade trigonométrica:

P(1) = (2 - 2 cos φ)/4

Simplificando:

**P(1) = (1 - cos φ)/2**

Portanto:

**P(1) = sen²(φ/2)**

Esses resultados demonstram matematicamente como uma fase relativa pode ser convertida em diferenças nas probabilidades de medição por meio da interferência.

## 6. Esfera de Bloch: geometria do qubit

A esfera de Bloch é uma representação geométrica do estado puro de um qubit.

Considerando:

|ψ⟩ = a|0⟩ + b|1⟩

Podemos representar o estado utilizando três coordenadas:

x = 2 Re(a* b)

y = 2 Im(a* b)

z = |a|² - |b|²

Uma parametrização tradicional utiliza dois ângulos:

a = cos(θ/2)

b = e^(iφ) sen(θ/2)

Portanto:

x = sen θ cos φ

y = sen θ sen φ

z = cos θ

Essas coordenadas obedecem à equação da esfera:

x² + y² + z² = 1

A fase relativa φ determina a posição angular em torno do eixo vertical.

O ângulo θ determina a posição em relação aos polos.

Essa representação é matemática e não significa que o qubit seja literalmente uma esfera física.

## 7. Relação matemática entre fase e ondas

O laboratório também utiliza uma representação de onda complexa:

ψ(x,t) = e^(i(kx - ωt))

Pela identidade de Euler:

ψ(x,t) = cos(kx - ωt) + i sen(kx - ωt)

A fase pode ser escrita como:

φ(x,t) = kx - ωt

Para observar como a fase muda em relação à posição, calculamos:

dφ/dx = k

Isso significa que a fase varia proporcionalmente à coordenada espacial no modelo de onda plana.

Para três dimensões:

φ(r,t) = k · r - ωt

E:

∇φ = k

O laboratório utiliza essas expressões para comparar matematicamente a fase de uma onda com a fase relativa presente nos estados quânticos.

Essa comparação é investigativa. Não estabelece que os dois conceitos sejam fisicamente idênticos.

## 8. Modelo de onda eletromagnética

Para complementar os experimentos, o programa utiliza uma representação simplificada de uma onda eletromagnética plana.

O campo elétrico é:

E(x,t) = E₀ cos(kx - ωt)

O campo magnético é:

B(x,t) = (E₀/c) cos(kx - ωt)

Onde:

- E₀ representa a amplitude do campo elétrico.
- c representa a velocidade da luz no vácuo.
- k representa o número de onda.
- ω representa a frequência angular.
- x representa a posição.
- t representa o tempo.

Para estudar o fluxo de energia, utilizamos a relação:

S = (1/μ₀) E × B

Essa expressão representa o vetor de Poynting na descrição eletromagnética clássica.

Para uma onda que se propaga na direção x:

Sx = Ey Bz / μ₀

No programa são utilizadas unidades normalizadas, com E₀ = 1 e c = 1.

Por isso, o gráfico é uma representação didática e não uma simulação completa em unidades do Sistema Internacional.

## 9. Debian Linux: ambiente de laboratório

O projeto utiliza o Debian Linux como ambiente de desenvolvimento e experimentação.

O Debian é uma distribuição GNU/Linux que oferece ferramentas para programação, administração de sistemas, desenvolvimento científico e execução de aplicações.

Neste laboratório, o Debian funciona como a infraestrutura computacional responsável por:

- Executar os programas Python.
- Gerenciar as bibliotecas matemáticas.
- Organizar os experimentos.
- Criar ambientes virtuais.
- Executar simulações.
- Gerar gráficos científicos.
- Integrar ferramentas de programação quântica.

A utilização do terminal permite acompanhar diretamente a execução dos programas e compreender o funcionamento do ambiente de desenvolvimento.

### Preparação do Debian

Instalar os componentes básicos:

```bash
sudo apt update

sudo apt install python3 python3-pip python3-venv git
```

Criar o diretório:

```bash
mkdir laboratorio-fisica-quantica

cd laboratorio-fisica-quantica
```

Criar o ambiente virtual:

```bash
python3 -m venv .venv
```

Ativar:

```bash
source .venv/bin/activate
```

Atualizar o pip:

```bash
python -m pip install --upgrade pip
```

Instalar as bibliotecas:

```bash
pip install numpy matplotlib
```

Verificar o ambiente:

```bash
python --version

pip list
```

O ambiente virtual permite manter as bibliotecas do laboratório separadas dos pacotes Python instalados globalmente no Debian.

É importante esclarecer que o `venv` não isola a rede nem substitui uma máquina virtual ou um mecanismo de segurança do sistema operacional.

## 10. IBM Qiskit: laboratório de programação quântica

O Qiskit é um conjunto de ferramentas de software de código aberto desenvolvido para trabalhar com computação quântica.

Seu principal componente é o Qiskit SDK, que permite construir circuitos, manipular operadores, representar estados e executar programas quânticos.

Neste projeto, o Qiskit funciona como uma segunda camada experimental.

Enquanto o Python com NumPy e Matplotlib permite desenvolver os cálculos matemáticos e visualizar os resultados, o Qiskit permite representar os mesmos experimentos por meio da linguagem de circuitos quânticos.

O laboratório pode trabalhar em três níveis:

**1. Desenvolvimento matemático**

Construção das equações e cálculo das amplitudes e probabilidades.

**2. Simulação computacional**

Representação dos estados e circuitos utilizando o Qiskit localmente.

**3. Hardware quântico**

Quando houver acesso aos serviços IBM Quantum, envio dos circuitos para execução em processadores quânticos reais.

É importante distinguir uma simulação clássica de uma execução em hardware quântico. O simples uso do Qiskit não significa que o programa esteja sendo executado em um computador quântico físico.

### Instalação no Debian

Com o ambiente virtual ativado:

```bash
pip install qiskit
```

Para acessar os serviços de computação quântica IBM, também pode ser instalado:

```bash
pip install qiskit-ibm-runtime
```

Para utilizar visualizações adicionais:

```bash
pip install "qiskit[visualization]"
```

### Exemplo: circuito quântico de interferência

```python
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
import numpy as np

phi = np.pi / 2

qc = QuantumCircuit(1)

qc.h(0)
qc.rz(phi, 0)
qc.h(0)

print(qc)

state = Statevector.from_instruction(qc)

print(state)
print(state.probabilities())
```

O circuito realiza três operações:

1. Aplica a porta Hadamard.
2. Aplica uma rotação em torno do eixo Z.
3. Aplica novamente a porta Hadamard.

A porta RZ(φ) está relacionada ao operador de fase U(φ) utilizado no laboratório:

U(φ) = e^(iφ/2) RZ(φ)

A diferença é apenas um fator de fase global, que não altera as probabilidades de medição desse experimento.

Para φ = 90 graus:

P(0) = cos²(45°) = 0,5

P(1) = sen²(45°) = 0,5

Portanto, o resultado esperado para as probabilidades é:

Estado zero: 50%

Estado um: 50%

## 11. Experimentos disponíveis

O laboratório apresenta seis visualizações principais:

1. Rotação de fase no plano complexo.
2. Fase em função da posição.
3. Representação geométrica na esfera de Bloch.
4. Circuito de interferência H → U(φ) → H.
5. Modelo simplificado de onda eletromagnética.
6. Varredura da fase e análise das probabilidades de interferência.

Esses experimentos permitem estudar diferentes aspectos das transformações matemáticas aplicadas aos estados quânticos.

## 12. Hipótese de investigação

A linha de investigação deste projeto pode ser representada pela sequência:

Informação → Estado → Fase → Transformação → Interferência → Observação.

A hipótese mais ampla é investigar se estruturas matemáticas relacionadas à fase, à transformação de estados e à geometria podem fornecer uma linguagem útil para estudar possíveis relações entre informação quântica e descrição física do espaço.

A hipótese de que a fase possa possuir alguma relação mais profunda com a geometria espacial não é considerada comprovada.

Para avançar nessa investigação, será necessário:

- Desenvolver formalmente as relações matemáticas.
- Comparar os resultados com a mecânica quântica estabelecida.
- Identificar possíveis previsões quantitativas.
- Formular experimentos capazes de testar as previsões.
- Identificar resultados que possam refutar a hipótese.

## 13. Limitações científicas

O projeto possui caráter exploratório e educacional.

Suas principais limitações são:

- Utilização de simulações numéricas.
- Ausência de experimentos quânticos próprios.
- Ausência de calibração de hardware.
- Ausência de modelagem completa de ruído e decoerência.
- Utilização de uma representação eletromagnética simplificada.
- Ausência de demonstração experimental de uma nova relação física entre fase e espaço.

Os resultados obtidos por simulação demonstram o comportamento dos modelos matemáticos implementados, mas não comprovam hipóteses físicas além desses modelos.

## 14. Possíveis desenvolvimentos

O projeto poderá evoluir por meio de:

- Novos circuitos quânticos.
- Simulações com múltiplos qubits.
- Estudos de emaranhamento.
- Introdução de ruído e decoerência.
- Comparação entre simulações clássicas e hardware quântico.
- Estudos matemáticos de operadores unitários.
- Desenvolvimento de novos modelos de ondas.
- Comparação com literatura científica.
- Formulação de previsões experimentais.

## 15. Status do projeto

**Laboratório computacional de física quântica e programação quântica.**

Pesquisa exploratória, matemática e educacional.

O projeto não apresenta uma teoria física estabelecida nem resultados experimentais confirmados.

Sua finalidade é desenvolver ferramentas computacionais e matemáticas para investigar relações entre informação, fase, geometria, ondas e transformações quânticas.

## 16. Referências técnicas

- Debian: https://www.debian.org/
- IBM Quantum — Introdução ao Qiskit: https://quantum.cloud.ibm.com/docs/en/qiskit
- IBM Quantum — Instalação do Qiskit: https://quantum.cloud.ibm.com/docs/en/qiskit/install-qiskit
- IBM Quantum — Primeiros circuitos: https://quantum.cloud.ibm.com/docs/en/guides/quick-start
- IBM Quantum — Cliente de computação quântica: https://quantum.cloud.ibm.com/docs/en/ibm-quantum-compute/install-qiskit-runtime

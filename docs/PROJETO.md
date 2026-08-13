# Projeto — Física Quântica, Informação e Programação Quântica

## 1. Apresentação

Este projeto nasceu de uma sequência de experimentos computacionais com números complexos, portas quânticas, amplitudes, fase relativa, esfera de Bloch e interferência.

O objetivo é construir um laboratório no qual diferentes representações matemáticas possam ser colocadas lado a lado:

- álgebra linear;
- números complexos;
- estados quânticos;
- circuitos quânticos;
- geometria da esfera de Bloch;
- funções de onda;
- ondas eletromagnéticas;
- informação e transformação.

A intenção não é afirmar previamente que esses objetos são fisicamente equivalentes. A intenção é investigar **quais relações matemáticas são reais, quais são apenas analogias e quais poderiam conduzir a hipóteses testáveis**.

## 2. Pergunta central

Uma pergunta orientadora é:

> Podemos utilizar a estrutura matemática da informação quântica — estado, amplitude, fase, transformação, interferência e medição — como uma linguagem para investigar relações mais profundas entre informação, geometria e descrição física?

Essa pergunta é deliberadamente aberta.

## 3. Experimento fundamental

O laboratório considera:

\[
|\psi_0\rangle=|0\rangle
\]

A porta Hadamard é:

\[
H=
\frac{1}{\sqrt2}
\begin{pmatrix}
1&1\\
1&-1
\end{pmatrix}
\]

Após `H`:

\[
H|0\rangle=
\frac{|0\rangle+|1\rangle}{\sqrt2}
\]

O operador de fase é:

\[
U_\phi=
\begin{pmatrix}
1&0\\
0&e^{i\phi}
\end{pmatrix}
\]

Portanto:

\[
U_\phi H|0\rangle
=
\frac{|0\rangle+e^{i\phi}|1\rangle}{\sqrt2}
\]

Aplicando novamente `H`:

\[
HU_\phi H|0\rangle
=
\frac{1+e^{i\phi}}{2}|0\rangle
+
\frac{1-e^{i\phi}}{2}|1\rangle
\]

As probabilidades resultantes são:

\[
P(0)=\cos^2\left(\frac{\phi}{2}\right)
\]

\[
P(1)=\sin^2\left(\frac{\phi}{2}\right)
\]

Esse experimento mostra computacionalmente como uma fase relativa pode ser convertida em uma diferença observável por interferência.

## 4. Casos particulares

Para:

\[
\phi=0
\]

temos:

\[
U_0=I
\]

e:

\[
P(0)=1,\quad P(1)=0
\]

Para:

\[
\phi=\pi
\]

temos:

\[
U_\pi=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}
=Z
\]

e:

\[
P(0)=0,\quad P(1)=1
\]

Além disso:

\[
HZH=X
\]

O código verifica numericamente essas relações.

## 5. Números complexos e fase

O laboratório utiliza:

\[
e^{i\phi}=\cos\phi+i\sin\phi
\]

Esse ponto é fundamental porque a fase pode ser visualizada como um ponto no círculo unitário do plano complexo.

Os pontos:

\[
1,\quad i,\quad -1,\quad -i
\]

correspondem, respectivamente, às fases:

\[
0,\quad \frac{\pi}{2},\quad \pi,\quad \frac{3\pi}{2}
\]

A visualização não transforma o número complexo em uma dimensão física. Ela mostra a geometria matemática associada à representação complexa.

## 6. Esfera de Bloch

O estado puro:

\[
|\psi\rangle=
\cos\left(\frac{\theta}{2}\right)|0\rangle+
e^{i\phi}\sin\left(\frac{\theta}{2}\right)|1\rangle
\]

pode ser representado por um ponto na esfera de Bloch.

O programa calcula:

\[
x=2\operatorname{Re}(a^*b)
\]

\[
y=2\operatorname{Im}(a^*b)
\]

\[
z=|a|^2-|b|^2
\]

A fase relativa modifica a orientação do estado no plano equatorial quando `θ = π/2`.

## 7. Relação com ondas

Para comparação matemática, o programa utiliza:

\[
\psi(x,t)=e^{i(kx-\omega t)}
\]

com:

\[
\phi(x,t)=kx-\omega t
\]

A fase varia em função de posição e tempo.

Essa representação permite comparar uma estrutura de fase dependente de uma coordenada com a fase relativa de um qubit.

### Mas existe uma diferença essencial

No qubit, `φ` é uma fase relativa entre componentes do estado.

Na onda:

\[
\phi(x,t)=kx-\omega t
\]

é uma função de espaço e tempo.

Portanto, não se deve concluir automaticamente:

\[
\phi_{\text{qubit}} \equiv x_{\text{espaço}}
\]

Qualquer identificação desse tipo precisaria de uma teoria física que fornecesse:

1. definição precisa;
2. dinâmica;
3. observáveis;
4. unidades;
5. simetrias;
6. limite clássico;
7. previsões novas;
8. testes experimentais.

## 8. Onda eletromagnética do laboratório

O programa utiliza:

\[
E_y=E_0\cos(kx-\omega t)
\]

\[
B_z=\frac{E_0}{c}\cos(kx-\omega t)
\]

e uma quantidade relativa:

\[
S_x\sim E_yB_z
\]

Para simplificar o gráfico, o código normaliza:

\[
E_0=1,\qquad c=1
\]

Isso é adequado para visualização, mas não representa uma simulação eletromagnética completa.

## 9. O que o programa realmente demonstra

O programa demonstra computacionalmente:

- operações matriciais sobre estados;
- normalização de vetores complexos;
- conversão de amplitudes em probabilidades;
- transformação por portas quânticas;
- representação de fase;
- coordenadas de Bloch;
- interferência;
- dependência da medição em relação à fase;
- representação matemática de ondas complexas.

## 10. O que o programa não demonstra

O programa não demonstra, por si só:

- uma nova dimensão física;
- uma nova teoria da gravidade;
- equivalência entre espaço e fase;
- que consciência seja um fenômeno quântico;
- que espaço-tempo seja necessariamente emergente de qubits;
- uma nova lei física;
- uma equivalência entre qubits e ondas eletromagnéticas.

Essas afirmações exigiriam desenvolvimento teórico e evidência independente.

## 11. Método científico proposto

Para transformar a hipótese em pesquisa mais forte, cada etapa deve seguir:

\[
\text{Hipótese}
\rightarrow
\text{Modelo matemático}
\rightarrow
\text{Predição}
\rightarrow
\text{Simulação}
\rightarrow
\text{Experimento}
\rightarrow
\text{Comparação}
\]

Uma hipótese que não produz uma diferença observável em relação às teorias existentes permanece uma interpretação possível, e não uma nova teoria física confirmada.

## 12. Laboratório isolado

O desenvolvimento deve ocorrer em ambiente controlado.

### Isolamento mínimo

Use um diretório próprio e um ambiente Python:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Instalação

```bash
python -m pip install --upgrade pip
pip install numpy matplotlib
```

### Execução

```bash
python laboratorio_fase_espaco.py
```

### Windows

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install numpy matplotlib
python laboratorio_fase_espaco.py
```

O `venv` fornece isolamento das dependências Python. Para experimentos que envolvam sistemas, redes ou softwares potencialmente incompatíveis, use uma máquina virtual dedicada ou outro mecanismo de isolamento apropriado.

## 13. Qiskit e IBM Quantum

O Qiskit fornece um ambiente de programação para circuitos e informação quântica. A IBM mantém a documentação e a infraestrutura IBM Quantum associadas ao ecossistema Qiskit.

Instalação:

```bash
pip install qiskit
```

Para acesso ao Qiskit Runtime:

```bash
pip install qiskit-ibm-runtime
```

A documentação oficial descreve o Qiskit SDK como open source e o Qiskit Runtime como serviço para execução de workloads em hardware IBM.

## 14. Reprodução do experimento em Qiskit

Uma implementação equivalente em Qiskit pode usar:

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

print("Estado:")
print(state)

print("Probabilidades:")
print(state.probabilities())
```

Para uma investigação experimental, a próxima etapa é comparar:

\[
P_{\text{teórica}}(\phi)
\]

com:

\[
P_{\text{simulação}}(\phi)
\]

e, posteriormente:

\[
P_{\text{hardware}}(\phi)
\]

incluindo os efeitos de ruído e erro de medição.

## 15. Organização dos gráficos

Os gráficos devem ser armazenados com nomes que identifiquem claramente o experimento:

```text
graficos/
├── 01_plano_complexo.png
├── 02_fase_posicao.png
├── 03_esfera_bloch.png
├── 04_interferencia_h_uphi_h.png
├── 05_onda_eletromagnetica.png
└── 06_varredura_fase.png
```

Para cada gráfico, recomenda-se documentar:

- hipótese;
- parâmetros;
- fórmula;
- resultado;
- interpretação;
- limitações.

## 16. Possíveis contribuições externas

Este projeto pode receber contribuições de diferentes áreas:

### Física

- revisão das hipóteses;
- formulação de modelos;
- análise dimensional;
- comparação com mecânica quântica;
- eletrodinâmica;
- relatividade;
- teorias de informação.

### Matemática

- álgebra linear;
- geometria diferencial;
- teoria de grupos;
- espaços de Hilbert;
- operadores unitários;
- teoria da informação.

### Computação quântica

- Qiskit;
- circuitos;
- simuladores;
- transpiler;
- ruído;
- hardware quântico;
- métodos estatísticos.

### Método científico

- testes independentes;
- reprodutibilidade;
- falsificabilidade;
- análise de erros;
- documentação experimental.

## 17. Aviso sobre contribuições

Contribuições são bem-vindas, inclusive contribuições que **contestem a hipótese**.

Uma contribuição científica importante não precisa confirmar a ideia inicial. Ela pode demonstrar:

- uma inconsistência;
- uma equivalência com uma teoria já conhecida;
- um caso em que a hipótese falha;
- uma interpretação alternativa;
- uma nova previsão;
- uma maneira melhor de testar a hipótese.

O objetivo é favorecer investigação reprodutível e crítica.

## 18. Estado atual

**Status: exploratório / experimental numérico / hipótese em desenvolvimento.**

O projeto deve ser entendido como um laboratório de investigação, e não como uma teoria física estabelecida.

## 19. Próximas etapas sugeridas

1. Reproduzir todos os gráficos.
2. Automatizar a varredura de `φ`.
3. Comparar a expressão analítica com a simulação.
4. Implementar os mesmos circuitos em Qiskit.
5. Comparar simulador e hardware.
6. Introduzir ruído.
7. Quantificar erros.
8. Formular previsões que diferenciem a hipótese das teorias existentes.
9. Documentar resultados positivos e negativos.
10. Submeter as hipóteses a revisão técnica e acadêmica.

# Laboratório de Física Quântica e Programação Quântica

> **Projeto exploratório sobre fase, qubit, geometria, interferência, ondas e informação.**

Este repositório apresenta um laboratório numérico desenvolvido em Python para investigar, de forma computacional e visual, relações entre:

**estado quântico → amplitude complexa → fase → transformação → interferência → medição**

O projeto parte de objetos fundamentais da informação quântica, como qubits, matrizes unitárias, portas `H`, `X`, `Z`, operadores de fase e esfera de Bloch, e compara essas estruturas com uma representação matemática de ondas complexas e uma onda eletromagnética simplificada.

## ⚠️ Natureza científica do projeto

Este trabalho é **exploratório e hipotético**. Ele não apresenta como fato estabelecido que:

- fase quântica seja uma dimensão espacial;
- espaço físico seja diretamente equivalente ao espaço de fase de um qubit;
- a função de onda quântica seja literalmente uma onda eletromagnética;
- a teoria proposta constitua uma teoria física completa.

O programa foi construído para estudar estruturas matemáticas e gerar experimentos numéricos que possam ajudar a formular hipóteses testáveis.

O próprio laboratório deixa explícito que **“fase quântica = dimensão espacial” não é assumido como resultado**. A hipótese deve ser avaliada por previsões observáveis e por comparação com a física conhecida.

## Objetivos

1. Estudar amplitudes complexas em sistemas quânticos.
2. Visualizar a fase como geometria no plano complexo.
3. Relacionar fase e posição em uma onda complexa.
4. Visualizar estados de um qubit na esfera de Bloch.
5. Estudar interferência através do circuito `H → Uφ → H`.
6. Observar como uma fase interna pode aparecer nas probabilidades de medição.
7. Comparar, com as devidas limitações, estruturas de fase quântica e ondas eletromagnéticas.
8. Criar uma base computacional para uma investigação mais ampla sobre informação, espaço, fase e transformação.

## Estrutura matemática central

Um qubit puro pode ser escrito como:

\[
|\psi\rangle = a|0\rangle+b|1\rangle
\]

com a condição de normalização:

\[
|a|^2+|b|^2=1
\]

O operador de fase utilizado no laboratório é:

\[
U_\phi=
\begin{pmatrix}
1&0\\
0&e^{i\phi}
\end{pmatrix}
\]

e:

\[
e^{i\phi}=\cos\phi+i\sin\phi
\]

Para o circuito:

\[
|0\rangle \xrightarrow{H} H|0\rangle
\xrightarrow{U_\phi} U_\phi H|0\rangle
\xrightarrow{H} HU_\phi H|0\rangle
\]

a amplitude final pode ser escrita como:

\[
HU_\phi H|0\rangle
=
\frac{1+e^{i\phi}}{2}|0\rangle+
\frac{1-e^{i\phi}}{2}|1\rangle
\]

ou, separando uma fase global:

\[
HU_\phi H|0\rangle
=
e^{i\phi/2}
\left[
\cos\left(\frac{\phi}{2}\right)|0\rangle
-i\sin\left(\frac{\phi}{2}\right)|1\rangle
\right]
\]

Logo:

\[
P(0)=\cos^2\left(\frac{\phi}{2}\right)
\]

\[
P(1)=\sin^2\left(\frac{\phi}{2}\right)
\]

Esse resultado é um dos pontos centrais do laboratório: **uma fase que não aparece diretamente como probabilidade após a primeira transformação pode tornar-se observável após interferência.**

## Esfera de Bloch

Para:

\[
|\psi\rangle=a|0\rangle+b|1\rangle
\]

o programa calcula:

\[
x=2\operatorname{Re}(a^*b)
\]

\[
y=2\operatorname{Im}(a^*b)
\]

\[
z=|a|^2-|b|^2
\]

A parametrização usada é:

\[
|\psi\rangle=
\cos\left(\frac{\theta}{2}\right)|0\rangle+
e^{i\phi}\sin\left(\frac{\theta}{2}\right)|1\rangle
\]

Assim, a fase relativa aparece como uma coordenada angular do estado na representação de Bloch.

## Relação com ondas

O laboratório também utiliza a forma:

\[
\psi(x,t)=e^{i(kx-\omega t)}
\]

com:

\[
\varphi(x,t)=kx-\omega t
\]

e:

\[
\nabla\varphi=k
\]

Isso permite visualizar a fase como uma variável que muda ao longo de uma coordenada espacial em um modelo de onda.

### Onda eletromagnética

O código usa uma representação didática e normalizada:

\[
E_y=E_0\cos(kx-\omega t)
\]

\[
B_z=\frac{E_0}{c}\cos(kx-\omega t)
\]

e, para visualização:

\[
S_x\sim E_yB_z
\]

No programa, são usadas unidades normalizadas (`E0 = 1` e `c = 1`). Portanto, esse gráfico **não deve ser interpretado como uma simulação eletromagnética completa em unidades SI**.

## Laboratório e isolamento

Recomenda-se executar o projeto em um **ambiente de laboratório isolado**.

Isso pode ser feito em:

- Linux;
- Windows;
- uma máquina virtual;
- um ambiente virtual Python (`venv`).

O `venv` isola as dependências Python do projeto. Para um isolamento mais forte, especialmente durante experimentos com software adicional, uma máquina virtual ou outro ambiente dedicado pode ser utilizada.

> **Importante:** `venv` não é um mecanismo de isolamento de rede nem uma barreira de segurança completa. Ele apenas separa o ambiente Python e seus pacotes.

## Linux

```bash
mkdir laboratorio-fisica-quantica
cd laboratorio-fisica-quantica

python3 -m venv .venv
source .venv/bin/activate

python -m pip install --upgrade pip
pip install -r requirements.txt
```

Verifique:

```bash
python --version
pip --version
```

Execute o laboratório:

```bash
python laboratorio_fase_espaco.py
```

Para sair do ambiente virtual:

```bash
deactivate
```

## Windows PowerShell

```powershell
mkdir laboratorio-fisica-quantica
cd laboratorio-fisica-quantica

py -m venv .venv
.\.venv\Scripts\Activate.ps1

python -m pip install --upgrade pip
pip install -r requirements.txt
```

Execute:

```powershell
python laboratorio_fase_espaco.py
```

Para sair:

```powershell
deactivate
```

Se a política do PowerShell bloquear a ativação do ambiente, consulte a documentação do Python/Windows e ajuste a política somente no escopo apropriado ao seu laboratório.

## Dependências do laboratório

O código principal fornecido neste projeto usa diretamente:

```text
numpy
matplotlib
```

O Qiskit é tratado como uma camada adicional para reproduzir os experimentos utilizando a linguagem de circuitos quânticos. Ele está separado em `requirements-qiskit.txt` para que o laboratório matemático básico permaneça leve.

## IBM Qiskit

[Qiskit](https://quantum.cloud.ibm.com/docs/en/guides/tools-intro) é um SDK open source para construção e manipulação de circuitos quânticos. A plataforma IBM Quantum complementa o SDK oferecendo serviços de execução quântica, incluindo o Qiskit Runtime para workloads em hardware quântico IBM. 

Instalação básica:

```bash
pip install qiskit
```

Para instalar a camada Qiskit do projeto:

```bash
pip install -r requirements-qiskit.txt
```

Ou, separadamente:

```bash
pip install qiskit
pip install qiskit-ibm-runtime
```

A documentação oficial recomenda o uso de ambientes virtuais para os projetos e orienta a instalação do SDK separadamente do cliente do Runtime.

### Exemplo mínimo com Qiskit

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

O exemplo reproduz a ideia central do laboratório: preparar uma superposição, aplicar uma transformação de fase e utilizar uma segunda transformação para converter a informação de fase em diferença observável nas amplitudes/probabilidades.

## Experimentos

O programa disponibiliza seis visualizações:

1. **Rotação de fase no plano complexo**
2. **Fase em função da posição**
3. **Esfera de Bloch**
4. **Circuito `H → Uφ → H`**
5. **Onda eletromagnética normalizada**
6. **Varredura da fase e interferência**


## Hipótese de trabalho

A linha de investigação deste projeto pode ser resumida como:

\[
\text{informação}
\rightarrow
\text{estado}
\rightarrow
\text{fase}
\rightarrow
\text{transformação}
\rightarrow
\text{interferência}
\rightarrow
\text{observação}
\]

A hipótese mais ampla é investigar se estruturas matemáticas associadas à fase e à transformação de estados podem fornecer uma linguagem útil para discutir relações entre informação quântica, geometria e descrição física.

**Essa hipótese permanece aberta e precisa de desenvolvimento matemático, comparação com teorias existentes e, principalmente, previsões experimentais falsificáveis.**

## Limitações

O laboratório atual é:

- numérico;
- didático;
- baseado em modelos simplificados;
- sem ruído quântico experimental;
- sem calibração de hardware;
- sem pretensão de substituir uma derivação física completa.

A parte eletromagnética é uma visualização normalizada. A esfera de Bloch é uma representação matemática do estado de um qubit. A analogia entre essas estruturas deve ser tratada como ferramenta de investigação, não como identidade física.

## Possíveis contribuições

Este repositório está aberto a contribuições que possam:

- reproduzir os resultados;
- verificar as deduções matemáticas;
- encontrar limitações ou contraexemplos;
- melhorar os experimentos numéricos;
- adicionar circuitos Qiskit;
- comparar simuladores clássicos e hardware quântico;
- introduzir ruído e decoerência;
- relacionar o modelo com literatura acadêmica;
- propor previsões quantitativas e testes falsificáveis;
- melhorar as visualizações e documentação.

Uma contribuição especialmente importante seria transformar hipóteses qualitativas em **predições quantitativas que possam ser comparadas com dados experimentais**.

## Status

**Pesquisa exploratória / laboratório educacional / hipótese em desenvolvimento.**

Não é uma teoria física estabelecida e não deve ser apresentada como resultado experimental confirmado.

## Referências técnicas

- [IBM Quantum Documentation — Qiskit](https://quantum.cloud.ibm.com/docs/en/guides/tools-intro)
- [IBM Quantum Documentation — Instalação do Qiskit](https://quantum.cloud.ibm.com/docs/en/guides/install-qiskit)
- [IBM Quantum Documentation — Qiskit Runtime](https://quantum.cloud.ibm.com/docs/en/guides/compute-services)
- [IBM Quantum Documentation — Statevector](https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.quantum_info.Statevector)



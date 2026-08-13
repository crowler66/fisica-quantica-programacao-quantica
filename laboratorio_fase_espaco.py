#!/usr/bin/env python3
"""
Laboratório: fase, qubit, geometria e onda eletromagnética

Este programa NÃO afirma que fase quântica = dimensão espacial.
Ele cria um laboratório matemático para investigar a hipótese:
energia/estado -> fase -> transformação -> interferência -> medição.

Dependências:
    pip install numpy matplotlib

Execute:
    python3 laboratorio_fase_espaco.py
"""








import matplotlib
matplotlib.use("TkAgg")



import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# 1. MATRIZES QUÂNTICAS
# ============================================================

I2 = np.eye(2, dtype=complex)

X = np.array([[0, 1],
              [1, 0]], dtype=complex)

Z = np.array([[1, 0],
              [0, -1]], dtype=complex)

H = (1 / np.sqrt(2)) * np.array([[1, 1],
                                  [1, -1]], dtype=complex)


def U_phi(phi):
    """Matriz de fase U_phi."""
    return np.array([[1, 0],
                     [0, np.exp(1j * phi)]], dtype=complex)


def ket0():
    return np.array([1, 0], dtype=complex)


def ket1():
    return np.array([0, 1], dtype=complex)


def normalize(state):
    n = np.linalg.norm(state)
    if n == 0:
        raise ValueError("Estado nulo não pode ser normalizado.")
    return state / n


def probabilities(state):
    state = normalize(state)
    return np.abs(state) ** 2


def print_matrix(name, matrix):
    print(f"\n{name} =")
    print(np.array2string(matrix, precision=4, suppress_small=True))


def print_state(name, state):
    print(f"\n{name} =")
    print(np.array2string(state, precision=4, suppress_small=True))
    p = probabilities(state)
    print(f"Probabilidades: P(0)={p[0]:.4f}, P(1)={p[1]:.4f}")


# ============================================================
# 2. H -> U_phi -> H
# ============================================================

def circuit_state(phi):
    """Executa |0> -> H -> U_phi -> H."""
    s0 = ket0()
    s1 = H @ s0
    s2 = U_phi(phi) @ s1
    s3 = H @ s2
    return s0, s1, s2, s3


# ============================================================
# 3. ESFERA DE BLOCH
# ============================================================

def bloch_coordinates(state):
    """
    Para |psi> = a|0> + b|1>:
      x = 2 Re(a* b)
      y = 2 Im(a* b)
      z = |a|^2 - |b|^2
    """
    state = normalize(state)
    a, b = state

    x = 2 * np.real(np.conj(a) * b)
    y = 2 * np.imag(np.conj(a) * b)
    z = np.abs(a)**2 - np.abs(b)**2

    return np.array([x, y, z])


def state_from_theta_phi(theta, phi):
    """Estado puro da esfera de Bloch."""
    return np.array([
        np.cos(theta / 2),
        np.exp(1j * phi) * np.sin(theta / 2)
    ], dtype=complex)


# ============================================================
# 4. ONDA COMPLEXA
# ============================================================

def complex_wave(x, k=2*np.pi, omega=2*np.pi, t=0):
    """
    Psi(x,t) = exp(i(kx - omega t))
    """
    phase = k * x - omega * t
    return np.exp(1j * phase)


# ============================================================
# 5. ONDA ELETROMAGNÉTICA
# ============================================================

def electromagnetic_wave(x, t=0, wavelength=1.0, frequency=1.0):
    """
    Onda plana simplificada:
        E_y = E0 cos(kx - wt)
        B_z = E0/c cos(kx - wt)
        S_x ~ E_y * B_z

    Para visualização, usamos unidades normalizadas:
        E0 = 1
        c = 1
    """
    k = 2 * np.pi / wavelength
    omega = 2 * np.pi * frequency
    phase = k * x - omega * t

    E = np.cos(phase)
    B = np.cos(phase)
    S = E * B

    return E, B, S


# ============================================================
# 6. VISUALIZAÇÃO PRINCIPAL
# ============================================================

def plot_complex_phase():
    theta = np.linspace(0, 2*np.pi, 500)
    z = np.exp(1j * theta)

    fig, ax = plt.subplots(figsize=(7, 7))
    ax.plot(z.real, z.imag, label=r"$e^{i\phi}$")
    ax.axhline(0, linewidth=1)
    ax.axvline(0, linewidth=1)

    # Pontos importantes
    angles = [0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi]
    labels = ["1", "i", "-1", "-i", "1"]
    for a, label in zip(angles, labels):
        p = np.exp(1j * a)
        ax.scatter([p.real], [p.imag], s=60)
        ax.text(p.real + 0.06, p.imag + 0.06, label, fontsize=12)

    ax.set_title(r"Geometria da fase: $e^{i\phi}=\cos\phi+i\sin\phi$")
    ax.set_xlabel("Parte real")
    ax.set_ylabel("Parte imaginária")
    ax.set_aspect("equal")
    ax.grid(True)
    ax.legend()
    plt.tight_layout()


def plot_phase_vs_position():
    x = np.linspace(0, 4, 1000)
    k = 2*np.pi
    psi = complex_wave(x, k=k)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(x, psi.real, label=r"$\Re(e^{ikx})=\cos(kx)$")
    ax.plot(x, psi.imag, label=r"$\Im(e^{ikx})=\sin(kx)$")
    ax.set_title(r"Fase espacial: $\psi(x)=e^{ikx}$")
    ax.set_xlabel("posição x")
    ax.set_ylabel("amplitude")
    ax.grid(True)
    ax.legend()
    plt.tight_layout()


def plot_bloch_sphere(phi=np.pi/2):
    theta = np.linspace(0, np.pi, 80)
    az = np.linspace(0, 2*np.pi, 100)
    TH, AZ = np.meshgrid(theta, az)

    Xs = np.sin(TH) * np.cos(AZ)
    Ys = np.sin(TH) * np.sin(AZ)
    Zs = np.cos(TH)

    # Estado inicial da superposição e rotação de fase
    state = state_from_theta_phi(np.pi/2, phi)
    point = bloch_coordinates(state)

    fig = plt.figure(figsize=(8, 7))
    ax = fig.add_subplot(111, projection="3d")

    ax.plot_surface(Xs, Ys, Zs, alpha=0.12, linewidth=0)
    ax.plot_wireframe(Xs[::8], Ys[::8], Zs[::8],
                      alpha=0.15, linewidth=0.5)

    ax.plot([0, point[0]], [0, point[1]], [0, point[2]],
            linewidth=3)
    ax.scatter([point[0]], [point[1]], [point[2]], s=80)

    ax.text(0, 0, 1.1, "|0>")
    ax.text(0, 0, -1.15, "|1>")

    ax.set_title(
        r"Esfera de Bloch: $|\psi\rangle="
        r"\cos(\theta/2)|0\rangle+e^{i\phi}\sin(\theta/2)|1\rangle$"
        + f"\nphi = {phi:.3f} rad = {np.degrees(phi):.1f}°"
    )
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    plt.tight_layout()


def plot_h_uz_h(phi=np.pi):
    states = circuit_state(phi)

    labels = [
        r"$|0\rangle$",
        r"$H|0\rangle$",
        r"$U_\phi H|0\rangle$",
        r"$HU_\phi H|0\rangle$"
    ]

    # Probabilidades
    probs = np.array([probabilities(s) for s in states])

    fig, ax = plt.subplots(figsize=(10, 5))
    x = np.arange(4)
    width = 0.35

    ax.bar(x - width/2, probs[:, 0], width, label="P(0)")
    ax.bar(x + width/2, probs[:, 1], width, label="P(1)")

    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylim(0, 1.05)
    ax.set_ylabel("probabilidade")
    ax.set_title(
        r"Interferência: $H\,U_\phi\,H$  "
        + f"(phi={phi:.3f} rad = {np.degrees(phi):.1f}°)"
    )
    ax.grid(axis="y")
    ax.legend()
    plt.tight_layout()


def plot_electromagnetic_wave():
    x = np.linspace(0, 3, 1000)
    E, B, S = electromagnetic_wave(x)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x, E, label="E (campo elétrico)")
    ax.plot(x, B, label="B (campo magnético)")
    ax.plot(x, S, label="S ~ E × B")
    ax.set_title("Onda eletromagnética — unidades normalizadas")
    ax.set_xlabel("posição x")
    ax.set_ylabel("amplitude / fluxo relativo")
    ax.grid(True)
    ax.legend()
    plt.tight_layout()


# ============================================================
# 7. EXPERIMENTO NUMÉRICO: FASE x MEDIÇÃO
# ============================================================

def phase_scan():
    phis = np.linspace(0, 2*np.pi, 361)

    p0 = []
    p1 = []

    for phi in phis:
        _, _, _, final = circuit_state(phi)
        p = probabilities(final)
        p0.append(p[0])
        p1.append(p[1])

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(phis, p0, label="P(0)")
    ax.plot(phis, p1, label="P(1)")

    ax.set_xlabel(r"fase $\phi$ (rad)")
    ax.set_ylabel("probabilidade")
    ax.set_title(r"Como a fase $e^{i\phi}$ aparece na medição após $H U_\phi H$")
    ax.set_ylim(-0.02, 1.02)
    ax.grid(True)
    ax.legend()
    plt.tight_layout()


# ============================================================
# 8. RELATÓRIO NUMÉRICO
# ============================================================

def report():
    print("=" * 65)
    print("LABORATÓRIO DE FASE, QUBIT, GEOMETRIA E LUZ")
    print("=" * 65)

    print_matrix("H", H)
    print_matrix("Z", Z)

    print("\nVerificação H Z H = X:")
    print_matrix("H @ Z @ H", H @ Z @ H)
    print_matrix("X", X)

    print("\nVerificação U_pi = Z:")
    print_matrix("U_pi", U_phi(np.pi))

    print("\nExemplo phi = pi/2:")
    phi = np.pi/2
    print_matrix("U_(pi/2)", U_phi(phi))

    s0, s1, s2, s3 = circuit_state(phi)
    print_state("Estado inicial", s0)
    print_state("Depois de H", s1)
    print_state("Depois de U_phi", s2)
    print_state("Depois do segundo H", s3)

    print("\nGeometria do estado final para phi = pi/2:")
    print("Bloch =", bloch_coordinates(s3))

    print("\nPara uma onda plana:")
    print("psi(x,t) = exp(i(kx - omega t))")
    print("grad(phi) = k  (para phi = kx - omega*t)")

    print("\nIMPORTANTE:")
    print("O programa trata fase como estrutura matemática/geométrica.")
    print("Ele NÃO assume que fase seja uma dimensão espacial física.")
    print("A hipótese dimensional deve ser testada por previsões observáveis.")


# ============================================================
# 9. MENU
# ============================================================

def main():
    report()

    while True:
        print("\n" + "-" * 65)
        print("Escolha uma visualização:")
        print("1 - Rotação de fase no plano complexo")
        print("2 - Fase em função da posição")
        print("3 - Esfera de Bloch")
        print("4 - Circuito H -> U_phi -> H")
        print("5 - Onda eletromagnética E, B e fluxo relativo")
        print("6 - Varredura da fase e interferência")
        print("0 - Sair")

        choice = input("Opção: ").strip()

        if choice == "1":
            plot_complex_phase()
            plt.show()

        elif choice == "2":
            plot_phase_vs_position()
            plt.show()

        elif choice == "3":
            value = input("Digite phi em graus [padrão 90]: ").strip()
            deg = 90 if not value else float(value)
            plot_bloch_sphere(np.radians(deg))
            plt.show()

        elif choice == "4":
            value = input("Digite phi em graus [padrão 180]: ").strip()
            deg = 180 if not value else float(value)
            plot_h_uz_h(np.radians(deg))
            plt.show()

        elif choice == "5":
            plot_electromagnetic_wave()
            plt.show()

        elif choice == "6":
            phase_scan()
            plt.show()

        elif choice == "0":
            print("Encerrando laboratório.")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()

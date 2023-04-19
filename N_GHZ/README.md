# GHZ for the n-qbits

The GHZ is a specific quantum circuit, that result in a specific entangled state, with the following form:

$$
\ket{\psi_{000}} = \alpha \ket{000} + \beta \ket{111}                       
$$

$$
\ket{\psi_{00000}} = \alpha \ket{00000} + \beta \ket{11111} 
$$

$$
\vdots \vdots \vdots 
$$

$$
\ket{\psi_{0^n}} =  \alpha \ket{0^n} + \beta \ket{1^n}
$$

Challenge: build a quantum algorithm that givesn the number of qubits in the circuit, returns a GHZ state with n = qubits.
Below you can see the circuit for n = 5 qubits.

![GHZ Circuit](https://raw.githubusercontent.com/rickapocalypse/quantum_algorithms/master/N_GHZ/img_example/qc_n%3D5.png)

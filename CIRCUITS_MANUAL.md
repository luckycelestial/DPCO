# Digital Principles & Computer Organization (DPCO)
## Complete Laboratory Circuit Implementations & Verification Manual

All circuit designs in this repository are engineered, cross-checked, and formatted for **Logisim 2.7.1** and browser Logisim ([logisim.app](https://logisim.app)).

---

## Index of Circuit Files

| Exp | Circuit File | Description | Core Components |
|:---:|:---|:---|:---|
| **1** | [exp1_half_and_full_adder.circ](file:///home/luckycelestial/Pavithran/DPCO/exp1_half_and_full_adder.circ) | Implementation of Half Adder & Full Adder | XOR, AND, OR Gates |
| **2** | [exp2_mux_and_demux.circ](file:///home/luckycelestial/Pavithran/DPCO/exp2_mux_and_demux.circ) | Implementation of 4:1 MUX & 1:4 DEMUX | NOT, 3-input AND, 2-stage OR network |
| **3** | [exp3_jk_and_d_flip_flop.circ](file:///home/luckycelestial/Pavithran/DPCO/exp3_jk_and_d_flip_flop.circ) | Verification of JK & D Flip-Flop | Edge-triggered JK-FF, D-FF, Clock, Async Reset |
| **4** | [exp4_siso_and_pipo.circ](file:///home/luckycelestial/Pavithran/DPCO/exp4_siso_and_pipo.circ) | Implementation of 4-bit SISO & PIPO Registers | 4 Cascaded D-FFs, 4 Parallel D-FFs, Bus Splitters |
| **5** | [exp5_4bit_ripple_counter_dff.circ](file:///home/luckycelestial/Pavithran/DPCO/exp5_4bit_ripple_counter_dff.circ) | Construction of 4-bit Ripple Counter (D-FF) | 4 D-FFs in Toggle Mode ($D=\overline{Q}$), Negative-edge Clock Ripple |
| **6** | [exp6_2bit_alu.circ](file:///home/luckycelestial/Pavithran/DPCO/exp6_2bit_alu.circ) | 2-Bit ALU (Adder, Subtractor, MUX, Divider) | 2-bit Adder, Subtractor, Divider, 4:1 MUX, Zero Comparator |

---

## Experiment 1: Half Adder & Full Adder

### 1.1 Objective
Design and implement:
1. **Half Adder**: Adds two 1-bit binary inputs $A$ and $B$, generating $Sum$ and $Carry$.
2. **Full Adder**: Adds three 1-bit inputs $A$, $B$, and $C_{in}$, constructed hierarchically from two Half Adders and an OR gate.

### 1.2 Boolean Logic & Schematics
- **Half Adder**:
  $$\text{Sum} = A \oplus B$$
  $$\text{Carry} = A \cdot B$$

- **Full Adder**:
  $$\text{Sum} = (A \oplus B) \oplus C_{in}$$
  $$C_{out} = (A \cdot B) + (C_{in} \cdot (A \oplus B))$$

```
Half Adder:
  A ──┬───────────) XOR ─── HA_SUM
      │   ┌───────)
  B ──┼───┴───────) AND ─── HA_CARRY
      └───┘

Full Adder (2 Half Adders + OR):
  A ──┬──────) XOR1 ────┬────────) XOR2 ─────────── FA_SUM
  B ──┴──────)          │    ┌───)
      ┌──────) AND1 ──┐ │    │
      └──────)        │ └──┬─┼───) AND2 ──┐
  Cin ────────────────┼────┴─┘   │        ├──) OR ── FA_COUT
                      └──────────┴────────┘
```

### 1.3 Truth Tables
#### Half Adder
| $A$ | $B$ | $\text{HA\_SUM}$ | $\text{HA\_CARRY}$ |
|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |

#### Full Adder
| $C_{in}$ | $B$ | $A$ | $\text{FA\_SUM}$ | $\text{FA\_COUT}$ | Decimal Equivalent |
|:---:|:---:|:---:|:---:|:---:|:---|
| 0 | 0 | 0 | 0 | 0 | $0 + 0 + 0 = 0$ |
| 0 | 0 | 1 | 1 | 0 | $0 + 0 + 1 = 1$ |
| 0 | 1 | 0 | 1 | 0 | $0 + 1 + 0 = 1$ |
| 0 | 1 | 1 | 0 | 1 | $0 + 1 + 1 = 2$ ($10_2$) |
| 1 | 0 | 0 | 1 | 0 | $1 + 0 + 0 = 1$ |
| 1 | 0 | 1 | 0 | 1 | $1 + 0 + 1 = 2$ ($10_2$) |
| 1 | 1 | 0 | 0 | 1 | $1 + 1 + 0 = 2$ ($10_2$) |
| 1 | 1 | 1 | 1 | 1 | $1 + 1 + 1 = 3$ ($11_2$) |

### 1.4 How to Verify in Logisim
1. Open [exp1_half_and_full_adder.circ](file:///home/luckycelestial/Pavithran/DPCO/exp1_half_and_full_adder.circ).
2. Use the **Poke Tool** (hand icon `👆` in top toolbar).
3. Toggle pins `HA_A` and `HA_B` to verify the 4 Half Adder states.
4. Toggle pins `FA_A`, `FA_B`, and `FA_CIN` to verify all 8 Full Adder rows.

---

## Experiment 2: 4:1 Multiplexer & 1:4 Demultiplexer

### 2.1 Objective
Construct and verify data routing circuits at gate level:
1. **4-to-1 Multiplexer (Data Selector)**: Routes one of four inputs ($I_0, I_1, I_2, I_3$) to output $Y$ using select lines $S_1, S_0$.
2. **1-to-4 Demultiplexer (Data Distributor)**: Steers a single input line $D_{in}$ to one of four output channels ($Y_0, Y_1, Y_2, Y_3$) using select lines $S_1, S_0$.

### 2.2 Boolean Equations
- **4:1 MUX Output**:
  $$Y = (\overline{S_1} \cdot \overline{S_0} \cdot I_0) + (\overline{S_1} \cdot S_0 \cdot I_1) + (S_1 \cdot \overline{S_0} \cdot I_2) + (S_1 \cdot S_0 \cdot I_3)$$

- **1:4 DEMUX Outputs**:
  $$Y_0 = D_{in} \cdot \overline{S_1} \cdot \overline{S_0}$$
  $$Y_1 = D_{in} \cdot \overline{S_1} \cdot S_0$$
  $$Y_2 = D_{in} \cdot S_1 \cdot \overline{S_0}$$
  $$Y_3 = D_{in} \cdot S_1 \cdot S_0$$

### 2.3 Function Tables
#### 4:1 MUX Function Table
| $S_1$ | $S_0$ | Selected Input | Output Equation |
|:---:|:---:|:---:|:---|
| 0 | 0 | $I_0$ | $Y = I_0$ |
| 0 | 1 | $I_1$ | $Y = I_1$ |
| 1 | 0 | $I_2$ | $Y = I_2$ |
| 1 | 1 | $I_3$ | $Y = I_3$ |

#### 1:4 DEMUX Function Table
| $S_1$ | $S_0$ | $Y_3$ | $Y_2$ | $Y_1$ | $Y_0$ | Note |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 0 | 0 | 0 | 0 | 0 | $D_{in}$ | Data steered to Channel 0 |
| 0 | 1 | 0 | 0 | $D_{in}$ | 0 | Data steered to Channel 1 |
| 1 | 0 | 0 | $D_{in}$ | 0 | 0 | Data steered to Channel 2 |
| 1 | 1 | $D_{in}$ | 0 | 0 | 0 | Data steered to Channel 3 |

### 2.4 How to Verify in Logisim
1. Open [exp2_mux_and_demux.circ](file:///home/luckycelestial/Pavithran/DPCO/exp2_mux_and_demux.circ).
2. **MUX Test**:
   - Set $I_0=1, I_1=0, I_2=1, I_3=0$.
   - Change `(MUX_S1, MUX_S0)` from `00` $\to$ `01` $\to$ `10` $\to$ `11`.
   - Observe `MUX_OUT` matches $I_0(1), I_1(0), I_2(1), I_3(0)$ respectively.
3. **DEMUX Test**:
   - Set `DEMUX_DIN = 1`.
   - Cycle select pins `(DEMUX_S1, DEMUX_S0)`. Observe high bit moving:
     - `00`: $Y_0=1$
     - `01`: $Y_1=1$
     - `10`: $Y_2=1$
     - `11`: $Y_3=1$

---

## Experiment 3: Verification of JK & D Flip-Flops

### 3.1 Objective
Verify edge-triggered and clocked storage elements in two distinct sections within the same schematic:
1. **Section 1 (Top)**: Integrated library flip-flops (`JK Flip-Flop` and `D Flip-Flop`) with asynchronous clear.
2. **Section 2 (Bottom)**: Gate-level implementations:
   - **Master-Slave J-K Flip-Flop**: Constructed entirely using 8 NAND gates + 1 NOT gate (Master stage on $CLK$, Slave stage on $\overline{CLK}$) to eliminate race-around conditions.
   - **Clocked D Flip-Flop / Latch**: Constructed using 4 NAND gates + 1 NOT gate.

### 3.2 Gate-Level Logic Schematics
#### Master-Slave JK Flip-Flop (NAND Gates)
```
          MASTER STAGE                                 SLAVE STAGE
     ┌──────────────────┐                         ┌──────────────────┐
     │  ┌───) NAND1 ──┐ │                         │  ┌───) NAND5 ──┐ │
J ───┼──┤             ├─┼──) NAND3 ─┐             │  │             ├─┼──) NAND7 ──┬──► Q
     │  └───)         │ │  │        ├─(Qm)────────┼──┤             │ │  │         │
CLK ─┴──┬─────────────┼─┼──┴─┐   ┌──┘             │  └───)         │ │  │         │
        │             │ │    └───┼────────────────┼──┬─────────────┼─┼──┴─┐   ┌───┘
        │   ┌───) NOT ┼─┼────────┼───(~CLK)───────┴──┤             │ │    └───┼───────┐
        │   │   └─────┘ │        │                   └───)         │ │        │       │
        └───┼─────────┼─┼──┬─┐   │                │  ┌───) NAND6 ──┼─┼──┬─┐   │       │
K ──────┬───┼─────────┼─┼──┘ └───┼────(~Qm)───────┼──┤             ├─┼──┘ └───┼───)   ▼
        │   └───)     │ │        │                │  └───)         │ │        │  NAND8 ─► ~Q
        │       NAND2 ├─┼──) NAND4                │                │ │        │   │
        └─────────────┘ │                         └────────────────┘ └────────┴───┘
```

#### Clocked D Latch / Flip-Flop (NAND Gates)
```
D ──┬─────────────) NAND1 ──┬──) NAND3 ──────┬──► Q
    │        ┌────)         │  │             │
    │        │              │  │      ┌──────┘
CLK ┴────────┼──────────────┼──┼──────┼──────┐
             │              │  │      ▼      │
    ┌───) NOT┴────) NAND2 ──┼──┴─) NAND4 ────┴──► ~Q
    └───┘                   │
```

### 3.3 Characteristic Equations & State Tables
- **JK Characteristic Equation**:
  $$Q_{next} = J\overline{Q} + \overline{K}Q$$
- **D Characteristic Equation**:
  $$Q_{next} = D$$

#### JK Flip-Flop Function Table
| $CLR$ (Async) | $CLK$ | $J$ | $K$ | $Q_{next}$ | $\overline{Q}_{next}$ | Operating Mode |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | $\times$ | $\times$ | $\times$ | **0** | **1** | Asynchronous Reset Override |
| 0 | $\downarrow$ | 0 | 0 | $Q$ | $\overline{Q}$ | **No Change (Hold/Memory)** |
| 0 | $\downarrow$ | 0 | 1 | **0** | **1** | **Reset** |
| 0 | $\downarrow$ | 1 | 0 | **1** | **0** | **Set** |
| 0 | $\downarrow$ | 1 | 1 | $\overline{Q}$ | $Q$ | **Toggle ($\text{Divide-by-2}$)** |

#### D Flip-Flop Function Table
| $CLR$ (Async) | $CLK$ | $D$ | $Q_{next}$ | $\overline{Q}_{next}$ | Operating Mode |
|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | $\times$ | $\times$ | **0** | **1** | Asynchronous Reset Override |
| 0 | $\downarrow$ | 0 | **0** | **1** | Reset / Store 0 |
| 0 | $\downarrow$ | 1 | **1** | **0** | Set / Store 1 |
| 0 | Steady | $\times$ | $Q$ | $\overline{Q}$ | Memory Hold |

### 3.4 How to Verify in Logisim
1. Open [exp3_jk_and_d_flip_flop.circ](file:///home/luckycelestial/Pavithran/DPCO/exp3_jk_and_d_flip_flop.circ).
2. **Top Section (Library Components)**:
   - Pulse `CLK_JK` while cycling $(J, K)$ through `00`, `01`, `10`, `11` to verify Hold, Reset, Set, and Toggle.
   - Pulse `CLK_D` with $D=0$ and $D=1$. Test `CLR_D = 1` for asynchronous clear override.
3. **Bottom Section (Gate-Level NAND Implementations)**:
   - **Gate-Level Master-Slave JK**:
     - Set `GATE_J = 1, GATE_K = 0`: Pulse `GATE_CLK_JK` (High then Low). Notice `GATE_Q_JK` transitions to `1` on clock falling edge.
     - Set `GATE_J = 0, GATE_K = 1`: Pulse clock. Notice `GATE_Q_JK` transitions to `0`.
     - Set `GATE_J = 1, GATE_K = 1`: Pulse clock repeatedly. On each complete pulse, `GATE_Q_JK` toggles cleanly without race-around oscillation.
   - **Gate-Level D Flip-Flop / Latch**:
     - When `GATE_CLK_D = 1`, toggle `GATE_D`. Notice `GATE_Q_D` immediately follows `GATE_D`.
     - When `GATE_CLK_D = 0`, toggle `GATE_D`. Notice `GATE_Q_D` holds its stored value.

---

## Experiment 4: SISO & PIPO Shift Registers

### 4.1 Objective
Implement 4-bit storage registers illustrating fundamental serial vs parallel architectures:
1. **SISO (Serial-In Serial-Out)**: Single-bit sequential ingress and single-bit sequential egress across 4 cascaded flip-flops.
2. **PIPO (Parallel-In Parallel-Out)**: All 4 bits loaded simultaneously in 1 clock edge and output immediately on a 4-bit bus.

### 4.2 Architecture Comparison
```
4-Bit SISO:
  SERIAL_IN ──► [FF3] ──► [FF2] ──► [FF1] ──► [FF0] ──► SERIAL_OUT
                  │         │         │         │
                 (Q3)      (Q2)      (Q1)      (Q0) ──► 4-bit Bus (SISO_HEX)

4-Bit PIPO:
  D3 ──────────► [FF3] ────────────────────────► PIPO_Q3 ┐
  D2 ──────────► [FF2] ────────────────────────► PIPO_Q2 ┼─► 4-bit Bus (PIPO_HEX)
  D1 ──────────► [FF1] ────────────────────────► PIPO_Q1 │
  D0 ──────────► [FF0] ────────────────────────► PIPO_Q0 ┘
```

### 4.3 SISO Clock Shift Trace Example (Loading Nibble `1011`)
Assume register cleared initially ($Q_3 Q_2 Q_1 Q_0 = 0000_2$):

| Clock Pulse | $SI$ (Serial In) | $Q_3$ | $Q_2$ | $Q_1$ | $Q_0$ ($SO$) | Bus Hex |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Init** | — | 0 | 0 | 0 | 0 | `0x0` |
| **Clock 1** | **1** | 1 | 0 | 0 | 0 | `0x8` |
| **Clock 2** | **1** | 1 | 1 | 0 | 0 | `0xC` |
| **Clock 3** | **0** | 0 | 1 | 1 | 0 | `0x6` |
| **Clock 4** | **1** | 1 | 0 | 1 | 1 | **`0xB`** |

*Notice: Exactly 4 clock pulses are required to load a 4-bit word serially, and another 4 pulses to shift it out.*

### 4.4 How to Verify in Logisim
1. Open [exp4_siso_and_pipo.circ](file:///home/luckycelestial/Pavithran/DPCO/exp4_siso_and_pipo.circ).
2. **SISO Verification**:
   - Pulse `RESET_SISO = 1` then `0` to clear.
   - Enter bit stream `1, 1, 0, 1` with `SERIAL_IN`, pulsing `CLK_SISO` after each bit.
   - Watch `SISO_HEX` update: `0x0` $\to$ `0x8` $\to$ `0xC` $\to$ `0x6` $\to$ `0xB`.
3. **PIPO Verification**:
   - Set inputs $D_3=1, D_2=0, D_1=1, D_0=0$ (`1010` = `0xA`).
   - Pulse `CLK_PIPO` once.
   - `PIPO_HEX` updates to `0xA` in a single clock cycle!

---

## Experiment 5: 4-Bit Up & Down Ripple Counters using D Flip-Flop

### 5.1 Objective
Construct and verify asynchronous 4-bit MOD-16 binary **UP** and **DOWN** ripple counters ($0 \leftrightarrow 15$) implemented separately using pure D flip-flops (without multiplexers), complete with multi-format output displays (Decimal, Hex, Binary, and 7-Segment Hex Display).

### 5.2 Operating Principle

#### 1. Toggle Mode Conversion ($D = \overline{Q}$)
In a standard D Flip-Flop, connecting the inverted output $\overline{Q}$ directly back to data input $D$ ($D = \overline{Q}$) causes the flip-flop to invert its state on every active falling clock edge:
$$Q_{next} = \overline{Q}$$
This naturally divides the input clock frequency by 2 ($\text{divide-by-2 counter}$).

#### 2. Separate UP and DOWN Clocking Architecture (No Multiplexers)
When using **negative-edge triggered** flip-flops:
- **Part A (4-Bit UP Counter):**
  - Next stage clock is driven directly by **$Q_n$**:
    $$CLK_{n+1} = Q_n$$
  - When stage $n$ transitions $1 \to 0$ (falling edge), stage $n+1$ toggles. This produces an incrementing binary sequence: $0000_2 \to 1111_2$ ($0 \to 15$).
- **Part B (4-Bit DOWN Counter):**
  - Next stage clock is driven directly by **$\overline{Q}_n$**:
    $$CLK_{n+1} = \overline{Q}_n$$
  - When stage $n$ transitions $0 \to 1$ (borrow, meaning $\overline{Q}_n$ falls $1 \to 0$), stage $n+1$ toggles. This produces a decrementing binary sequence: $1111_2 \to 0000_2$ ($15 \to 0$).

```
PART A: UP COUNTER (Top Section)
  CLK_UP ──► [ CLK | FF0 ] ──► Q0 (LSB) ──┬──► Splitter [0]
               D ◄── ~Q0 ──┘              │
                                          └──► [ CLK | FF1 ] ──► Q1 ──┬──► Splitter [1]
                                                 D ◄── ~Q1 ──┘        │
                                                                      └──► [ CLK | FF2 ] ──► Q2 ──┬──► Splitter [2]
                                                                             D ◄── ~Q2 ──┘        │
                                                                                                  └──► [ CLK | FF3 ] ──► Q3 (MSB) ──► Splitter [3]
                                                                                                         D ◄── ~Q3 ──┘

PART B: DOWN COUNTER (Bottom Section)
  CLK_DN ──► [ CLK | FF0 ] ──► Q0 (LSB) ──────────────────────────────┬──► Splitter [0]
               D ◄── ~Q0 ──┬──────────────┐                           │
                           └──────────────┴──► [ CLK | FF1 ] ──► Q1 ──┼──► Splitter [1]
                                                 D ◄── ~Q1 ──┬────────┘
                                                             └────────► [ CLK | FF2 ] ──► Q2 ──┬──► Splitter [2]
                                                                          D ◄── ~Q2 ──┬────────┘
                                                                                      └────────► [ CLK | FF3 ] ──► Q3 (MSB) ──► Splitter [3]
                                                                                                   D ◄── ~Q3 ──┘
```

### 5.3 Complete Count Sequences (MOD-16)

| State / Pulse | $Q_3$ | $Q_2$ | $Q_1$ | $Q_0$ | UP Count Decimal | DOWN Count Decimal | Hex Glyph |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 0 | 0 | **0** | **0** | `0` |
| 1 | 0 | 0 | 0 | 1 | **1** | **15** | `1` / `F` |
| 2 | 0 | 0 | 1 | 0 | **2** | **14** | `2` / `E` |
| 3 | 0 | 0 | 1 | 1 | **3** | **13** | `3` / `d` |
| 4 | 0 | 1 | 0 | 0 | **4** | **12** | `4` / `C` |
| 5 | 0 | 1 | 0 | 1 | **5** | **11** | `5` / `b` |
| 6 | 0 | 1 | 1 | 0 | **6** | **10** | `6` / `A` |
| 7 | 0 | 1 | 1 | 1 | **7** | **9** | `7` / `9` |
| 8 | 1 | 0 | 0 | 0 | **8** | **8** | `8` |
| 9 | 1 | 0 | 0 | 1 | **9** | **7** | `9` / `7` |
| 10 | 1 | 0 | 1 | 0 | **10** | **6** | `A` / `6` |
| 11 | 1 | 0 | 1 | 1 | **11** | **5** | `b` / `5` |
| 12 | 1 | 1 | 0 | 0 | **12** | **4** | `C` / `4` |
| 13 | 1 | 1 | 0 | 1 | **13** | **3** | `d` / `3` |
| 14 | 1 | 1 | 1 | 0 | **14** | **2** | `E` / `2` |
| 15 | 1 | 1 | 1 | 1 | **15** | **1** | `F` / `1` |
| 16 (Roll) | 0 | 0 | 0 | 0 | **0** | **0** | `0` |

### 5.4 How to Show Output in Logisim (Display Guide)

Both the UP and DOWN sections are independently equipped with full output instrumentation:

1. **4-Bit Bus Splitter (`Wiring -> Splitter`)**:
   - `Fan Out = 4`, `Incoming Lines = 4`.
   - Combines $Q_0, Q_1, Q_2, Q_3$ into a single 4-bit bus.
2. **Digital Probes (`Wiring -> Probe`)**:
   - **Decimal Probe (`Radix = 10 unsigned`)**: Displays count as integer `0` to `15`.
   - **Hex Probe (`Radix = 16`)**: Displays count as `0` to `F`.
   - **Binary Probe (`Radix = 2`)**: Displays 4-bit binary pattern `0000` to `1111`.
3. **Hex Digit 7-Segment Display (`Input/Output -> Hex Digit Display`)**:
   - Directly renders the 4-bit nibble on a simulated LED digit.
4. **Individual Bit Output Pins**:
   - `UP_Q3..UP_Q0` and `DN_Q3..DN_Q0` with live green wire states.

### 5.5 Step-by-Step Verification in Logisim

1. **Open the Circuit File**:
   Open [exp5_4bit_ripple_counter_dff.circ](file:///home/luckycelestial/Pavithran/DPCO/exp5_4bit_ripple_counter_dff.circ) in Logisim.
2. **Select the Poke Tool** (`👆` or `Ctrl+1`).
3. **Verify UP Counter (Top Section)**:
   - Click `CLK_UP` repeatedly (or press **Ctrl+K** for auto-ticking).
   - Watch `UP_DECIMAL` and `Hex Digit Display` count up: `0 -> 1 -> 2 -> ... -> 15 -> 0`.
   - Test `RESET_UP = 1`: immediately clears to `0`.
4. **Verify DOWN Counter (Bottom Section)**:
   - Click `CLK_DOWN` repeatedly (or press **Ctrl+K** for auto-ticking).
   - Watch `DN_DECIMAL` and `Hex Digit Display` count down: `15 -> 14 -> 13 -> ... -> 0 -> 15`.
   - Test `RESET_DOWN = 1`: immediately clears to `0`.

---

## Experiment 6: 2-Bit Arithmetic Logic Unit (ALU)

### 6.1 Objective
Construct a 2-bit ALU that integrates:
1. **2-bit Binary Adder**
2. **2-bit Binary Subtractor**
3. **2-bit Binary Divider (with Quotient & Remainder outputs)**
4. **4-to-1 Multiplexer (Bus Width 2)** to select which operation drives the main output bus.
5. **Zero-Divisor Comparator** detecting division-by-zero exceptions ($B = 00_2$).

### 6.2 ALU Architecture Block Diagram
```
           OPERAND_A [1:0]           OPERAND_B [1:0]
                 │                          │
                 ├──────────────────────────┤
                 │                          │
         ┌───────▼────────┐         ┌───────▼────────┐
         │ 2-BIT ADDER    │         │ 2-BIT SUBTRACT │
         └───────┬────────┘         └───────┬────────┘
             Sum │ (2b)                 Diff│ (2b)
                 │                          │
                 │   ┌──────────────────────┤
                 │   │                      │
                 │   │              ┌───────▼────────┐
                 │   │              │ 2-BIT DIVIDER  │
                 │   │              └───────┬────────┘
                 │   │         Quotient (2b)│   │ Remainder (2b)
                 ▼   ▼                      ▼   ▼
               ┌───┬───┬──────────────────┬───┬───┐
               │In0│In1│                  │In2│In3│
               └───┴───┴──────────────────┴───┴───┘
               │          4:1 MULTIPLEXER         │◄─── ALU_SEL [1:0]
               └─────────────────┬────────────────┘
                                 │
                                 ▼
                          ALU_RESULT [1:0]
```

### 6.3 ALU Function Selection Table
| $S_1$ | $S_0$ | Selected Operation | Output Equation | Arithmetic Description |
|:---:|:---:|:---|:---|:---|
| **0** | **0** | **ADDITION** | $ALU = (A + B) \pmod 4$ | 2-bit sum with carry flag |
| **0** | **1** | **SUBTRACTION** | $ALU = (A - B) \pmod 4$ | 2-bit difference with borrow flag |
| **1** | **0** | **DIVISION (QUOTIENT)** | $ALU = \lfloor A / B \rfloor$ | Integer quotient |
| **1** | **1** | **DIVISION (REMAINDER)** | $ALU = A \pmod B$ | Integer remainder (modulo) |

### 6.4 Verification Test Vectors
Let $A = 11_2$ ($3 \text{ dec}$) and $B = 10_2$ ($2 \text{ dec}$):

| Select ($S_1 S_0$) | Mode | Formula | Calculation | Expected `ALU_RESULT` | Auxiliary Flags |
|:---:|:---|:---|:---|:---:|:---|
| `00` | Addition | $A + B$ | $3 + 2 = 5 = 101_2$ | **`01` ($1$)** | `ADD_CARRY = 1` |
| `01` | Subtraction | $A - B$ | $3 - 2 = 1 = 001_2$ | **`01` ($1$)** | `SUB_BORROW = 0` |
| `10` | Division (Quotient) | $\lfloor A / B \rfloor$ | $\lfloor 3 / 2 \rfloor = 1$ | **`01` ($1$)** | `DIV_ZERO_ERR = 0` |
| `11` | Division (Remainder) | $A \pmod B$ | $3 \pmod 2 = 1$ | **`01` ($1$)** | `DIV_ZERO_ERR = 0` |

Divide-by-zero check:
- When $B = 00_2$, the 2-bit Comparator detects $B == 0$ and asserts **`DIV_ZERO_ERR = 1`**.

### 6.5 How to Verify in Logisim
1. Open [exp6_2bit_alu.circ](file:///home/luckycelestial/Pavithran/DPCO/exp6_2bit_alu.circ).
2. Set operands using the Poke Tool:
   - `OPERAND_A`: click to set binary value `00` (0), `01` (1), `10` (2), or `11` (3).
   - `OPERAND_B`: click to set binary value `00` (0), `01` (1), `10` (2), or `11` (3).
3. Toggle `ALU_SEL`:
   - `00` displays Addition result.
   - `01` displays Subtraction result.
   - `10` displays Division Quotient.
   - `11` displays Division Remainder.
4. Set $B = 00$ to verify `DIV_ZERO_ERR` indicator turns ON.

---

## Summary Checklist for Laboratory Assessment

- [x] **Circuit 1**: Both Half Adder and Full Adder isolated, labeled, and mapped to truth tables.
- [x] **Circuit 2**: Gate-level 4:1 MUX (NOT, AND, cascaded OR) and 1:4 DEMUX with input distribution.
- [x] **Circuit 3**: Truth table verification for JK (Hold, Set, Reset, Toggle) and D flip-flops with asynchronous clear.
- [x] **Circuit 4**: 4-bit SISO with serial shifting trace, and 4-bit PIPO with single-cycle parallel capture.
- [x] **Circuit 5**: 4-bit MOD-16 Ripple Up-Counter ($0 \to 15$) using D Flip-Flops in toggle configuration ($D = \overline{Q}$).
- [x] **Circuit 6**: Modular 2-bit ALU uniting Adder, Subtractor, Divider (Quotient & Remainder) and 4:1 MUX selection.

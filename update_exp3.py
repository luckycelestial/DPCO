#!/usr/bin/env python3
"""
Update build_circuits.py with gate-level JK and D flip-flops in exp3.
"""

import os
import xml.etree.ElementTree as ET

CIRCUITS_DIR = "/home/luckycelestial/Pavithran/DPCO"

def get_header(title="main"):
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<project source="2.7.1" version="1.0">
This file is intended to be loaded by Logisim (http://www.cburch.com/logisim/).
<lib desc="#Wiring" name="0"/>
  <lib desc="#Gates" name="1"/>
  <lib desc="#Plexers" name="2"/>
  <lib desc="#Arithmetic" name="3"/>
  <lib desc="#Memory" name="4"/>
  <lib desc="#I/O" name="5"/>
  <lib desc="#Base" name="6">
    <tool name="Text Tool">
      <a name="text" val=""/>
      <a name="font" val="SansSerif plain 12"/>
      <a name="halign" val="center"/>
      <a name="valign" val="base"/>
    </tool>
  </lib>
  <main name="{title}"/>
  <options>
    <a name="gateUndefined" val="ignore"/>
    <a name="simlimit" val="1000"/>
    <a name="simrand" val="0"/>
  </options>
  <mappings>
    <tool lib="6" map="Button2" name="Menu Tool"/>
    <tool lib="6" map="Button3" name="Menu Tool"/>
    <tool lib="6" map="Ctrl Button1" name="Menu Tool"/>
  </mappings>
  <toolbar>
    <tool lib="6" name="Poke Tool"/>
    <tool lib="6" name="Edit Tool"/>
    <tool lib="6" name="Text Tool">
      <a name="text" val=""/>
      <a name="font" val="SansSerif plain 12"/>
      <a name="halign" val="center"/>
      <a name="valign" val="base"/>
    </tool>
    <sep/>
    <tool lib="0" name="Pin">
      <a name="tristate" val="false"/>
    </tool>
    <tool lib="0" name="Pin">
      <a name="facing" val="west"/>
      <a name="output" val="true"/>
      <a name="labelloc" val="east"/>
    </tool>
    <tool lib="1" name="NOT Gate"/>
    <tool lib="1" name="AND Gate"/>
    <tool lib="1" name="OR Gate"/>
  </toolbar>
"""

def build_exp3():
    xml = get_header("main") + """  <circuit name="main">
    <a name="circuit" val="main"/>
    <a name="clabel" val=""/>
    <a name="clabelup" val="east"/>
    <a name="clabelfont" val="SansSerif plain 12"/>

    <!-- Title and Documentation -->
    <comp lib="6" loc="(500,30)" name="Text">
      <a name="text" val="EXPERIMENT 3: VERIFICATION OF JK &amp; D FLIP-FLOPS"/>
      <a name="font" val="SansSerif bold 18"/>
    </comp>
    <comp lib="6" loc="(500,50)" name="Text">
      <a name="text" val="Section 1: Integrated Library Flip-Flops | Section 2: Gate-Level Implementations (NAND Gates)"/>
      <a name="font" val="SansSerif plain 12"/>
    </comp>

    <!-- ========================================================================= -->
    <!-- SECTION 1: INTEGRATED FLIP-FLOPS                                          -->
    <!-- ========================================================================= -->

    <!-- ================= PART A: JK FLIP-FLOP (LIBRARY) ================= -->
    <comp lib="6" loc="(230,85)" name="Text">
      <a name="text" val="PART A: J-K FLIP-FLOP (INTEGRATED COMPONENT)"/>
      <a name="font" val="SansSerif bold 13"/>
    </comp>

    <!-- JK Inputs -->
    <comp lib="0" loc="(80,140)" name="Pin">
      <a name="tristate" val="false"/>
      <a name="label" val="J"/>
    </comp>
    <comp lib="0" loc="(80,160)" name="Clock">
      <a name="label" val="CLK_JK"/>
    </comp>
    <comp lib="0" loc="(80,180)" name="Pin">
      <a name="tristate" val="false"/>
      <a name="label" val="K"/>
    </comp>
    <comp lib="0" loc="(80,230)" name="Pin">
      <a name="tristate" val="false"/>
      <a name="label" val="CLR_JK (Async)"/>
    </comp>

    <!-- J-K Flip-Flop Component (loc = 260, 160) -->
    <comp lib="4" loc="(260,160)" name="J-K Flip-Flop">
      <a name="trigger" val="falling"/>
      <a name="label" val="JK-FF"/>
      <a name="labelloc" val="north"/>
    </comp>

    <!-- JK Outputs -->
    <comp lib="0" loc="(350,160)" name="Pin">
      <a name="facing" val="west"/>
      <a name="output" val="true"/>
      <a name="label" val="Q_JK"/>
      <a name="labelloc" val="east"/>
    </comp>
    <comp lib="0" loc="(350,180)" name="Pin">
      <a name="facing" val="west"/>
      <a name="output" val="true"/>
      <a name="label" val="~Q_JK"/>
      <a name="labelloc" val="east"/>
    </comp>

    <!-- JK Wires -->
    <wire from="(80,140)" to="(180,140)"/>
    <wire from="(180,140)" to="(180,160)"/>
    <wire from="(180,160)" to="(220,160)"/>

    <wire from="(80,160)" to="(150,160)"/>
    <wire from="(150,160)" to="(150,170)"/>
    <wire from="(150,170)" to="(220,170)"/>

    <wire from="(80,180)" to="(220,180)"/>

    <wire from="(260,160)" to="(350,160)"/>
    <wire from="(260,180)" to="(350,180)"/>

    <!-- Async Clear wire to (250, 190) -->
    <wire from="(80,230)" to="(250,230)"/>
    <wire from="(250,230)" to="(250,190)"/>

    <!-- JK Truth Table -->
    <comp lib="6" loc="(230,270)" name="Text">
      <a name="text" val="JK TRUTH TABLE:"/>
      <a name="font" val="SansSerif bold 11"/>
    </comp>
    <comp lib="6" loc="(230,285)" name="Text">
      <a name="text" val="J=0, K=0 -&gt; Hold | J=0, K=1 -&gt; Reset (0)"/>
      <a name="font" val="SansSerif plain 11"/>
    </comp>
    <comp lib="6" loc="(230,300)" name="Text">
      <a name="text" val="J=1, K=0 -&gt; Set (1) | J=1, K=1 -&gt; Toggle (~Q)"/>
      <a name="font" val="SansSerif plain 11"/>
    </comp>
    <comp lib="6" loc="(230,315)" name="Text">
      <a name="text" val="CLR=1   -&gt; Q = 0 (Asynchronous Override)"/>
      <a name="font" val="SansSerif italic 10"/>
    </comp>

    <!-- ================= PART B: D FLIP-FLOP (LIBRARY) ================= -->
    <comp lib="6" loc="(730,85)" name="Text">
      <a name="text" val="PART B: D FLIP-FLOP (INTEGRATED COMPONENT)"/>
      <a name="font" val="SansSerif bold 13"/>
    </comp>

    <!-- D Inputs -->
    <comp lib="0" loc="(560,160)" name="Clock">
      <a name="label" val="CLK_D"/>
    </comp>
    <comp lib="0" loc="(560,180)" name="Pin">
      <a name="tristate" val="false"/>
      <a name="label" val="D"/>
    </comp>
    <comp lib="0" loc="(560,230)" name="Pin">
      <a name="tristate" val="false"/>
      <a name="label" val="CLR_D (Async)"/>
    </comp>

    <!-- D Flip-Flop Component (loc = 740, 160) -->
    <comp lib="4" loc="(740,160)" name="D Flip-Flop">
      <a name="trigger" val="falling"/>
      <a name="label" val="D-FF"/>
      <a name="labelloc" val="north"/>
    </comp>

    <!-- D Outputs -->
    <comp lib="0" loc="(830,160)" name="Pin">
      <a name="facing" val="west"/>
      <a name="output" val="true"/>
      <a name="label" val="Q_D"/>
      <a name="labelloc" val="east"/>
    </comp>
    <comp lib="0" loc="(830,180)" name="Pin">
      <a name="facing" val="west"/>
      <a name="output" val="true"/>
      <a name="label" val="~Q_D"/>
      <a name="labelloc" val="east"/>
    </comp>

    <!-- D Wires -->
    <wire from="(560,160)" to="(700,160)"/>
    <wire from="(560,180)" to="(700,180)"/>
    <wire from="(740,160)" to="(830,160)"/>
    <wire from="(740,180)" to="(830,180)"/>

    <!-- Async Clear wire to (730, 190) -->
    <wire from="(560,230)" to="(730,230)"/>
    <wire from="(730,230)" to="(730,190)"/>

    <!-- D Truth Table -->
    <comp lib="6" loc="(730,270)" name="Text">
      <a name="text" val="D TRUTH TABLE:"/>
      <a name="font" val="SansSerif bold 11"/>
    </comp>
    <comp lib="6" loc="(730,285)" name="Text">
      <a name="text" val="CLK v, D=0 -&gt; Q=0 | CLK v, D=1 -&gt; Q=1"/>
      <a name="font" val="SansSerif plain 11"/>
    </comp>
    <comp lib="6" loc="(730,300)" name="Text">
      <a name="text" val="No Clock   -&gt; Q(t+1) = Q(t) (Hold)"/>
      <a name="font" val="SansSerif plain 11"/>
    </comp>
    <comp lib="6" loc="(730,315)" name="Text">
      <a name="text" val="CLR=1      -&gt; Q = 0 (Asynchronous Override)"/>
      <a name="font" val="SansSerif italic 10"/>
    </comp>

    <!-- ========================================================================= -->
    <!-- SECTION 2: GATE-LEVEL IMPLEMENTATIONS (LOGIC GATES BELOW)                 -->
    <!-- ========================================================================= -->

    <!-- ================= PART C: GATE-LEVEL MASTER-SLAVE JK-FF ================= -->
    <comp lib="6" loc="(260,370)" name="Text">
      <a name="text" val="PART C: GATE-LEVEL MASTER-SLAVE J-K FLIP-FLOP (NAND GATES)"/>
      <a name="font" val="SansSerif bold 13"/>
    </comp>
    <comp lib="6" loc="(260,390)" name="Text">
      <a name="text" val="Master Stage (Active High CLK) + Slave Stage (Active Low CLK) - Free of Race Conditions"/>
      <a name="font" val="SansSerif plain 11"/>
    </comp>

    <!-- Gate-Level JK Inputs -->
    <comp lib="0" loc="(70,450)" name="Pin">
      <a name="tristate" val="false"/>
      <a name="label" val="GATE_J"/>
    </comp>
    <comp lib="0" loc="(70,500)" name="Clock">
      <a name="label" val="GATE_CLK_JK"/>
    </comp>
    <comp lib="0" loc="(70,550)" name="Pin">
      <a name="tristate" val="false"/>
      <a name="label" val="GATE_K"/>
    </comp>

    <!-- Master Stage: 2 3-input NANDs at (190,450) and (190,550) -->
    <comp lib="1" loc="(190,450)" name="NAND Gate">
      <a name="size" val="30"/>
      <a name="inputs" val="3"/>
    </comp>
    <comp lib="1" loc="(190,550)" name="NAND Gate">
      <a name="size" val="30"/>
      <a name="inputs" val="3"/>
    </comp>

    <!-- Master Latch: 2 cross-coupled NANDs at (260,460) and (260,540) -->
    <comp lib="1" loc="(260,460)" name="NAND Gate">
      <a name="size" val="30"/>
      <a name="inputs" val="2"/>
    </comp>
    <comp lib="1" loc="(260,540)" name="NAND Gate">
      <a name="size" val="30"/>
      <a name="inputs" val="2"/>
    </comp>

    <!-- Clock Inverter for Slave Stage -->
    <comp lib="1" loc="(280,500)" name="NOT Gate"/>

    <!-- Slave Steering: 2 2-input NANDs at (340,460) and (340,540) -->
    <comp lib="1" loc="(340,460)" name="NAND Gate">
      <a name="size" val="30"/>
      <a name="inputs" val="2"/>
    </comp>
    <comp lib="1" loc="(340,540)" name="NAND Gate">
      <a name="size" val="30"/>
      <a name="inputs" val="2"/>
    </comp>

    <!-- Slave Latch: 2 cross-coupled NANDs at (420,470) and (420,530) -->
    <comp lib="1" loc="(420,470)" name="NAND Gate">
      <a name="size" val="30"/>
      <a name="inputs" val="2"/>
    </comp>
    <comp lib="1" loc="(420,530)" name="NAND Gate">
      <a name="size" val="30"/>
      <a name="inputs" val="2"/>
    </comp>

    <!-- Gate-Level JK Outputs -->
    <comp lib="0" loc="(480,470)" name="Pin">
      <a name="facing" val="west"/>
      <a name="output" val="true"/>
      <a name="label" val="GATE_Q_JK"/>
      <a name="labelloc" val="east"/>
    </comp>
    <comp lib="0" loc="(480,530)" name="Pin">
      <a name="facing" val="west"/>
      <a name="output" val="true"/>
      <a name="label" val="GATE_~Q_JK"/>
      <a name="labelloc" val="east"/>
    </comp>

    <!-- ================= WIRING FOR GATE-LEVEL JK ================= -->
    <!-- Input J to NAND1 middle pin (160,450) -->
    <wire from="(70,450)" to="(160,450)"/>

    <!-- Input K to NAND2 middle pin (160,550) -->
    <wire from="(70,550)" to="(160,550)"/>

    <!-- Input CLK distribution to Master NANDs and NOT gate -->
    <wire from="(70,500)" to="(120,500)"/>
    <wire from="(120,500)" to="(120,460)"/>
    <wire from="(120,460)" to="(160,460)"/>
    <wire from="(120,500)" to="(120,540)"/>
    <wire from="(120,540)" to="(160,540)"/>
    <wire from="(120,500)" to="(250,500)"/>

    <!-- Master Stage Wires -->
    <!-- NAND1 output to NAND3 pin 1 -->
    <wire from="(190,450)" to="(230,450)"/>
    <!-- NAND2 output to NAND4 pin 2 -->
    <wire from="(190,550)" to="(230,550)"/>

    <!-- Master Latch Cross-Coupling -->
    <!-- NAND3 Out (260,460) to (290,460) and cross to NAND4 In1 (230,530) -->
    <wire from="(260,460)" to="(280,460)"/>
    <wire from="(280,460)" to="(280,480)"/>
    <wire from="(280,480)" to="(220,480)"/>
    <wire from="(220,480)" to="(220,530)"/>
    <wire from="(220,530)" to="(230,530)"/>
    <!-- Tap to Slave NAND5 In1 (310,450) -->
    <wire from="(280,460)" to="(310,460)"/>
    <wire from="(310,460)" to="(310,450)"/>

    <!-- NAND4 Out (260,540) to (280,540) and cross to NAND3 In2 (230,470) -->
    <wire from="(260,540)" to="(280,540)"/>
    <wire from="(280,540)" to="(280,520)"/>
    <wire from="(280,520)" to="(220,520)"/>
    <wire from="(220,520)" to="(220,470)"/>
    <wire from="(220,470)" to="(230,470)"/>
    <!-- Tap to Slave NAND6 In2 (310,550) -->
    <wire from="(280,540)" to="(310,540)"/>
    <wire from="(310,540)" to="(310,550)"/>

    <!-- Inverted Clock distribution to Slave Steering NANDs -->
    <wire from="(280,500)" to="(300,500)"/>
    <wire from="(300,500)" to="(300,470)"/>
    <wire from="(300,470)" to="(310,470)"/>
    <wire from="(300,500)" to="(300,530)"/>
    <wire from="(300,530)" to="(310,530)"/>

    <!-- Slave Steering to Slave Latch -->
    <!-- NAND5 Out (340,460) to NAND7 In1 (390,460) -->
    <wire from="(340,460)" to="(390,460)"/>
    <!-- NAND6 Out (340,540) to NAND8 In2 (390,540) -->
    <wire from="(340,540)" to="(390,540)"/>

    <!-- Slave Latch Cross-Coupling & Outputs -->
    <!-- NAND7 Out (420,470) to Final Q (480,470) -->
    <wire from="(420,470)" to="(440,470)"/>
    <wire from="(440,470)" to="(480,470)"/>
    <!-- Cross to NAND8 In1 (390,520) -->
    <wire from="(440,470)" to="(440,490)"/>
    <wire from="(440,490)" to="(380,490)"/>
    <wire from="(380,490)" to="(380,520)"/>
    <wire from="(380,520)" to="(390,520)"/>
    <!-- Feedback from Q to NAND2 In3 (160,560) via lower rail y=590 -->
    <wire from="(440,470)" to="(450,470)"/>
    <wire from="(450,470)" to="(450,590)"/>
    <wire from="(450,590)" to="(140,590)"/>
    <wire from="(140,590)" to="(140,560)"/>
    <wire from="(140,560)" to="(160,560)"/>

    <!-- NAND8 Out (420,530) to Final ~Q (480,530) -->
    <wire from="(420,530)" to="(440,530)"/>
    <wire from="(440,530)" to="(480,530)"/>
    <!-- Cross to NAND7 In2 (390,480) -->
    <wire from="(440,530)" to="(440,510)"/>
    <wire from="(440,510)" to="(380,510)"/>
    <wire from="(380,510)" to="(380,480)"/>
    <wire from="(380,480)" to="(390,480)"/>
    <!-- Feedback from ~Q to NAND1 In1 (160,440) via upper rail y=420 -->
    <wire from="(440,530)" to="(460,530)"/>
    <wire from="(460,530)" to="(460,420)"/>
    <wire from="(460,420)" to="(140,420)"/>
    <wire from="(140,420)" to="(140,440)"/>
    <wire from="(140,440)" to="(160,440)"/>


    <!-- ================= PART D: GATE-LEVEL CLOCKED D FLIP-FLOP / LATCH ================= -->
    <comp lib="6" loc="(750,370)" name="Text">
      <a name="text" val="PART D: GATE-LEVEL CLOCKED D LATCH / FLIP-FLOP (NAND GATES)"/>
      <a name="font" val="SansSerif bold 13"/>
    </comp>
    <comp lib="6" loc="(750,390)" name="Text">
      <a name="text" val="4 NAND Gates + Inverter: When CLK=1 Q follows D, When CLK=0 Q holds state"/>
      <a name="font" val="SansSerif plain 11"/>
    </comp>

    <!-- Gate-Level D Inputs -->
    <comp lib="0" loc="(570,450)" name="Pin">
      <a name="tristate" val="false"/>
      <a name="label" val="GATE_D"/>
    </comp>
    <comp lib="0" loc="(570,500)" name="Clock">
      <a name="label" val="GATE_CLK_D"/>
    </comp>

    <!-- Inverter for D input -->
    <comp lib="1" loc="(640,550)" name="NOT Gate"/>

    <!-- Steering NANDs at (710,460) and (710,540) -->
    <comp lib="1" loc="(710,460)" name="NAND Gate">
      <a name="size" val="30"/>
      <a name="inputs" val="2"/>
    </comp>
    <comp lib="1" loc="(710,540)" name="NAND Gate">
      <a name="size" val="30"/>
      <a name="inputs" val="2"/>
    </comp>

    <!-- Cross-Coupled Storage NANDs at (810,470) and (810,530) -->
    <comp lib="1" loc="(810,470)" name="NAND Gate">
      <a name="size" val="30"/>
      <a name="inputs" val="2"/>
    </comp>
    <comp lib="1" loc="(810,530)" name="NAND Gate">
      <a name="size" val="30"/>
      <a name="inputs" val="2"/>
    </comp>

    <!-- Gate-Level D Outputs -->
    <comp lib="0" loc="(870,470)" name="Pin">
      <a name="facing" val="west"/>
      <a name="output" val="true"/>
      <a name="label" val="GATE_Q_D"/>
      <a name="labelloc" val="east"/>
    </comp>
    <comp lib="0" loc="(870,530)" name="Pin">
      <a name="facing" val="west"/>
      <a name="output" val="true"/>
      <a name="label" val="GATE_~Q_D"/>
      <a name="labelloc" val="east"/>
    </comp>

    <!-- ================= WIRING FOR GATE-LEVEL D ================= -->
    <!-- Input D distribution -->
    <wire from="(570,450)" to="(600,450)"/>
    <wire from="(600,450)" to="(680,450)"/>
    <wire from="(600,450)" to="(600,550)"/>
    <wire from="(600,550)" to="(610,550)"/>

    <!-- Inverted D to lower NAND In2 (680,550) -->
    <wire from="(640,550)" to="(680,550)"/>

    <!-- Input CLK_D distribution to both steering NANDs -->
    <wire from="(570,500)" to="(650,500)"/>
    <wire from="(650,500)" to="(650,470)"/>
    <wire from="(650,470)" to="(680,470)"/>
    <wire from="(650,500)" to="(650,530)"/>
    <wire from="(650,530)" to="(680,530)"/>

    <!-- Steering NANDs to Cross-Coupled Storage NANDs -->
    <wire from="(710,460)" to="(780,460)"/>
    <wire from="(710,540)" to="(780,540)"/>

    <!-- Cross-Coupled Storage Wires -->
    <!-- Top Storage NAND Out (810,470) to Pin (870,470) and Cross -->
    <wire from="(810,470)" to="(840,470)"/>
    <wire from="(840,470)" to="(870,470)"/>
    <wire from="(840,470)" to="(840,500)"/>
    <wire from="(840,500)" to="(760,500)"/>
    <wire from="(760,500)" to="(760,520)"/>
    <wire from="(760,520)" to="(780,520)"/>

    <!-- Bottom Storage NAND Out (810,530) to Pin (870,530) and Cross -->
    <wire from="(810,530)" to="(840,530)"/>
    <wire from="(840,530)" to="(870,530)"/>
    <wire from="(840,530)" to="(840,500)"/>
    <wire from="(840,530)" to="(850,530)"/>
    <wire from="(850,530)" to="(850,500)"/>
    <wire from="(850,500)" to="(770,500)"/>
    <wire from="(770,500)" to="(770,480)"/>
    <wire from="(770,480)" to="(780,480)"/>

  </circuit>
</project>
"""
    return xml

def update_exp3_only():
    filepath = os.path.join(CIRCUITS_DIR, "exp3_jk_and_d_flip_flop.circ")
    content = build_exp3()
    with open(filepath, "w") as f:
        f.write(content)
    # Parse check
    tree = ET.parse(filepath)
    root = tree.getroot()
    circuit = root.find("circuit")
    comps = circuit.findall("comp")
    wires = circuit.findall("wire")
    print(f"exp3_jk_and_d_flip_flop.circ successfully updated!")
    print(f"Total components: {len(comps)} | Total wires: {len(wires)}")

if __name__ == "__main__":
    update_exp3_only()

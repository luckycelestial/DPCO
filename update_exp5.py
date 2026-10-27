#!/usr/bin/env python3
"""
Update exp5_4bit_ripple_counter_dff.circ to implement 4-Bit Synchronized UP and DOWN ripple counter
with comprehensive output displays (Decimal probe, Hex probe, Binary probe, 7-Segment Hex Display,
individual LED bits, and 4-bit bus pin).
"""

import os
import xml.etree.ElementTree as ET

CIRCUITS_DIR = "/home/luckycelestial/Pavithran/DPCO"

def build_exp5_up_down():
    xml = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
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
  <main name="main"/>
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
  <circuit name="main">
    <a name="circuit" val="main"/>
    <a name="clabel" val=""/>
    <a name="clabelup" val="east"/>
    <a name="clabelfont" val="SansSerif plain 12"/>

    <!-- Title and Documentation -->
    <comp lib="6" loc="(560,35)" name="Text">
      <a name="text" val="EXPERIMENT 5: 4-BIT ASYNCHRONOUS UP / DOWN RIPPLE COUNTER (D-FF)"/>
      <a name="font" val="SansSerif bold 18"/>
    </comp>
    <comp lib="6" loc="(560,60)" name="Text">
      <a name="text" val="Mode UP_DOWN = 1: Counts UP (0 to 15) via Q | Mode UP_DOWN = 0: Counts DOWN (15 to 0) via ~Q"/>
      <a name="font" val="SansSerif plain 12"/>
    </comp>

    <!-- Master Controls on Left -->
    <comp lib="0" loc="(80,200)" name="Clock">
      <a name="label" val="MASTER_CLK"/>
    </comp>
    <comp lib="0" loc="(80,290)" name="Pin">
      <a name="tristate" val="false"/>
      <a name="label" val="UP_DOWN_SEL (1=UP, 0=DN)"/>
    </comp>
    <comp lib="0" loc="(80,330)" name="Pin">
      <a name="tristate" val="false"/>
      <a name="label" val="RESET (Async Clear)"/>
    </comp>

    <!-- 4 D Flip-Flops in Toggle Mode (Falling-Edge Triggered) -->
    <!-- FF0 (LSB, bit 0): loc = 220, 200 -->
    <comp lib="4" loc="(220,200)" name="D Flip-Flop">
      <a name="trigger" val="falling"/>
      <a name="label" val="FF0 (LSB)"/>
      <a name="labelloc" val="north"/>
    </comp>

    <!-- FF1 (bit 1): loc = 420, 200 -->
    <comp lib="4" loc="(420,200)" name="D Flip-Flop">
      <a name="trigger" val="falling"/>
      <a name="label" val="FF1"/>
      <a name="labelloc" val="north"/>
    </comp>

    <!-- FF2 (bit 2): loc = 620, 200 -->
    <comp lib="4" loc="(620,200)" name="D Flip-Flop">
      <a name="trigger" val="falling"/>
      <a name="label" val="FF2"/>
      <a name="labelloc" val="north"/>
    </comp>

    <!-- FF3 (MSB, bit 3): loc = 820, 200 -->
    <comp lib="4" loc="(820,200)" name="D Flip-Flop">
      <a name="trigger" val="falling"/>
      <a name="label" val="FF3 (MSB)"/>
      <a name="labelloc" val="north"/>
    </comp>

    <!-- 3 Multiplexers for Up/Down Ripple Clock Steering -->
    <!-- MUX 0: selects ~Q0 (down) or Q0 (up) to clock FF1 -->
    <comp lib="2" loc="(340,180)" name="Multiplexer">
      <a name="enable" val="false"/>
    </comp>
    <comp lib="6" loc="(340,155)" name="Text">
      <a name="text" val="CLK1 SEL"/>
      <a name="font" val="SansSerif plain 10"/>
    </comp>

    <!-- MUX 1: selects ~Q1 (down) or Q1 (up) to clock FF2 -->
    <comp lib="2" loc="(540,180)" name="Multiplexer">
      <a name="enable" val="false"/>
    </comp>
    <comp lib="6" loc="(540,155)" name="Text">
      <a name="text" val="CLK2 SEL"/>
      <a name="font" val="SansSerif plain 10"/>
    </comp>

    <!-- MUX 2: selects ~Q2 (down) or Q2 (up) to clock FF3 -->
    <comp lib="2" loc="(740,180)" name="Multiplexer">
      <a name="enable" val="false"/>
    </comp>
    <comp lib="6" loc="(740,155)" name="Text">
      <a name="text" val="CLK3 SEL"/>
      <a name="font" val="SansSerif plain 10"/>
    </comp>

    <!-- Individual Bit Pins & Probes (Top) -->
    <comp lib="0" loc="(250,150)" name="Pin">
      <a name="facing" val="south"/>
      <a name="output" val="true"/>
      <a name="label" val="Q0 (LSB)"/>
      <a name="labelloc" val="north"/>
    </comp>
    <comp lib="0" loc="(450,150)" name="Pin">
      <a name="facing" val="south"/>
      <a name="output" val="true"/>
      <a name="label" val="Q1"/>
      <a name="labelloc" val="north"/>
    </comp>
    <comp lib="0" loc="(650,150)" name="Pin">
      <a name="facing" val="south"/>
      <a name="output" val="true"/>
      <a name="label" val="Q2"/>
      <a name="labelloc" val="north"/>
    </comp>
    <comp lib="0" loc="(850,150)" name="Pin">
      <a name="facing" val="south"/>
      <a name="output" val="true"/>
      <a name="label" val="Q3 (MSB)"/>
      <a name="labelloc" val="north"/>
    </comp>

    <!-- Combined 4-Bit Bus Splitter -->
    <comp lib="0" loc="(940,200)" name="Splitter">
      <a name="facing" val="west"/>
      <a name="fanout" val="4"/>
      <a name="incoming" val="4"/>
      <a name="appear" val="right"/>
    </comp>

    <!-- Output Visualization Displays -->
    <!-- 1. Decimal Numeric Value (0 to 15) -->
    <comp lib="0" loc="(980,160)" name="Probe">
      <a name="radix" val="10unsigned"/>
      <a name="label" val="DECIMAL"/>
      <a name="labelloc" val="north"/>
    </comp>

    <!-- 2. Hexadecimal Numeric Value (0 to F) -->
    <comp lib="0" loc="(980,200)" name="Probe">
      <a name="radix" val="16"/>
      <a name="label" val="HEX"/>
      <a name="labelloc" val="north"/>
    </comp>

    <!-- 3. Binary 4-Bit Bus Representation (0000 to 1111) -->
    <comp lib="0" loc="(980,240)" name="Probe">
      <a name="radix" val="2"/>
      <a name="label" val="BINARY [Q3..Q0]"/>
      <a name="labelloc" val="north"/>
    </comp>

    <!-- 4. Graphical 7-Segment Hex Digit Display (I/O Library) -->
    <comp lib="5" loc="(1040,200)" name="Hex Digit Display"/>

    <!-- 5. 4-Bit Bus Output Terminal Pin -->
    <comp lib="0" loc="(1080,200)" name="Pin">
      <a name="facing" val="west"/>
      <a name="output" val="true"/>
      <a name="width" val="4"/>
      <a name="label" val="COUNT_BUS"/>
      <a name="labelloc" val="east"/>
    </comp>

    <!-- ================= WIRING ================= -->
    <!-- MASTER_CLK to FF0 Clock (180, 200) -->
    <wire from="(80,200)" to="(180,200)"/>

    <!-- D Flip-Flop Toggle Feedback: D = ~Q for all 4 stages -->
    <!-- FF0: ~Q at (220, 220) -> D at (180, 220) via y=250 -->
    <wire from="(220,220)" to="(230,220)"/>
    <wire from="(230,220)" to="(230,250)"/>
    <wire from="(230,250)" to="(160,250)"/>
    <wire from="(160,250)" to="(160,220)"/>
    <wire from="(160,220)" to="(180,220)"/>

    <!-- FF1: ~Q at (420, 220) -> D at (380, 220) via y=250 -->
    <wire from="(420,220)" to="(430,220)"/>
    <wire from="(430,220)" to="(430,250)"/>
    <wire from="(430,250)" to="(360,250)"/>
    <wire from="(360,250)" to="(360,220)"/>
    <wire from="(360,220)" to="(380,220)"/>

    <!-- FF2: ~Q at (620, 220) -> D at (580, 220) via y=250 -->
    <wire from="(620,220)" to="(630,220)"/>
    <wire from="(630,220)" to="(630,250)"/>
    <wire from="(630,250)" to="(560,250)"/>
    <wire from="(560,250)" to="(560,220)"/>
    <wire from="(560,220)" to="(580,220)"/>

    <!-- FF3: ~Q at (820, 220) -> D at (780, 220) via y=250 -->
    <wire from="(820,220)" to="(830,220)"/>
    <wire from="(830,220)" to="(830,250)"/>
    <wire from="(830,250)" to="(760,250)"/>
    <wire from="(760,250)" to="(760,220)"/>
    <wire from="(760,220)" to="(780,220)"/>

    <!-- Q and ~Q connections to MUXes and output bus -->
    <!-- STAGE 0 (FF0): -->
    <!-- Q0 (220, 200) to Pin, Bus, and MUX0 In1 (320, 190) -->
    <wire from="(220,200)" to="(250,200)"/>
    <wire from="(250,200)" to="(250,150)"/>
    <wire from="(250,200)" to="(300,200)"/>
    <wire from="(300,200)" to="(300,190)"/>
    <wire from="(300,190)" to="(320,190)"/>
    <!-- Wire Q0 to 4-bit bus bit 0 -->
    <wire from="(250,150)" to="(250,110)"/>
    <wire from="(250,110)" to="(900,110)"/>
    <wire from="(900,110)" to="(900,240)"/>
    <wire from="(900,240)" to="(920,240)"/>

    <!-- ~Q0 to MUX0 In0 (320, 170) -->
    <wire from="(230,220)" to="(280,220)"/>
    <wire from="(280,220)" to="(280,170)"/>
    <wire from="(280,170)" to="(320,170)"/>

    <!-- MUX0 Output (340, 180) to FF1 Clock (380, 200) -->
    <wire from="(340,180)" to="(360,180)"/>
    <wire from="(360,180)" to="(360,200)"/>
    <wire from="(360,200)" to="(380,200)"/>

    <!-- STAGE 1 (FF1): -->
    <!-- Q1 (420, 200) to Pin, Bus, and MUX1 In1 (520, 190) -->
    <wire from="(420,200)" to="(450,200)"/>
    <wire from="(450,200)" to="(450,150)"/>
    <wire from="(450,200)" to="(500,200)"/>
    <wire from="(500,200)" to="(500,190)"/>
    <wire from="(500,190)" to="(520,190)"/>
    <!-- Wire Q1 to 4-bit bus bit 1 -->
    <wire from="(450,150)" to="(450,120)"/>
    <wire from="(450,120)" to="(890,120)"/>
    <wire from="(890,120)" to="(890,230)"/>
    <wire from="(890,230)" to="(920,230)"/>

    <!-- ~Q1 to MUX1 In0 (520, 170) -->
    <wire from="(430,220)" to="(480,220)"/>
    <wire from="(480,220)" to="(480,170)"/>
    <wire from="(480,170)" to="(520,170)"/>

    <!-- MUX1 Output (540, 180) to FF2 Clock (580, 200) -->
    <wire from="(540,180)" to="(560,180)"/>
    <wire from="(560,180)" to="(560,200)"/>
    <wire from="(560,200)" to="(580,200)"/>

    <!-- STAGE 2 (FF2): -->
    <!-- Q2 (620, 200) to Pin, Bus, and MUX2 In1 (720, 190) -->
    <wire from="(620,200)" to="(650,200)"/>
    <wire from="(650,200)" to="(650,150)"/>
    <wire from="(650,200)" to="(700,200)"/>
    <wire from="(700,200)" to="(700,190)"/>
    <wire from="(700,190)" to="(720,190)"/>
    <!-- Wire Q2 to 4-bit bus bit 2 -->
    <wire from="(650,150)" to="(650,130)"/>
    <wire from="(650,130)" to="(880,130)"/>
    <wire from="(880,130)" to="(880,220)"/>
    <wire from="(880,220)" to="(920,220)"/>

    <!-- ~Q2 to MUX2 In0 (720, 170) -->
    <wire from="(630,220)" to="(680,220)"/>
    <wire from="(680,220)" to="(680,170)"/>
    <wire from="(680,170)" to="(720,170)"/>

    <!-- MUX2 Output (740, 180) to FF3 Clock (780, 200) -->
    <wire from="(740,180)" to="(760,180)"/>
    <wire from="(760,180)" to="(760,200)"/>
    <wire from="(760,200)" to="(780,200)"/>

    <!-- STAGE 3 (FF3, MSB): -->
    <!-- Q3 (820, 200) to Pin and Bus bit 3 (920, 210) -->
    <wire from="(820,200)" to="(850,200)"/>
    <wire from="(850,200)" to="(850,150)"/>
    <wire from="(850,200)" to="(870,200)"/>
    <wire from="(870,200)" to="(870,210)"/>
    <wire from="(870,210)" to="(920,210)"/>

    <!-- MODE CONTROL: UP_DOWN_SEL (80, 290) distributed to all 3 MUXes -->
    <wire from="(80,290)" to="(330,290)"/>
    <wire from="(330,290)" to="(330,200)"/>
    <wire from="(330,290)" to="(530,290)"/>
    <wire from="(530,290)" to="(530,200)"/>
    <wire from="(530,290)" to="(730,290)"/>
    <wire from="(730,290)" to="(730,200)"/>

    <!-- ASYNCHRONOUS RESET: distributed to all 4 Flip-Flop Clear pins (loc - (10, -30) = y=230) -->
    <wire from="(80,330)" to="(210,330)"/>
    <wire from="(210,330)" to="(210,230)"/>
    <wire from="(210,330)" to="(410,330)"/>
    <wire from="(410,330)" to="(410,230)"/>
    <wire from="(410,330)" to="(610,330)"/>
    <wire from="(610,330)" to="(610,230)"/>
    <wire from="(610,330)" to="(810,330)"/>
    <wire from="(810,330)" to="(810,230)"/>

    <!-- 4-Bit Output Bus Distribution to Probes & Displays -->
    <wire from="(940,200)" to="(960,200)"/>
    <wire from="(960,200)" to="(980,200)"/>
    <wire from="(980,200)" to="(1040,200)"/>
    <wire from="(1040,200)" to="(1080,200)"/>

    <wire from="(960,200)" to="(960,160)"/>
    <wire from="(960,160)" to="(980,160)"/>

    <wire from="(960,200)" to="(960,240)"/>
    <wire from="(960,240)" to="(980,240)"/>

    <!-- State Sequence Guide on Canvas -->
    <comp lib="6" loc="(560,370)" name="Text">
      <a name="text" val="COUNT SEQUENCE GUIDE:"/>
      <a name="font" val="SansSerif bold 12"/>
    </comp>
    <comp lib="6" loc="(560,390)" name="Text">
      <a name="text" val="UP MODE   (UP_DOWN=1):  0 -&gt; 1 -&gt; 2 -&gt; 3 -&gt; 4 -&gt; 5 -&gt; 6 -&gt; 7 -&gt; 8 -&gt; 9 -&gt; 10(A) -&gt; 11(B) -&gt; 12(C) -&gt; 13(D) -&gt; 14(E) -&gt; 15(F) -&gt; 0"/>
      <a name="font" val="SansSerif plain 11"/>
    </comp>
    <comp lib="6" loc="(560,410)" name="Text">
      <a name="text" val="DOWN MODE (UP_DOWN=0): 15(F) -&gt; 14(E) -&gt; 13(D) -&gt; 12(C) -&gt; 11(B) -&gt; 10(A) -&gt; 9 -&gt; 8 -&gt; 7 -&gt; 6 -&gt; 5 -&gt; 4 -&gt; 3 -&gt; 2 -&gt; 1 -&gt; 0 -&gt; 15(F)"/>
      <a name="font" val="SansSerif plain 11"/>
    </comp>
    <comp lib="6" loc="(560,430)" name="Text">
      <a name="text" val="Display Output Options: Decimal Probe (0..15), Hex Probe (0..F), Binary Probe (4 bits), and 7-Segment Hex Digit Display"/>
      <a name="font" val="SansSerif italic 11"/>
    </comp>

  </circuit>
</project>
"""
    filepath = os.path.join(CIRCUITS_DIR, "exp5_4bit_ripple_counter_dff.circ")
    with open(filepath, "w") as f:
        f.write(xml)
    tree = ET.parse(filepath)
    root = tree.getroot()
    circuit = root.find("circuit")
    comps = circuit.findall("comp")
    wires = circuit.findall("wire")
    print(f"exp5_4bit_ripple_counter_dff.circ successfully upgraded to UP/DOWN!")
    print(f"Total components: {len(comps)} | Total wires: {len(wires)}")

if __name__ == "__main__":
    build_exp5_up_down()

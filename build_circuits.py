#!/usr/bin/env python3
"""
Comprehensive Generator for all 6 DPCO Laboratory Circuit files:
1. exp1_half_and_full_adder.circ
2. exp2_mux_and_demux.circ
3. exp3_jk_and_d_flip_flop.circ (Includes Library Components + Gate-Level Master-Slave JK & Clocked D Flip-Flops)
4. exp4_siso_and_pipo.circ
5. exp5_4bit_ripple_counter_dff.circ
6. exp6_2bit_alu.circ
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

# ==============================================================================
# EXP 1: HALF ADDER & FULL ADDER
# ==============================================================================
def build_exp1():
    xml = get_header("main") + """  <circuit name="main">
    <a name="circuit" val="main"/>
    <a name="clabel" val=""/>
    <a name="clabelup" val="east"/>
    <a name="clabelfont" val="SansSerif plain 12"/>

    <!-- Title and Documentation -->
    <comp lib="6" loc="(500,35)" name="Text">
      <a name="text" val="EXPERIMENT 1: IMPLEMENTATION OF HALF ADDER &amp; FULL ADDER"/>
      <a name="font" val="SansSerif bold 18"/>
    </comp>
    <comp lib="6" loc="(500,58)" name="Text">
      <a name="text" val="Half Adder: Sum = A ^ B, Carry = A &amp; B | Full Adder: 2 Half Adders + OR Gate"/>
      <a name="font" val="SansSerif plain 12"/>
    </comp>

    <!-- ================= PART A: HALF ADDER ================= -->
    <comp lib="6" loc="(200,95)" name="Text">
      <a name="text" val="PART A: HALF ADDER"/>
      <a name="font" val="SansSerif bold 14"/>
    </comp>

    <!-- Inputs A and B for Half Adder -->
    <comp lib="0" loc="(100,140)" name="Pin">
      <a name="tristate" val="false"/>
      <a name="label" val="HA_A"/>
    </comp>
    <comp lib="0" loc="(100,200)" name="Pin">
      <a name="tristate" val="false"/>
      <a name="label" val="HA_B"/>
    </comp>

    <!-- Half Adder XOR Gate (loc = 260, 150) -->
    <comp lib="1" loc="(260,150)" name="XOR Gate">
      <a name="size" val="30"/>
      <a name="inputs" val="2"/>
    </comp>
    <!-- Half Adder AND Gate (loc = 260, 210) -->
    <comp lib="1" loc="(260,210)" name="AND Gate">
      <a name="size" val="30"/>
      <a name="inputs" val="2"/>
    </comp>

    <!-- Half Adder Outputs -->
    <comp lib="0" loc="(330,150)" name="Pin">
      <a name="facing" val="west"/>
      <a name="output" val="true"/>
      <a name="label" val="HA_SUM"/>
      <a name="labelloc" val="east"/>
    </comp>
    <comp lib="0" loc="(330,210)" name="Pin">
      <a name="facing" val="west"/>
      <a name="output" val="true"/>
      <a name="label" val="HA_CARRY"/>
      <a name="labelloc" val="east"/>
    </comp>

    <!-- Half Adder Wiring -->
    <wire from="(100,140)" to="(150,140)"/>
    <wire from="(150,140)" to="(220,140)"/>
    <wire from="(150,140)" to="(150,200)"/>
    <wire from="(150,200)" to="(230,200)"/>

    <wire from="(100,200)" to="(170,200)"/>
    <wire from="(170,200)" to="(170,160)"/>
    <wire from="(170,160)" to="(220,160)"/>
    <wire from="(170,200)" to="(170,220)"/>
    <wire from="(170,220)" to="(230,220)"/>

    <wire from="(260,150)" to="(330,150)"/>
    <wire from="(260,210)" to="(330,210)"/>

    <!-- ================= PART B: FULL ADDER (2 HAs + OR Gate) ================= -->
    <comp lib="6" loc="(680,95)" name="Text">
      <a name="text" val="PART B: FULL ADDER (2 HALF ADDERS + OR GATE)"/>
      <a name="font" val="SansSerif bold 14"/>
    </comp>

    <!-- Inputs for Full Adder -->
    <comp lib="0" loc="(480,140)" name="Pin">
      <a name="tristate" val="false"/>
      <a name="label" val="FA_A"/>
    </comp>
    <comp lib="0" loc="(480,200)" name="Pin">
      <a name="tristate" val="false"/>
      <a name="label" val="FA_B"/>
    </comp>
    <comp lib="0" loc="(480,260)" name="Pin">
      <a name="tristate" val="false"/>
      <a name="label" val="FA_CIN"/>
    </comp>

    <!-- First Half Adder in Full Adder -->
    <comp lib="1" loc="(630,150)" name="XOR Gate">
      <a name="size" val="30"/>
      <a name="inputs" val="2"/>
    </comp>
    <comp lib="1" loc="(630,210)" name="AND Gate">
      <a name="size" val="30"/>
      <a name="inputs" val="2"/>
    </comp>

    <!-- Second Half Adder in Full Adder -->
    <comp lib="1" loc="(770,160)" name="XOR Gate">
      <a name="size" val="30"/>
      <a name="inputs" val="2"/>
    </comp>
    <comp lib="1" loc="(770,250)" name="AND Gate">
      <a name="size" val="30"/>
      <a name="inputs" val="2"/>
    </comp>

    <!-- OR Gate for Carry -->
    <comp lib="1" loc="(870,230)" name="OR Gate">
      <a name="size" val="30"/>
      <a name="inputs" val="2"/>
    </comp>

    <!-- Full Adder Outputs -->
    <comp lib="0" loc="(840,160)" name="Pin">
      <a name="facing" val="west"/>
      <a name="output" val="true"/>
      <a name="label" val="FA_SUM"/>
      <a name="labelloc" val="east"/>
    </comp>
    <comp lib="0" loc="(920,230)" name="Pin">
      <a name="facing" val="west"/>
      <a name="output" val="true"/>
      <a name="label" val="FA_COUT"/>
      <a name="labelloc" val="east"/>
    </comp>

    <!-- Full Adder Wiring -->
    <wire from="(480,140)" to="(530,140)"/>
    <wire from="(530,140)" to="(590,140)"/>
    <wire from="(530,140)" to="(530,200)"/>
    <wire from="(530,200)" to="(600,200)"/>

    <wire from="(480,200)" to="(550,200)"/>
    <wire from="(550,200)" to="(550,160)"/>
    <wire from="(550,160)" to="(590,160)"/>
    <wire from="(550,200)" to="(550,220)"/>
    <wire from="(550,220)" to="(600,220)"/>

    <wire from="(630,150)" to="(680,150)"/>
    <wire from="(680,150)" to="(730,150)"/>
    <wire from="(680,150)" to="(680,240)"/>
    <wire from="(680,240)" to="(740,240)"/>

    <wire from="(480,260)" to="(700,260)"/>
    <wire from="(700,260)" to="(700,170)"/>
    <wire from="(700,170)" to="(730,170)"/>
    <wire from="(700,260)" to="(740,260)"/>

    <wire from="(770,160)" to="(840,160)"/>

    <wire from="(630,210)" to="(810,210)"/>
    <wire from="(810,210)" to="(810,220)"/>
    <wire from="(810,220)" to="(840,220)"/>

    <wire from="(770,250)" to="(810,250)"/>
    <wire from="(810,250)" to="(810,240)"/>
    <wire from="(810,240)" to="(840,240)"/>

    <wire from="(870,230)" to="(920,230)"/>

    <!-- Truth Tables as on-canvas text -->
    <comp lib="6" loc="(200,310)" name="Text">
      <a name="text" val="HALF ADDER TRUTH TABLE:"/>
      <a name="font" val="SansSerif bold 12"/>
    </comp>
    <comp lib="6" loc="(200,330)" name="Text">
      <a name="text" val="A=0, B=0 -&gt; SUM=0, CARRY=0"/>
      <a name="font" val="SansSerif plain 11"/>
    </comp>
    <comp lib="6" loc="(200,345)" name="Text">
      <a name="text" val="A=0, B=1 -&gt; SUM=1, CARRY=0"/>
      <a name="font" val="SansSerif plain 11"/>
    </comp>
    <comp lib="6" loc="(200,360)" name="Text">
      <a name="text" val="A=1, B=0 -&gt; SUM=1, CARRY=0"/>
      <a name="font" val="SansSerif plain 11"/>
    </comp>
    <comp lib="6" loc="(200,375)" name="Text">
      <a name="text" val="A=1, B=1 -&gt; SUM=0, CARRY=1"/>
      <a name="font" val="SansSerif plain 11"/>
    </comp>

    <comp lib="6" loc="(700,310)" name="Text">
      <a name="text" val="FULL ADDER TRUTH TABLE:"/>
      <a name="font" val="SansSerif bold 12"/>
    </comp>
    <comp lib="6" loc="(700,330)" name="Text">
      <a name="text" val="Cin B A | SUM COUT | Cin B A | SUM COUT"/>
      <a name="font" val="SansSerif bold 11"/>
    </comp>
    <comp lib="6" loc="(700,345)" name="Text">
      <a name="text" val=" 0  0 0 |  0    0   |  1  0 0 |  1    0 "/>
      <a name="font" val="SansSerif plain 11"/>
    </comp>
    <comp lib="6" loc="(700,360)" name="Text">
      <a name="text" val=" 0  0 1 |  1    0   |  1  0 1 |  0    1 "/>
      <a name="font" val="SansSerif plain 11"/>
    </comp>
    <comp lib="6" loc="(700,375)" name="Text">
      <a name="text" val=" 0  1 0 |  1    0   |  1  1 0 |  0    1 "/>
      <a name="font" val="SansSerif plain 11"/>
    </comp>
    <comp lib="6" loc="(700,390)" name="Text">
      <a name="text" val=" 0  1 1 |  0    1   |  1  1 1 |  1    1 "/>
      <a name="font" val="SansSerif plain 11"/>
    </comp>
  </circuit>
</project>
"""
    return xml

# ==============================================================================
# EXP 2: MUX & DEMUX
# ==============================================================================
def build_exp2():
    xml = get_header("main") + """  <circuit name="main">
    <a name="circuit" val="main"/>
    <a name="clabel" val=""/>
    <a name="clabelup" val="east"/>
    <a name="clabelfont" val="SansSerif plain 12"/>

    <!-- Title and Documentation -->
    <comp lib="6" loc="(500,35)" name="Text">
      <a name="text" val="EXPERIMENT 2: IMPLEMENTATION OF 4:1 MUX &amp; 1:4 DEMUX"/>
      <a name="font" val="SansSerif bold 18"/>
    </comp>
    <comp lib="6" loc="(500,58)" name="Text">
      <a name="text" val="Gate Level Design with Inverters, AND &amp; OR Gates + Logisim Integrated Blocks"/>
      <a name="font" val="SansSerif plain 12"/>
    </comp>

    <!-- ================= PART A: 4:1 MULTIPLEXER ================= -->
    <comp lib="6" loc="(230,95)" name="Text">
      <a name="text" val="PART A: 4-TO-1 MULTIPLEXER (DATA SELECTOR)"/>
      <a name="font" val="SansSerif bold 14"/>
    </comp>

    <!-- Data Inputs I0, I1, I2, I3 -->
    <comp lib="0" loc="(80,140)" name="Pin">
      <a name="tristate" val="false"/>
      <a name="label" val="I0"/>
    </comp>
    <comp lib="0" loc="(80,180)" name="Pin">
      <a name="tristate" val="false"/>
      <a name="label" val="I1"/>
    </comp>
    <comp lib="0" loc="(80,220)" name="Pin">
      <a name="tristate" val="false"/>
      <a name="label" val="I2"/>
    </comp>
    <comp lib="0" loc="(80,260)" name="Pin">
      <a name="tristate" val="false"/>
      <a name="label" val="I3"/>
    </comp>

    <!-- Select Inputs S1, S0 -->
    <comp lib="0" loc="(80,310)" name="Pin">
      <a name="tristate" val="false"/>
      <a name="label" val="MUX_S1"/>
    </comp>
    <comp lib="0" loc="(80,350)" name="Pin">
      <a name="tristate" val="false"/>
      <a name="label" val="MUX_S0"/>
    </comp>

    <!-- NOT Gates for Select Lines -->
    <comp lib="1" loc="(150,310)" name="NOT Gate"/>
    <comp lib="1" loc="(150,350)" name="NOT Gate"/>

    <!-- 4 AND Gates (3-input, size 30) -->
    <comp lib="1" loc="(280,150)" name="AND Gate">
      <a name="size" val="30"/>
      <a name="inputs" val="3"/>
    </comp>
    <comp lib="1" loc="(280,190)" name="AND Gate">
      <a name="size" val="30"/>
      <a name="inputs" val="3"/>
    </comp>
    <comp lib="1" loc="(280,230)" name="AND Gate">
      <a name="size" val="30"/>
      <a name="inputs" val="3"/>
    </comp>
    <comp lib="1" loc="(280,270)" name="AND Gate">
      <a name="size" val="30"/>
      <a name="inputs" val="3"/>
    </comp>

    <!-- 2-Stage OR network combining 4 AND terms -->
    <comp lib="1" loc="(350,170)" name="OR Gate">
      <a name="size" val="30"/>
      <a name="inputs" val="2"/>
    </comp>
    <comp lib="1" loc="(350,250)" name="OR Gate">
      <a name="size" val="30"/>
      <a name="inputs" val="2"/>
    </comp>
    <comp lib="1" loc="(420,210)" name="OR Gate">
      <a name="size" val="30"/>
      <a name="inputs" val="2"/>
    </comp>

    <!-- MUX Gate-Level Output -->
    <comp lib="0" loc="(460,210)" name="Pin">
      <a name="facing" val="west"/>
      <a name="output" val="true"/>
      <a name="label" val="MUX_OUT"/>
      <a name="labelloc" val="east"/>
    </comp>

    <!-- MUX WIRING -->
    <wire from="(80,140)" to="(250,140)"/>
    <wire from="(80,180)" to="(250,180)"/>
    <wire from="(80,220)" to="(250,220)"/>
    <wire from="(80,260)" to="(250,260)"/>

    <!-- S1 true rail at x=190 -->
    <wire from="(80,310)" to="(110,310)"/>
    <wire from="(110,310)" to="(120,310)"/>
    <wire from="(110,310)" to="(110,380)"/>
    <wire from="(110,380)" to="(190,380)"/>
    <wire from="(190,380)" to="(190,230)"/>
    <wire from="(190,230)" to="(250,230)"/>
    <wire from="(190,230)" to="(190,270)"/>
    <wire from="(190,270)" to="(250,270)"/>

    <!-- S1 inverted rail at x=170 -->
    <wire from="(150,310)" to="(170,310)"/>
    <wire from="(170,310)" to="(170,150)"/>
    <wire from="(170,150)" to="(250,150)"/>
    <wire from="(170,150)" to="(170,190)"/>
    <wire from="(170,190)" to="(250,190)"/>

    <!-- S0 true rail at x=230 -->
    <wire from="(80,350)" to="(100,350)"/>
    <wire from="(100,350)" to="(120,350)"/>
    <wire from="(100,350)" to="(100,400)"/>
    <wire from="(100,400)" to="(230,400)"/>
    <wire from="(230,400)" to="(230,200)"/>
    <wire from="(230,200)" to="(250,200)"/>
    <wire from="(230,200)" to="(230,280)"/>
    <wire from="(230,280)" to="(250,280)"/>

    <!-- S0 inverted rail at x=210 -->
    <wire from="(150,350)" to="(210,350)"/>
    <wire from="(210,350)" to="(210,160)"/>
    <wire from="(210,160)" to="(250,160)"/>
    <wire from="(210,160)" to="(210,240)"/>
    <wire from="(210,240)" to="(250,240)"/>

    <!-- OR network wires -->
    <wire from="(280,150)" to="(310,150)"/>
    <wire from="(310,150)" to="(310,160)"/>
    <wire from="(310,160)" to="(320,160)"/>

    <wire from="(280,190)" to="(310,190)"/>
    <wire from="(310,190)" to="(310,180)"/>
    <wire from="(310,180)" to="(320,180)"/>

    <wire from="(280,230)" to="(310,230)"/>
    <wire from="(310,230)" to="(310,240)"/>
    <wire from="(310,240)" to="(320,240)"/>

    <wire from="(280,270)" to="(310,270)"/>
    <wire from="(310,270)" to="(310,260)"/>
    <wire from="(310,260)" to="(320,260)"/>

    <wire from="(350,170)" to="(380,170)"/>
    <wire from="(380,170)" to="(380,200)"/>
    <wire from="(380,200)" to="(390,200)"/>

    <wire from="(350,250)" to="(380,250)"/>
    <wire from="(380,250)" to="(380,220)"/>
    <wire from="(380,220)" to="(390,220)"/>

    <wire from="(420,210)" to="(460,210)"/>

    <!-- ================= PART B: 1:4 DEMULTIPLEXER ================= -->
    <comp lib="6" loc="(730,95)" name="Text">
      <a name="text" val="PART B: 1-TO-4 DEMULTIPLEXER (DATA DISTRIBUTOR)"/>
      <a name="font" val="SansSerif bold 14"/>
    </comp>

    <!-- Data Input Din -->
    <comp lib="0" loc="(560,140)" name="Pin">
      <a name="tristate" val="false"/>
      <a name="label" val="DEMUX_DIN"/>
    </comp>

    <!-- Select Inputs S1, S0 -->
    <comp lib="0" loc="(560,310)" name="Pin">
      <a name="tristate" val="false"/>
      <a name="label" val="DEMUX_S1"/>
    </comp>
    <comp lib="0" loc="(560,350)" name="Pin">
      <a name="tristate" val="false"/>
      <a name="label" val="DEMUX_S0"/>
    </comp>

    <!-- NOT Gates for Select Lines -->
    <comp lib="1" loc="(630,310)" name="NOT Gate"/>
    <comp lib="1" loc="(630,350)" name="NOT Gate"/>

    <!-- 4 AND Gates for Demux Outputs -->
    <comp lib="1" loc="(780,150)" name="AND Gate">
      <a name="size" val="30"/>
      <a name="inputs" val="3"/>
    </comp>
    <comp lib="1" loc="(780,190)" name="AND Gate">
      <a name="size" val="30"/>
      <a name="inputs" val="3"/>
    </comp>
    <comp lib="1" loc="(780,230)" name="AND Gate">
      <a name="size" val="30"/>
      <a name="inputs" val="3"/>
    </comp>
    <comp lib="1" loc="(780,270)" name="AND Gate">
      <a name="size" val="30"/>
      <a name="inputs" val="3"/>
    </comp>

    <!-- Demux Outputs Y0, Y1, Y2, Y3 -->
    <comp lib="0" loc="(840,150)" name="Pin">
      <a name="facing" val="west"/>
      <a name="output" val="true"/>
      <a name="label" val="Y0"/>
      <a name="labelloc" val="east"/>
    </comp>
    <comp lib="0" loc="(840,190)" name="Pin">
      <a name="facing" val="west"/>
      <a name="output" val="true"/>
      <a name="label" val="Y1"/>
      <a name="labelloc" val="east"/>
    </comp>
    <comp lib="0" loc="(840,230)" name="Pin">
      <a name="facing" val="west"/>
      <a name="output" val="true"/>
      <a name="label" val="Y2"/>
      <a name="labelloc" val="east"/>
    </comp>
    <comp lib="0" loc="(840,270)" name="Pin">
      <a name="facing" val="west"/>
      <a name="output" val="true"/>
      <a name="label" val="Y3"/>
      <a name="labelloc" val="east"/>
    </comp>

    <!-- DEMUX WIRING -->
    <wire from="(560,140)" to="(730,140)"/>
    <wire from="(730,140)" to="(750,140)"/>
    <wire from="(730,140)" to="(730,180)"/>
    <wire from="(730,180)" to="(750,180)"/>
    <wire from="(730,180)" to="(730,220)"/>
    <wire from="(730,220)" to="(750,220)"/>
    <wire from="(730,220)" to="(730,260)"/>
    <wire from="(730,260)" to="(750,260)"/>

    <!-- S1 true rail at x=670 -->
    <wire from="(560,310)" to="(590,310)"/>
    <wire from="(590,310)" to="(600,310)"/>
    <wire from="(590,310)" to="(590,380)"/>
    <wire from="(590,380)" to="(670,380)"/>
    <wire from="(670,380)" to="(670,230)"/>
    <wire from="(670,230)" to="(750,230)"/>
    <wire from="(670,230)" to="(670,270)"/>
    <wire from="(670,270)" to="(750,270)"/>

    <!-- S1 inverted rail at x=650 -->
    <wire from="(630,310)" to="(650,310)"/>
    <wire from="(650,310)" to="(650,150)"/>
    <wire from="(650,150)" to="(750,150)"/>
    <wire from="(650,150)" to="(650,190)"/>
    <wire from="(650,190)" to="(750,190)"/>

    <!-- S0 true rail at x=710 -->
    <wire from="(560,350)" to="(580,350)"/>
    <wire from="(580,350)" to="(600,350)"/>
    <wire from="(580,350)" to="(580,400)"/>
    <wire from="(580,400)" to="(710,400)"/>
    <wire from="(710,400)" to="(710,200)"/>
    <wire from="(710,200)" to="(750,200)"/>
    <wire from="(710,200)" to="(710,280)"/>
    <wire from="(710,280)" to="(750,280)"/>

    <!-- S0 inverted rail at x=690 -->
    <wire from="(630,350)" to="(690,350)"/>
    <wire from="(690,350)" to="(690,160)"/>
    <wire from="(690,160)" to="(750,160)"/>
    <wire from="(690,160)" to="(690,240)"/>
    <wire from="(690,240)" to="(750,240)"/>

    <wire from="(780,150)" to="(840,150)"/>
    <wire from="(780,190)" to="(840,190)"/>
    <wire from="(780,230)" to="(840,230)"/>
    <wire from="(780,270)" to="(840,270)"/>

    <!-- Function Tables in Text -->
    <comp lib="6" loc="(230,440)" name="Text">
      <a name="text" val="4:1 MUX FUNCTION TABLE:"/>
      <a name="font" val="SansSerif bold 12"/>
    </comp>
    <comp lib="6" loc="(230,460)" name="Text">
      <a name="text" val="S1=0, S0=0 -&gt; Y = I0"/>
      <a name="font" val="SansSerif plain 11"/>
    </comp>
    <comp lib="6" loc="(230,475)" name="Text">
      <a name="text" val="S1=0, S0=1 -&gt; Y = I1"/>
      <a name="font" val="SansSerif plain 11"/>
    </comp>
    <comp lib="6" loc="(230,490)" name="Text">
      <a name="text" val="S1=1, S0=0 -&gt; Y = I2"/>
      <a name="font" val="SansSerif plain 11"/>
    </comp>
    <comp lib="6" loc="(230,505)" name="Text">
      <a name="text" val="S1=1, S0=1 -&gt; Y = I3"/>
      <a name="font" val="SansSerif plain 11"/>
    </comp>

    <comp lib="6" loc="(730,440)" name="Text">
      <a name="text" val="1:4 DEMUX FUNCTION TABLE:"/>
      <a name="font" val="SansSerif bold 12"/>
    </comp>
    <comp lib="6" loc="(730,460)" name="Text">
      <a name="text" val="S1=0, S0=0 -&gt; Y0=Din, Y1=0, Y2=0, Y3=0"/>
      <a name="font" val="SansSerif plain 11"/>
    </comp>
    <comp lib="6" loc="(730,475)" name="Text">
      <a name="text" val="S1=0, S0=1 -&gt; Y0=0, Y1=Din, Y2=0, Y3=0"/>
      <a name="font" val="SansSerif plain 11"/>
    </comp>
    <comp lib="6" loc="(730,490)" name="Text">
      <a name="text" val="S1=1, S0=0 -&gt; Y0=0, Y1=0, Y2=Din, Y3=0"/>
      <a name="font" val="SansSerif plain 11"/>
    </comp>
    <comp lib="6" loc="(730,505)" name="Text">
      <a name="text" val="S1=1, S0=1 -&gt; Y0=0, Y1=0, Y2=0, Y3=Din"/>
      <a name="font" val="SansSerif plain 11"/>
    </comp>

  </circuit>
</project>
"""
    return xml

# ==============================================================================
# EXP 3: JK & D FLIP FLOP VERIFICATION (LIBRARY + GATE-LEVEL)
# ==============================================================================
def build_exp3():
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

    <!-- Document Header -->
    <comp lib="6" loc="(500,30)" name="Text">
      <a name="text" val="EXPERIMENT 3: VERIFICATION OF JK AND D FLIP-FLOPS"/>
      <a name="font" val="SansSerif bold 18"/>
    </comp>
    <comp lib="6" loc="(500,50)" name="Text">
      <a name="text" val="Top: Integrated Library Components | Bottom: Gate-Level (NAND Gates) Implementations"/>
      <a name="font" val="SansSerif plain 12"/>
    </comp>

    <!-- ================= PART A: JK FLIP-FLOP (LIBRARY) ================= -->
    <comp lib="6" loc="(230,85)" name="Text">
      <a name="text" val="PART A: JK FLIP-FLOP (INTEGRATED COMPONENT)"/>
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

    <!-- JK Flip-Flop Component (loc = 260, 160) -->
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
    <comp lib="0" loc="(60,450)" name="Pin">
      <a name="tristate" val="false"/>
      <a name="label" val="GATE_J"/>
    </comp>
    <comp lib="0" loc="(60,500)" name="Clock">
      <a name="label" val="GATE_CLK_JK"/>
    </comp>
    <comp lib="0" loc="(60,550)" name="Pin">
      <a name="tristate" val="false"/>
      <a name="label" val="GATE_K"/>
    </comp>
    <comp lib="0" loc="(60,600)" name="Pin">
      <a name="tristate" val="false"/>
      <a name="label" val="GATE_CLR_JK"/>
    </comp>

    <!-- Active-High Clear Inverter: produces ~CLR at (100,600) -->
    <comp lib="1" loc="(100,600)" name="NOT Gate"/>

    <!-- Master Stage: 2 3-input NANDs at (190,450) and (190,550) -->
    <!-- In Logisim size=30 NAND inputs are at X-40=(150). Pins at Y-10, Y, Y+10 -->
    <comp lib="1" loc="(190,450)" name="NAND Gate">
      <a name="size" val="30"/>
      <a name="inputs" val="3"/>
    </comp>
    <comp lib="1" loc="(190,550)" name="NAND Gate">
      <a name="size" val="30"/>
      <a name="inputs" val="3"/>
    </comp>

    <!-- Master Latch: 
         Top NAND at (270,460): 2 inputs at (230,450) and (230,470)
         Bottom NAND at (270,540): 3 inputs at (230,530), (230,540), (230,550)
    -->
    <comp lib="1" loc="(270,460)" name="NAND Gate">
      <a name="size" val="30"/>
      <a name="inputs" val="2"/>
    </comp>
    <comp lib="1" loc="(270,540)" name="NAND Gate">
      <a name="size" val="30"/>
      <a name="inputs" val="3"/>
    </comp>

    <!-- Clock Inverter for Slave Stage: loc=(290,500), in at (260,500) -->
    <comp lib="1" loc="(290,500)" name="NOT Gate"/>

    <!-- Slave Steering: 2 2-input NANDs at (350,460) and (350,540): inputs at X-40=(310) -->
    <comp lib="1" loc="(350,460)" name="NAND Gate">
      <a name="size" val="30"/>
      <a name="inputs" val="2"/>
    </comp>
    <comp lib="1" loc="(350,540)" name="NAND Gate">
      <a name="size" val="30"/>
      <a name="inputs" val="2"/>
    </comp>

    <!-- Slave Latch:
         Top NAND at (430,470): 2 inputs at (390,460) and (390,480)
         Bottom NAND at (430,530): 3 inputs at (390,520), (390,530), (390,540)
    -->
    <comp lib="1" loc="(430,470)" name="NAND Gate">
      <a name="size" val="30"/>
      <a name="inputs" val="2"/>
    </comp>
    <comp lib="1" loc="(430,530)" name="NAND Gate">
      <a name="size" val="30"/>
      <a name="inputs" val="3"/>
    </comp>

    <!-- Gate-Level JK Outputs -->
    <comp lib="0" loc="(490,470)" name="Pin">
      <a name="facing" val="west"/>
      <a name="output" val="true"/>
      <a name="label" val="GATE_Q_JK"/>
      <a name="labelloc" val="east"/>
    </comp>
    <comp lib="0" loc="(490,530)" name="Pin">
      <a name="facing" val="west"/>
      <a name="output" val="true"/>
      <a name="label" val="GATE_~Q_JK"/>
      <a name="labelloc" val="east"/>
    </comp>

    <!-- ================= WIRING FOR GATE-LEVEL JK ================= -->
    <!-- Input J to (150,450) -->
    <wire from="(60,450)" to="(150,450)"/>
    <!-- Input K to (150,550) -->
    <wire from="(60,550)" to="(150,550)"/>

    <!-- Clock distribution to (150,460), (150,540), and (260,500) -->
    <wire from="(60,500)" to="(110,500)"/>
    <wire from="(110,500)" to="(110,460)"/>
    <wire from="(110,460)" to="(150,460)"/>
    <wire from="(110,500)" to="(110,540)"/>
    <wire from="(110,540)" to="(150,540)"/>
    <wire from="(110,500)" to="(260,500)"/>

    <!-- Master Input NAND outputs to Master Latch -->
    <wire from="(190,450)" to="(230,450)"/>
    <wire from="(190,550)" to="(230,540)"/>

    <!-- Clear line (~CLR) from (100,600) to Master (230,550) and Slave (390,540) -->
    <wire from="(60,600)" to="(70,600)"/>
    <wire from="(100,600)" to="(230,600)"/>
    <wire from="(230,600)" to="(230,550)"/>
    <wire from="(230,600)" to="(390,600)"/>
    <wire from="(390,600)" to="(390,540)"/>

    <!-- Master Latch Cross-Coupling & Feedforward to Slave -->
    <wire from="(270,460)" to="(290,460)"/>
    <wire from="(290,460)" to="(310,460)"/>
    <wire from="(310,460)" to="(310,450)"/>
    <wire from="(290,460)" to="(290,480)"/>
    <wire from="(290,480)" to="(210,480)"/>
    <wire from="(210,480)" to="(210,530)"/>
    <wire from="(210,530)" to="(230,530)"/>

    <wire from="(270,540)" to="(290,540)"/>
    <wire from="(290,540)" to="(310,540)"/>
    <wire from="(310,540)" to="(310,550)"/>
    <wire from="(290,540)" to="(290,520)"/>
    <wire from="(290,520)" to="(220,520)"/>
    <wire from="(220,520)" to="(220,470)"/>
    <wire from="(220,470)" to="(230,470)"/>

    <!-- Inverted Clock distribution to Slave Steering NANDs -->
    <wire from="(290,500)" to="(300,500)"/>
    <wire from="(300,500)" to="(300,470)"/>
    <wire from="(300,470)" to="(310,470)"/>
    <wire from="(300,500)" to="(300,530)"/>
    <wire from="(300,530)" to="(310,530)"/>

    <!-- Slave Steering to Slave Latch -->
    <wire from="(350,460)" to="(390,460)"/>
    <wire from="(350,540)" to="(390,530)"/>

    <!-- Slave Latch Cross-Coupling & Outputs -->
    <wire from="(430,470)" to="(450,470)"/>
    <wire from="(450,470)" to="(490,470)"/>
    <wire from="(450,470)" to="(450,490)"/>
    <wire from="(450,490)" to="(370,490)"/>
    <wire from="(370,490)" to="(370,520)"/>
    <wire from="(370,520)" to="(390,520)"/>

    <!-- Feedback from Q to NAND2 In2 (150,560) via lower rail y=620 -->
    <wire from="(450,470)" to="(470,470)"/>
    <wire from="(470,470)" to="(470,620)"/>
    <wire from="(470,620)" to="(130,620)"/>
    <wire from="(130,620)" to="(130,560)"/>
    <wire from="(130,560)" to="(150,560)"/>

    <wire from="(430,530)" to="(460,530)"/>
    <wire from="(460,530)" to="(490,530)"/>
    <wire from="(460,530)" to="(460,510)"/>
    <wire from="(460,510)" to="(380,510)"/>
    <wire from="(380,510)" to="(380,480)"/>
    <wire from="(380,480)" to="(390,480)"/>

    <!-- Feedback from ~Q to NAND1 In0 (150,440) via upper rail y=410 -->
    <wire from="(460,530)" to="(480,530)"/>
    <wire from="(480,530)" to="(480,410)"/>
    <wire from="(480,410)" to="(130,410)"/>
    <wire from="(130,410)" to="(130,440)"/>
    <wire from="(130,440)" to="(150,440)"/>


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

    <!-- Inverter for D input: loc=(640,550), in at (610,550) -->
    <comp lib="1" loc="(640,550)" name="NOT Gate"/>

    <!-- Steering NANDs at (720,460) and (720,540): inputs at X-40=(680) -->
    <comp lib="1" loc="(720,460)" name="NAND Gate">
      <a name="size" val="30"/>
      <a name="inputs" val="2"/>
    </comp>
    <comp lib="1" loc="(720,540)" name="NAND Gate">
      <a name="size" val="30"/>
      <a name="inputs" val="2"/>
    </comp>

    <!-- Cross-Coupled Storage NANDs at (820,470) and (820,530): inputs at X-40=(780) -->
    <comp lib="1" loc="(820,470)" name="NAND Gate">
      <a name="size" val="30"/>
      <a name="inputs" val="2"/>
    </comp>
    <comp lib="1" loc="(820,530)" name="NAND Gate">
      <a name="size" val="30"/>
      <a name="inputs" val="2"/>
    </comp>

    <!-- Gate-Level D Outputs -->
    <comp lib="0" loc="(880,470)" name="Pin">
      <a name="facing" val="west"/>
      <a name="output" val="true"/>
      <a name="label" val="GATE_Q_D"/>
      <a name="labelloc" val="east"/>
    </comp>
    <comp lib="0" loc="(880,530)" name="Pin">
      <a name="facing" val="west"/>
      <a name="output" val="true"/>
      <a name="label" val="GATE_~Q_D"/>
      <a name="labelloc" val="east"/>
    </comp>

    <!-- ================= WIRING FOR GATE-LEVEL D ================= -->
    <!-- Input D distribution to (680,450) and inverter in (610,550) -->
    <wire from="(570,450)" to="(590,450)"/>
    <wire from="(590,450)" to="(680,450)"/>
    <wire from="(590,450)" to="(590,550)"/>
    <wire from="(590,550)" to="(610,550)"/>

    <!-- Inverted D to lower NAND In1 (680,550) -->
    <wire from="(640,550)" to="(680,550)"/>

    <!-- Input CLK_D distribution to both steering NANDs at (680,470) and (680,530) -->
    <wire from="(570,500)" to="(650,500)"/>
    <wire from="(650,500)" to="(650,470)"/>
    <wire from="(650,470)" to="(680,470)"/>
    <wire from="(650,500)" to="(650,530)"/>
    <wire from="(650,530)" to="(680,530)"/>

    <!-- Steering NANDs to Cross-Coupled Storage NANDs at (780,460) and (780,540) -->
    <wire from="(720,460)" to="(780,460)"/>
    <wire from="(720,540)" to="(780,540)"/>

    <!-- Cross-Coupled Storage Wires -->
    <!-- Top Storage NAND Out (820,470) to Pin (880,470) and Cross down to NAND In0 (780,520) -->
    <wire from="(820,470)" to="(840,470)"/>
    <wire from="(840,470)" to="(880,470)"/>
    <wire from="(840,470)" to="(840,490)"/>
    <wire from="(840,490)" to="(760,490)"/>
    <wire from="(760,490)" to="(760,520)"/>
    <wire from="(760,520)" to="(780,520)"/>

    <!-- Bottom Storage NAND Out (820,530) to Pin (880,530) and Cross up to NAND In1 (780,480) -->
    <wire from="(820,530)" to="(850,530)"/>
    <wire from="(850,530)" to="(880,530)"/>
    <wire from="(850,530)" to="(850,510)"/>
    <wire from="(850,510)" to="(770,510)"/>
    <wire from="(770,510)" to="(770,480)"/>
    <wire from="(770,480)" to="(780,480)"/>

  </circuit>
</project>
"""
    return xml

def build_exp4():
    xml = get_header("main") + """  <circuit name="main">
    <a name="circuit" val="main"/>
    <a name="clabel" val=""/>
    <a name="clabelup" val="east"/>
    <a name="clabelfont" val="SansSerif plain 12"/>

    <!-- Title and Documentation -->
    <comp lib="6" loc="(500,35)" name="Text">
      <a name="text" val="EXPERIMENT 4: IMPLEMENTATION OF 4-BIT SISO &amp; PIPO REGISTERS"/>
      <a name="font" val="SansSerif bold 18"/>
    </comp>
    <comp lib="6" loc="(500,58)" name="Text">
      <a name="text" val="Serial-In Serial-Out (Cascade Shift) &amp; Parallel-In Parallel-Out (Immediate Load)"/>
      <a name="font" val="SansSerif plain 12"/>
    </comp>

    <!-- ================= PART A: 4-BIT SISO ================= -->
    <comp lib="6" loc="(480,95)" name="Text">
      <a name="text" val="PART A: 4-BIT SERIAL-IN SERIAL-OUT (SISO) SHIFT REGISTER"/>
      <a name="font" val="SansSerif bold 14"/>
    </comp>

    <!-- SISO Controls & Input -->
    <comp lib="0" loc="(80,140)" name="Clock">
      <a name="label" val="CLK_SISO"/>
    </comp>
    <comp lib="0" loc="(80,180)" name="Pin">
      <a name="tristate" val="false"/>
      <a name="label" val="SERIAL_IN"/>
    </comp>
    <comp lib="0" loc="(80,220)" name="Pin">
      <a name="tristate" val="false"/>
      <a name="label" val="RESET_SISO"/>
    </comp>

    <!-- 4 Cascaded D Flip-Flops for SISO -->
    <comp lib="4" loc="(240,160)" name="D Flip-Flop">
      <a name="trigger" val="falling"/>
      <a name="label" val="FF3 (Q3)"/>
      <a name="labelloc" val="north"/>
    </comp>
    <comp lib="4" loc="(400,160)" name="D Flip-Flop">
      <a name="trigger" val="falling"/>
      <a name="label" val="FF2 (Q2)"/>
      <a name="labelloc" val="north"/>
    </comp>
    <comp lib="4" loc="(560,160)" name="D Flip-Flop">
      <a name="trigger" val="falling"/>
      <a name="label" val="FF1 (Q1)"/>
      <a name="labelloc" val="north"/>
    </comp>
    <comp lib="4" loc="(720,160)" name="D Flip-Flop">
      <a name="trigger" val="falling"/>
      <a name="label" val="FF0 (Q0)"/>
      <a name="labelloc" val="north"/>
    </comp>

    <!-- Probes for intermediate bits -->
    <comp lib="0" loc="(280,120)" name="Pin">
      <a name="facing" val="south"/>
      <a name="output" val="true"/>
      <a name="label" val="Q3"/>
      <a name="labelloc" val="north"/>
    </comp>
    <comp lib="0" loc="(440,120)" name="Pin">
      <a name="facing" val="south"/>
      <a name="output" val="true"/>
      <a name="label" val="Q2"/>
      <a name="labelloc" val="north"/>
    </comp>
    <comp lib="0" loc="(600,120)" name="Pin">
      <a name="facing" val="south"/>
      <a name="output" val="true"/>
      <a name="label" val="Q1"/>
      <a name="labelloc" val="north"/>
    </comp>
    <comp lib="0" loc="(760,120)" name="Pin">
      <a name="facing" val="south"/>
      <a name="output" val="true"/>
      <a name="label" val="Q0"/>
      <a name="labelloc" val="north"/>
    </comp>

    <!-- SISO Final Output -->
    <comp lib="0" loc="(820,160)" name="Pin">
      <a name="facing" val="west"/>
      <a name="output" val="true"/>
      <a name="label" val="SERIAL_OUT"/>
      <a name="labelloc" val="east"/>
    </comp>

    <!-- SISO Bus Splitter & Hex Probe -->
    <comp lib="0" loc="(840,120)" name="Splitter">
      <a name="facing" val="west"/>
      <a name="fanout" val="4"/>
      <a name="incoming" val="4"/>
      <a name="appear" val="right"/>
    </comp>
    <comp lib="0" loc="(880,120)" name="Probe">
      <a name="radix" val="16"/>
      <a name="label" val="SISO_HEX"/>
      <a name="labelloc" val="north"/>
    </comp>

    <!-- SISO WIRING -->
    <wire from="(80,180)" to="(200,180)"/>

    <wire from="(80,140)" to="(140,140)"/>
    <wire from="(140,140)" to="(180,140)"/>
    <wire from="(180,140)" to="(180,160)"/>
    <wire from="(180,160)" to="(200,160)"/>

    <wire from="(180,140)" to="(340,140)"/>
    <wire from="(340,140)" to="(340,160)"/>
    <wire from="(340,160)" to="(360,160)"/>

    <wire from="(340,140)" to="(500,140)"/>
    <wire from="(500,140)" to="(500,160)"/>
    <wire from="(500,160)" to="(520,160)"/>

    <wire from="(500,140)" to="(660,140)"/>
    <wire from="(660,140)" to="(660,160)"/>
    <wire from="(660,160)" to="(680,160)"/>

    <wire from="(80,220)" to="(230,220)"/>
    <wire from="(230,220)" to="(230,190)"/>
    <wire from="(230,220)" to="(390,220)"/>
    <wire from="(390,220)" to="(390,190)"/>
    <wire from="(390,220)" to="(550,220)"/>
    <wire from="(550,220)" to="(550,190)"/>
    <wire from="(550,220)" to="(710,220)"/>
    <wire from="(710,220)" to="(710,190)"/>

    <!-- Cascaded Data Wires between Flip-Flops -->
    <wire from="(240,160)" to="(280,160)"/>
    <wire from="(280,160)" to="(280,120)"/>
    <wire from="(280,160)" to="(320,160)"/>
    <wire from="(320,160)" to="(320,180)"/>
    <wire from="(320,180)" to="(360,180)"/>

    <wire from="(280,120)" to="(280,90)"/>
    <wire from="(280,90)" to="(820,90)"/>
    <wire from="(820,90)" to="(820,130)"/>

    <wire from="(400,160)" to="(440,160)"/>
    <wire from="(440,160)" to="(440,120)"/>
    <wire from="(440,160)" to="(480,160)"/>
    <wire from="(480,160)" to="(480,180)"/>
    <wire from="(480,180)" to="(520,180)"/>

    <wire from="(440,120)" to="(440,100)"/>
    <wire from="(440,100)" to="(810,100)"/>
    <wire from="(810,100)" to="(810,140)"/>
    <wire from="(810,140)" to="(820,140)"/>

    <wire from="(560,160)" to="(600,160)"/>
    <wire from="(600,160)" to="(600,120)"/>
    <wire from="(600,160)" to="(640,160)"/>
    <wire from="(640,160)" to="(640,180)"/>
    <wire from="(640,180)" to="(680,180)"/>

    <wire from="(600,120)" to="(600,110)"/>
    <wire from="(600,110)" to="(800,110)"/>
    <wire from="(800,110)" to="(800,150)"/>
    <wire from="(800,150)" to="(820,150)"/>

    <wire from="(720,160)" to="(760,160)"/>
    <wire from="(760,160)" to="(760,120)"/>
    <wire from="(760,160)" to="(820,160)"/>

    <wire from="(760,120)" to="(760,160)"/>
    <wire from="(760,160)" to="(820,160)"/>

    <wire from="(840,120)" to="(880,120)"/>

    <!-- ================= PART B: 4-BIT PIPO ================= -->
    <comp lib="6" loc="(480,275)" name="Text">
      <a name="text" val="PART B: 4-BIT PARALLEL-IN PARALLEL-OUT (PIPO) REGISTER"/>
      <a name="font" val="SansSerif bold 14"/>
    </comp>

    <!-- PIPO Parallel Data Inputs -->
    <comp lib="0" loc="(160,360)" name="Pin">
      <a name="tristate" val="false"/>
      <a name="label" val="D3"/>
    </comp>
    <comp lib="0" loc="(320,360)" name="Pin">
      <a name="tristate" val="false"/>
      <a name="label" val="D2"/>
    </comp>
    <comp lib="0" loc="(480,360)" name="Pin">
      <a name="tristate" val="false"/>
      <a name="label" val="D1"/>
    </comp>
    <comp lib="0" loc="(640,360)" name="Pin">
      <a name="tristate" val="false"/>
      <a name="label" val="D0"/>
    </comp>

    <!-- PIPO Common Clock & Clear -->
    <comp lib="0" loc="(80,320)" name="Clock">
      <a name="label" val="CLK_PIPO"/>
    </comp>
    <comp lib="0" loc="(80,410)" name="Pin">
      <a name="tristate" val="false"/>
      <a name="label" val="RESET_PIPO"/>
    </comp>

    <!-- 4 D Flip-Flops for PIPO -->
    <comp lib="4" loc="(240,340)" name="D Flip-Flop">
      <a name="trigger" val="falling"/>
      <a name="label" val="PIPO_FF3"/>
      <a name="labelloc" val="north"/>
    </comp>
    <comp lib="4" loc="(400,340)" name="D Flip-Flop">
      <a name="trigger" val="falling"/>
      <a name="label" val="PIPO_FF2"/>
      <a name="labelloc" val="north"/>
    </comp>
    <comp lib="4" loc="(560,340)" name="D Flip-Flop">
      <a name="trigger" val="falling"/>
      <a name="label" val="PIPO_FF1"/>
      <a name="labelloc" val="north"/>
    </comp>
    <comp lib="4" loc="(720,340)" name="D Flip-Flop">
      <a name="trigger" val="falling"/>
      <a name="label" val="PIPO_FF0"/>
      <a name="labelloc" val="north"/>
    </comp>

    <!-- Parallel Outputs -->
    <comp lib="0" loc="(270,300)" name="Pin">
      <a name="facing" val="south"/>
      <a name="output" val="true"/>
      <a name="label" val="PIPO_Q3"/>
      <a name="labelloc" val="north"/>
    </comp>
    <comp lib="0" loc="(430,300)" name="Pin">
      <a name="facing" val="south"/>
      <a name="output" val="true"/>
      <a name="label" val="PIPO_Q2"/>
      <a name="labelloc" val="north"/>
    </comp>
    <comp lib="0" loc="(590,300)" name="Pin">
      <a name="facing" val="south"/>
      <a name="output" val="true"/>
      <a name="label" val="PIPO_Q1"/>
      <a name="labelloc" val="north"/>
    </comp>
    <comp lib="0" loc="(750,300)" name="Pin">
      <a name="facing" val="south"/>
      <a name="output" val="true"/>
      <a name="label" val="PIPO_Q0"/>
      <a name="labelloc" val="north"/>
    </comp>

    <!-- PIPO Bus Splitter & Hex Display -->
    <comp lib="0" loc="(840,340)" name="Splitter">
      <a name="facing" val="west"/>
      <a name="fanout" val="4"/>
      <a name="incoming" val="4"/>
      <a name="appear" val="right"/>
    </comp>
    <comp lib="0" loc="(880,340)" name="Probe">
      <a name="radix" val="16"/>
      <a name="label" val="PIPO_HEX"/>
      <a name="labelloc" val="north"/>
    </comp>

    <!-- PIPO WIRING -->
    <wire from="(160,360)" to="(200,360)"/>
    <wire from="(320,360)" to="(360,360)"/>
    <wire from="(480,360)" to="(520,360)"/>
    <wire from="(640,360)" to="(680,360)"/>

    <wire from="(80,320)" to="(180,320)"/>
    <wire from="(180,320)" to="(180,340)"/>
    <wire from="(180,340)" to="(200,340)"/>

    <wire from="(180,320)" to="(340,320)"/>
    <wire from="(340,320)" to="(340,340)"/>
    <wire from="(340,340)" to="(360,340)"/>

    <wire from="(340,320)" to="(500,320)"/>
    <wire from="(500,320)" to="(500,340)"/>
    <wire from="(500,340)" to="(520,340)"/>

    <wire from="(500,320)" to="(660,320)"/>
    <wire from="(660,320)" to="(660,340)"/>
    <wire from="(660,340)" to="(680,340)"/>

    <wire from="(80,410)" to="(230,410)"/>
    <wire from="(230,410)" to="(230,370)"/>
    <wire from="(230,410)" to="(390,410)"/>
    <wire from="(390,410)" to="(390,370)"/>
    <wire from="(390,410)" to="(550,410)"/>
    <wire from="(550,410)" to="(550,370)"/>
    <wire from="(550,410)" to="(710,410)"/>
    <wire from="(710,410)" to="(710,370)"/>

    <wire from="(240,340)" to="(270,340)"/>
    <wire from="(270,340)" to="(270,300)"/>
    <wire from="(270,300)" to="(270,280)"/>
    <wire from="(270,280)" to="(820,280)"/>
    <wire from="(820,280)" to="(820,350)"/>

    <wire from="(400,340)" to="(430,340)"/>
    <wire from="(430,340)" to="(430,300)"/>
    <wire from="(430,300)" to="(430,290)"/>
    <wire from="(430,290)" to="(810,290)"/>
    <wire from="(810,290)" to="(810,360)"/>
    <wire from="(810,360)" to="(820,360)"/>

    <wire from="(560,340)" to="(590,340)"/>
    <wire from="(590,340)" to="(590,300)"/>
    <wire from="(590,300)" to="(800,300)"/>
    <wire from="(800,300)" to="(800,370)"/>
    <wire from="(800,370)" to="(820,370)"/>

    <wire from="(720,340)" to="(750,340)"/>
    <wire from="(750,340)" to="(750,300)"/>
    <wire from="(750,300)" to="(790,300)"/>
    <wire from="(790,300)" to="(790,380)"/>
    <wire from="(790,380)" to="(820,380)"/>

    <wire from="(840,340)" to="(880,340)"/>

  </circuit>
</project>
"""
    return xml

# ==============================================================================
# EXP 5: 4-BIT RIPPLE COUNTER USING D FLIP-FLOP
# ==============================================================================
def build_exp5():
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

    <!-- Document Header -->
    <comp lib="6" loc="(560,30)" name="Text">
      <a name="text" val="EXPERIMENT 5: 4-BIT ASYNCHRONOUS UP &amp; DOWN RIPPLE COUNTERS (D FLIP-FLOPS)"/>
      <a name="font" val="SansSerif bold 18"/>
    </comp>
    <comp lib="6" loc="(560,50)" name="Text">
      <a name="text" val="Pure D Flip-Flop Architecture (No Mux): Top = 4-Bit UP Counter (CLK = Q) | Bottom = 4-Bit DOWN Counter (CLK = ~Q)"/>
      <a name="font" val="SansSerif plain 12"/>
    </comp>

    <!-- ========================================================================= -->
    <!-- PART A: 4-BIT ASYNCHRONOUS UP COUNTER (TOP SECTION)                       -->
    <!-- ========================================================================= -->
    <comp lib="6" loc="(300,90)" name="Text">
      <a name="text" val="PART A: 4-BIT BINARY UP COUNTER (Counts 0 to 15, Next Clock = Q)"/>
      <a name="font" val="SansSerif bold 14"/>
    </comp>

    <!-- Master Controls for UP Counter -->
    <comp lib="0" loc="(80,180)" name="Clock">
      <a name="label" val="CLK_UP"/>
    </comp>
    <comp lib="0" loc="(80,250)" name="Pin">
      <a name="tristate" val="false"/>
      <a name="label" val="RESET_UP (Clear)"/>
    </comp>

    <!-- 4 D Flip-Flops for UP Counter (Toggle Mode: D = ~Q, Falling Edge) -->
    <!-- D-FF 0: in CLK=(180,180), in D=(180,200), out Q=(220,180), out ~Q=(220,200), clr=(210,210) -->
    <comp lib="4" loc="(220,180)" name="D Flip-Flop">
      <a name="trigger" val="falling"/>
      <a name="label" val="UP_FF0 (LSB)"/>
      <a name="labelloc" val="north"/>
    </comp>
    <comp lib="4" loc="(420,180)" name="D Flip-Flop">
      <a name="trigger" val="falling"/>
      <a name="label" val="UP_FF1"/>
      <a name="labelloc" val="north"/>
    </comp>
    <comp lib="4" loc="(620,180)" name="D Flip-Flop">
      <a name="trigger" val="falling"/>
      <a name="label" val="UP_FF2"/>
      <a name="labelloc" val="north"/>
    </comp>
    <comp lib="4" loc="(820,180)" name="D Flip-Flop">
      <a name="trigger" val="falling"/>
      <a name="label" val="UP_FF3 (MSB)"/>
      <a name="labelloc" val="north"/>
    </comp>

    <!-- Individual UP Bit Outputs -->
    <comp lib="0" loc="(250,130)" name="Pin">
      <a name="facing" val="south"/>
      <a name="output" val="true"/>
      <a name="label" val="UP_Q0"/>
      <a name="labelloc" val="north"/>
    </comp>
    <comp lib="0" loc="(450,130)" name="Pin">
      <a name="facing" val="south"/>
      <a name="output" val="true"/>
      <a name="label" val="UP_Q1"/>
      <a name="labelloc" val="north"/>
    </comp>
    <comp lib="0" loc="(650,130)" name="Pin">
      <a name="facing" val="south"/>
      <a name="output" val="true"/>
      <a name="label" val="UP_Q2"/>
      <a name="labelloc" val="north"/>
    </comp>
    <comp lib="0" loc="(850,130)" name="Pin">
      <a name="facing" val="south"/>
      <a name="output" val="true"/>
      <a name="label" val="UP_Q3"/>
      <a name="labelloc" val="north"/>
    </comp>

    <!-- Combined UP 4-Bit Bus Splitter & Displays -->
    <comp lib="0" loc="(920,180)" name="Splitter">
      <a name="facing" val="west"/>
      <a name="fanout" val="4"/>
      <a name="incoming" val="4"/>
      <a name="appear" val="right"/>
    </comp>
    <comp lib="0" loc="(960,140)" name="Probe">
      <a name="radix" val="10unsigned"/>
      <a name="label" val="UP_DECIMAL"/>
      <a name="labelloc" val="north"/>
    </comp>
    <comp lib="0" loc="(960,180)" name="Probe">
      <a name="radix" val="16"/>
      <a name="label" val="UP_HEX"/>
      <a name="labelloc" val="north"/>
    </comp>
    <comp lib="0" loc="(960,220)" name="Probe">
      <a name="radix" val="2"/>
      <a name="label" val="UP_BINARY"/>
      <a name="labelloc" val="north"/>
    </comp>
    <comp lib="5" loc="(1060,180)" name="Hex Digit Display"/>

    <!-- Wiring for UP Counter -->
    <!-- CLK_UP to FF0 CLK (180,180) -->
    <wire from="(80,180)" to="(180,180)"/>

    <!-- FF0: Toggle feedback ~Q0 (220,200) to D (180,200) via loop -->
    <wire from="(220,200)" to="(240,200)"/>
    <wire from="(240,200)" to="(240,230)"/>
    <wire from="(240,230)" to="(160,230)"/>
    <wire from="(160,230)" to="(160,200)"/>
    <wire from="(160,200)" to="(180,200)"/>

    <!-- FF0 Q0: Output to Pin, Splitter [0], and next stage CLK (380,180) -->
    <wire from="(220,180)" to="(250,180)"/>
    <wire from="(250,180)" to="(250,130)"/>
    <wire from="(250,180)" to="(270,180)"/>
    <wire from="(270,180)" to="(380,180)"/>
    <wire from="(270,180)" to="(270,110)"/>
    <wire from="(270,110)" to="(900,110)"/>
    <wire from="(900,110)" to="(900,170)"/>
    <wire from="(900,170)" to="(920,170)"/>

    <!-- FF1: Toggle feedback ~Q1 (420,200) to D (380,200) via loop -->
    <wire from="(420,200)" to="(440,200)"/>
    <wire from="(440,200)" to="(440,230)"/>
    <wire from="(440,230)" to="(360,230)"/>
    <wire from="(360,230)" to="(360,200)"/>
    <wire from="(360,200)" to="(380,200)"/>

    <!-- FF1 Q1: Output to Pin, Splitter [1], and next stage CLK (580,180) -->
    <wire from="(420,180)" to="(450,180)"/>
    <wire from="(450,180)" to="(450,130)"/>
    <wire from="(450,180)" to="(470,180)"/>
    <wire from="(470,180)" to="(580,180)"/>
    <wire from="(470,180)" to="(470,120)"/>
    <wire from="(470,120)" to="(890,120)"/>
    <wire from="(890,120)" to="(890,160)"/>
    <wire from="(890,160)" to="(920,160)"/>

    <!-- FF2: Toggle feedback ~Q2 (620,200) to D (580,200) via loop -->
    <wire from="(620,200)" to="(640,200)"/>
    <wire from="(640,200)" to="(640,230)"/>
    <wire from="(640,230)" to="(560,230)"/>
    <wire from="(560,230)" to="(560,200)"/>
    <wire from="(560,200)" to="(580,200)"/>

    <!-- FF2 Q2: Output to Pin, Splitter [2], and next stage CLK (780,180) -->
    <wire from="(620,180)" to="(650,180)"/>
    <wire from="(650,180)" to="(650,130)"/>
    <wire from="(650,180)" to="(670,180)"/>
    <wire from="(670,180)" to="(780,180)"/>
    <wire from="(670,180)" to="(670,150)"/>
    <wire from="(670,150)" to="(920,150)"/>

    <!-- FF3: Toggle feedback ~Q3 (820,200) to D (780,200) via loop -->
    <wire from="(820,200)" to="(840,200)"/>
    <wire from="(840,200)" to="(840,230)"/>
    <wire from="(840,230)" to="(760,230)"/>
    <wire from="(760,230)" to="(760,200)"/>
    <wire from="(760,200)" to="(780,200)"/>

    <!-- FF3 Q3: Output to Pin and Splitter [3] -->
    <wire from="(820,180)" to="(850,180)"/>
    <wire from="(850,180)" to="(850,130)"/>
    <wire from="(850,180)" to="(870,180)"/>
    <wire from="(870,180)" to="(870,140)"/>
    <wire from="(870,140)" to="(920,140)"/>

    <!-- Reset Line for UP counter to clear pins at (210,210), (410,210), (610,210), (810,210) -->
    <wire from="(80,250)" to="(210,250)"/>
    <wire from="(210,250)" to="(210,210)"/>
    <wire from="(210,250)" to="(410,250)"/>
    <wire from="(410,250)" to="(410,210)"/>
    <wire from="(410,250)" to="(610,250)"/>
    <wire from="(610,250)" to="(610,210)"/>
    <wire from="(610,250)" to="(810,250)"/>
    <wire from="(810,250)" to="(810,210)"/>

    <!-- Splitter Out (940,180) distribution to Probes and 7-Seg Hex Display -->
    <wire from="(940,180)" to="(960,180)"/>
    <wire from="(960,180)" to="(960,140)"/>
    <wire from="(960,180)" to="(960,220)"/>
    <wire from="(960,180)" to="(1060,180)"/>


    <!-- ========================================================================= -->
    <!-- PART B: 4-BIT ASYNCHRONOUS DOWN COUNTER (BOTTOM SECTION)                  -->
    <!-- ========================================================================= -->
    <comp lib="6" loc="(300,340)" name="Text">
      <a name="text" val="PART B: 4-BIT BINARY DOWN COUNTER (Counts 15 to 0, Next Clock = ~Q)"/>
      <a name="font" val="SansSerif bold 14"/>
    </comp>

    <!-- Master Controls for DOWN Counter -->
    <comp lib="0" loc="(80,420)" name="Clock">
      <a name="label" val="CLK_DOWN"/>
    </comp>
    <comp lib="0" loc="(80,490)" name="Pin">
      <a name="tristate" val="false"/>
      <a name="label" val="RESET_DOWN (Clear)"/>
    </comp>

    <!-- 4 D Flip-Flops for DOWN Counter (Toggle Mode: D = ~Q, Falling Edge, Ripple Clock = ~Q) -->
    <comp lib="4" loc="(220,420)" name="D Flip-Flop">
      <a name="trigger" val="falling"/>
      <a name="label" val="DN_FF0 (LSB)"/>
      <a name="labelloc" val="north"/>
    </comp>
    <comp lib="4" loc="(420,420)" name="D Flip-Flop">
      <a name="trigger" val="falling"/>
      <a name="label" val="DN_FF1"/>
      <a name="labelloc" val="north"/>
    </comp>
    <comp lib="4" loc="(620,420)" name="D Flip-Flop">
      <a name="trigger" val="falling"/>
      <a name="label" val="DN_FF2"/>
      <a name="labelloc" val="north"/>
    </comp>
    <comp lib="4" loc="(820,420)" name="D Flip-Flop">
      <a name="trigger" val="falling"/>
      <a name="label" val="DN_FF3 (MSB)"/>
      <a name="labelloc" val="north"/>
    </comp>

    <!-- Individual DOWN Bit Outputs -->
    <comp lib="0" loc="(250,370)" name="Pin">
      <a name="facing" val="south"/>
      <a name="output" val="true"/>
      <a name="label" val="DN_Q0"/>
      <a name="labelloc" val="north"/>
    </comp>
    <comp lib="0" loc="(450,370)" name="Pin">
      <a name="facing" val="south"/>
      <a name="output" val="true"/>
      <a name="label" val="DN_Q1"/>
      <a name="labelloc" val="north"/>
    </comp>
    <comp lib="0" loc="(650,370)" name="Pin">
      <a name="facing" val="south"/>
      <a name="output" val="true"/>
      <a name="label" val="DN_Q2"/>
      <a name="labelloc" val="north"/>
    </comp>
    <comp lib="0" loc="(850,370)" name="Pin">
      <a name="facing" val="south"/>
      <a name="output" val="true"/>
      <a name="label" val="DN_Q3"/>
      <a name="labelloc" val="north"/>
    </comp>

    <!-- Combined DOWN 4-Bit Bus Splitter & Displays -->
    <comp lib="0" loc="(920,420)" name="Splitter">
      <a name="facing" val="west"/>
      <a name="fanout" val="4"/>
      <a name="incoming" val="4"/>
      <a name="appear" val="right"/>
    </comp>
    <comp lib="0" loc="(960,380)" name="Probe">
      <a name="radix" val="10unsigned"/>
      <a name="label" val="DN_DECIMAL"/>
      <a name="labelloc" val="north"/>
    </comp>
    <comp lib="0" loc="(960,420)" name="Probe">
      <a name="radix" val="16"/>
      <a name="label" val="DN_HEX"/>
      <a name="labelloc" val="north"/>
    </comp>
    <comp lib="0" loc="(960,460)" name="Probe">
      <a name="radix" val="2"/>
      <a name="label" val="DN_BINARY"/>
      <a name="labelloc" val="north"/>
    </comp>
    <comp lib="5" loc="(1060,420)" name="Hex Digit Display"/>

    <!-- Wiring for DOWN Counter -->
    <!-- CLK_DOWN to FF0 CLK (180,420) -->
    <wire from="(80,420)" to="(180,420)"/>

    <!-- FF0: Toggle feedback and Clock to Stage 1 from ~Q0 (220,440) -->
    <!-- ~Q0 goes to D (180,440) AND ripples to FF1 CLK (380,420) -->
    <wire from="(220,440)" to="(240,440)"/>
    <wire from="(240,440)" to="(240,470)"/>
    <wire from="(240,470)" to="(160,470)"/>
    <wire from="(160,470)" to="(160,440)"/>
    <wire from="(160,440)" to="(180,440)"/>
    <!-- Ripple connection from ~Q0 to next stage clock: (240,440) -> (380,420) -->
    <wire from="(240,440)" to="(290,440)"/>
    <wire from="(290,440)" to="(290,420)"/>
    <wire from="(290,420)" to="(380,420)"/>

    <!-- FF0 Q0: Output to Pin and Splitter [0] -->
    <wire from="(220,420)" to="(250,420)"/>
    <wire from="(250,420)" to="(250,370)"/>
    <wire from="(250,420)" to="(270,420)"/>
    <wire from="(270,420)" to="(270,350)"/>
    <wire from="(270,350)" to="(900,350)"/>
    <wire from="(900,350)" to="(900,410)"/>
    <wire from="(900,410)" to="(920,410)"/>

    <!-- FF1: Toggle feedback and Clock to Stage 2 from ~Q1 (420,440) -->
    <wire from="(420,440)" to="(440,440)"/>
    <wire from="(440,440)" to="(440,470)"/>
    <wire from="(440,470)" to="(360,470)"/>
    <wire from="(360,470)" to="(360,440)"/>
    <wire from="(360,440)" to="(380,440)"/>
    <!-- Ripple from ~Q1 to FF2 CLK (580,420) -->
    <wire from="(440,440)" to="(490,440)"/>
    <wire from="(490,440)" to="(490,420)"/>
    <wire from="(490,420)" to="(580,420)"/>

    <!-- FF1 Q1: Output to Pin and Splitter [1] -->
    <wire from="(420,420)" to="(450,420)"/>
    <wire from="(450,420)" to="(450,370)"/>
    <wire from="(450,420)" to="(470,420)"/>
    <wire from="(470,420)" to="(470,360)"/>
    <wire from="(470,360)" to="(890,360)"/>
    <wire from="(890,360)" to="(890,400)"/>
    <wire from="(890,400)" to="(920,400)"/>

    <!-- FF2: Toggle feedback and Clock to Stage 3 from ~Q2 (620,440) -->
    <wire from="(620,440)" to="(640,440)"/>
    <wire from="(640,440)" to="(640,470)"/>
    <wire from="(640,470)" to="(560,470)"/>
    <wire from="(560,470)" to="(560,440)"/>
    <wire from="(560,440)" to="(580,440)"/>
    <!-- Ripple from ~Q2 to FF3 CLK (780,420) -->
    <wire from="(640,440)" to="(690,440)"/>
    <wire from="(690,440)" to="(690,420)"/>
    <wire from="(690,420)" to="(780,420)"/>

    <!-- FF2 Q2: Output to Pin and Splitter [2] -->
    <wire from="(620,420)" to="(650,420)"/>
    <wire from="(650,420)" to="(650,370)"/>
    <wire from="(650,420)" to="(670,420)"/>
    <wire from="(670,420)" to="(670,390)"/>
    <wire from="(670,390)" to="(920,390)"/>

    <!-- FF3: Toggle feedback ~Q3 (820,440) to D (780,440) via loop -->
    <wire from="(820,440)" to="(840,440)"/>
    <wire from="(840,440)" to="(840,470)"/>
    <wire from="(840,470)" to="(760,470)"/>
    <wire from="(760,470)" to="(760,440)"/>
    <wire from="(760,440)" to="(780,440)"/>

    <!-- FF3 Q3: Output to Pin and Splitter [3] -->
    <wire from="(820,420)" to="(850,420)"/>
    <wire from="(850,420)" to="(850,370)"/>
    <wire from="(850,420)" to="(870,420)"/>
    <wire from="(870,420)" to="(870,380)"/>
    <wire from="(870,380)" to="(920,380)"/>

    <!-- Reset Line for DOWN counter to clear pins at (210,450), (410,450), (610,450), (810,450) -->
    <wire from="(80,490)" to="(210,490)"/>
    <wire from="(210,490)" to="(210,450)"/>
    <wire from="(210,490)" to="(410,490)"/>
    <wire from="(410,490)" to="(410,450)"/>
    <wire from="(410,490)" to="(610,490)"/>
    <wire from="(610,490)" to="(610,450)"/>
    <wire from="(610,490)" to="(810,490)"/>
    <wire from="(810,490)" to="(810,450)"/>

    <!-- Splitter Out (940,420) distribution to Probes and 7-Seg Hex Display -->
    <wire from="(940,420)" to="(960,420)"/>
    <wire from="(960,420)" to="(960,380)"/>
    <wire from="(960,420)" to="(960,460)"/>
    <wire from="(960,420)" to="(1060,420)"/>

  </circuit>
</project>
"""
    return xml

def build_exp6():
    xml = get_header("main") + """  <circuit name="main">
    <a name="circuit" val="main"/>
    <a name="clabel" val=""/>
    <a name="clabelup" val="east"/>
    <a name="clabelfont" val="SansSerif plain 12"/>

    <!-- Title and Documentation -->
    <comp lib="6" loc="(500,35)" name="Text">
      <a name="text" val="EXPERIMENT 6: 2-BIT ARITHMETIC LOGIC UNIT (ALU)"/>
      <a name="font" val="SansSerif bold 18"/>
    </comp>
    <comp lib="6" loc="(500,58)" name="Text">
      <a name="text" val="Integrated Functional Units: Adder, Subtractor, Divider (Quotient &amp; Remainder) via 4:1 MUX"/>
      <a name="font" val="SansSerif plain 12"/>
    </comp>

    <!-- Function Table Banner -->
    <comp lib="6" loc="(500,80)" name="Text">
      <a name="text" val="SEL 00: ADD (A + B) | SEL 01: SUB (A - B) | SEL 10: DIV QUOTIENT (A / B) | SEL 11: DIV REMAINDER (A % B)"/>
      <a name="font" val="SansSerif bold 12"/>
    </comp>

    <!-- ================= INPUTS ================= -->
    <!-- Operand A (2-bit pin, default 0x2 = 10_2) -->
    <comp lib="0" loc="(100,160)" name="Pin">
      <a name="width" val="2"/>
      <a name="tristate" val="false"/>
      <a name="label" val="OPERAND_A (2-bit)"/>
    </comp>
    <comp lib="0" loc="(150,140)" name="Probe">
      <a name="facing" val="south"/>
      <a name="radix" val="10unsigned"/>
      <a name="label" val="A (DEC)"/>
      <a name="labelloc" val="north"/>
    </comp>

    <!-- Operand B (2-bit pin, default 0x1 = 01_2) -->
    <comp lib="0" loc="(100,240)" name="Pin">
      <a name="width" val="2"/>
      <a name="tristate" val="false"/>
      <a name="label" val="OPERAND_B (2-bit)"/>
    </comp>
    <comp lib="0" loc="(150,220)" name="Probe">
      <a name="facing" val="south"/>
      <a name="radix" val="10unsigned"/>
      <a name="label" val="B (DEC)"/>
      <a name="labelloc" val="north"/>
    </comp>

    <!-- 2-Bit ALU Selection Pin (S1, S0) -->
    <comp lib="0" loc="(100,380)" name="Pin">
      <a name="width" val="2"/>
      <a name="tristate" val="false"/>
      <a name="label" val="ALU_SEL (2-bit)"/>
    </comp>
    <comp lib="0" loc="(150,360)" name="Probe">
      <a name="facing" val="south"/>
      <a name="radix" val="2"/>
      <a name="label" val="SEL (BIN)"/>
      <a name="labelloc" val="north"/>
    </comp>

    <!-- Divide-By-Zero Warning Detection via 2-bit Comparator with 0x0 -->
    <comp lib="3" loc="(240,290)" name="Comparator">
      <a name="width" val="2"/>
    </comp>
    <comp lib="0" loc="(180,300)" name="Constant">
      <a name="width" val="2"/>
      <a name="value" val="0x0"/>
    </comp>
    <comp lib="0" loc="(280,290)" name="Pin">
      <a name="facing" val="west"/>
      <a name="output" val="true"/>
      <a name="label" val="DIV_ZERO_ERR"/>
      <a name="labelloc" val="east"/>
    </comp>

    <!-- ================= ARITHMETIC FUNCTIONAL UNITS ================= -->
    <!-- 1. 2-BIT ADDER (Code 00): loc = 360, 160 -->
    <comp lib="3" loc="(360,160)" name="Adder">
      <a name="width" val="2"/>
    </comp>
    <comp lib="6" loc="(360,135)" name="Text">
      <a name="text" val="1. ADDER [00]"/>
      <a name="font" val="SansSerif bold 11"/>
    </comp>
    <comp lib="0" loc="(420,150)" name="Probe">
      <a name="facing" val="south"/>
      <a name="radix" val="10unsigned"/>
      <a name="label" val="A+B"/>
      <a name="labelloc" val="north"/>
    </comp>
    <comp lib="0" loc="(340,190)" name="Pin">
      <a name="facing" val="north"/>
      <a name="output" val="true"/>
      <a name="label" val="ADD_CARRY"/>
      <a name="labelloc" val="south"/>
    </comp>

    <!-- 2. 2-BIT SUBTRACTOR (Code 01): loc = 360, 240 -->
    <comp lib="3" loc="(360,240)" name="Subtractor">
      <a name="width" val="2"/>
    </comp>
    <comp lib="6" loc="(360,215)" name="Text">
      <a name="text" val="2. SUBTRACTOR [01]"/>
      <a name="font" val="SansSerif bold 11"/>
    </comp>
    <comp lib="0" loc="(420,230)" name="Probe">
      <a name="facing" val="south"/>
      <a name="radix" val="10unsigned"/>
      <a name="label" val="A-B"/>
      <a name="labelloc" val="north"/>
    </comp>
    <comp lib="0" loc="(340,270)" name="Pin">
      <a name="facing" val="north"/>
      <a name="output" val="true"/>
      <a name="label" val="SUB_BORROW"/>
      <a name="labelloc" val="south"/>
    </comp>

    <!-- 3. 2-BIT DIVIDER (Code 10 for Quotient, Code 11 for Remainder): loc = 360, 330 -->
    <comp lib="3" loc="(360,330)" name="Divider">
      <a name="width" val="2"/>
    </comp>
    <comp lib="6" loc="(360,305)" name="Text">
      <a name="text" val="3. DIVIDER [10 &amp; 11]"/>
      <a name="font" val="SansSerif bold 11"/>
    </comp>
    <comp lib="0" loc="(420,310)" name="Probe">
      <a name="facing" val="south"/>
      <a name="radix" val="10unsigned"/>
      <a name="label" val="A/B (Quot)"/>
      <a name="labelloc" val="north"/>
    </comp>
    <comp lib="0" loc="(420,360)" name="Probe">
      <a name="facing" val="south"/>
      <a name="radix" val="10unsigned"/>
      <a name="label" val="A%B (Rem)"/>
      <a name="labelloc" val="north"/>
    </comp>

    <!-- ================= 4-TO-1 MULTIPLEXER ================= -->
    <!-- 4:1 MUX (2-bit width, 2 select lines, loc = 560, 240) -->
    <comp lib="2" loc="(560,240)" name="Multiplexer">
      <a name="select" val="2"/>
      <a name="width" val="2"/>
      <a name="enable" val="false"/>
    </comp>

    <!-- Final ALU Output Indicators -->
    <comp lib="0" loc="(630,240)" name="Probe">
      <a name="radix" val="2"/>
      <a name="label" val="ALU_OUT (BIN)"/>
      <a name="labelloc" val="north"/>
    </comp>
    <comp lib="0" loc="(710,240)" name="Probe">
      <a name="radix" val="10unsigned"/>
      <a name="label" val="ALU_OUT (DEC)"/>
      <a name="labelloc" val="north"/>
    </comp>
    <comp lib="0" loc="(780,240)" name="Pin">
      <a name="facing" val="west"/>
      <a name="output" val="true"/>
      <a name="width" val="2"/>
      <a name="label" val="ALU_RESULT"/>
      <a name="labelloc" val="east"/>
    </comp>

    <!-- ================= WIRING ================= -->
    <!-- Operand A distribution (width 2) -->
    <wire from="(100,160)" to="(150,160)"/>
    <wire from="(150,160)" to="(150,140)"/>
    <wire from="(150,160)" to="(200,160)"/>
    <wire from="(200,160)" to="(200,150)"/>
    <wire from="(200,150)" to="(320,150)"/>
    <wire from="(200,160)" to="(200,230)"/>
    <wire from="(200,230)" to="(320,230)"/>
    <wire from="(200,230)" to="(200,320)"/>
    <wire from="(200,320)" to="(320,320)"/>

    <!-- Operand B distribution (width 2) -->
    <wire from="(100,240)" to="(150,240)"/>
    <wire from="(150,240)" to="(150,220)"/>
    <wire from="(150,240)" to="(170,240)"/>

    <!-- Comparator zero check -->
    <wire from="(170,240)" to="(170,280)"/>
    <wire from="(170,280)" to="(200,280)"/>
    <wire from="(180,300)" to="(200,300)"/>
    <wire from="(240,290)" to="(280,290)"/>

    <!-- Tap to ADDER B (320, 170) -->
    <wire from="(170,240)" to="(220,240)"/>
    <wire from="(220,240)" to="(220,170)"/>
    <wire from="(220,170)" to="(320,170)"/>
    <!-- Tap to SUBTRACTOR B (320, 250) -->
    <wire from="(220,240)" to="(220,250)"/>
    <wire from="(220,250)" to="(320,250)"/>
    <!-- Tap to DIVIDER B (320, 340) -->
    <wire from="(220,250)" to="(220,340)"/>
    <wire from="(220,340)" to="(320,340)"/>

    <!-- Arithmetic Flags -->
    <wire from="(340,180)" to="(340,190)"/>
    <wire from="(340,260)" to="(340,270)"/>

    <!-- UNIT OUTPUTS TO 4:1 MUX INPUTS -->
    <wire from="(360,160)" to="(420,160)"/>
    <wire from="(420,160)" to="(420,150)"/>
    <wire from="(420,160)" to="(470,160)"/>
    <wire from="(470,160)" to="(470,220)"/>
    <wire from="(470,220)" to="(520,220)"/>

    <wire from="(360,240)" to="(420,240)"/>
    <wire from="(420,240)" to="(420,230)"/>
    <wire from="(420,240)" to="(480,240)"/>
    <wire from="(480,240)" to="(480,230)"/>
    <wire from="(480,230)" to="(520,230)"/>

    <wire from="(360,330)" to="(420,330)"/>
    <wire from="(420,330)" to="(420,310)"/>
    <wire from="(420,330)" to="(490,330)"/>
    <wire from="(490,330)" to="(490,240)"/>
    <wire from="(490,240)" to="(520,240)"/>

    <wire from="(340,350)" to="(340,380)"/>
    <wire from="(340,380)" to="(420,380)"/>
    <wire from="(420,380)" to="(420,360)"/>
    <wire from="(420,380)" to="(500,380)"/>
    <wire from="(500,380)" to="(500,250)"/>
    <wire from="(500,250)" to="(520,250)"/>

    <!-- ALU SELECT to MUX (540, 260) -->
    <wire from="(100,380)" to="(150,380)"/>
    <wire from="(150,380)" to="(150,360)"/>
    <wire from="(150,380)" to="(540,380)"/>
    <wire from="(540,380)" to="(540,260)"/>

    <!-- MUX OUTPUT (560, 240) TO PROBES & PIN -->
    <wire from="(560,240)" to="(630,240)"/>
    <wire from="(630,240)" to="(710,240)"/>
    <wire from="(710,240)" to="(780,240)"/>

  </circuit>
</project>
"""
    return xml

def main():
    files = {
        "exp1_half_and_full_adder.circ": build_exp1(),
        "exp2_mux_and_demux.circ": build_exp2(),
        "exp3_jk_and_d_flip_flop.circ": build_exp3(),
        "exp4_siso_and_pipo.circ": build_exp4(),
        "exp5_4bit_ripple_counter_dff.circ": build_exp5(),
        "exp6_2bit_alu.circ": build_exp6(),
    }
    for filename, content in files.items():
        filepath = os.path.join(CIRCUITS_DIR, filename)
        with open(filepath, "w") as f:
            f.write(content)
        try:
            tree = ET.parse(filepath)
            root = tree.getroot()
            circuit = root.find("circuit")
            comps = circuit.findall("comp")
            wires = circuit.findall("wire")
            print(f"SUCCESS: {filename} -> Valid XML | {len(comps)} components, {len(wires)} wires")
        except Exception as e:
            print(f"ERROR in {filename}: {e}")

if __name__ == "__main__":
    main()

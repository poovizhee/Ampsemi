from time import sleep

from AMPS_API.Chroma import chroma6314A, chroma62006P
from AMPS_API.Keysight import keysight34461A
from AMPS_API.Agilent import agilentE3631A

# a = agilentE3631A.AgilentE3631A()
# a.open("GPIB0::6::INSTR", reset=False, idn=False)
# a.output(output=0)
# a.configure(supply_voltage=0, output_voltage=1.2, output_current=0.1, display=0, beeper=1)
# a.configure(supply_voltage=1, output_voltage=3.3, output_current=0.3, display=0, beeper=1)
# a.output(1)
# print(a.read_outputvoltage())
# print(a.read_outputcurrent())


# V3p3 = agilentE3631A.AgilentE3631A()
# V3p3.open(inst_resource="GPIB0::6::INSTR", reset=False, idn=False)
# V3p3.configure(supply_voltage=3.3)
# print("V3p3 voltage:", V3p3.read_PS())
# print("V3p3 current:", V3p3.read_outputcurrent())

"""" Vin Subsytem """

#VIN voltage change without reset
# V = chroma62006P.Chroma62006P()
# V.open(inst_resource="TCPIP0::192.168.199.132::2101::SOCKET", reset=False, idn=False)
# V.configure(output_voltage=12.0, output_current=5.0, beeper=1)
# V.output(output=1)
# sleep(2)
# print("Vin:", V.read_outputvoltage())
# print(V.read_outputcurrent())
#END of VIN voltage change without reset

# V.close()

"""" Iout Subsytem """

# # Load change For railA -1     Resistive load #######################
# I = chroma6314A.Chroma6314A()
# I.open(inst_resource="GPIB0::15::INSTR", reset=False, idn=False)
# I.channel_subsystem(channel=0, active=1, synchronized=1)
# I.mode_subsystem(mode=4)
# I.resistance_subsystem(max_resistance_load=(1/0.01), min_resistance_load=(1/0.01), rise_slewrate=0.01, fall_slewrate=0.01)
# I.load_subsystem(1)
# sleep(1)
# print("Rail A Slot 0 Iout:", I.measure_I(),"Vout:", I.measure_V())
# I1=I.measure_I()
# # END of Load change
#
# # Load change For railA -2       Resistive load #######################
# I = chroma6314A.Chroma6314A()
# I.open(inst_resource="GPIB0::15::INSTR", reset=False, idn=False)
# I.channel_subsystem(channel=2, active=1, synchronized=1)
# I.mode_subsystem(mode=4)
# I.resistance_subsystem(max_resistance_load=(1/0.01), min_resistance_load=(1/0.01), rise_slewrate=0.01, fall_slewrate=0.01)
# I.load_subsystem(1)
# sleep(1)
# print("Rail A Slot 2 Iout:", I.measure_I(),"Vout:", I.measure_V())
# I2=I.measure_I()
# sleep(1)
# I_total=float(I1) + float(I2)
# sleep(1)
# print("I_Total:", I_total)
# END of Load change


# # Load change For railB     Resistive load #######################
# I = chroma6314A.Chroma6314A()
# I.open(inst_resource="GPIB0::15::INSTR", reset=False, idn=False)
# I.channel_subsystem(channel=4, active=1, synchronized=1)
# I.mode_subsystem(mode=4)
# # I.configure_subsystem(key=0)
# IOUT=0.01
# I.resistance_subsystem(max_resistance_load=(1/IOUT), min_resistance_load=(1/IOUT), rise_slewrate=0.01, fall_slewrate=0.01)
# I.load_subsystem(1)
# sleep(1)
# print("Rail B Slot 4 IOUT:", I.measure_I(),"Vout:", I.measure_V())
# END of Load change











####### -CC MODE- ##########
# I = chroma6314A.Chroma6314A()
# I.open(inst_resource="GPIB0::15::INSTR", reset=False, idn=False)
# I.mode_subsystem(mode=1)    #(CCL=0, CCH=1, CCDL=2, CCDH=3, CRL=4, CRH=5)
# I.channel_subsystem(channel=0, active=1, synchronized=1)
# I.current_subsystem(curr_subsystem=0, max_iload1=5, min_iload2=5, rise_slewrate=2.5,
#                           fall_slewrate=1, dynamic_duration1=0.020, dynamic_duration2=0.010)    # (curr_subsystem: 0-static, 1- Dynamic loads)
# I.load_subsystem(0)
# sleep(2)
# print("Iout:", I.measure_I(),"Vout:", I.measure_V())
#I.load_subsystem(0)
##############################


####### -CCMODE- ##########
# I = chroma6314A.Chroma6314A()
# I.open(inst_resource="GPIB0::15::INSTR", reset=False, idn=False)
# I.mode_subsystem(mode=1)    #(CCL=0, CCH=1, CCDL=2, CCDH=3, CRL=4, CRH=5)
# I.channel_subsystem(channel=2, active=1, synchronized=1)
# I.current_subsystem(curr_subsystem=0, max_iload1=5, min_iload2=5, rise_slewrate=2.5,
#                           fall_slewrate=1, dynamic_duration1=0.020, dynamic_duration2=0.010)    # (curr_subsystem: 0-static, 1- Dynamic loads)
# I.load_subsystem(0)
# sleep(2)
# print("Iout:", I.measure_I(),"Vout:", I.measure_V())
#I.load_subsystem(0)
##############################

# ## DMM
dmm1_resource = "TCPIP0::K-34461A-07403::5025::SOCKET"
DMM1 = keysight34461A.Keysight34461A()  # Initializes class object
DMM1.open(f'{dmm1_resource}')  # Opens instrument resource
DMM1.configure_V(type=1, bandwidth=1, auto_impedance=0,
                              voltage_range=3)  # Configures DMM1 as voltage with 100V
print(DMM1.read_DMM(sample_count=1, trigger_source=0))

# I.close()
# CTRL + / to comment
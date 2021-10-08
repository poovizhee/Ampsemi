from AMPS_API.Keithley import keithley2200, keithley2602, keithleyN6700
from AMPS_API.Keysight import keysight34461A
from AMPS_API.Tektronix import tektronixAFG3102 as AFG, tektronixMSO4000B as SCOPE
from AMPS_API.Chroma import chroma62006P
from AMPS_API.Chroma import chroma6314A
from AMPS_API.Agilent import agilentE3631A
from time import sleep



# CHROMA = chroma62006P.Chroma62006P()
# CHROMA.open("TCPIP0::192.168.199.132::2101::SOCKET")
# CHROMA.voltagelimit_high(20)
# CHROMA.currentlimit_high(2)
# CHROMA.configure(12.0,1.0,1)
#
# CHROMA.output(1)
# CHROMA.output(0)
# CHROMA.close()
''
# import keysight34461A as Keysight
# KEYSIGHT = Keysight.Keysight34461A()
# KEYSIGHT.open("TCPIP0::K-34461A-07388::5025::SOCKET")
# KEYSIGHT.configure_V(1, 1, 0, 3)
# A=KEYSIGHT.read_DMM(1,0)
# print(A)
# KEYSIGHT.close()


# CHROMA_load = chroma6314A.Chroma6314A()
# CHROMA_load.open("GPIB0::15::INSTR")
# CHROMA_load.channel_subsystem( 1, 1, 0)   #(channel,active or not, synchronise)
# CHROMA_load.mode_subsystem(2) # (0-CCL   1-CCH     2-CCDL   3-CCDH    4-CRL   5-CRH   6-CV  )
# CHROMA_load.current_subsystem(1, 1,0, 2.5, 1, 0.020, 0.010)   #(Static=0,dyn=1    ,hi lim, low lim, on slew rate , off slew rate,dyna dure1, dyna Dure2)
# CHROMA_load.load_subsystem(1)
# CHROMA_load.load_subsystem(0)
# CHROMA_load.close()

                                               # Importing chroma6314A file

# AGILENT = agilentE3631A.AgilentE3631A()                                               # Initialize & open an instrument reference
# AGILENT.open("GPIB0::6::INSTR")
# AGILENT.configure(0, 3, 0.5, 1, 1)                                             # Configures parameters based on output selection(P6V/P25V/N25V)
# AGILENT.output(1)
# AGILENT.close()


                                           # Importing chroma6314A file
TEKTRONIX = SCOPE.TektronixMSO4000B()                                       # Initialize & open an instrument reference
TEKTRONIX.open("TCPIP0::192.168.199.138::4000::SOCKET")
Pwidth = TEKTRONIX.time_measurement(acquisition=1, channel=5, time_measure_type=0, measure_visible=1, measure_active=0, display=1)
print(Pwidth)                                      # Configures time_measurement parameters based on the channel selection
print(TEKTRONIX.read_measurement(4))                                                                                       # Reads the measurement value
TEKTRONIX.close()


# Initial power up.
# CHROMA = chroma62006P.Chroma62006P()
# CHROMA.open("TCPIP0::192.168.199.132::2101::SOCKET")
# CHROMA.voltagelimit_high(20)
# CHROMA.currentlimit_high(2)
# CHROMA.configure(12.0,2.0,1)
# CHROMA.output(1)
# #CHROMA.output(0)
#
# AGILENT = agilentE3631A.AgilentE3631A()                                               # Initialize & open an instrument reference
# AGILENT.open("GPIB0::6::INSTR")
# AGILENT.configure(0, 3.3, 0.5, 1, 1)                                             # Configures parameters based on output selection(P6V/P25V/N25V)
# AGILENT.output(0)
# AGILENT.close()
#
# import keysight34461A as Keysight
# KEYSIGHT = Keysight.Keysight34461A()
# KEYSIGHT.open("TCPIP0::K-34461A-07388::5025::SOCKET")
# KEYSIGHT.configure_V(1, 1, 0, 3)
# A=KEYSIGHT.read_DMM(1,0)
# print(A)
#
# if A >0.5:
#       CHROMA = chroma6314A.Chroma6314A()
#       CHROMA.open("GPIB0::15::INSTR")
#       CHROMA.channel_subsystem( 1, 1, 0)   #(channel,active or not, synchronise)
#       CHROMA.mode_subsystem(2) # (0-CCL   1-CCH     2-CCDL   3-CCDH    4-CRL   5-CRH   6-CV  )
#       CHROMA.current_subsystem(1, 1,0, 2.5, 1, 0.020, 0.010)   #(Static=0,dyn=1    ,hi lim, low lim, on slew rate , off slew rate,dyna dure1, dyna Dure2)
#       CHROMA.load_subsystem(1)
#
# else:
#   print("Device is not up, Check the connections")

# CHROMA.close()
#
# KEYSIGHT.close()
#
#
# CHROMA.close()
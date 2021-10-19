from AMPS_API.Keithley import keithley2200, keithley2602, keithleyN6700
from AMPS_API.Keysight import keysight34461A
# from AMPS_API.Tektronix import tektronixAFG3102 as AFG, tektronixMSO4000B as SCOPE
from AMPS_API.Chroma import chroma62006P
from AMPS_API.Chroma import chroma6314A
from AMPS_API.Agilent import agilentE3631A
from time import sleep




#Initial power up.


# AGILENT = agilentE3631A.AgilentE3631A()                                               # Initialize & open an instrument reference
# AGILENT.open("GPIB0::6::INSTR")
# # AGILENT.configure(0, 3.3, 0.3, 1, 1)                                             # Configures parameters based on output selection(P6V/P25V/N25V)
# # AGILENT.configure(1, 3.3, 0.3, 1, 1)
# # AGILENT.output(1)
# AGILENT.close()
#
# import keysight34461A as Keysight
# KEYSIGHT = Keysight.Keysight34461A()
# KEYSIGHT.open("TCPIP0::K-34461A-07388::5025::SOCKET")
# KEYSIGHT.configure_V(1, 1, 0, 3)
# A=KEYSIGHT.read_DMM(1,0)
# print(A)


# CHROMA = chroma62006P.Chroma62006P()
# CHROMA.open("TCPIP0::192.168.199.132::2101::SOCKET")
# # # CHROMA.voltagelimit_high(20)
# # # CHROMA.currentlimit_high(2)
# # # CHROMA.configure(8.0,2.0,1)
# # # CHROMA.output(1)
# CHROMA.close()



# if A >0.5:
#         print("Device is up, connections are Okay")
#
# TEKTRONIX = SCOPE.TektronixMSO4000B()  # Initialize & open an instrument reference
# TEKTRONIX.open("TCPIP0::192.168.199.138::4000::SOCKET")
# TEKTRONIX.time_measurement(1, 5, 2, 1, 0,1)              # Configures time_measurement parameters based on the channel selection
# Pwidth = TEKTRONIX.read_measurement(1)  # Reads the measurement value
# print(Pwidth)
#
# sleep(2)
# AGILENT.output(0)
# sleep(2)
# CHROMA.output(0)
# sleep(2)
# KEYSIGHT.close()
print(not "dfs"  False)
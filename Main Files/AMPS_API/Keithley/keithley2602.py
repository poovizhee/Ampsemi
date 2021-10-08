"""
*******************************************
© AMP Semiconductor Pvt Ltd 2021
© Tessolve Semiconductor Pvt Ltd 2021
*******************************************

Administrator                   : LabAutomation
Author                          : KARTHICK B
Developed Tool and Version      : Python 3.9
Description                     : General functions for Keithley 2602
Module Name                     : Keithley-2602 SourceMeter
Module Version                  : 0.0.1
Created                         : March 2021
"""


import pyvisa

class Keithley2602():

    """ This KEITHLEY 2602 library file provides you with the information
        required to use functions for remotely controlling your instrument.

        import keithley2602 as KEITHLEY

        K = KEITHLEY.Keithley2602()                                              # Initialize & open an instrument reference
        K.open("TCPIP0::192.168.199.132::2101::SOCKET")

        K.apply_voltage_A(0.05)                                             # set the voltage to 0.05V over channel A
        K.sourcevoltage_limit_A(6)                                          # limiting the voltage to 6V
        K.apply_current_A(0.5)                                              # set the current to 0.5A over channel A
        K.output_A(1)                                                       # turn on the output
        K.close()                                                           # Close an instrument reference
    """

    def __init__(self):
        self.resources = pyvisa.ResourceManager()
        self.D = list(self.resources.list_resources())
        if (len(self.D)) == 0:
            print("No devices connected")

        self.display_channel = ['SMUA', 'SMUB']
        self.display_measure = ['DCAMPS', 'DCVOLTS', 'OHMS', 'WATTS']
        self.source = ['DCAMPS', 'DCVOLTS']

    def __repr__(self):
        return repr(self.D)

    def open(self, inst_address, reset=True, idn=True):
        try:
            self.inst = self.resources.open_resource("%s" %(inst_address))
            if reset:
                self.reset()                                         # Calling reset function
            if idn:
                print("{} has connected.".format(self.idn_Q().strip()))      # Calling idn function
        except Exception as error:
            self.check_error(error)

    def reset(self):
        try:
            self.inst.write("reset()")
            #self.default_setup()                                   # Calling default_setup function
        except Exception as error:
            self.check_error(error)
    '''
    Sends a default command string to the instrument whenever a new VISA session is opened, or the instrument is reset.
    Use this function as a subfunction for the Initialize and Reset.
    '''
    def default_setup(self):
        try:
            self.inst.write("*ESE 60;*SRE 48;*CLS")
        except Exception as error:
            self.check_error(error)

    def close(self, idn=True):
            try:
                if idn:
                    print("{} has disconnected.".format(self.idn_Q().strip()))   # Calling idn function
                    self.inst.close()
            except Exception as error:
                self.check_error(error)

############################################ Error Handler ###########################################                         #

    '''
    Update import error reported by the system
    '''
    def import_error(self):
        print("Invalid Adapter provided for Instrument since, 'VISA driver is not present'")

    '''
    Update device error reported by the system
    '''
    def check_error(self, error):
        print("Device Error:", error)


############################################ Common Query ###########################################

    '''
    Identify the instrument name
    '''
    def idn_Q(self):
        try:
            self.idn = self.inst.query("*IDN?")
            return self.idn
        except Exception as error:
            self.check_error(error)
    '''
        *ESR? - Returns the contents of the event status register in decimal form
                and subsequently sets the register to zero.
        *STB? - Reads the contents of the status byte in decimal form.
        *TST? - Initiates self-tests of the instrument and returns an error code

        Passing an argument for setting_query variable from above listed commands;

        Example: common_Q = (0)
    '''
    def common_Q(self, setting_query=0):
        Setting_query = ["*ESR?", "*STB?", "*TST?"]
        try:
            self.common_Q = self.inst.query("%s" %(Setting_query[int(setting_query)]))
            return self.common_Q
        except Exception as error:
            self.check_error(error)

############################################# Configuration #############################################

    def configure_display(self, display_channel=0, display_measure=0):
        try:
            self.inst.write(f"display.screen = display.{self.display_channel[int(display_channel)]}")
            self.inst.write(f"display.smua.measure.func = display.MEASURE_{self.display_measure[int(display_measure)]}")
        except Exception as error:
            self.check_error(error)

    def configure_source(self, source=0):
        try:
            self.inst.write(f"smua.source.func = smua.OUTPUT_{self.source[int(source)]}")
        except Exception as error:
            self.check_error(error)

    def sourcevoltage_limit_A(self, voltage=0):
        try:
            self.inst.write("smua.source.limitv=%f" %voltage)
        except Exception as error:
            self.check_error(error)

    def sourcevoltage_limit_B(self, voltage=0):
        try:
            self.inst.write("smub.source.limitv=%f" %voltage)
        except Exception as error:
            self.check_error(error)

    def sourcecurrent_limit_A(self, current=0):
        try:
            self.inst.write("smua.source.limiti=%f" %current)
        except Exception as error:
            self.check_error(error)

    def sourcecurrent_limit_B(self, current=0):
        try:
            self.inst.write("smub.source.limiti=%f" %current)
        except Exception as error:
            self.check_error(error)

    ''' Configure the external voltage level(V)
    '''
    def sourcevoltage_level_A(self, voltage=0):
        try:
            self.inst.write("smua.source.lowrangev=%f" %voltage)
        except Exception as error:
            self.check_error(error)

    def sourcevoltage_level_B(self, voltage=0):
        try:
            self.inst.write("smub.source.lowrangev=%f" %voltage)
        except Exception as error:
            self.check_error(error)

    ''' Configure the external current level(A)
    '''
    def sourcecurrent_level_A(self, current=0):
        try:
            self.inst.write("smua.source.lowrangei=%f" %current)
        except Exception as error:
            self.check_error(error)

    def sourcecurrent_level_B(self, current=0):
        try:
            self.inst.write("smub.source.lowrangei=%f" %current)
        except Exception as error:
            self.check_error(error)

    ''' Configure the external voltage level(V) to measure
    '''
    def measurevoltage_level_A(self, voltage=0):
        try:
            self.inst.write("smua.measure.lowrangev=%f" %voltage)
        except Exception as error:
            self.check_error(error)

    def measurevoltage_level_B(self, voltage=0):
        try:
            self.inst.write("smub.measure.lowrangev=%f" %voltage)
        except Exception as error:
            self.check_error(error)

    ''' Configure the external current level(A) to measure
    '''
    def measurecurrent_level_A(self, current=0):
        try:
            self.inst.write("smua.measure.lowrangei=%f" %current)
        except Exception as error:
            self.check_error(error)

    def measurecurrent_level_B(self, current=0):
        try:
            self.inst.write("smub.measure.lowrangei=%f" %current)
        except Exception as error:
            self.check_error(error)

    '''Enable/disable the output of power supply
    1 = ON; 0 = OFF
    '''
    def output_A(self, output=1):
        if output==1:
            try:
                self.inst.write("smua.source.output = smua.OUTPUT_ON")
            except Exception as error:
                self.check_error(error)
        else:
           self.inst.write("smua.source.output = smua.OUTPUT_OFF")

    def output_B(self, output=1):
        if output==1:
            try:
                self.inst.write("smub.source.output = smub.OUTPUT_ON")
            except Exception as error:
                self.check_error(error)
        else:
           self.inst.write("smub.source.output = smub.OUTPUT_OFF")

    '''Turns beeper on/off
    1 = ON; 0 = OFF
    '''
    def beeper(self, beep_duration=1, beep_frequency=1000):
        try:
            self.inst.write("beeper.beep (%f,%d)" %(beep_duration, beep_frequency))
        except Exception as error:
            self.check_error(error)

    def buffer_A(self):
        self.inst.write("smua.nvbuffer1.clear()")
        self.inst.write("smua.nvbuffer2.clear()")
        self.inst.write("smua.nvbuffer1.clearcache()")
        self.inst.write("smua.nvbuffer2.clearcache()")

    def buffer_B(self):
        self.inst.write("smub.nvbuffer1.clear()")
        self.inst.write("smub.nvbuffer2.clear()")
        self.inst.write("smub.nvbuffer1.clearcache()")
        self.inst.write("smub.nvbuffer2.clearcache()")

    def autorange_A(self,auto=1):
        if auto==0:
            self.inst.write("smua.measure.autorangei = smua.AUTORANGE_OFF")
            self.inst.write("smua.measure.autorangev = smua.AUTORANGE_OFF")
            self.inst.write("smua.source.autorangei = smua.AUTORANGE_OFF")
            self.inst.write("smua.source.autorangev = smua.AUTORANGE_OFF")
        elif auto==1:
            self.inst.write("smua.measure.autorangei = smua.AUTORANGE_ON")
            self.inst.write("smua.measure.autorangev = smua.AUTORANGE_ON")
            self.inst.write("smua.source.autorangei = smua.AUTORANGE_ON")
            self.inst.write("smua.source.autorangev = smua.AUTORANGE_ON")
        else:
            pass
    def autorange_B(self,auto=1):
        if auto==0:
            self.inst.write("smub.measure.autorangei = smub.AUTORANGE_OFF")
            self.inst.write("smub.measure.autorangev = smub.AUTORANGE_OFF")
            self.inst.write("smub.source.autorangei = smub.AUTORANGE_OFF")
            self.inst.write("smub.source.autorangev = smub.AUTORANGE_OFF")
        elif auto==1:
            self.inst.write("smub.measure.autorangei = smub.AUTORANGE_ON")
            self.inst.write("smub.measure.autorangev = smub.AUTORANGE_ON")
            self.inst.write("smub.source.autorangei = smub.AUTORANGE_ON")
            self.inst.write("smub.source.autorangev = smub.AUTORANGE_ON")
        else:
            pass


############################################# Read ############################################

    ''' Read the actual voltage and current level of output
    '''
    def read_actualoutput_A(self):
        try:
            self.measure_voltage_current_A()
            actual_current=float(self.inst.query("print(currenta)"))
            actual_voltage=float(self.inst.query("print(voltagea)"))
            actual_current="{:f}".format(actual_current)
            actual_voltage="{:f}".format(actual_voltage)
            return actual_current,actual_voltage
        except Exception as error:
            self.check_error(error)

    ''' Read the actual voltage and current level of output
    '''
    def read_actualoutput_B(self):
        try:
            self.measure_voltage_current_B()
            actual_current=float(self.inst.query("print(currentb)"))
            actual_voltage=float(self.inst.query("print(voltageb)"))
            actual_current="{:f}".format(actual_current)
            actual_voltage="{:f}".format(actual_voltage)
            return actual_current,actual_voltage
        except Exception as error:
            self.check_error(error)

############################################# Write & Measure #############################################

    """
    Turns on the specified SMU and applies a voltage.
    :param smu: A keithley smu instance.
    :param voltage: Voltage to apply in Volts.
    """
    def apply_voltage_A(self,voltage: float) -> None:
        self.inst.write("smua.source.levelv = %f"%voltage)

    """
    Turns on the specified SMU and applies a voltage.
    :param smu: A keithley smu instance.
    :param voltage: Voltage to apply in Volts.
    """
    def apply_voltage_B(self,voltage: float) -> None:
        self.inst.write("smub.source.levelv = %f"%voltage)

    """
    Turns on the specified SMU and sources a current.
    :param smu: A keithley smu instance.
    :param curr: Current to apply in Ampere.
    """
    def apply_current_A(self,curr: float) -> None:
        self.inst.write("smua.source.leveli = %f"%curr)

    """
    Turns on the specified SMU and sources a current.
    :param smu: A keithley smu instance.
    :param curr: Current to apply in Ampere.
    """
    def apply_current_B(self,curr: float) -> None:
        self.inst.write("smub.source.limiti = %f"%curr)

    """
    Measures a voltage at the specified SMU.
    :param smu: A keithley smu instance.
    :returns: Measured voltage in Volts.
    """
    def measure_voltage_current_A(self) -> float:
        return self.inst.write("currenta, voltagea=smua.measure.iv()")

    """
    Measures a current at the specified SMU.
    :param smu: A keithley smu instance.
    :returns: Measured current in Ampere.
    """
    def measure_voltage_current_B(self) -> float:
        return self.inst.write("currentb, voltageb=smub.measure.iv()")

    def func_a(self, function=0):
        # 0=current, 1=voltage
        function = ["smua.OUTPUT_DCVOLTS", "smua.OUTPUT_DCCURR"]
        self.inst.write(f"smua.source.func={function}")

    def func_b(self, function=0):
        self.inst.write(f"smub.source.func={function}")

    def linearVoltSweep_MeasureI(self,Channel="smua",PulseStart=0,PulseStop=1,DelayTime=0.2,SweepPoints=5):
        outputI=[]
        self.inst.write("SweepVLinMeasureI(%s, %f, %f, %f, %d)"%(Channel,PulseStart,PulseStop,DelayTime,SweepPoints))
        self.inst.write("print(smua.nvbuffer1.n)")
        self.inst.write("printbuffer(1, 1, smua.nvbuffer1) ")
        print(self.read_actualoutput_A())

# k2602=Keithley2602()
# k=k2602.open("GPIB0::26::INSTR")
# k2602.reset()
# k2602.configure_display(display_channel=0, display_measure=0)
# k2602.configure_source(source=0)
# k2602.apply_current_A(curr=-0.005)
# k2602.sourcevoltage_limit_A(voltage=2)                                    # To measure 10μA, configure current > 1mA
# # k2602.autorange_A(1)
# # k2602.measurevoltage_level_A(1)
# # k2602.measurecurrent_level_A(1)
# # k2602.beeper(0.1,2000)
# # k2602.func_a(1)
# # k2602.beeper(0.1,2000)
# # k2602.apply_voltage_A(0.05)
# # k2602.beeper(0.1,2000)
# k2602.output_A(1)
# # k2602.sourcevoltage_limit_A(6)
# # k2602.beeper(0.1,2000)
# # k2602.apply_current_A(0)
# # k2602.beeper(0.1,2000)
# # k2602.apply_current_A(0.5)
# # k2602.sourcevoltage_limit_A(6)
# # print(k2602.linearVoltSweep_MeasureI())
# # k2602.output_A(1)
# # k2602.beeper(0.1,2000)
# print(k2602.read_actualoutput_A())
# # k2602.beeper(0.1,2000)
# # k2602.apply_voltage_B(2)
# # k2602.beeper(0.1,2000)
# # k2602.apply_current_B(0.7)
# # k2602.beeper(0.1,2000)
# # print(k2602.read_actualoutput_B())
# # k2602.beeper(0.1,2000)
# # k2602.output_B(1)
# # k2602.beeper(0.1,2000)
# # print(k2602.common_Q(1))
# k2602.close()

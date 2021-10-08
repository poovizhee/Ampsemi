"""
*******************************************
© AMP Semiconductor Pvt Ltd 2021
© Tessolve Semiconductor Pvt Ltd 2021
*******************************************

Administrator                   : LabAutomation
Author                          : KARTHICK B
Developed Tool and Version      : Python 3.9
Description                     : General functions for Chroma_PS_62006P-30-80
Module Name                     : Chroma general Interface of 62006P-30-80  DC Power Supply
Module Version                  : 0.0.1
Created                         : March 2021
"""

import time
import pyvisa as visa                                       # Provides a programming interface to control Ethernet/LXI, GPIB, serial, USB, PXI, and VXI instruments

class Chroma62006P(object):

    """ This CHROMA 6200^P-30-80 library file provides you with the information
        required to use functions for remotely controlling your instrument.

        import chroma_PS_62006P-30-80 as Chroma

        CHROMA = Chroma.Chroma6200P()                                            # Initialize & open an instrument reference
        CHROMA.open("TCPIP0::192.168.199.132::2101::SOCKET")

        CHROMA.configure(15.0,1.0,1)                                             # Configures parameters
        CHROMA.output(1)                                                         # Enables the output
        CHROMA.read_outputvoltage()                                              # Returns the output voltage
        CHROMA.read_outputcurrent()                                              # Returns the output current
        CHROMA.close()                                                           # Close an instrument reference
    """

    def __init__(self):
        """ Initialize visa resources & get list out all connected instruemnts resources with the system """
        try:
            self.rm              = visa.ResourceManager()                               # Provides access to all resources registered with it
            self.D               = list(self.rm.list_resources())                       # Lists the available resources

        except Exception as ex:
            self.import_error(ex)

        """ Create variable instances for function commands """
        self.output_enable      = ["OFF", "ON"]                                         # Enables/disables output state
        self.beeper_enable      = ["OFF", "ON"]                                         # Enables/disables command beep sound
        self.remote_mode        = ["OFF", "ON"]
        self.backlight_level    = ["HIGH","NOR","DIM","OFF"]
        self.master_slave       = ["MASTER", "SLAVE1", "SLAVE2", "SLAVE3", "SLAVE4"]
    def __repr__(self):
        """ print statement to compute the 'informal' string representation of an object """
        return repr(self.D)

    def resource_list(self):
        """ List out connected instruments from list_resources """
        return self.D

    def open(self, inst_resource: str="", reset=True, idn=True):
        """ Establishes communication with the instrument and
            optionally performs an instrument identification query and/or an instrument reset.
        """
        try:
            self.inst = self.rm.open_resource(f"{inst_resource}")                       # Opens the resource of an instrument

            if (self.inst.resource_name.startswith("ASRL") or
                self.inst.resource_name.startswith("TCPIP") or
                self.inst.resource_name.startswith("TCPIP0") or
                self.inst.resource_name.endswith("SOCKET")
                ):
                self.inst.read_termination = "\n"                                       # Add read_termination = "\n" if communication type is TCP/IP

            if (len(self.D)) == 0:
                print("No devices connected.")
            else:
                if reset:
                    self.reset()
                if idn:
                    print(f"{self.inst_Q().strip()} resource has been connected")
        except Exception as ex:
            self.exceptionhandler(ex)

    def close(self):
        """ Closes connections to the instrument """
        try:
            close = self.inst_Q().strip()
            self.inst.close()
            self.rm.close()
            print(f"{close} resource has been disconnected")
        except Exception as ex:
            self.exceptionhandler(ex)

    #############################################################
    # Error Handler
    #############################################################

    def import_error(self):
        """ Update import error reported by the system
        """
        print("Invalid Adapter provided for Instrument since, 'Chroma6314A - Load Python file is not present/installed'.")

    def exceptionhandler(self, exception):
        """ Update device error reported by the system
        """
        print("Command Error:", exception)

    #############################################################
    # Utility
    #############################################################

    def reset(self):
        """ Resets the instrument and then sends a set of default setup commands to the instrument """
        try:
            self.write("*RST")                                                          # Calling "write" instance to write SCPI commands
            self.default_setup()                                                        # Calling "default setup" instance
        except Exception as ex:
            self.exceptionhandler(ex)

    def default_setup(self):
        """ Sends a default command string to the instrument whenever a new VISA session is opened, or the instrument is reset.
            Use this function as a subfunction for the Initialize and Reset.
        """
        try:
            self.write("*ESE 60;*SRE 48;*CLS")                                          # Calling "write" instance to write SCPI commands
        except Exception as ex:
            self.exceptionhandler(ex)

    #############################################################
    # Query
    #############################################################

    def inst_Q(self):
        """ Query an instrument identification """
        try:
            inst_Q = self.write("*IDN?")                                                # Calling "query" instance to write SCPI commands
            return inst_Q
        except Exception as ex:
            self.exceptionhandler(ex)

    def common_Q(self, setting_q=0):
        """
        *CAL? - Query an instruemnt calibration status.
                Note: The self-calibration can take several minutes to respond.
                      No other commands will be executed until calibration is complete.
        *ESR? - Returns the contents of the event status register in decimal form
                and subsequently sets the register to zero.
        *STB? - Reads the contents of the status byte in decimal form.
        *TST? - Initiates self-tests of the instrument and returns an error code

        Passing an argument for setting_q variable from above listed commands;

        Example: common_Q = (0)
        """
        try:
            common_Q = self.write(self.setting_Q[int(setting_q)])
            return common_Q

        except Exception as ex:
            self.exceptionhandler(ex)

    #############################################################
    # Common
    #############################################################

    def write(self, cmd: str=""):
        ''' SCIPI command directly can be sent using this function
            cmd : type string / parameter - SCIPI command with proper format e.g. 'MEAS:CURR?'
        '''
        if isinstance(cmd, str):
            if cmd.endswith('?'):
                try:
                    query = self.inst.query(cmd)
                    return query
                except Exception as ex:
                    self.exceptionhandler(ex)
            else:
                try:
                    self.inst.write(cmd)
                except Exception as ex:
                    self.exceptionhandler(ex)
        else:
            print("Invalid SCPI command: Please provid valid SCPI command input")

    #############################################################
    # Configuration
    #############################################################

    def configure(self, output_voltage=0.0, output_current=0.0, beeper=1):
        """ Configures parameters of output voltage/current """
        """
            output_voltage      ->  Sets an output voltage limit
            output_current      ->  Sets an output current limit
            beeper              ->  Enables/disables beeper sound
        """
        self.write(":SOUR:VOLT {};:SOUR:CURR {};:CONFigure:BEEPer {}"
                    .format(output_voltage, output_current, self.beeper_enable[beeper]
                            )
                    )

    def voltagelimit_high(self, value=20.0):
        """ Configures voltage limit """
        """ output ->  set voltage with high limit """
        self.write(":SOUR:VOLT:LIMIT:HIGH {};"
                    .format(value)
                            )

    def voltagelimit_low(self, value=1.0):
        """ Configures voltage limit """
        """ output ->  set voltage with low limit """
        self.write(":SOUR:VOLT:LIMIT:LOW {};"
                    .format(value)
                            )

    def currentlimit_high(self, value=2.0):
        """ Configures current limit """
        """ output ->  set current with high limit """
        self.write(":SOUR:CURR:LIMIT:HIGH {};"
                    .format(value)
                            )

    def currentlimit_low(self, value=0.5):
        """ Configures current limit """
        """ output ->  set current with low limit """
        self.write(":SOUR:CURR:LIMIT:LOW {};"
                    .format(value)
                            )

    def voltage_slewrate(self, value=0.01):
        """ Configures voltage slewrate """
        """ output ->  set the voltage slewrate of the output voltage """
        self.write(":SOUR:VOLT:SLEW {};"
                    .format(value)
                            )

    def current_slewrate(self, value=0.01):
        """ Configures current slewrate """
        """ output ->  set the current slewrate of the output current """
        self.write(":SOUR:CURR:SLEW {};"
                    .format(value)
                            )

    def output(self, output=1):
        """ Configures output state """
        """ output ->  Enables/disables output state """
        self.write(":CONFigure:OUTPut {};"
                    .format(self.output_enable[int(output)]
                            )
                    )

    def remote(self,state=0):
        """configures remote mode
        remote ->  Enables/disables remote state"""
        self.write(":CONFigure:REMote {};".format(self.remote_mode[int(state)]
                                                )
                    )

    def backlight(self,level=0):
        """configures backlight level
        backlight ->  Enables/disables backlight level with  HIGH | NOR | DIM | OFF"""
        self.write(":CONFigure:BACKLIGHT {};".format(self.backlight_level[int(level)]
                                                )
                    )

    def Set_MSTSLV(self,state=0):
        """set the supply to master or SLAVE
        master slave ->  set the supply to any one of the list [ MASTER | SLAVE1 | SLAVE2 | SLAVE3 | SLAVE4 ] """
        self.write(":CONFigure:MSTSLV:ID {};".format(self.master_slave[int(state)]
                                                )
                    )

    def slavescount(self,count=0):
        """set the SLAVE counts
        slave ->  set the number of slaves count """
        self.write(":CONFigure:MSTSLV:NUMSLV {};".format(int(count)
                                                )
                    )
    #############################################################
    # Read
    #############################################################

    def read_outputvoltage(self):
        """ Returns the voltage measured at the output terminals of the power supply """
        read_voltage = self.write(":MEAS:VOLT?")
        return float(read_voltage)

    def read_outputcurrent(self):
        """ Returns the current measured at the output terminals of the power supply """
        read_current = self.write(":MEAS:CURR?")
        return float(read_current)

    def read_outputpower(self):
        """ Returns the power measured at the output terminals of the power supply """
        read_power = self.write(":MEAS:POW?")
        return float(read_power)

    def fetch_outputvoltage(self):
        """ Returns the voltage fetched at the output terminals of the power supply in real time"""
        fetch_voltage = self.write(":FETCh:VOLTage?")
        return float(fetch_voltage)

    def fetch_outputcurrent(self):
        """ Returns the current fetched at the output terminals of the power supply in real time"""
        fetch_current = self.write(":FETC:CURR?")
        return float(fetch_current)

    def fetch_outputpower(self):
        """ Returns the power fetched at the output terminals of the power supply in real time"""
        fetch_power = self.write(":FETC:POW?")
        return float(fetch_power)

    def fetch_status(self):
        """ Returns the status fetched"""
        fetch_status = self.write(":FETCh:STATus?")
        return fetch_status

    def read_voltagelimit(self):
        """ Returns the configured voltage limit """
        read_voltagelimithigh = self.write("SOUR:VOLT:LIMIT:HIGH?")
        read_voltagelimitlow = self.write("SOUR:VOLT:LIMIT:LOW?")
        read_voltagelimit=[read_voltagelimithigh,read_voltagelimitlow]
        return read_voltagelimit

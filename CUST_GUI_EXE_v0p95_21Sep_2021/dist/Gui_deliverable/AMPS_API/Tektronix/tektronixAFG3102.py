"""
*******************************************
© AMP Semiconductor Pvt Ltd 2021
© Tessolve Semiconductor Pvt Ltd 2021
*******************************************

Administrator                   : LabAutomation
Author                          : KARTHICK B
Developed Tool and Version      : Python 3.9
Description                     : General functions for AFG3102 DUAL CHANNEL ARBITRARY / FUNCTION GENERATOR
Module Name                     : AFG3102 FUNCTION GENERATOR
Module Version                  : 0.0.1
Created                         : March 2021
"""


import pyvisa

class TektronixAFG3102():
    """ This FUNCTION GENERATOR AFG3102 library file provides you with the information
    required to use functions for remotely controlling your instrument.

    import TektronixAFG3102 as Funcgen

    FG = Funcgen.FuncgenAFG3102()                                         # Initialize & open an instrument reference
    FG.open("USB0::0x05E6::0x2200::9205873::INSTR")

    FG.set_outputwaveform('ch1',3)                                        # output waveform configuration for channel one
    FG.set_outputwaveform('ch2',0)                                        # output waveform configuration for channel two
    FG.set_frequency('ch1','40E3')                                        # output waveform configuration with frequency 40KHz for channel one
    FG.set_frequency('ch2','30E3')                                        # output waveform configuration with frequency 40KHz for channel two
    FG.set_amplitude('ch1',2.00)                                          # output waveform configuration with amplitude 2 for channel one
    FG.set_amplitude('ch2',5.00)                                          # output waveform configuration with amplitude 5 for channel two
    FG.set_offset('ch1',1.00)                                             # offset Configuration
    FG.set_phase('ch1',00)                                                # phase Configuration
    FG.set_dutycycle('ch1',80.00)                                         # setting up the duty cycle percentage for output waveform
    FG.close()                                                            # Close an instrument reference
    """
    def __init__(self):
        self.resources = pyvisa.ResourceManager()
        self.D = list(self.resources.list_resources())
        if (len(self.D)) == 0:
            print("No devices connected")

    def __repr__(self):
        return repr(self.D)

    def open(self, inst_address, reset=True, idn=True):
        try:
            self.inst = self.resources.open_resource("%s" %(inst_address))
            if reset:
                self.reset()                                         # Calling reset function
            if idn:
                print("{} has connected.".format(self.idn_Q()))      # Calling idn function
        except Exception as error:
            self.check_error(error)

    def reset(self):
        try:
            self.inst.write("*RST")
            self.default_setup()                                     # Calling default_setup function
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
                            print("{} has disconnected.".format(self.idn_Q()))   # Calling idn function
                            self.inst.close()
            except Exception as error:
                    self.check_error(error)
    #############################################
    #                                           #
    #             Error Handler                 #
    #                                           #
    #############################################
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

    #############################################
    #                                           #
    #             Common Query                  #
    #                                           #
    #############################################

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

    #############################################
    #                                           #
    #           Configuration                   #
    #                                           #
    #############################################
    '''state 1 | 0 means ON | OFF
    '''
    def set_beeper(self,state=0):
        if state==1:
            try:
                self.inst.write("SYSTem:BEEPer:STATe ON")
            except Exception as error:
                self.check.error(error)
        else:
            self.inst.write("SYSTem:BEEPer:STATe OFF")

    def set_source(self,channel='ch1'):
        if channel=='ch1':
            try:
                self.inst.write("SOURce1:AM:SOURce INTernal")
            except Exception as error:
                self.check_error(error)
        elif channel=='ch2':
            try:
                self.inst.write("SOURce2:AM:SOURce INTernal")
            except Exception as error:
                self.check_error(error)

    '''Runmode [0,1,2,3,4] means ['AM','FM','PWM','SWEep','BURSt'] and state 0 | 1 means OFF | ON'''
    def set_runmode(self,channel='ch1',runmode=0,state=1):
        state_list=['OFF','ON']
        runmode_list=['AM','FM','PWM','SWEep','BURSt']
        if channel=='ch1':
            try:
                self.inst.write("SOURce1:%s:STATe %s"%(runmode_list[runmode],state_list[state]))
            except Exception as error:
                self.check_error(error)
        elif channel=='ch2':
            try:
                self.inst.write("SOURce2:%s:STATe %s"%(runmode_list[runmode],state_list[state]))
            except Exception as error:
                self.check_error(error)

    '''state 0 | 1 means OFF | ON'''
    def set_runmode_burst(self,channel='ch1',state=0):
        state_list=['TRIGgered','GATed']
        if channel=='ch1':
            try:
                self.inst.write("SOURce1:BURSt:MODE %s"%state_list[state])
            except Exception as error:
                self.check_error(error)
        elif channel=='ch2':
            try:
                self.inst.write("SOURce2:BURSt:MODE %s"%state_list[state])
            except Exception as error:
                self.check_error(error)

    '''count shows the number of cycles'''
    def set_burstcycles(self,channel='ch1',count=0):
        if channel=='ch1':
            try:
                self.inst.write("SOURce1:BURSt:NCYCles %d"%count)
            except Exception as error:
                self.check_error(error)
        elif channel=='ch2':
            try:
                self.inst.write("SOURce1:BURSt:NCYCles %d"%count)
            except Exception as error:
                self.check_error(error)
    '''
    state 0 means SINusoid, State 1 means SQUare, State 2 means RAMP, State 3 means PULse
    '''
    def set_outputwaveform(self,channel='ch1',state=0):
        waveform_list=['SINusoid','SQUare','RAMP','PULse']
        if channel=='ch1':
            try:
                self.inst.write("FUNCTION %s"%waveform_list[state])
            except Exception as error:
                self.check_error(error)
        elif channel=='ch2':
            try:
                self.inst.write("SOURCE2:FUNCTION %s"%waveform_list[state])
            except Exception as error:
                self.check_error(error)

    def set_frequency(self,channel='ch1',value='30E3'):
        if channel=='ch1':
            try:
                self.inst.write("FREQUENCY %s"%value)
            except Exception as error:
                self.check_error(error)
        elif channel=='ch2':
            try:
                self.inst.write("SOURCE2:FREQUENCY %s"%value)
            except Exception as error:
                self.check_error(error)

    def set_amplitude(self,channel='ch1',value=5.00):
        if channel=='ch1':
            try:
                self.inst.write("VOLTAGE:AMPLITUDE %f"%value)
            except Exception as error:
                self.check_error(error)
        elif channel=='ch2':
            try:
                self.inst.write("SOURCE2:VOLTAGE:AMPLITUDE %f"%value)
            except Exception as error:
                self.check_error(error)

    def set_offset(self,channel='ch1',value=1.00):
        if channel=='ch1':
            try:
                self.inst.write("VOLTAGE:OFFSET %f"%value)
            except Exception as error:
                self.check_error(error)
        elif channel=='ch2':
            try:
                self.inst.write("SOURCE2:VOLTAGE:OFFSET %f"%value)
            except Exception as error:
                self.check_error(error)

    def set_phase(self,channel='ch1',value='45DEG'):
        if channel=='ch1':
            try:
                self.inst.write("PHASE:ADJUST %s"%value)
            except Exception as error:
                self.check_error(error)
        elif channel=='ch2':
            try:
                self.inst.write("SOURCE2:PHASE:ADJUST %s"%value)
            except Exception as error:
                self.check_error(error)

    def set_dutycycle(self,channel='ch1',percentage=50):
        if channel=='ch1':
            try:
                self.inst.write("SOURce1:PULSe:DCYCle %f"%percentage)
            except Exception as error:
                self.check_error(error)
        elif channel=='ch2':
            try:
                self.inst.write("SOURce2:PULSe:DCYCle %f"%percentage)
            except Exception as error:
                self.check_error(error)

    ''' mode 0 means PULSe , mode 1 means BURSt'''
    def set_delay(self,mode=0,channel='ch1',delaytime='20ms'):
        mode_list=['PULSe','BURSt']
        if channel=='ch1':
            try:
                self.inst.write("SOURce1:%s:DELay %s"%(mode_list[0],delaytime))
            except Exception as error:
                self.check_error(error)
        elif channel=='ch2':
            try:
                self.inst.write("SOURce2:%s:DELay %s"%(mode_list[0],delaytime))
            except Exception as error:
                self.check_error(error)

    def set_pulseleading(self,channel='ch1',time='20ms'):
        if channel=='ch1':
            try:
                self.inst.write("SOURce1:PULSe:TRANsition:LEADing %s"%time)
            except Exception as error:
                self.check_error(error)
        elif channel=='ch2':
            try:
                self.inst.write("SOURce2:PULSe:TRANsition:LEADing %s"%time)
            except Exception as error:
                self.check_error(error)

    def set_pulsetrailing(self,channel='ch1',time='20ms'):
        if channel=='ch1':
            try:
                self.inst.write("SOURce1:PULSe:TRANsition:TRAiling %s"%time)
            except Exception as error:
                self.check_error(error)
        elif channel=='ch2':
            try:
                self.inst.write("SOURce2:PULSe:TRANsition:TRAiling %s"%time)
            except Exception as error:
                self.check_error(error)

    def set_pulsewidth(self,channel='ch1',time='200ns'):
        if channel=='ch1':
            try:
                self.inst.write("SOURce1:PULSe:WIDTh %s"%time)
            except Exception as error:
                self.check_error(error)
        elif channel=='ch2':
            try:
                self.inst.write("SOURce2:PULSe:WIDTh %s"%time)
            except Exception as error:
                self.check_error(error)

    def set_rampsymmetry(self,channel='ch1',percentage=60):
        if channel=='ch1':
            try:
                self.inst.write("SOURce1:FUNCtion:RAMP:SYMMetry %f"%percentage)
            except Exception as error:
                self.check_error(error)
        elif channel=='ch2':
            try:
                self.inst.write("SOURce2:FUNCtion:RAMP:SYMMetry %f"%percentage)
            except Exception as error:
                self.check_error(error)

    def set_sweeptime(self,channel='ch1',time='60ms'):
        if channel=='ch1':
            try:
                self.inst.write("SOURce1:SWEep:TIME %s"%time)
            except Exception as error:
                self.check_error(error)
        elif channel=='ch2':
            try:
                self.inst.write("SOURce2:SWEep:TIME %s"%time)
            except Exception as error:
                self.check_error(error)

    ''' mode 0 means AUTO, mode 1 means MANual'''
    def set_sweepmode(self,channel='ch1',mode=0):
        mode_list=['AUTO','MANual']
        if channel=='ch1':
            if mode==0:
                try:
                    self.inst.write("SOURce1:SWEep:MODE %s"%mode_list[mode])
                except Exception as error:
                    self.check_error(error)
            elif mode==1:
                try:
                    self.inst.write("SOURce1:SWEep:MODE %s"%mode_list[mode])
                except Exception as error:
                    self.check_error(error)
        elif channel=='ch2':
            if mode==0:
                try:
                    self.inst.write("SOURce2:SWEep:MODE %s"%mode_list[mode])
                except Exception as error:
                    self.check_error(error)
            elif mode==1:
                try:
                    self.inst.write("SOURce2:SWEep:MODE %s"%mode_list[mode])
                except Exception as error:
                    self.check_error(error)

    '''level 0 means MAXimum, level1 means MINimum'''
    def set_AMdepth(self,channel='ch1',level=0):
        level_list=[MAXimum,MINimum]
        if channel=='ch1':
            try:
                self.inst.write("SOURce1:AM:DEPth %s"%level_list[level])
            except Exception as error:
                self.check_error(error)
        elif channel=='ch2':
            try:
                self.inst.write("SOURce2:AM:DEPth %s"%level_list[level])
            except Exception as error:
                self.check_error(error)

    ''' mmode [0,1,2] means ['AM','FM','PWM'] and func [0,1,2,3] means ['SINusoid','SQUare','RAMP','PULse'] '''
    def set_internalfunc(self,channel='ch1',mod=0,func=0):
        mod_list=['AM','FM','PWM']
        function_list=['SINusoid','SQUare','RAMP','PULse']
        if channel=='ch1':
            try:
                self.inst.write("SOURce1:%s:INTernal:FUNCtion %s"%(mod_list[mod],function_list[func]))
            except Exception as error:
                self.check_error(error)
        elif channel=='ch2':
            try:
                self.inst.write("SOURce2:%s:INTernal:FUNCtion %s"%(mod_list[mod],function_list[func]))
            except Exception as error:
                self.check_error(error)

    '''channel [0,1] means ['SOURce1','SOURce2'] and runmode [0,1,2] means ['AM','FM','PWM'] '''
    def set_internalfreq(self,channel=0,runmode=0,freq='10kHz'):
            channel_list=['SOURce1','SOURce2']
            runmode_list=['AM','FM','PWM']
            try:
                self.inst.write("%s:%s:INTernal:FREQuency %s"%(channel_list[channel],runmode_list[runmode],freq))
            except Exception as error:
                self.check_error(error)

    def set_output(self,channel='ch1',state=0):
        channel_list={'ch1':1,'ch2':2}
        state_list=['OFF','ON']
        try:
            self.inst.write("OUTPut%d:STATe %s"%(channel_list[channel],state_list[state]))
        except Exception as error:
            self.check_error(error)



    #############################################
    #                                           #
    #                 Save & output             #
    #                                           #
    #############################################

    def save(self):
        try:
            self.inst.write("*SAV 1")
        except Exception as error:
            self.check_error(error)

    def recall(self):
        try:
            self.inst.write("*RCL 1")
        except Exception as error:
            self.check_error(error)

    #############################################
    #                                           #
    #           Write & Measure                 #
    #                                           #
    #############################################

    def voltage_highLow(self,channel='ch1',state='low',HV='2V',LV='-2V'):
        if state=='both':
            if channel=='ch1':
                try:
                    self.inst.write("SOURce1:VOLTage:LEVel:IMMediate:HIGH %s"%HV)
                    self.inst.write("SOURce1:VOLTage:LEVel:IMMediate:LOW %s"%LV)
                except Exception as error:
                    self.check_error(error)
            elif channel=='ch2':
                try:
                    self.inst.write("SOURce2:VOLTage:LEVel:IMMediate:HIGH %s"%HV)
                    self.inst.write("SOURce2:VOLTage:LEVel:IMMediate:LOW %s"%LV)
                except Exception as error:
                    self.check_error(error)
        elif state=='high':
            if channel=='ch1':
                try:
                    self.inst.write("SOURce1:VOLTage:LEVel:IMMediate:HIGH %s"%HV)
                except Exception as error:
                    self.check_error(error)
            elif channel=='ch2':
                try:
                    self.inst.write("SOURce2:VOLTage:LEVel:IMMediate:HIGH %s"%HV)
                except Exception as error:
                    self.check_error(error)
        elif state=='low':
            if channel=='ch1':
                try:
                    self.inst.write("SOURce1:VOLTage:LEVel:IMMediate:LOW %s"%LV)
                except Exception as error:
                    self.check_error(error)
            elif channel=='ch2':
                try:
                    self.inst.write("SOURce2:VOLTage:LEVel:IMMediate:LOW %s"%LV)
                except Exception as error:
                    self.check_error(error)



# FG=FuncgenAFG3102()
# FG.open("USB0::0x0699::0x0343::C023084::INSTR")
# FG.reset()
# FG.set_beeper(0)
# FG.set_runmode('ch1',2,1)
# FG.set_internalfunc()
# FG.set_outputwaveform('ch1',3)
# FG.set_outputwaveform('ch2',0)
# FG.set_frequency('ch1','40E3')
# FG.set_frequency('ch2','30E3')
# FG.set_amplitude('ch1',2.00)
# FG.set_amplitude('ch2',5.00)
# FG.set_offset('ch1',1.00)
# FG.set_phase('ch1',00)
# FG.set_dutycycle('ch1',80.00)
# FG.set_delay(0,'ch1','20ns')
# FG.set_pulseleading('ch1','10ns')
# FG.set_pulsetrailing('ch1','5ns')
# FG.set_pulsewidth('ch1','20us')
# FG.set_rampsymmetry('ch1',60)
# FG.voltage_highLow('ch1','both')
# FG.set_output('ch1',1)
# FG.save()
# FG.recall()
# FG.close()

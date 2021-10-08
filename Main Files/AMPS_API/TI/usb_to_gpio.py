"""
*******************************************
© AMP Semiconductor Pvt Ltd 2021
© Tessolve Semiconductor Pvt Ltd 2021
*******************************************

Administrator                   : LabAutomation
Author                          : SABARI SARAVANAN M
Developed Tool and Version      : Python 3.9
Description                     : General functions for HPA172 USB interface adapter
Module Name                     : USB-TO-GPIO
Module Version                  : 0.0.1
Created                         : April 2021
"""

import clr, array, os                                                                   # Import clr from 'pythonnet' to interface runtime engine with .net
from System import Byte, Int32, Array, Boolean

class USB_TO_GPIO(object):

    def __init__(self):
        """ SAA adapter constructor -  discovering a device via the SMBus API.
            This library file provides you with the information required to use functions for remotely controlling your instrument.

            from usb_to_gpio import USB_TO_GPIO                                             # Importing USB_TO_GPIO file

            TI = USB_TO_GPIO()                                                              # Initialize & opens an instrument reference

            TI.configure(pec_enabled=False)                                                 # Selects 100-KHz/400-KHz bus speed & PEC mode
            TI.send_byte(dev_addr=0x001, cmd_addr=0x00)                                     # Performs a “Send_Byte”
            TI.write_byte(dev_addr=0x01, cmd_addr=0x00, data=0x00)                          # Performs a “Write_Byte”

            TI.close()                                                                      # Close the device reference

        """
        try:
            # clr.AddReference("C:\\Program Files (x86)\\Texas Instruments Fusion API\\Library\\TIDP.SAA.dll")
            clr.AddReference(os.getcwd()+"\Texas_Instruments_Fusion_API\Library\TIDP.SAA.dll")# Load the dll file(C:\\ folder)
            import TIDP.SAA as API                                                                              # Import TIDP.SAA dll file

            if API.SMBusAdapter.Discover() != 0:                                                                # Find an adapter
                self.device = API.SMBusAdapter.Adapter                                                          # Import class from C# namespace
                print("USB_TO_GPIO device has opened")
                self.adapter_status = 1                                                                         # If adapter found

            else:
                print('No Adapter Found')
                self.adapter_status = 0                                                                         # If adapter not found

        except:
            self.import_error()

        self.status = 0                                                                                         # To read the device write/read status

    def __repr__(self):
        ''' print statement to compute the "informal" string representation of an object '''
        return repr(self.adapter_status)

    def close(self):
        try:
            self.device.Dispose()
            print('USB_TO_GPIO device has closed')
        except Exception as ex:
            self.exception_handler(ex)

    ###########################################
    # Error Handler
    ###########################################

    def import_error(self):
        ''' Update import error reported by the system of loading dll driver error.
        '''
        print("dll file not loaded, 'TI USB-TO-GPIO driver was not present/installed'.")
        exit()

    def exception_handler(self, exception):
        print("Exception occured:", exception)

    ###########################################
    # SMBus Adapter
    ###########################################

    def configure(self, pec_enabled:bool=False):
        ''' Select 100-KHz/400-KHz bus speed & PEC mode'''
        try:
            self.device.Set_Bus_Speed(self.device.BusSpeed.Speed100KHz)
            self.device.Set_PEC_Enabled(pec_enabled)

        except Exception as ex:
            self.exception_handler(ex)
            
    def send_byte(self, address:int=0x70, commandcode:int=0x04):
        '''
        Wrapper for SAA Write Byte Function, explicitly states which overload to use in Fusion API
        Args:
            (uint8) dev_addr = PMBus Slave Address (0-127) - b'\x7F'
            (uint8) cmd_addr = PMBus CMD Address (0-255) - b'\xFF'

        Returns:
            (bool) True if successful
            (bool) False otherwise
        '''
        try:
            if self.device.Send_Byte(Byte(address), Byte(commandcode)) == 0:                        # 0 = received acknowledgement
                # return 'Success'
                self.status = 0

        except Exception as ex:
            self.status = 1
            self.exception_handler(ex)

    def write_byte(self, address:int=0x70, commandcode:int=0x04, writedata:int=0x00):
        '''
        Wrapper for SAA Write Byte Function, explicitly states which overload to use in Fusion API
        Args:
            (uint8) dev_addr = PMBus Slave Address (0-127) - b'\x7F'
            (uint8) cmd_addr = PMBus CMD Address (0-255) - b'\xFF'
            (uint8) data = Data Byte to Write (0-255) - b'\xFF'

        Returns:
            (bool) True if successful
            (bool) False otherwise
        '''
        try:
            if self.device.Write_Byte(Byte(address), Byte(commandcode), Byte(writedata)) == 0:     # 0 = received acknowledgement
                return 'Success'

        except Exception as ex:
            self.exception_handler(ex)

    def read_byte(self, dev_addr, cmd_addr):
        '''
        Wrapper for SAA Write Byte Function, explicitly states which overload to use in Fusion API
        Args:
            (uint8) dev_addr = PMBus Slave Address (0-127) - b'\x7F'
            (uint8) cmd_addr = PMBus CMD Address (0-255) - b'\xFF'

        Returns:
            (uint8) Data Byte if successful
            NACK otherwise
        '''
        try:
            status = self.device.Read_Byte(Byte(dev_addr), Byte(cmd_addr))
            if status.SAA_Status == 'ACK':
                return int(status.Data.Hex, base=16)
            else:
                return 'NACK'

        except Exception as ex:
            self.exception_handler(ex)

    def i2c_write(self, address:int=0x70, commandcode:int=0x04, writesize:int=0, writedata=[0x00]):
        '''
        Wrapper for SAA Write Byte Function, explicitly states which overload to use in Fusion API
        Args:
            (uint8) dev_addr = PMBus Slave Address (0-127) - b'\x7F'
            (uint8) cmd_addr = PMBus CMD Address (0-255) - b'\xFF'
            (Int32) dataLen = Data Byte length - 0
            (uint8) data = Data Byte to Write (0-255) - b'\xFF'

        Returns:
            (uint8) Data Byte if successful
            NACK otherwise
        '''
        try:
            returnvalue = self.device.I2C_Write(Byte(address), Byte(commandcode), Int32(writesize), Array[Byte](array.array('i', writedata)))
            self.status = 0

        except Exception as ex:
            self.status = 1
            self.exception_handler(ex)

    def i2c_read(self, address:int=0x70, commandcode:int=0x04, noofbytestoread:int=0):
        '''
        Wrapper for SAA Write Byte Function, explicitly states which overload to use in Fusion API
        Args:
            (uint8) dev_addr = PMBus Slave Address (0-127) - b'\x7F'
            (uint8) cmd_addr = PMBus CMD Address (0-255) - b'\xFF'
            (Int32) dataLen = Data Byte length - 0
            (uint8) data = Data Bytes to read (0-255)

        Returns:
            (uint8) return Data Bytes if successfully read
        '''
        try:
            returnvalue = self.device.I2C_Read(Byte(address), Byte(commandcode), Int32(noofbytestoread))

            returnvalue = returnvalue.Data.Hex[2:]
            b = []
            for i in range(0, len(returnvalue), 2):
                b.append(int(returnvalue[i:i + 2], base=16))
            returnvalue = b
            self.status = 0
            return returnvalue

        except Exception as ex:
            self.status = 1

            # return value added as list of zeros to handle the exception in case of device no present
            returnvalue = [0 for i in range(0, noofbytestoread)]
            return returnvalue

            self.exception_handler(ex)

    def gpio_read_write(self, readmask:int=0x00, writedata:int=0x04):
        '''
        Wrapper for SAA Write Byte Function, explicitly states which overload to use in Fusion API
        Args:
            (Int32) readmask = Reads(1) and/or writes(0) a GPIO. The readMask determines whether a given bit will be read or written.
                               If a bit in readMask is 1, then the corresponding GPIO will be read and the bit result placed in readData.
                               If it is 0, the corresponding bit will be written. The bit to write will be taken from writeData.
                               There are easier to use versions of this that do not use byte bitmasks.
            (uint8) writedata = Data Byte to Write (0-255) - b'\xFF'

        Returns:
            (uint8) return Data Bytes if successfully read
        '''
        try:
            returnvalue = self.device.GPIO_Read_Write(Byte(readmask), Byte(writedata))

            returnvalue = returnvalue.Data.Hex
            self.status = returnvalue
            return returnvalue

        except Exception as ex:
                self.exception_handler(ex)

    def set_control(self, control_line_number:int=1, control_on:bool=False):
        """ Sets the CONTROL line specified, numbered 1 to 5. Leaves other lines alone. Returns status of the change.
            Use 1 for CONTROL line 1, 2 for CONTROL line 2, ..., 5 for CONTROL line 5.
        """
        try:
            self.device.Set_Control(Int32(control_line_number), Boolean(control_on))

        except Exception as ex:
            self.exception_handler(ex)

    def get_control(self, control_line_number:int=1):
        """ Gets the value of the specified control line. control_line_number should be 1 to 5. Returns null on read error.
            Fires ControlLineUpdated when the value read differs from what was previously read or on first read.
            Use 1 for CONTROL line 1, 2 for CONTROL line 2, ..., 5 for CONTROL line 5.
        """
        try:
            returnvalue = self.device.Get_Control(Int32(control_line_number))

            return returnvalue

        except Exception as ex:
            self.exception_handler(ex)


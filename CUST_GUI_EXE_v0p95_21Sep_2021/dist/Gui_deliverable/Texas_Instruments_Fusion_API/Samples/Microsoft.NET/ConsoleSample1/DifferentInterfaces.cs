using System;
using System.Collections.Generic;
using System.Text;
using TIDP.PMBus;
using TIDP.PMBus.Standard.Commands;
using TIDP.PMBus.Parts.UCD92XX;
using TIDP.PMBus.Parts.Generic11;
using TIDP.SAA;
using TIDP;
using TIDP.PMBus.Parts.UCD3100ISO1;

namespace ConsoleSample1
{
    /// <summary>
    /// was originally a 92xx sample but was quickly converted to UCD3138 device without testing 
    /// so may not be completely applicable.
    /// </summary>
    partial class ConsoleSample1
    {
        static void DifferentInterfaces()
        {
            try
            {
                if (PMBusDevice.Discover() == 0)
                    throw new Exception("no Texas Instruments devices found on bus");

                // Get reference to our two UCD9240s that should be on the bus
                var ucd3138_1 = Find_UCD3138(88);
                var ucd3138_2 = Find_UCD3138(89);

                // Turn on exception mode: errors in most PMBus/SAA transactions will
                // cause the program to exit, thus simplifying error checking
                PMBusDevice.Exceptions_On_SAA_Error = true;


                // Change setpoint on two rails
                ucd3138_1.Commands.VOUT_COMMAND(0).Write(1.1); // Rail #1
                ucd3138_1.Commands.VOUT_COMMAND(1).Write(2.1); // Rail #2

                // Start conversion on all rails by doing "the right thing" (set OPERATION and/or CONTROL)
                ucd3138_1.Start_Conversion();

                // Print out output voltage reading (many ways to do this, and this lends itself to creating
                // custom functions)
                ucd3138_1.Commands.READ_VOUT(0).Refresh();
                ucd3138_1.Commands.READ_VOUT(1).Refresh();
                ConsoleApp.WriteLine("READ_VOUT on rail #1 is now {}", ucd3138_1.Commands.READ_VOUT(0).Latest_Formatted_Plus_Encoded);
                ConsoleApp.WriteLine("READ_VOUT on rail #2 is now {}", ucd3138_1.Commands.READ_VOUT(1).Latest_Formatted_Plus_Encoded);

                // Create a generic device for our non-TI controller at address 28; we still have access to
                // commands via high-level API
                var other_device = new Generic11PMBusDevice(28);

                // Immedate does a read and returns what was read; this is also
                // available via various Latest* properties, which was used in
                // READ_VOUT example above
                double? vout = other_device.Commands.READ_VOUT().Immediate;
                double? iout = other_device.Commands.READ_IOUT().Immediate;
                ConsoleApp.WriteLine("Device 28's Vout is {:N3} V, Iout is {:N3} V, and Power is {:N3} W",
                    vout, iout, vout * iout);

                // This is the low-level interface into the USB adapter (aka SAA)
                var saa = SMBusAdapter.Adapters[0];

                // Perform lower-level SMBus calls with a 3rd device that is not a PMBus device but does
                // support SMBus
                //
                // Arguments are address, comnmand code, block
                saa.Write_Block(32, 0x9C, "0x44414C4C4153");

                // Same thing as above, but passing the block as an array of bytes
                byte[] block = new byte[] { 0x44, 0x41, 0x4C, 0x41, 0x53 };
                saa.Write_Block(32, 0x9C, block);

                // Now, do the same thing but through even lower level I2C interface;
                // NOTE: do not add PEC byte; the SAA adapter adds this if PEC mode
                // is enabled at the SAA level
                saa.I2C_Write_Generic("0xFC9C0644414C4C4153"); // could also pass a byte array
            }
            catch (Exception ex)
            {
                ConsoleApp.WriteLine("fatal script error: {}", ex.Message);
            }
        }

        /// <summary>
        /// Look for a UCD92XX device amoung previously discovered devices. 
        /// Throws exception on error.
        /// </summary>
        static UCD3100ISO1PMBusDevice Find_UCD3138(int address)
        {
            var device = PMBusDevice.Find(address);
            if (device == null)
                throw new TIException("there is no Texas Instruments device at address {} as expected", address);
            var device_as_ucd3138 = device as UCD3100ISO1PMBusDevice;
            if (device_as_ucd3138 == null)
                throw new TIException("found a device at address {}, but it was a {}, not the expected UCD3138",
                    address, device.Part_ID);
            return device_as_ucd3138;
        }

    }
}

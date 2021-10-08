using System;
using System.Collections.Generic;
using System.Text;
using TIDP.PMBus.MemoryMaps;
using TIDP.PMBus.Parts.UCD3000;


namespace ConsoleSample1
{
    /// <summary>
    /// This example shows how to peek/poke low-level IC registers from ROM or 
    /// program mode. All API calls throw an exception on error, so there are
    /// no status return values to check.
    /// </summary>
    public static class UCD31XX64Registers
    {
        public static void Test()
        {
            // Automatic bootstrap mode: finds SAA adapter and looks for ROM then program
            var api = new UCD31XX64R1RegistersEasyMemoryMap();

            // Listen for low-level driver read/write events
            api.Memory_Driver.ReadMemory += new EventHandler<TIDP.Memory.ReadMemoryEventArgs>(Memory_Driver_ReadMemory);
            api.Memory_Driver.WroteMemory += new EventHandler<TIDP.Memory.WroteMemoryEventArgs>(Memory_Driver_WroteMemory);

            // The "ToString()" method of each memory node prints out the read/write status
            // UARTTXBUF below is equivalent to UARTTXBUF.ToString(). At this point no
            // read has been done. "?" is used to represent a "null" byte: not read
            // or written yet.
            ConsoleApp.WriteLine("Inspecting API state of Uart0Regs.UARTTXBUF ...");
            ConsoleApp.WriteLine(api.Variables.Uart0Regs.UARTTXBUF);

            // Read_Flash() reads memory for a node and all child nodes (memory locations).
            // For example, api.Variables.Uart0Regs.Read_Flash() will read 56 bytes starting
            // at address 0xFFF7D800.
            ConsoleApp.WriteLine();
            ConsoleApp.WriteLine("Calling Uart0Regs.UARTTXBUF.Read() ...");
            api.Variables.Uart0Regs.UARTTXBUF.Read();

            // Again, thus dumps the status of a node
            ConsoleApp.WriteLine();
            ConsoleApp.WriteLine("Inspecting API state of Uart0Regs.UARTTXBUF ...");
            ConsoleApp.WriteLine(api.Variables.Uart0Regs.UARTTXBUF);            
            
            // We are now setting the "to write" property of a node. Unions
            // are fully supported, and you can set values from any one
            // union vector and the change will show up in the other union
            // representations of the memory: these .NET nodes are wrappers
            // around a single "virtual" view of the device memory. 
            //
            // Setting .Value just updates a "to write" area in this virtual
            // memory.
            ConsoleApp.WriteLine();
            ConsoleApp.WriteLine("Setting Uart0Regs.UARTTXBUF.bit \"to write\" values ...");
            api.Variables.Uart0Regs.UARTTXBUF.bit.rsvd0.Value = 0xAAAAAA;
            api.Variables.Uart0Regs.UARTTXBUF.bit.TXDAT.Value = 0xFF;

            // We could have done this instead, but above is easier
            // ConsoleApp.WriteLine("Setting Uart0Regs.UARTTXBUF.all ...");
            // api.Variables.Uart0Regs.UARTTXBUF.all.Value = 0xAAAAAAFF;

            // NOTE: silly example; rsvd0 bits are just ignored on write

            // Note when we get the "Value" property for a node it returns
            // the pending write data, if one exists. Otherwise it returns
            // whatever was last read from the device.

            ConsoleApp.WriteLine();
            ConsoleApp.WriteLine("Inspecting API state of Uart0Regs.UARTTXBUF ...");
            ConsoleApp.WriteLine("Uart0Regs.UARTTXBUF.bit.rsvd0.Value = 0x{:X}", api.Variables.Uart0Regs.UARTTXBUF.bit.rsvd0.Value);
            ConsoleApp.WriteLine("Uart0Regs.UARTTXBUF.bit.TXDAT.Value = 0x{:X}", api.Variables.Uart0Regs.UARTTXBUF.bit.TXDAT.Value);
            ConsoleApp.WriteLine("Uart0Regs.UARTTXBUF.all.Value = 0x{:X}", api.Variables.Uart0Regs.UARTTXBUF.all.Value);
            ConsoleApp.WriteLine(api.Variables.Uart0Regs.UARTTXBUF);
            ConsoleApp.WriteLine(api.Variables.Uart0Regs.UARTTXBUF.bit);
            ConsoleApp.WriteLine(api.Variables.Uart0Regs.UARTTXBUF.bit.rsvd0);
            ConsoleApp.WriteLine(api.Variables.Uart0Regs.UARTTXBUF.bit.TXDAT);

            // All this showing different parts of the union/struct above is overkill in everyday
            // use; this is just to show you that the .NET API works similar to "C" code 
            // version for accessing the data structures.

            // This writes the "dirty" bytes out. Every byte that is written is read back,
            // and after this Value will contain what was read back. If there was an error,
            // an exception would be thrown and unwritten bytes would continue to be 
            // marked dirty.
            ConsoleApp.WriteLine();
            ConsoleApp.WriteLine("Writing dirty bytes (this also does a refresh of addresses written) ...");
            api.Write_Pending();

            ConsoleApp.WriteLine();
            ConsoleApp.WriteLine("Inspecting API state of Uart0Regs.UARTTXBUF ...");
            ConsoleApp.WriteLine(api.Variables.Uart0Regs.UARTTXBUF);
            ConsoleApp.WriteLine("Uart0Regs.UARTTXBUF.bit.rsvd0.Value = 0x{:X}", api.Variables.Uart0Regs.UARTTXBUF.bit.rsvd0.Value);
            ConsoleApp.WriteLine("Uart0Regs.UARTTXBUF.bit.TXDAT.Value = 0x{:X}", api.Variables.Uart0Regs.UARTTXBUF.bit.TXDAT.Value);

            // Shows access to array-based variables
            ConsoleApp.WriteLine();
            ConsoleApp.WriteLine("Reading AdcRegs.ADCRESULT[] ...");
            api.Variables.AdcRegs.ADCRESULT.Read();
            for (int i = 0; i < api.Variables.AdcRegs.ADCRESULT.Length; i++)
            {
                ConsoleApp.WriteLine("ADCRESULT[{}] = 0x{:X}", i,
                    api.Variables.AdcRegs.ADCRESULT[i].bit.RESULT.Value);
            }


            //
            // Shows how to export/import memory settings file "save files". This is an API
            // version of the same functionality available in the GUI.
            //

            // Export does not force a read; it reflects the current state of the memory cache.
            // So we force a read because above we were just working with sub-registers in
            // Uart0Regs
            ConsoleApp.WriteLine();
            ConsoleApp.WriteLine("Reading memory Uart0Regs ...");
            api.Variables.Uart0Regs.Read();

            ConsoleApp.WriteLine();
            ConsoleApp.WriteLine("Inspecting API state of Uart0Regs.UARTTXBUF ...");
            ConsoleApp.WriteLine(api.Variables.Uart0Regs.UARTTXBUF);

            // Export to file
            ConsoleApp.WriteLine();
            ConsoleApp.WriteLine("Exporting Uart0Regs ...");
            api.Variables.Uart0Regs.Export("Uart0Regs.xml");

            // Change something inside of Uart0Regs
            ConsoleApp.WriteLine();
            ConsoleApp.WriteLine("Changing TXDAT ...");
            api.Variables.Uart0Regs.UARTTXBUF.bit.TXDAT.Value = 0xBC;
            api.Write_Pending();

            // Import our saved memory, wiping out above change
            ConsoleApp.WriteLine();
            ConsoleApp.WriteLine("Importing Uart0Regs ...");
            api.Import("Uart0Regs.xml");

        }

        static void Memory_Driver_ReadMemory(object sender, TIDP.Memory.ReadMemoryEventArgs e)
        {
            ConsoleApp.WriteLine(e.Message);
        }

        static void Memory_Driver_WroteMemory(object sender, TIDP.Memory.WroteMemoryEventArgs e)
        {
            ConsoleApp.WriteLine(e.Message);
        }
    }
}

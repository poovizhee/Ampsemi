using System;
using System.Collections.Generic;
using System.Text;
using TIDP.PMBus;
using TIDP.PMBus.Parts.UCD3000;
using TIDP.SAA;
using TIDP.Memory;

namespace ConsoleSample1
{
    public static class DynamicMemoryMap
    {
        public static void Test()
        {
            // Find adapter and device
            if (SMBusAdapter.Discover() == 0)
                throw new Exception("no SAA found");
            if (PMBusDevice.Discover() == 0)
                throw new Exception("no device found on bus");

            // Get our device that was on the bus
            var device = (UCD3000PMBusDevice)PMBusDevice.Devices[0];

            // Create memory driver, which does actual peek/poke
            var mem_driver = new UCD3000ProgramMemoryDriver(device);

            // Create memory cache
            var memory = new DeviceMemory(mem_driver);

            // Create debugger API
            var opts = new UCD3000MapConstructOptions(ICFamilyID.UCD3000, 
                @"C:\Users\a0271759.ENT\Desktop\TEMP\Memory Debugger\UCD9246-64_5.13.0.12409");
            opts.Memory = memory;
            opts.Small_Enums = true;
            var api = new UCD3000MemoryMap(opts);

            // Listen for low-level driver read/write events
            mem_driver.ReadMemory += new EventHandler<TIDP.Memory.ReadMemoryEventArgs>(Memory_Driver_ReadMemory);
            mem_driver.WroteMemory += new EventHandler<TIDP.Memory.WroteMemoryEventArgs>(Memory_Driver_WroteMemory);

            // The "ToString()" method of each memory node prints out the read/write status
            // UARTTXBUF below is equivalent to UARTTXBUF.ToString(). At this point no
            // read has been done. "?" is used to represent a "null" byte: not read
            // or written yet.
            ConsoleApp.WriteLine("Inspecting API state of Uart1Regs.UARTTXBUF ...");
            ConsoleApp.WriteLine(api["Uart1Regs.UARTTXBUF"].ToString());

            // Read_Flash() reads memory for a node and all child nodes (memory locations).
            // For example, api["Uart1Regs.Read_Flash() will read 56 bytes starting
            // at address 0xFFF7D800.
            ConsoleApp.WriteLine();
            ConsoleApp.WriteLine("Calling Uart1Regs.UARTTXBUF.Read() ...");
            api["Uart1Regs.UARTTXBUF"].Read();

            // This dumps the status of a node
            ConsoleApp.WriteLine();
            ConsoleApp.WriteLine("Inspecting API state of Uart1Regs.UARTTXBUF ...");
            ConsoleApp.WriteLine(api["Uart1Regs.UARTTXBUF"].ToString());

            ConsoleApp.WriteLine();
            ConsoleApp.WriteLine("Dumping Uart1Regs.UARTTXBUF ...");
            ConsoleApp.WriteLine(api["Uart1Regs.UARTTXBUF"].Dump_Flat());

            // We are now setting the "to write" property of a node. Unions
            // are fully supported, and you can set values from any one
            // union vector and the change will show up in the other union
            // representations of the memory: these .NET nodes are wrappers
            // around a single "virtual" view of the device memory. 
            //
            // Calling Set_Memory only updates a "to write" area in this virtual
            // memory. It does not perform an actual write.
            ConsoleApp.WriteLine();
            ConsoleApp.WriteLine("Setting Uart1Regs.UARTTXBUF.bit \"to write\" values ...");
            api["Uart1Regs.UARTTXBUF.bit.rsvd0"].Set_Memory_UInt32(0xAAAAAA);
            api["Uart1Regs.UARTTXBUF.bit.TXDAT"].Set_Memory_UInt32(0xFF);
            api["Dpwm1Regs.DPWMCLFCTRL.bit.CLF_ENA"].Set_Memory_UInt32(1);

            // NOTE: silly example; rsvd0 bits are just ignored on write

            // Note Get_Memory*() returns the pending write data, if one exists. 
            // Otherwise it returns whatever was last read from the device.

            ConsoleApp.WriteLine();
            ConsoleApp.WriteLine("Inspecting API state of Uart1Regs.UARTTXBUF ...");
            ConsoleApp.WriteLine("Uart1Regs.UARTTXBUF.bit.rsvd0.Value = 0x{:X}", api["Uart1Regs.UARTTXBUF.bit.rsvd0"].Get_Memory_UInt32());
            ConsoleApp.WriteLine("Uart1Regs.UARTTXBUF.bit.TXDAT.Value = 0x{:X}", api["Uart1Regs.UARTTXBUF.bit.TXDAT"].Get_Memory_UInt32());
            ConsoleApp.WriteLine("Uart1Regs.UARTTXBUF.all.Value = 0x{:X}", api["Uart1Regs.UARTTXBUF.all"].Get_Memory_UInt32());
            ConsoleApp.WriteLine(api["Uart1Regs.UARTTXBUF"].ToString());
            ConsoleApp.WriteLine(api["Uart1Regs.UARTTXBUF.bit"].ToString());
            ConsoleApp.WriteLine(api["Uart1Regs.UARTTXBUF.bit.rsvd0"].ToString());
            ConsoleApp.WriteLine(api["Uart1Regs.UARTTXBUF.bit.TXDAT"].ToString());

            ConsoleApp.WriteLine();
            ConsoleApp.WriteLine("The following will show the pendidng write ...");
            ConsoleApp.WriteLine(api["Uart1Regs.UARTTXBUF"].Dump_Flat());

            ConsoleApp.WriteLine();
            ConsoleApp.WriteLine("Can also dump in tree mode  ...");
            ConsoleApp.WriteLine(api["Uart1Regs.UARTTXBUF"].Dump_Tree());

            // All this showing different parts of the union/struct above is overkill in everyday
            // use; this is just to show you that the .NET API works similar to "C" code 
            // version for accessing the data structures.

            // This writes the "dirty" bytes out. Every byte that is written is read back,
            // and after this Value will contain what was read back. If there was an error,
            // an exception would be thrown and unwritten bytes would continue to be 
            // marked dirty.
            ConsoleApp.WriteLine();
            ConsoleApp.WriteLine("Writing dirty bytes (this also does a refresh of addresses written) ...");
            api.Write(WriteMode.ToWriteSetAndDiffers, true);

            ConsoleApp.WriteLine();
            ConsoleApp.WriteLine("Inspecting API state of Uart1Regs.UARTTXBUF ...");
            ConsoleApp.WriteLine(api["Uart1Regs.UARTTXBUF"].ToString());

            ConsoleApp.WriteLine();
            ConsoleApp.WriteLine("Dumping Uart1Regs.UARTTXBUF.bit ...");
            ConsoleApp.WriteLine(api["Uart1Regs.UARTTXBUF.bit"].Dump_Flat());

            //
            // Shows how to export/import memory settings file "save files". This is an API
            // version of the same functionality available in the GUI.
            //

            // Export does not force a read; it reflects the current state of the memory cache.
            // So we force a read because above we were just working with sub-registers in
            // Uart1Regs
            ConsoleApp.WriteLine();
            ConsoleApp.WriteLine("Reading memory Uart1Regs ...");
            api["Uart1Regs"].Read();

            ConsoleApp.WriteLine();
            ConsoleApp.WriteLine("Inspecting API state of Uart1Regs.UARTTXBUF ...");
            ConsoleApp.WriteLine(api["Uart1Regs.UARTTXBUF"].ToString());

            // Export to file
            ConsoleApp.WriteLine();
            ConsoleApp.WriteLine("Exporting Uart1Regs ...");
            api["Uart1Regs"].Export("Uart1Regs.xml");

            // Change something inside of Uart1Regs
            ConsoleApp.WriteLine();
            ConsoleApp.WriteLine("Changing TXDAT ...");
            api["Uart1Regs.UARTTXBUF.bit.TXDAT"].Set_Memory_UInt32(0xBC);
            api.Write(WriteMode.ToWriteSetAndDiffers, true);

            // Import our saved memory, wiping out above change
            ConsoleApp.WriteLine();
            ConsoleApp.WriteLine("Importing Uart1Regs ...");
            api.Import("Uart1Regs.xml");
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

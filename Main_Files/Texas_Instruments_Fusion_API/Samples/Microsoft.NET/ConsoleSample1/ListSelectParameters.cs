using System;
using System.Collections.Generic;
using System.Text;
using TIDP.PMBus;
using TIDP.PMBus.Commands;
using TIDP;

namespace ConsoleSample1
{
    /// <summary>
    /// Print out a small group of parameters for all rails to the console.
    /// </summary>
    public static class ListSelectParameters
    {
        /// <summary>
        /// This version loops over the Pages collection. Pages contains
        /// a list of the configured rails for a device. It is even available
        /// when a device does not support more than one rail.
        /// </summary>
        public static void Via_Pages_Collection()
        {
            foreach (var page in MyApp.Device.Pages)
            {
                ConsoleApp.WriteLine("VOUT_COMMAND #{}: {}", 
                    page.Number, MyApp.Device.Commands.VOUT_COMMAND(page.Index).Latest_Formatted);
                ConsoleApp.WriteLine("TON_DELAY #{}:    {}",
                    page.Number, MyApp.Device.Commands.TON_DELAY(page.Index).Latest_Formatted);
                ConsoleApp.WriteLine();
            }
        }

        public static void Via_For_Classic_Loop()
        {
            for (int page_i = 0; page_i < MyApp.Device.Num_Outputs; page_i++)
            {
                ConsoleApp.WriteLine("VOUT_COMMAND #{}: {}",
                    page_i+1, MyApp.Device.Commands.VOUT_COMMAND(page_i).Latest_Formatted);
                ConsoleApp.WriteLine("TON_DELAY #{}:    {}",
                    page_i+1, MyApp.Device.Commands.TON_DELAY(page_i).Latest_Formatted);
                ConsoleApp.WriteLine();
            }
        }
    }
}

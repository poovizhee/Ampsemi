using System;
using System.Collections.Generic;
using System.Text;
using TIDP.PMBus;

using TIDP.SAA;

namespace ConsoleSample1
{
    public static class SAA
    {
        /// <summary>
        /// Provide easy access to the SAA object for our device. Because the API supports multiple 
        /// USB adapters, we want to ensure we are using the adapter associted with our target device.
        /// </summary>
        private static SMBusAdapter Adapter
        {
            get { return MyApp.Device.Adapter; }
        }

        public static void Change_Control_Line()
        {
            // Get current control line setting; exception mode is on in these samples,
            // so we can ignore return result
            var result = Adapter.Get_Control();
            ConsoleApp.WriteLine("CONTROL #1 is currently {}", result.Level);

            // Change to other state
            var new_level = (result.Level == LogicLevel.High) ? LogicLevel.Low : LogicLevel.High;
            ConsoleApp.WriteLine("Changing CONTROL #1 to {}", new_level);
            Adapter.Set_Control(new_level);

            // Print control setting
            result = Adapter.Get_Control();
            ConsoleApp.WriteLine("CONTROL #1 is now {}", result.Level);
        }
    }
}

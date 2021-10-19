using System;
using System.Collections.Generic;
using System.Text;
using TIDP.PMBus;

namespace ConsoleSample1
{
    public static class ComputePower
    {
        public static void Run()
        {
            double vout = MyApp.Commands.READ_VOUT(0).Latest.Value;
            double iout = MyApp.Commands.READ_IOUT(0).Latest.Value;
            ConsoleApp.WriteLine("Vout  = {:n3} V\nIout  = {:n3} A\nPower = {:n3} W",
                 vout, iout, vout * iout);
        }
    }
}

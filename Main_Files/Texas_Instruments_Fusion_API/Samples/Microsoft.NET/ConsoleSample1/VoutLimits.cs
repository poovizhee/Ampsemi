using System;
using System.Collections.Generic;
using System.Threading;
using System.Text;
using TIDP.PMBus;
using TIDP.PMBus.Standard.Commands;


namespace ConsoleSample1
{
    /// <summary>
    /// Increase voltage from VOUT_COMMAND to VOUT_OV_FAULT_LIMIT + 20% and report on
    /// status registers and vout/iout readings for each voltage change. You could get
    /// much fancier here, and verify that the trips occur within X% of the limits, etc.
    /// </summary>
    public static class VoutLimits
    {
        /// <summary>
        /// Pass page_i=0xFF if your device is not PAGEd.
        /// </summary>
        /// <param name="page_i"></param>
        public static void Run(int page_i)
        {
            // You can get a reference -- like a pointer -- to a command object; you
            // are referencing the command itself, not the data. So you could use
            // this technique to provide prettier/easier access to a command within
            // a script
            var vout_cmd = MyApp.Commands.VOUT_COMMAND(page_i);
            var vout_ov_warn_limit_cmd = MyApp.Commands.VOUT_OV_WARN_LIMIT(page_i);
            var vout_ov_fault_limit_cmd = MyApp.Commands.VOUT_OV_FAULT_LIMIT(page_i);
            var status_word_cmd = MyApp.Commands.STATUS_WORD();
            var read_vout_cmd = MyApp.Commands.READ_VOUT(page_i);
            var status_vout_cmd = MyApp.Commands.STATUS_VOUT(page_i);

            // Take a snapshot of VOUT_COMMAND: we will restore it to it's original value
            // when we exit this test; the finally {} block always runs, even if an 
            // exception is thrown
            vout_cmd.Take_Snapshot();

            try
            {
                // Display current OV limits
                ConsoleApp.WriteLine("VOUT_OV_WARN_LIMIT:  {}", vout_ov_warn_limit_cmd.Latest_Formatted_Plus_Encoded);
                ConsoleApp.WriteLine("VOUT_OV_FAULT_LIMIT: {}", vout_ov_fault_limit_cmd.Latest_Formatted_Plus_Encoded);

                // Make sure power is off and faults are cleared before 
                // starting test. Start_Conversion() is a PMBusDevice helper 
                // function looks at ON_OFF_CONFIG to determine the appropriate 
                // method of turning on the device (CONTROL or OPERATION).
                MyApp.Device.Stop_Conversion(page_i);
                MyApp.Commands.CLEAR_FAULTS().Execute();
                ConsoleApp.WriteLine("OPERATION:           {}", MyApp.Commands.OPERATION(page_i).Latest_Formatted_Plus_Encoded);
                ConsoleApp.WriteLine("ON_OFF_CONFIG:       {}", MyApp.Commands.ON_OFF_CONFIG(page_i).Latest_Formatted_Plus_Encoded);
                ConsoleApp.WriteLine();

                double vout_start = vout_cmd.Latest.Value;
                double vout_end = MyApp.Commands.VOUT_OV_FAULT_LIMIT(page_i).Latest.Value * 1.2;

                // Increase vout from VOUT_COMMAND to VOUT_OV_FAULT_LIMIT + 20% stepping by 0.01V
                for (double vout = vout_start; vout <= vout_end; vout += 0.01)
                {
                    // Write VOUT_COMMAND
                    bool write_status = vout_cmd.Write(vout);

                    // First time through give unit time to power up
                    if (vout == vout_start)
                    {
                        MyApp.Device.Start_Conversion(page_i);
                        Thread.Sleep(15); // 15 msec pause on PC

                        // Verify READ_VOUT is within += 0.1V of VOUT_COMMAND. Exception
                        // thrown if not.
                        MyApp.Device.Verify_Converting(page_i, 0.1);
                    }

                    // Refresh read values
                    read_vout_cmd.Refresh();
                    status_word_cmd.Refresh();
                    status_vout_cmd.Refresh();

                    ConsoleApp.WriteLine("{}\t{}\t{}\t{}", vout_cmd.Latest_Formatted,
                        read_vout_cmd.Latest_Formatted, 
                        status_word_cmd.Latest_Formatted_Plus_Encoded,
                        status_vout_cmd.Latest_Formatted_Plus_Encoded);
                }

            }
            finally
            {
                // Restore pre-test VOUT_COMMAND
                vout_cmd.Restore_Snapshot();
            }
        }

    }
}

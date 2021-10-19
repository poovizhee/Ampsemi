using System;
using System.Collections.Generic;
using System.Text;
using TIDP.PMBus;
using TIDP;

namespace ConsoleSample1
{
    /// <summary>
    /// Shows how to output some arbitrary device data to a tab or CSV file or
    /// to the console.
    /// </summary>
    public static class DeviceSummary
    {
        /// <summary>
        /// If output_filename is "-", we output to the Console. If it
        /// is not, we save to a file.
        /// </summary>
        public static void Run(string output_filename)
        {
            ConsoleApp.WriteLine("Number of Rails: {}", MyApp.Device.Num_Outputs);

            // LineOutput is a handy class for creating tab or comma seperated
            // output, either to the console or saved to a file
            var output = new LineOutput(output_filename, LineOutputFormat.CSV);

            // Create header
            output.Write_Params("Rail", "VOUT_COMMAND", "READ_VOUT", "READ_IOUT");

            // Loops through *configured* rails
            for (int page_i = 0; page_i < MyApp.Device.Num_Outputs; page_i++)
            {
                output.Write_Params(
                    page_i + 1,
                    MyApp.Device.Commands.VOUT_COMMAND(page_i).Latest,
                    MyApp.Device.Commands.READ_VOUT(page_i).Latest,
                    MyApp.Device.Commands.READ_IOUT(page_i).Latest
                    );

            }

            output.Close();
        }
    }
}

using System;
using System.Collections.Generic;
using System.Text;
using TIDP.PMBus;
using TIDP.PMBus.Commands;
using TIDP;

namespace ConsoleSample1
{
    /// <summary>
    /// Print out all parameters and values to the console.
    /// </summary>
    public static class ListAllParameters
    {
        public static void Run()
        {
            // Header
            ConsoleApp.WriteLine("ID\tCode\tRail\tRead Only?\tStatus\tDecoded\tDecoded Formated\tEncoded");

            // ParameterBase is the base class of a PMBus parameter. Unlike a command-specific
            // sub-class like Linear11ReadWriteParameter, it does not provide a "strongly typed"
            // interface into the data it mirrors. But you can access it's data via the o*
            // properties and methods, such as oLatest
            //
            // Parameters list is sorted by alphabetical command ID
            foreach (ParameterBase param in MyApp.Commands.Parameters)
            {
                // Certain commands, such as one emulating the CONTROL pin, are so-called
                // "meta-commands." On certain devices these are used to encapsulate a
                // series of commands used to read/write a parameter. For example, on the
                // UCD9112 a series of commands are used to read/write a coefficient table.
                // We'll skip these.
                if (param.Is_Meta_Command)
                    continue;

                // Likewise skip any low-level parameters that would normally be hidden from
                // the user
                if (!param.Show_To_User || !param.Phase_Available() || param.Is_Write_Only)
                    continue;

                // Force a refresh; results are cached in the parameter object
                param.Refresh();

                // Normally you would be doing things like "Latest" or
                // "Latest_Encoded" -- if the parameter has never been read or the
                // last read failed, we will try again. But for ultimate performance
                // you can do a refesh like above and then just access the latest
                // "no immediate" results
                //
                // The o* properties and methods give you generic, object "untyped" 
                // access to certain properties and functions. So oLatest returns
                // an object and is available through the ParameterBase base class
                // that all parameter objects inherit from. But Latest is strongly 
                // typed and is therefore only available through lower level 
                // concrete classes such as those that define a "voltage read" command
                // such as READ_VIN.
                ConsoleApp.WriteLine(StringUtils.Join("\t", param.ID, param.Code, param.Page.Number,
                    (param.Is_Read_Only_Parameter) ? "Yes" : "No",
                    PMBusUtils.ACK_NACK(param.Last_Status), // "ACK" or "NACK"
                    param.oLatest_No_Immediate, param.Latest_No_Immediate_Formatted, 
                    param.oLatest_Encoded_No_Immediate));
            }
        }
    }
}

using System;
using System.Collections.Generic;
using System.Text;
using TIDP.PMBus;

using TIDP.PMBus.Standard.Commands;

namespace ConsoleSample1
{
    /// <summary>
    /// Shows how you could go crazy and work with a parameter like OPERATION
    /// via it's strongly type interface (OperationCommand). Or you could just
    /// write 
    /// </summary>
    public static class OnOff
    {
        /// <summary>
        /// Provide quick access to OPERATION.
        /// </summary>
        private static OperationReadWriteParameter OPERATION
        {
            get { return MyApp.Device.Commands.OPERATION(); }
        }

        public static void Run()
        {
            // Get a copy of the latest OPERATION value, since we will be adjusting it.
            // You only need to do this when modifying "Latest" values that return an 
            // object.
            OperationCommand op = OPERATION.Latest.Clone();

            // Turn on and explicitly set all operation segments
            op.Operation = OperationCommand.UnitOperation.On;
            op.Margin = OperationCommand.VoutMargin.High;
            op.Margin_Fault = OperationCommand.VoutMarginFaultMode.ActOnFault;
            ConsoleApp.WriteLine("Setting OPERATION to On/High/ActOnFault");
            OPERATION.Write(op);
            Print_Operation();

            // Turn off
            ConsoleApp.WriteLine("Setting OPERATION to ImmediateOff/High/ActOnFault");
            op.Operation = OperationCommand.UnitOperation.ImmediateOff;
            OPERATION.Write(op);
            Print_Operation();

            // Turn on via write of encoded value
            ConsoleApp.WriteLine("Setting OPERATION to 0x88");
            OPERATION.Write_Encoded(0x88);
            Print_Operation();

            // Turn off via write of encoded value: this might be easier for you
            // anyway
            ConsoleApp.WriteLine("Setting OPERATION to 0x00");
            OPERATION.Write_Encoded(0x00);
            Print_Operation();

            // Another way to turn the unit on or off: this leaves margin
            // as-is and just updates the operation segment
            ConsoleApp.WriteLine("Calling OPERATION.Write_New_Operation(true)");
            OPERATION.Write_New_Operation(true);
            Print_Operation();

            ConsoleApp.WriteLine("Calling OPERATION.Write_New_Operation(false)");
            OPERATION.Write_New_Operation(false);
            Print_Operation();

        }

        static void Print_Operation()
        {
            OPERATION.Refresh();
            ConsoleApp.WriteLine("OPERATION.Latest:");
            ConsoleApp.WriteLine("   Encoded:      {}", OPERATION.Latest_Encoded);
            ConsoleApp.WriteLine("   On:           {}", OPERATION.Latest.Is_On);
            ConsoleApp.WriteLine("   Margin:       {}", OPERATION.Latest.Margin);
            ConsoleApp.WriteLine("   Margin Fault: {}", OPERATION.Latest.Margin);
            ConsoleApp.WriteLine("");
        }
    }
}

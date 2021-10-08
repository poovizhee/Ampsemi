using System;
using TIDP.SAA;
using TIDP.PMBus;


namespace ConsoleSample1
{
    /// <summary>
    /// Run test against sample SMBusAdapter driver.
    /// </summary>
    public static class SampleDriverTest
    {
        public static void Run()
        {
            // Register our custom driver; this is the only special code
            // required outside the driver itself
            ConsoleApp.WriteLine("Registering custom adapter driver ...");
            SMBusAdapter.Register_Driver(new SampleDriverFactory());

            // Turn on API exception mode: any adapter driver error will throw a
            // detailed exception (vs. default of dealing with status codes)
            SMBusAdapter.Exceptions_On_Error = true;

            // Subscribe to adapter events to see log of everything done at that level
            // Note that PMBusLogger provides a simple way to capture these messages to
            // a log file, console, etc. It just wraps these events for you.
            SMBusAdapter.AdapterFound += new EventHandler<SMBusAdapter.AdapterFoundEventArgs>(SMBusAdapter_AdapterFound);
            SMBusAdapter.ControlLineUpdated += new EventHandler<SMBusAdapter.ControlLineUpdatedEventArgs>(SMBusAdapter_ControlLineUpdated);
            SMBusAdapter.RequestComplete += new EventHandler<SMBusAdapter.RequestCompleteEventArgs>(SMBusAdapter_RequestComplete);
            SMBusAdapter.SMBusAlertLineUpdated += new EventHandler<SMBusAdapter.SMBusAlertLineUpdatedEventArgs>(SMBusAdapter_SMBusAlertLineUpdated);

            // Note that currently no way is provided to unregister a driver.
            // This the API will still look for a USB-TO-GPIO

            // Use normal adapter discovery routines, even though we have custom adapter/driver
            ConsoleApp.WriteLine("");
            ConsoleApp.WriteLine("Searching for adapters ...");
            if (SMBusAdapter.Discover() == 0)
            {
                // Should be impossible to get here with our sample driver
                throw new Exception("no adapter found");
            }

            // Force DEVICE_CODE PMBus device discovery mode. Why? We have created
            // a sample adapter driver that emulates a TPS53819 at address 100d, 
            // and this device family uses DEVICE_CODE (0xFC, read word) command 
            // instead of DEVICE_ID (0xFC, read block) command for device
            // identification
            ConsoleApp.WriteLine("");
            ConsoleApp.WriteLine("Scanning for devices ...");
            var opts = new PMBusDevice.DiscoverOptions();
            opts.Scan_Mode = PMBusDevice.ScanMode.DeviceCode;
            if (PMBusDevice.Discover(opts) == 0)
            {
                // Should be impossible to get here with our sample driver
                throw new Exception("no device found");
            }

            // Get a reference to the device we found
            var device = PMBusDevice.Devices[0];
            ConsoleApp.WriteLine("");
            ConsoleApp.WriteLine("Found device: {}", device);

            //
            // Do some PMBus command API stuff
            //

            // Dump all command values
            ConsoleApp.WriteLine("");
            ConsoleApp.WriteLine("Dumping standard commands ...");
            foreach (var param in device.Commands.Parameters)
            {
                // Skip test mode commands
                if (param.Is_Test_Mode_Command || !param.Include_In_Export)
                    continue;
                ConsoleApp.WriteLine("{}: {}", param.ID_Display, param.Latest_Formatted_Plus_Encoded);
            }

            // Edit a few
            ConsoleApp.WriteLine("");
            ConsoleApp.WriteLine("Writing a few commands ...");
            ConsoleApp.WriteLine("Note that on this device the API reads back the commands");
            ConsoleApp.WriteLine("to validate write in addition to check for ACK.");
            //device.Commands.TPS53819_MFR_SPECIFIC_01().Write_Encoded("02");
            device.Commands.OPERATION().Write_Encoded("0x28");

            // Dump back out: force refresh from device via Immediate (normally no need to do this)
            //ConsoleApp.WriteLine("");
            //ConsoleApp.WriteLine("Dumping edited back ...");
            //device.Commands.TPS53819_MFR_SPECIFIC_01().Refresh();
            //ConsoleApp.WriteLine("DELAY_CONTROL [MFR01]: {}",
            //    device.Commands.TPS53819_MFR_SPECIFIC_01().Latest_Formatted_Plus_Encoded);
            //device.Commands.OPERATION().Refresh();
            ConsoleApp.WriteLine("DELAY_CONTROL [MFR01]: {}",
                device.Commands.OPERATION().Latest_Formatted_Plus_Encoded);

            // Dump signal lines
            ConsoleApp.WriteLine("");
            ConsoleApp.WriteLine("Dumping signal line state ...");
            ConsoleApp.WriteLine("Control #1 is {}", device.Adapter.Get_Control(1).Level);
            ConsoleApp.WriteLine("SMBALERT# is {}", device.Adapter.Get_SMBus_Alert().Level);

            // Above we got to the SMBusAdapter object via device.Adapter. Since the API
            // supports multiple adapters on a PC, each PMBusDevice has an Adapter property
            // giving you access to the adapter associated with a device. But below we just
            // use SMBusAdapter.Adapter to access adapter #1, which for most customers is
            // all they would have

            // Set control
            ConsoleApp.WriteLine("");
            ConsoleApp.WriteLine("Setting control #1 high ...");
            SMBusAdapter.Adapter.Set_Control(LogicLevel.High);
            ConsoleApp.WriteLine("Control #1 is {}", SMBusAdapter.Adapter.Get_Control(1).Level);
        }

        static void SMBusAdapter_SMBusAlertLineUpdated(object sender, SMBusAdapter.SMBusAlertLineUpdatedEventArgs e)
        {
            ConsoleApp.WriteLine("   SMBusAdapter: {}", e.Msg);
        }

        static void SMBusAdapter_RequestComplete(object sender, SMBusAdapter.RequestCompleteEventArgs e)
        {
            ConsoleApp.WriteLine("   SMBusAdapter: {}", e.Message);
        }

        static void SMBusAdapter_ControlLineUpdated(object sender, SMBusAdapter.ControlLineUpdatedEventArgs e)
        {
            ConsoleApp.WriteLine("   SMBusAdapter: {}", e.Msg);
        }

        static void SMBusAdapter_AdapterFound(object sender, SMBusAdapter.AdapterFoundEventArgs e)
        {
            ConsoleApp.WriteLine("   SMBusAdapter: Found {}", e.Adapter);
        }
    }
}
using System;
using System.Collections.Generic;
using System.Text;
using TIDP.PMBus;

using TIDP.SAA;
using TIDP;
using TIDP.PMBus.Parts.UCD92XX;
using TIDP.PMBus.Parts.UCD3000;

namespace ConsoleSample1
{
    public class MyApp
    {
        /// <summary>
        /// Easy way to access the 1st USB adapter found. The following is a static
        /// property. SMBusAdapter.Adapters is a static list (array) of devices found.
        /// </summary>
        public static SMBusAdapter Adapter
        {
            get { return SMBusAdapter.Adapters[0]; }
        }

        /// <summary>
        /// Easy way to access the 1st device found. The following is a static
        /// property. PMBusDevice.Devices is a static list (array) of devices found.
        /// </summary>
        public static PMBusDevice Device
        {
            get { return PMBusDevice.Devices[0]; }
        }

        /// <summary>
        /// For ROM-mode samples, the ROM that was found. Will be null for most
        /// samples that are working with program-mode devices.
        /// </summary>
        public static UCD3000RomApi Rom;

        /// <summary>
        /// Likewise, provide easy access to our device's commands
        /// </summary>
        public static PMBusCommands Commands
        {
            get { return Device.Commands; }
        }

        [STAThread()]
        static void Main(string[] args)
        {
            if (args.Length == 0)
            {
                ConsoleApp.CWarn("bad usage");
                Usage();
            }

            // Force "Exception" mode: any device/bus/adapter error will cause an exception
            // (error) to be "thrown" and program execution to halt. This greatly simplifies
            // error handling and means you generally do not have to check return status codes/etc.
            PMBusDevice.Exceptions_On_SAA_Error = true;

            // Trap exceptions (errors) and print them on the console. CDie will set an exit
            // code of 1, which in DOS/UN*X indicates that an error occured.
            try
            {
                Run_Test(args);
            }
            // If you want to catch exceptions, catch Exception; if you want and exception
            // to bubble up to the debugger, catch NeverException
            catch (NeverException ex)
            //catch (Exception ex)
            {
                ConsoleApp.CDie("fatal error: {}", MiscUtils.Concat_Exceptions(ex));
            }

            // Prompts the user to press return if running from the debugger ONLY
            ConsoleApp.Return_To_Continue();
        }

        private static void Run_Test(string[] args)
        {
            switch (args[0])
            {
                case "list-params":
                    Discover_Device();
                    ListAllParameters.Run();
                    break;

                case "list-select-params":
                    Discover_Device();
                    ListSelectParameters.Via_Pages_Collection();
                    break;

                case "vout-limits":
                    Discover_Device();
                    int page_i = (args.Length == 2) ? (int.Parse(args[1]) - 1) : 0xFF;
                    VoutLimits.Run(page_i);
                    break;

                case "on-off":
                    Discover_Device();
                    OnOff.Run();
                    break;

                case "compute-power":
                    Discover_Device();
                    ComputePower.Run();
                    break;
                
                case "import-project":
                    Discover_Device();
                    if (args.Length != 2)
                        ConsoleApp.CDie("missing project filename");
                    Importer.Import_Project(args[1]);
                    break;

                case "import-dflash":
                    Discover_Device();
                    if (args.Length != 2)
                        ConsoleApp.CDie("missing dflash image filename");
                    Importer.Import_Data_Flash(args[1]);
                    break;

                case "export-project":
                    if (args.Length != 2)
                        ConsoleApp.CDie("missing project filename");
                    Exporter.Export_Project(args[1]);
                    break;

                case "export-text":
                    Discover_Device();
                    if (args.Length != 2)
                        ConsoleApp.CDie("missing text filename");
                    Exporter.Export_Text(args[1]);
                    break;

                case "export-dflash":
                    Discover_Device();
                    if (args.Length != 2)
                        ConsoleApp.CDie("missing dflash image filename");
                    Exporter.Export_Project(args[1]);
                    break;

                case "firmware-update":
                    Discover_Device();
                    if (args.Length != 3)
                        ConsoleApp.CDie("missing firmware-file and/or firmware-version-in-file arguments");
                    FirmwareDownload.Download(args[1], args[2]);
                    break;

                case "firmware-download":
                    Discover_Device();
                    if (args.Length != 2)
                        ConsoleApp.CDie("missing firmware-file argument");
                    FirmwareDownload.Download(args[1], "");
                    break;

                case "control":
                    Discover_Device();
                    SAA.Change_Control_Line();
                    break;

               
                case "mfr-gui-headless1":
                    // Discovery handled by headless engine
                    ManufacturingGUIHeadless1.Run();
                    break;

                case "ucd30xx-registers":
                    UCD30XXRegisters.Test();
                    break;

                case "ucd31xx-registers":
                    UCD31XXRegisters.Test();
                    break;

                case "dynamic-memory-map":
                    DynamicMemoryMap.Test();
                    break;

                case "create-memory-map-wrapper-api":
                    CreateMemoryMapWrapperAPI.Create();
                    break;

                case "multi-device-project-import":
                    StandAloneMultiDeviceProjectImport.Run();
                    break;

                case "custom-adapter-driver":
                    SampleDriverTest.Run();
                    break;

                default:
                    ConsoleApp.CWarn("unknown sample '{}'", args[0]);
                    Usage();
                    break;
            }

        }

        // This should only ever be called once
        private static void Discover_Adapter()
        {
            if (SMBusAdapter.Discover() == 0)
                ConsoleApp.CDie("no USB serial adapter found");
            ConsoleApp.WriteLine("Adapter {} found", SMBusAdapter.Adapter);
        }

        // This should only ever be called once
        private static void Discover_Device()
        {
            Discover_Adapter();

            // Use this style for most devices supported by Fusion Digital Power Designer
            // Examples: UCD9240, UCD90120, UCD7231
            int num_devices = PMBusDevice.Discover();

            // Another way to call -- only scan the addresses listed; very fast
            // int num_devices = PMBusDevice.Discover(75, 126);

            // Use this style for select devices that do not support DEVICE_ID
            // Examples: TPS40400, TPS4100
            // int num_devices = PMBusUtils.Attach_And_Discover(PartID.TPS40400, true);

            if (num_devices == 0)
                ConsoleApp.CDie("no devices found on the bus (but adapter OK)");

            if (num_devices == 1)
                ConsoleApp.WriteLine("Found {}", Device);
            else
                ConsoleApp.WriteLine("Found {} devices; using {} for test", num_devices, Device);
        }

        private static void Discover_ROM()
        {
            Discover_Adapter();

            Rom = (UCD3000RomApi)RomApi.Create();

            if (Rom == null)
                ConsoleApp.CDie("no devices in ROM mode found on the bus (but adapter OK)");

            ConsoleApp.WriteLine("Found {}", Rom);
        }


        private static void Usage()
        {
            Console.Error.WriteLine(@"
Usage: ConsoleSample1 <sample> [ sample arguments ]
                
where <sample> is one of:

   list-params
      This shows you how to loop through all parameters that
      a device supports and use properties (meta data) of the
      parameters to conditionally include a parameter in the
      output and various forms of the parameter's device value
      (encoded, decoded, formatted, etc.).

   list-select-params
      Similar to list-params, but focused on just a few pre-defined
      parameters.

   vout-limits [ rail-num ]
      Ramps up voltage and reports on whether Vout OV warning
      and faults are triggered. 

   on-off
      Shows various ways of setting the OPERATION command.

   compute-power
      Trivial computation example: displays output power based
      on READ_VOUT and READ_IOUT settings for rail #1. Note that some devices
      support a descrete READ_POUT command, and this should be used
      if available because it will be more accurate: the vout and
      iout readings used will be sampled closer together than 
      possible via PMBus.

   import-project projectfile.xml
      Imports a project file. There are many options to project 
      import. This sample uses 'update' mode: only changes between
      project and device are written out.

   import-dflash dflash-file
      The input file can be Intel Hex or S-Record format.

   export-project projectfile.xml
      Export filenames can contain the same macro tokens that the
      Fusion Digital Power Designer's File->Export tool supports.
      So for example, you can use a filename of 
      '{PN} {DV} Address {DA} {EF}.{EXT}' might produce a 
      filename like 'UCD9240-80 3.24.0.8163 Address 25 Project.xml'.

   export-text textfile.csv
      Outputs device configuration and readings in a spreadsheet. 
      This example is hard coded to produce CSV output. The API 
      also supports tab seperated output.

   export-dflash dflash-file.hex
      The example is hard coded to produce an Intel Hex formatted 
      image. The filename can also contain macro callouts.

   control
      Uses the low-level USB Serial Adapter (aka SAA) API to 
      get and set the SAA's control line state. In some device
      configurations this may be used to control device operation.

   firmware-update firmware-file firmware-version-in-file
      Updates firmware on the device. Only downloads the firmware
      if the firmware version on the device is different than
      firmware-version-in-file. Example: 

      ConsoleSample1 firmware-update c:/temp/fw.x0 3.24.0.1234

   firmware-download firmware-file
      Downloads firmware on the device. Always downloads the 
      specified firmware file, regardless of the firmware 
      currently on the device.

   ucd92xx-auto-tune project-file
      Runs auto tune on all rails and CLA banks and writes the 
      resulting coefficients to the device. Uses the design 
      embedded within the project file, except that the voltage
      setpoint from the current VOUT_COMMAND setting for each
      rail is used instead of the output voltage embedded within
      the project.

   ucd90xx-write-fault-responses
      Defines FAULT_RESPONSES from scratch and writes to hardware.

   ucd90xx-clear-pins
      Equivalent to deleting all UCD90XX rails, GPIs, GPOs, fans, etc. manually.

   ucd90xx-configure-pins
      Creates various monitors (voltage, temperarture, current), margin 
      pins, enable pins, GPIs, GPOs, a fan, and PWM. Configures each, 
      showing how to use the API to programmatically configure items
      available in the GUI's 'Pin Assignment' tab.

    ucd90xx-list-pins
      Prints all pin assignments to the console.

    ucd90xx-list-pin pin-num1 pin-num2 ...
      Prints pin assignments to the console for specific pins.

    ucd90xx-pin-function-supported
      Shows how you can query the API to determine whether a pin
      supports a given function (FanTach, FanPWM, GPI, etc).

    ucd90xx-unassign-pin pin-num1 pin-num2 ...
      Removes a pin assignment. This can even be a fan tach, 
      fan enable, or fan PWM.

    ucd90xx-define-log-enables
      Set LOGGED_FAULT_DETAIL_ENABLES from scratch.

    ucd90xx-update-log-enables
        Update LOGGED_FAULT_DETAIL_ENABLES settings. This shows how you just tweak 
        existing settings.      

    mfr-gui-headless1
      Runs a series of Manufacturing GUI tasks through code in so-called
      'headless' mode. This example is targeted at a UCD92xx controller,
      and will perform manual calibration of vout on rail #1.

    ucd30xx-registers *or*
    ucd31xx-registers
      Shows how to peek/poke low-level IC registers from ROM or program mode.
      This should only be used by Isolated customers developing their own
      firmware on the UCD30xx or UCD31xx Isolated platform.

   dynamic-memory-map
      Shows how to access registers/variables in a memory map via runtime
      addressable variable path strings such as api[""foo.bar[0].abc""]. This does
      not require creating any special .NET library ahead of time.

    create-memory-map-wrapper-api
      Shows how to create a custom variable/register API for a select memory map/pp 
      files. This is how the built-in UCD30xx and UCD31xx APIs are created.

    threading
      Starts three threads to poll data from the device. By default there is 0 or 1 msec 
      delay between each request. See Threading.cs.

    multi-device-project-import
      A stand-alone example that looks for multiple devices on the bus and downloads a
      project file to each. Easily extendable to download a data flash (hex) file 
      instead on devices that support direct dflash programming (UCDxxxx).

    custom-adapter-driver
      An example of creating and using a custom SMBus adapter hardware driver for the
      SMBusAdapter class. See the CustomAdapterDriver folder for the driver code
      and example of how to load the custom driver.
");
            ConsoleApp.Return_To_Continue();
            Environment.Exit(1);
        }

        private static int[] Pin_Num_Args(string[] args)
        {
            return Int_Args(args, "pin number");
        }

        private static int[] Int_Args(string[] args, string arg_descr)
        {
            if (args.Length == 1)
                ConsoleApp.CDie("you must specify at least one {} on the command line", arg_descr);
            var int_args = new int[args.Length - 1];
            for (int i = 1; i < args.Length; i++)
            {
                try
                {
                    int_args[i - 1] = int.Parse(args[i]);
                }
                catch
                {
                    ConsoleApp.CDie("argument '{}' is not a valid {}", args[i], arg_descr);
                }
            }
            return int_args;
        }
    }
}

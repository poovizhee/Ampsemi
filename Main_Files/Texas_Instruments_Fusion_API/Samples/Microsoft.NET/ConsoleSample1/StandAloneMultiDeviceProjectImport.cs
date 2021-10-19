using System;
using System.Collections.Generic;
using System.Text;
using TIDP.SAA;
using TIDP.PMBus;

namespace ConsoleSample1
{
    /// <summary>
    /// An stand-alone example for writing project files (PMBus command-based configuration)
    /// to multiple devices on the I2C bus. 
    /// </summary>
    public static class StandAloneMultiDeviceProjectImport
    {
        private static byte[] Addresses = new byte[] { 78, 126 };
        private static PartID Expected_Part = PartID.UCD3100ISO1;
        private static string Project_File_Path = @"C:\Users\a0271759.ENT\Documents\TI\Projects\92XX\Projects\Misc\API-Demo\UCD9244-";

        // DeviceImporter is the helper class that can import a project file, data flash hex file, etc.
        private static DeviceImporter Importer;

        // One time initialization
        static StandAloneMultiDeviceProjectImport()
        {
            // Find I2C adapter on PC; throw exception if not present
            if (SMBusAdapter.Discover() == 0)
                throw new Exception("no GPIO-TO-USB adapter found");

            // Create import helper API
            Importer = new DeviceImporter();

            // Capture messages from import helper API
            Importer.Message += new EventHandler<DeviceImporter.MessageEventArgs>(Importer_Message);
        }

        // This can be called any number of times
        public static void Run()
        {
            // Look for devices on I2C
            Console.WriteLine("Scanning I2C bus for TI devices ...");
            if (PMBusDevice.Discover() == 0)
                throw new Exception("no PMBus devices found");

            // Report on devices found 
            Console.WriteLine();
            Console.WriteLine("Devices found:");
            foreach (var device in PMBusDevice.Devices)
            {
                Console.WriteLine("   - " + device);
            }

            // Verify up-front that all expected devices are present; that way
            // we don't waste time programming some devices if all devices are
            // not present (could skip this and instead program all devices that
            // *are* present.
            Console.WriteLine();
            Console.WriteLine("Verifying all expected devices are present:");
            var devices = new List<PMBusDevice>();
            foreach (byte address in Addresses)
            {
                var device = PMBusDevice.Devices.Find(address, Expected_Part);
                Console.Write("   - " + Expected_Part + " @ " + address + ": ");
                if (device == null)
                    Console.WriteLine("MISSING");
                else
                {
                    Console.WriteLine("PRESENT");
                    devices.Add(device);
                }
            }

            // Stop programming if missing a device
            if (devices.Count != Addresses.Length)
                throw new Exception("an expected device is not on I2C bus");

            // Write config to each device
            foreach (var device in devices)
            {
                // Setup options for "import"
                var import_opts = new DeviceImporter.ProjectImportOptions();
                import_opts.Store_To_Flash_On_Success = true;
                import_opts.Updates_Only = false;
                
                // Validate each PMBus write
                import_opts.Validate_Writes_With_Readback = 
                    DeviceImporter.ProjectImportOptions.ValidateWritesWithReadback.WarningMessageEventsThenException;
                
                // Per-device options
                import_opts.Device = device;
                import_opts.Filename = Project_File_Path + device.Address + ".xml";

                // Perform import
                Console.WriteLine();
                Console.WriteLine("Writing config to " + device + " ...");

                // Throws exception on fatal error
                Importer.Import_Project(import_opts);
            }
        }

        static void Importer_Message(object sender, DeviceImporter.MessageEventArgs e)
        {
            Console.WriteLine("   " + e.Message);
        }
    }
}

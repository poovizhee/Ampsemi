using System;
using System.Collections.Generic;
using System.Text;
using TIDP.PMBus;


namespace ConsoleSample1
{
    public static class Importer
    {
        /// <summary>
        /// Throws an exception on error.
        /// </summary>
        public static void Import_Project(string project_filename)
        {
            // Throws exception on error
            var importer = new DeviceImporter();
            importer.Message += new EventHandler<DeviceImporter.MessageEventArgs>(Importer_Message);
            var import_opts = new DeviceImporter.ProjectImportOptions();
            import_opts.Device = MyApp.Device;
            import_opts.Filename = project_filename;
            import_opts.Store_To_Flash_On_Success = true;
            import_opts.Validate_Writes_With_Readback = 
                DeviceImporter.ProjectImportOptions.ValidateWritesWithReadback.WarningMessageEventsThenException;
            import_opts.Updates_Only = true;
            importer.Import_Project(import_opts);
        }

        /// <summary>
        /// Accepts either intel hex or S-Record files. Throws exception on error.
        /// </summary>
        public static void Import_Data_Flash(string dflash_filename)
        {
            // Throws exception on error
            var importer = new DeviceImporter();
            importer.Message += new EventHandler<DeviceImporter.MessageEventArgs>(Importer_Message);
            var import_opts = new DeviceImporter.DataFlashImportPrefs();
            import_opts.Device = MyApp.Device;
            import_opts.Filename = dflash_filename;
            importer.Import_Data_Flash(import_opts);

            double? read_vout = 
                MyApp.Device.Commands.READ_VOUT(0).Immediate;
        }

        static void Importer_Message(object sender, DeviceImporter.MessageEventArgs e)
        {
            Console.WriteLine(e.Message);
        }

    }
}

using System;
using System.Collections.Generic;
using System.Text;
using TIDP;
using TIDP.PMBus;

namespace ConsoleSample1
{
    public static class FirmwareDownload
    {
        /// <summary>
        /// Performs a conditional firmware download. Will only download FW if the current FW on the
        /// device is not equal to firmware_version_in_file. Passing "" as 
        /// firmware_version_in_file will turn this off and always download the firmware. Throws an 
        /// exception on error.
        /// </summary>
        public static void Download(string firmware_file, string firmware_version_in_file)
        {
            MyApp.Device.FirmwareDownloadMessage += new EventHandler<PMBusDevice.FirmwareDownloadMessageEventArgs>(Device_FirmwareDownloadMessage);

            // This is a simple "stopwatch" that can be used to time things
            var sw = new Stopwatch(true);

            try
            {
                MyApp.Device.Download_Firmware(firmware_file, firmware_version_in_file);
            }
            finally
            {
                // Put here to unsubscribe to event event if an exception is thrown
                MyApp.Device.FirmwareDownloadMessage -= new EventHandler<PMBusDevice.FirmwareDownloadMessageEventArgs>(Device_FirmwareDownloadMessage);
            }

            ConsoleApp.WriteLine("Firmware download took {}", sw.Elapsed);
            ConsoleApp.WriteLine("Firmware on the device is now {}", MyApp.Device.Firmware.Version);
        }

        /// <summary>
        /// Event handler for Device.FirmwareDownloadMessage.
        /// </summary>
        static void Device_FirmwareDownloadMessage(object sender, PMBusDevice.FirmwareDownloadMessageEventArgs e)
        {
            ConsoleApp.WriteLine(e.Message);
        }
    }
}

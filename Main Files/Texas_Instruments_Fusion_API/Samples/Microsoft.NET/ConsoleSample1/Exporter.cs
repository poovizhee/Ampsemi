using System;
using System.Collections.Generic;
using System.Text;
using TIDP.PMBus;


namespace ConsoleSample1
{
    public static class Exporter
    {
        /// <summary>
        /// Throws an exception on error.
        /// </summary>
        public static void Export_Project(string project_filename_template)
        {
            // There is a convienence static function for project save
            DeviceExporter.Export_Project(MyApp.Device, project_filename_template);
        }

        /// <summary>
        /// Throws an exception on error.
        /// </summary>
        public static void Export_Data_Flash(string dflash_filename_template)
        {
            // There is a convienence static function for project save
            DeviceExporter.Export_Data_Flash(MyApp.Device, TIDP.EepromData.Format.Intel, false,
                dflash_filename_template);
        }

        /// <summary>
        /// Throws an exception on error.
        /// </summary>
        public static void Export_Text(string dflash_filename_template)
        {
            DeviceExporter.Export_Text(MyApp.Device, TIDP.LineOutputFormat.CSV, 
                null, DeviceExporter.ParameterType.Both, dflash_filename_template);
        }
}
}

using System;
using System.Collections.Generic;
using System.Text;
using TIDP.Factory.Core;
using TIDP.Factory.TaskLibrary;
using TIDP.PMBus;

namespace ConsoleSample1
{
    /// <summary>
    /// This example shows how you can invoke Manufacturing GUI (MFR GUI) 
    /// "tasks" from C#. The normal PMBusDevice.Discover() device discovery 
    /// is performed by the FactoryGUIHeadless "headless" engine used to 
    /// bootstrap the MFR GUI framework so that standard MFR GUI tasks can
    /// be called. A "task" in the MFR GUI is simply a static function. These 
    /// tasks will indicate an error by throwing an exception. If the task 
    /// requires user input and this input is cancelled by the user, 
    /// FactoryScriptCancelledException will be thrown. If the task passes, 
    /// it will return a PASS condition. If a task was skipped because the task 
    /// was not necessary, a SKIPPED condition will be returned. Because 
    /// exceptions are used to indicate error, failire, and cancel conditions, you can 
    /// string together task calls and also mix them with standard Fusion API calls.
    /// </summary>
    public static class ManufacturingGUIHeadless1
    {
        // You would only want to do the following once per device
        public static void Run()
        {
            // Ensure exception mode for Fusion API calls is enabled; this will
            // cause MFR API tasks and standard Fusion API tasks to throw an
            // exception on PMBus/etc error
            PMBusDevice.Exceptions_On_SAA_Error = true;

            // Create a Manfacturing GUI headless engine
            var gui_headless = new FactoryGUIHeadless();

            // Setup the event handlers to be called when Initialization, Normal and Shutdown activities
            // are called. Task or other API calls will be placed there.
            gui_headless.RunInitializationTasks +=
                new EventHandler(GUI_Headless_RunInitializationTasks);
            gui_headless.RunNormalTasks +=
                new EventHandler(GUI_Headless_RunNormalTasks);
            gui_headless.RunShutdownTasks +=
                new EventHandler(GUI_Headless_RunShutdownTasks);

            // Setup logging: you can log to HTML or CSV formats; we do both here
            string logfile_base = "C:/temp/log-" + DateTimeUtils.Timestamp_For_File();
            Plugin.Logger.Add_Logfile(FactoryLogger.LogType.Html, logfile_base + ".html", false);
            Plugin.Logger.Add_Logfile(FactoryLogger.LogType.Csv, logfile_base + ".csv", false);

            // Kick off device discovery and run activities
            var start_opts = new FactoryGUIHeadless.FactoryGUIHeadlessInput(PartID.UCD3100ISO1, 126);
            gui_headless.Start(start_opts);

            // If your app will just exit, you could skip this. The following un-wires the activity
            // event handlers
            gui_headless.RunInitializationTasks -= GUI_Headless_RunInitializationTasks;
            gui_headless.RunNormalTasks -= GUI_Headless_RunNormalTasks;
            gui_headless.RunShutdownTasks -= GUI_Headless_RunShutdownTasks;
        }

        /// <summary>
        /// Called first, equivalent to an Initialization activity in the MFR GUI.
        /// </summary>
        static void GUI_Headless_RunInitializationTasks(object sender, EventArgs e)
        {
        }

        /// <summary>
        /// Called 2nd, after Initialization and a Device Scan. This is equqivalent to a
        /// Normal activity in the MFR GUI.
        /// </summary>
        static void GUI_Headless_RunNormalTasks(object sender, EventArgs e)
        {
            // If any of the following fail, an exception will be thrown

            //
            // Download a project file
            //
            var config_val = TIDP.Factory.TaskLibrary.Manufacturing.ConfigProjectDevice.FIRST_IN_PROJECT_FILE;// new ConfigValue();
            //config_val.Config_Option = ConfigValue.ConfigOption.FIRST_IN_PROJECT_FILE;

            // Invoke a MFR task library function; this is also available through the MFR GUI task browser
            // Manufacturing.Configure_and_Validate(@"C:\Documents and Settings\a0271759\Desktop\TEMP\DELTA UCD9211 Issue\Inputs\SBC20W_S3_S0_Aug27 Partial UCD9240 EVM.xml", true, config_val, true);

            //
            // Calibrate Vout on rail #1
            //

            // Invoke some other MFR tasks
            UCD9XXX.Configure_Discrete_Operation_Mode();
            UCD9XXX.UCD92XX_Calibrate_Vout_Rail(1, 1.575, 1.425, 1.5, 2, 5, 3, false, 6, 1, false, 15, 15, false);
            UCD9XXX.Undo_Configure_Discrete_Operation_Mode();

            // Call the Fusion API directly; Plugin.Device is the PMBusDevice that was found when
            // GUI_Headless.Start() was called.
            Plugin.Device.Clear_Data_Flash_Logs();

            // Call nother MFR task
            Manufacturing.Store_Default();
        }

        /// <summary>
        /// This is called last or if something failed in Normal. This is equivalent to a
        /// Shutdown activity in the MFR GUI.
        /// </summary>
        static void GUI_Headless_RunShutdownTasks(object sender, EventArgs e)
        {
        }

        // 
        // Some other task invoke examples
        //

        // Download firmware when it is in ROM mode
        static void Download_Firmware_Via_Rom()
        {
            Manufacturing.Firmware_Download_via_Rom(@"UCD9246-64_5.6.0.11220.x0", true,
                Manufacturing.DataFlashOptions.Erase, false, false, 0, false,
                ProgramFlashBlockSelection.Block0,
                ProgramFlashChecksumCalculation.EntireBlockIncludingBoot,
                ProgramChecksumMode.CalculateAndWrite, false, 0, false, false, 0, 0,0,0,false);
        }

        // Download firmware when it is in program mode
        static void Download_Firmware_Upgrade()
        {
            Manufacturing.Firmware_Update(@"UCD9224-48_5.8.0.11401.x0",
                UCD9XXX.ConditionForFlash.AlwaysFlash, "", true,
                new Manufacturing.DataFlashOptions(), true, false,
                false, 0, false,
                ProgramFlashBlockSelection.Block0,
                ProgramFlashChecksumCalculation.EntireBlockIncludingBoot,
                ProgramChecksumMode.CalculateAndWrite, false, 1, false, false, 1, 1, 0, 0,false);
        }
    }

}

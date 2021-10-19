using System;
using System.Collections.Generic;
using System.Text;
using TIDP.Memory;
using TIDP.PMBus.Parts.UCD3000;
using TIDP.PMBus;

namespace ConsoleSample1
{
    public static class CreateMemoryMapWrapperAPI
    {
        /// <summary>
        /// Shows how you can create a custom memory debugger C# API wrapper around your
        /// map/pp file(s).
        /// </summary>
        public static void Create()
        {
            var opts = new UCD3000EasyMemoryMapCreator.CreatorOptions();

            //
            // These are the items you would need to change
            //

            // Original "C" compiler options used
            opts.Small_Enums = true;

            // What type of IC this is
            opts.IC_Family_ID = ICFamilyID.UCD3100;

            // Where the map/pp files are. There are other modes you can use such as
            // pointing to individual pp and map files. See SourceFilesMode.
            opts.Source_Files_Mode = SourceFilesMode.FlatFolder;
            opts.Source_Files_Dir = @"C:\Documents and Settings\a0271759.ENT\Desktop\TEMP\Memory Debugger\UCD9246-64_5.13.0.12409";
            
            // Where to save the .cs file to
            opts.Dest_Folder = @"C:\Workspaces\FusionTools-Main\Libraries\TIDP\TIDP.PMBus\Tests\TestPMBusMiscViaConsole1\Debugger";

            // File/class to create (this.cs)
            opts.Class_Name = "EasyMemoryMapUCD9246";

            // Do it; this throws an exception on error.
            UCD3000EasyMemoryMapCreator.Create(opts);
        }
    }
}

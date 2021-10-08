using System;
using System.Collections.Generic;
using System.Text;
using TIDP.SAA;

namespace ConsoleSample1
{
    /// <summary>
    /// Sample SMBusAdapter driver factory.
    /// </summary>
    public class SampleDriverFactory : IAdapterDriverFactory
    {
        public IList<IAdapterDriver> Discover()
        {
            // We return a list of drivers; each driver manages a single physical adapter
            var drivers = new List<IAdapterDriver>();

            // This sample driver only supports a single virtual adapter
            var driver = new SampleDriver();
            drivers.Add(driver);

            // We return all drivers, which 1:1 map to a phsysical driver (although in this 
            // case this is a virtual test driver)
            return drivers;
        }

        // Here is the code for TI's SAADriverFactory, which creates an SAADriver for
        // each USB-TO-GPIO adapter found.

        /*        
        protected const UInt16 HID_VENDOR_ID = 0x451;
        protected const UInt16 HID_PRODUCT_ID = 0x5F00;

        public IList<IAdapterDriver> Discover()
        {
            var drivers = new TIList<IAdapterDriver>();

            foreach (var device in HidDeviceFactory.Enumerate(HID_VENDOR_ID, HID_PRODUCT_ID))
            {
                var driver = new SAADriver(device);
                drivers.Add(driver);
            }

            return drivers;
        }
         */
    }
}

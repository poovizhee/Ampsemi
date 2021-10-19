The Fusion API supports alternative SMBus adapter hardware through a series 
of interfaces. At the minimum you must create a class that implements
IAdapterDriverFactory and defines a Discover() method. This method will
create one or more drivers for each hardware adapter that is found. What
it returns must implement IAdapterDriver, but for the sake of doing anything
useful with the API, should also implement ISMBusAdapterDriver to provide
SMBus methods.

The sample in this folder creates a dummy driver that will emulate a simple
controller Fusion Digital Power Designer supports, TPS53819.

See the Word document "Creating a Custom Adater Driver for Fusion API" that
is bundled with the Fusion API installer for much more information.
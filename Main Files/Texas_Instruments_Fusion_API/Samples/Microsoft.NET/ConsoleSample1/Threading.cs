using System;
using System.Collections.Generic;
using System.Text;
using System.Threading;
using TIDP;

using TIDP.PMBus.Commands;

namespace ConsoleSample1
{
    public static class Threading
    {
        private const int NUM_THREADS = 3;
        private const int NUM_REQUESTS_IN_THREAD = 50;

        // A random delay between each request will be performed, up to 10 msec
        private const int MAX_DELAY_BETWEEN_REQUESTS = 1;

        private static int Num_Done = 0;
        private static AutoSeedRandom Random = new AutoSeedRandom();

        public static void Manual_Polling()
        {
            // This fires a static event; the event should be fired on the same
            // thread that wired in the event
            PMBusCommand.ReadParameter += new EventHandler<ReadParameterEventArgs>(PMBusCommand_ReadParameter);
            PMBusCommand.WriteParameter += new EventHandler<WriteParameterEventArgs>(PMBusCommand_WriteParameter);
            
            for (int thread_num = 1; thread_num <= NUM_THREADS; thread_num++)
            {
                ConsoleApp.WriteLine("Starting thread #{} ...", thread_num);
                Start_Thread();
            }

            while (Num_Done != NUM_THREADS)
            {
                Thread.Sleep(1);
            }

            ConsoleApp.WriteLine();
            ConsoleApp.WriteLine("All threads finished");
        }

        static void PMBusCommand_WriteParameter(object sender, WriteParameterEventArgs e)
        {
            ConsoleApp.WriteLine("{}: Thread {}: {}", Timestamp(),
                Thread.CurrentThread.ManagedThreadId, e.Debug);
        }

        static void PMBusCommand_ReadParameter(object sender, ReadParameterEventArgs e)
        {
            ConsoleApp.WriteLine("{}: Thread {}: {}", Timestamp(),
                Thread.CurrentThread.ManagedThreadId, e.Debug);
        }

        private static void Start_Thread()
        {
            var thread = new Thread(new ThreadStart(Thread_Func));
            thread.Start();
        }

        private static void Thread_Func()
        {
            for (int n = 1; n <= NUM_REQUESTS_IN_THREAD; n++)
            {
                if (n != 1)
                {
                    int delay = Random.NextInt32(0, MAX_DELAY_BETWEEN_REQUESTS);
                    Thread.Sleep(delay);
                }

                // Use random rail #
                int page_i = Random.NextInt32(0, MyApp.Device.Num_Outputs - 1);
                string log_prefix = StringUtils.Format("{}: Thread {}, Req #{}, Rail #{}",
                    Timestamp(), Thread.CurrentThread.ManagedThreadId, n, page_i + 1);

                try
                {
                    MyApp.Device.Lock();
                    double vout = MyApp.Device.Commands.READ_VOUT(page_i).Immediate.Value;
                    ConsoleApp.WriteLine("{}: {:N3} V", log_prefix, vout);
                }
                catch (Exception ex)
                {
                    ConsoleApp.WriteLine("{}: {}", log_prefix, MiscUtils.Concat_Exceptions(ex));
                }
                MyApp.Device.Release();
            }

            ++Num_Done;
        }

        private static string Timestamp()
        {
            var ts = DateTime.Now;
            return ts.Second.ToString("00") + "." + ts.Millisecond.ToString("000");
        }
    }
}

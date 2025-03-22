using System;
using System.Device.Gpio;
using System.Diagnostics;
using System.Threading;

class Program
{
    private const int TRIG = 24;
    private const int ECHO = 23;

    static void Main()
    {
        GpioController gpioController = new GpioController();

        // Initialise pins for ultrasonic
        gpioController.OpenPin(TRIG, PinMode.Output);
        gpioController.OpenPin(ECHO, PinMode.Input);

        Console.WriteLine("Startup..." + Time.Time);
        while (true) // Loop...
        {
            double distance = MeasureDistance(gpioController);
            Console.WriteLine($"Distance: {distance} cm");
            Thread.Sleep(100); // 100ms delay
        }
    }

    float MeasureDistance(GpioController gpio)
    {
        gpio.Write(TRIG, PinValue.Low);
        Thread.Sleep(500);
        gpio.Write(TRIG, PinValue.High);
        Thread.Sleep(TimeSpan.FromMilliseconds(0.01)); // 10µs pulse
        gpio.Write(TRIG, PinValue.Low);

        var stopwatch = Stopwatch.StartNew();
        while (gpio.Read(ECHO) == PinValue.Low);
        stopwatch.Restart();
        while (gpio.Read(ECHO) == PinValue.High);
        stopwatch.Stop();

        double pulseDuration = stopwatch.Elapsed.TotalSeconds;
        double distance = pulseDuration * 17150; // Speed of sound in cm/s
        return Math.Round(distance, 2);
    }
}

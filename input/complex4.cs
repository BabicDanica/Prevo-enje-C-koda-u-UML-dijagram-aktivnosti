using System;

class Program
{
    static void Main(string[] args)
    {
        int number = 7;

        // if else if else
        if (number < 5){
            Console.WriteLine("Broj je manji od 5");
        }else if (number == 5){
            Console.WriteLine("Broj je jednak 5");
        }else{
            Console.WriteLine("Broj je veci od 5");
        }

        // try catch
        try
        {
            int a = 10;
            int b = 0;
            int c = a / b;  // izaziva izuzetak deljenja sa nulom
            Console.WriteLine("Rezultat je: " + c);
        }
        catch (DivideByZeroException e)
        {
            Console.WriteLine("Greska: Deljenje sa nulom nije dozvoljeno.");
        }

        // switch case
        switch (number)
        {
            case 1:
                Console.WriteLine("Broj je 1");
                break;
            case 7:
                Console.WriteLine("Broj je 7");
                break;
            default:
                Console.WriteLine("Broj nije 1 ni 7");
                break;
        }

        // for petlja
        Console.WriteLine("For petlja:");
        for (int i = 0; i < 3; i++)
        {
            Console.WriteLine("i = " + i);
        }

        // while petlja
        Console.WriteLine("While petlja:");
        int j = 0;
        while (j < 3)
        {
            j = j + 1;
        }
    }
}

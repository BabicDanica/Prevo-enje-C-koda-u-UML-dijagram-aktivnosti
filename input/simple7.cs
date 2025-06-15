
using System;

namespace MyApplication
{
  class Program
  {
    void Test(int x)
    {
      if (x < 10)
      {
        Console.WriteLine("Less than 10");
      }
      else if (x < 20)
      {
        Console.WriteLine("Between 10 and 19");
      }
      else if (x < 30)
      {
        Console.WriteLine("Between 20 and 29");
      }
      else
      {
        Console.WriteLine("30 or more");
      }

    }
  }
}

using System;
using DataStructures.Models;

namespace DataStructures
{
    class Program
    {
        static void Main(string[] args)
        {
            var stack = new Stack<int>();
            stack.push(10);
            stack.push(20);

            Console.WriteLine(stack.viewElements());
        }
    }
}

using System;
using System.Collections.Generic;
using System.Linq;

namespace DataStructures.Models
{
    public class Stack<T>
    {
        public int MAXLEN { get; set; }

        public int top { get; set; }
        public T[] elements { get; set; }

        public Stack()
        {
            top = -1;
            elements = new T[MAXLEN];
            MAXLEN = 5;
        }

        private bool reachedMaxCapacity {
            get {
                return top == MAXLEN - 1;
            }
        }

        public void push(T element) {
            if (reachedMaxCapacity) {
                throw new Exception("Stack reached max capacity!");
            }
            
            top += 1;
            elements[top] = element;
        }

        public T pop() {
            if (top == -1) {
                throw new Exception("Oops... The stack is empty! Please add a few elements :)");
            }
            var foos = new List<int>();
            foos.Add(2);
            foos.RemoveAt(2);

            var poppedElement = elements[top];
            top -= 1;

            return poppedElement;
        }

        public T[] viewElements() {
            return elements;
        }
    }
}
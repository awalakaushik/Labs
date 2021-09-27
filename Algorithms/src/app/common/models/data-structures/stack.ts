export class Stack<T> {

    private MAXLEN: number;
    private elements: Array<T>;
    private top: number;

    constructor() {
        this.MAXLEN = 50;
        this.elements = [];
        this.top = -1;
    }

    /**
     * Pushes an element on top of the stack.
     * @param element An element to push on to the stack
     */
    push(element: T): void {
        if (this.isStackFull) {
            throw new Error("Stack Overflow Exception: The stack has reached max capacity!");
        }

        this.top += 1;
        this.elements[this.top] = element;
    }

    /**
     * Pops the top element in the stack and returns the value
     * @returns Popped element of Type T
     */
    pop(): T {
        if (this.isStackEmpty) {
            throw new Error("Stack Underflow Exception: The stack has no elements!");
        }

        const poppedElement = this.elements[this.top];
        this.elements.splice(this.top, 1);
        this.top -= 1;

        return poppedElement;
    }

    /**
     * A getter property that returns the count of elements in the stack.
     */
    get currentSize(): number {
        return this.elements.length;
    }

    /**
     * A getter property that returns true if the stack reaches max capacity and false, otherwise.
     */
    get isStackFull(): boolean {
        return this.top === (this.MAXLEN - 1);
    }

    /**
     * A getter property that returns true if the stack is empty and false, otherwise.
     */
    get isStackEmpty(): boolean {
        return this.top === -1;
    }

    /**
     * A getter property that returns the list of elements on the stack.
     */
    get viewElements(): Array<T> {
        return [...this.elements];
    }

    /**
     * A getter property that returns the max size of the stack.
     */
    get maxSize(): number {
        return this.MAXLEN;
    }

    /**
     * A setter property that sets the stack size to a custom value.
     */
    set size(stackSize: number) {
        this.MAXLEN = stackSize;
    }
}

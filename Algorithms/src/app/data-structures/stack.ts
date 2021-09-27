export class Stack<T> {

    private MAXLEN: number = 50;
    private elements: Array<T> = [];
    private top: number = -1;

    push(element: T): void {
        if (this.reachedMaxCapacity) {
            throw new Error("Stack Overflow Exception: The stack has reached max capacity!");
        }

        this.top += 1;
        this.elements[this.top] = element;
    }

    pop(): T {
        if (this.stackHasNoElements) {
            throw new Error("Stack Underflow Exception: The stack has no elements!");
        }

        const poppedElement = this.elements[this.top];
        this.elements.splice(this.top, 1);
        this.top -= 1;

        return poppedElement;
    }

    get elementCount(): number {
        return this.elements.length;
    }

    get reachedMaxCapacity(): boolean {
        return this.top === (this.MAXLEN - 1);
    }

    get stackHasNoElements(): boolean {
        return this.top === -1;
    }

    get viewElements(): Array<T> {
        return [...this.elements];
    }

    get maxLength(): number {
        return this.MAXLEN;
    }
    set size(stackSize: number) {
        this.MAXLEN = stackSize;
    }
}

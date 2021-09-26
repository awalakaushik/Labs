class Stack {

    constructor() {
        this.MAX_LEN = 5;
        this.top = -1;
        this.elements = [];
    }

    push(element) {
        if (this.top == this.MAX_LEN - 1) {
            throw new Error("StackOverFlowException: The stack is currently full...Pop some elements instead!");
        }
        
        this.top += 1;
        this.elements[this.top] = element;
        return;
    }

    pop() {
        if (this.top == -1) {
            throw new Error("StackUnderflowException: The stack is currently empty... Add more elements instead!");
        }

        const poppedElement = this.elements[this.top];
        // remove the last element and the index value in top
        this.elements.splice(this.top, 1);
        this.top -= 1;

        return poppedElement;
    }

    get topElement() {

        if (this.top == MAX_LEN - 1) {
            throw new Error("StackUnderflowException: The stack is empty! Add more elements instead!")
        }
        return this.elements[top];
    }

    get length() {
        return this.MAX_LEN;
    }

    get view() {

        if (this.top == -1) {
            return [];
        }
        return [...this.elements];
    }

    set maxLength(size) {
        this.MAX_LEN = size;
    }
}

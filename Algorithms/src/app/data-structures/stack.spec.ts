import { Stack } from './stack';

let stack: Stack<number>;

beforeEach(() => {
  stack = new Stack();
});

describe('Stack', () => {

  it('should create an instance', () => {
    expect(new Stack()).toBeTruthy();
  });

  it('should be able to set custom size for the stack', () => {
    stack.size = 5;

    expect(stack.maxLength).toBe(5);
  });

  it('should be able to view elements in a stack', () => {
    stack.push(1);
    stack.push(2);
    stack.push(3);

    expect(stack.viewElements).toEqual([1, 2, 3]);
  });

  it('stackHasNoElements should return true when stack has no elements', () => {
    expect(stack.stackHasNoElements).toBe(true);
  });

  it('stackHasNoElements should return false when stack has elements', () => {
    stack.push(1);
    expect(stack.stackHasNoElements).toBe(false);
  });
  
  it('stackReachedMaxCapacity should return true when stack reaches max capacity', () => {
    stack.size = 5;
    [1, 2, 3, 4, 5].forEach(el => stack.push(el));
    expect(stack.reachedMaxCapacity).toBe(true);
  });

  it('stackReachedMaxCapacity should return false when stack does not reach max capacity', () => {
    expect(stack.reachedMaxCapacity).toBe(false);
  });

  it ('should return element count', () => {
    stack.push(10);
    stack.push(20);

    expect(stack.elementCount).toBe(2);
  });

});

class Stack:

    def __init__(self):
        """ 
            stack: List used a stack
        """
        self.stack = []

    def empty(self):
        """
        Returns true if stack is empty, or false if it isn't
        """
        return True if len(self.stack) == 0 else False

    def push(self, item):
        """
            item: Value inserted in stack
        Inserts an item in the stack, always in the top
        """
        self.stack.insert(0, item)

    def pop(self):
        """
        Removes item in the head of the list and returns it
        """ 
        if len(self.stack) == 0:
            return None
        return self.stack.pop(0)



def Parentheses():
    """
    Reads a string of round, curly and square brackets and prints 
    a message if it is balanced or not.
    """
    print("Insert your string:")
    str = input()


    stack = Stack()

    "Iterate the string"
    for i in str:
        "When we get opening part, push it in the stack"
        if i == '(' or i == '{' or i == '[':
            stack.push(i)
        else:
            "When we get closing part, pop the stack."
            closing = stack.pop()
            "If it is None(empty stack) or not matching with current symbol, then it isn't balanced"
            if closing is None or (i == ')' and closing != '(') or (i == '}' and closing != '{') or (i == ']' and closing != '['):
                print("NOT balanced!")
                return
    "If stack is empty, then we know it is balanced"
    if stack.empty() == True:
        print("Balanced!")
    else:
        print("NOT balanced!")


if __name__ == '__main__':
    Parentheses()

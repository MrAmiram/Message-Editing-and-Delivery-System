#editor.py
#madule for a simple message editor with undo and redo functionality with stack management

class MessageEditor:
    def __init__(self):
        self.message = ""                            #text of the message
        self.undo_stack = []                         #stack of message chengings  
        self.redo_stack = []                         #stack for redo of message changes
        
    def write(self, text):                           #adds text to the message
        self.undo_stack.append(self.message)         #save current state befor adding a new text or changing the message
        self.message += text                         
        self.redo_stack.clear()                      #clear the message and add the new text
        
    def undo(self):                                  #reverts the last change made to the message
        if self.undo_stack:
            self.redo_stack.append(self.message)
            self.message = self.undo_stack.pop()
        else:
            print("Nothing to undo.")

    def redo (self):
        if self.redo_stack:
            self.undo_stack.append(self.message)
            self.message = self.redo_stack.pop()
        else:
            print("Nothing to redo.")

    def get_message(self):
        return self.message
    
    def clear(self):
        self.message = "" 
        self.undo_stack.clear()
        self.redo_stack.clear()

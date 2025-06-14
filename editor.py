#editor.py
#madule for a simple message editor with undo and redo functionality with stack management
from storage_maanager import StorageManager
class MessageEditor:
    def __init__(self):
        self.message = ""                                       #text of the message
        self.undo_stack = []                                    #stack of message chengings  
        self.redo_stack = []                                    #stack for redo of message changes

    def write(self, text):                                      #adds text to the message
        self._save_state_for_undo()                             #save the current state before making changes
        self.message += text                                    
        self.redo_stack.clear()                                 #clear the message and add the new text

    def undo(self):                                             #reverts the last change made to the message
        if self.undo_stack:         
            self.redo_stack.append(self.message)                #save the current state before undoing
            self.message = self.undo_stack.pop()                # restore the last state
        else:           
            print("Nothing to undo.")           

    def redo (self):                                            #reapplies the last undone change to the message            
        if self.redo_stack:         
            self.undo_stack.append(self.message)                #save the current state before redoing
            self.message = self.redo_stack.pop()                # restore the last redo state
        else:           
            print("Nothing to redo.")           

    def delete_last_word(self):                                 #deletes the last word from the message
        self._save_state_for_undo()         
        words = self.message.strip().split()                    # split the message into words
        if words:           
            self.message = ' '.join(words[:-1])         
        self.redo_stack.clear()                                 # clear the redo stack after deletion

    def get_message(self):                                      #returns the current message    
        return self.message.strip()                             # strip to remove leading/trailing whitespace

    def clear(self):                                            #clears the message and resets the stacks
        self.message = ""           
        self.undo_stack.clear()                                 # clear the undo stack
        self.redo_stack.clear()                                 # clear the redo stack

    def _save_state_for_undo(self):                             #saves the current state of the message for undo
        self.undo_stack.append(self.message)                    # append the current message to the undo stack

    def save_to_file(self, filename):                           #saves the current message to a file
        StorageManager.save_draft(self)

    def load_from_file(self, filename):                         #loads the message from a file
        StorageManager.load_draft(self)
            

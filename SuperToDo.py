######################################################################################################
# SUPER TO DO
# Megan West
# A program that allows a user to manage items in a to do list and save it to a file to load later.
# The user is currently able to add items, remove items, edit items, and search items.
######################################################################################################


import datetime
from pip._vendor.distlib.compat import raw_input


"""CLASS LISTITEM:
A to do list item that will be stored in a ToDoList. A modified Node class. Has a description string, the date it was added, and
a reference to the next listitem in the list.
"""
class ListItem:

    description = ""
    date_added = ""
    next_node = None


    """ __INIT__():
        Input: description: stores a description string for the list item.
        Input: current_time: stores the time the list item was created.
        Precondition: need a description input, need to know current_time.
        Return: void
    """
    def __init__(self, description, current_time):
        self.update_description(description)
        self.set_date(current_time)


    """ GET_DESCRIPTION():
        Getter for the description attribute.
        Input: none
        Output: none
        Return: description string
    """
    def get_description(self):
        return self.description


    """ UPDATE_DESCRIPTION():
        Setter for the description attribute.
        Input: the new ListItem description entered by the user.
        Output: none
        Return: void
    """
    def update_description(self, description):
        self.description = description


    """ GET_NEXT():
        Getter for the next node in the list.
        Input: none
        Output: none
        Return: next list_item in the to-do list
    """
    def get_next(self):
        return self.next_node


    """ SET_NEXT():
        Setter for the next node in the list.
        Input: The next node
        Output: none
        Return: void
    """
    def set_next(self, next_node):
        self.next_node = next_node


    """ SET_DATE():
        Setter for the node's date_added attribute.
        Input: The date the node was added
        Output: none
        Return: void
    """
    def set_date(self, date):
        self.date_added = date


    """ GET_DATE():
        Getter for the date_added attribute. 
        Input: none
        Output: none
        Return: date
    """
    def get_date(self):
        return self.date_added


""" CLASS LINKEDTODOLIST: 
Linked ToDoList is a linked list implementation of a to do list where items are sorted based on date added.
Items are added to the bottom of the list and removed from the top.
"""
class LinkedToDoList:

    head = None
    size = 0


    """ __INIT__(): 
        Assigns the head node to 'None'.
        Input: none
        Output: none
        Return: none
    """
    def __init__(self, head = None):
        self.head = head


    """ GET_SIZE():
        Returns the current number of list items.
        Input: none
        Output: none
        Return: integer representing num of list items
    """
    def get_size(self):
        return self.size


    """ INCR_SIZE():
        Increases the size attribute for the list by one.
        Input: none
        Output: none
        Return: none
    """
    def incr_size(self):
        self.size += 1


    """ DECR_SIZE():
        Decreases the size attribute for the list by one if there are any list items present.
        Input: none
        Output: none
        Return: True if successful. False if failure.
        Precondition: List must have at least one listitem
    """
    def decr_size(self):
        if self.get_size() <= 0:
            print("Error: Unable to decrease size. Nothing to remove.")
            success = False
        else:
            self.size -= 1
            success = True
        return success


    """ CLEAR():
        Clears the entire list.
        Input: none
        Output: none
        Return: none
    """
    def clear(self):
        self.set_root(None)
        list.size = 0


    """ DISPLAY_LIST():
        Prints all of the list items for the user to see.
        Input: none
        Output: the linked list descriptions
        Precondition: List must have at least one listitem.
    """
    def display_list(self):
        current = self.root

        if self.get_size() > 0:
            for i in range(0, self.size - 1):
                print(current.get_description())
                current = current.get_next()
                i += 1

            print(current.get_description())

        else:
            print("There are no list items to display.")

    """ SET_ROOT():
        Assigns a new head node to the linked list.
        Input: The new head node
        Output: None
        Return: void
    """
    def set_root(self, new_head):
        self.root = new_head


    """ GET_ROOT():
        Returns the root node of the linked list.
        Input: none
        Output: None
        Return: the root node of the linked list (the oldest item)
    """
    def get_root(self):
        return self.root


    """ ADD_ITEM():
        Adds a new listitem to the to-do list.
        Input: item_to_do is the string description value for the new node that was entered by the user.
        Output:None
        Return:True if successful
    """
    def add_item(self, item_to_do):

        index = -1

        # RUN SEARCH ONLY IF LIST HAS ITEMS.
        if self.get_size() > 0:
            index = self.search(item_to_do)

        # IF ITEM IS NOT ALREADY IN THE LIST, ADD IT.
        if index == -1:

            new_li = ListItem(item_to_do, datetime.datetime.now())

            if self.get_size() == 0:
                self.set_root(new_li)
            else:
                current = self.root
                while current.get_next() != None:
                    current = current.get_next()

                current.set_next(new_li)

            self.size += 1
            success = True

        # IF ITEM IS ALREADY IN THE LIST, DON'T ADD IT. FAIL.
        else:
            success = False

        return success


    """ REMOVE_ITEM():
        Removes the user-entered item from the list.
        Input: keyword is the word or phrase entered by the user.
        Output: none
        Return: True if successful
        Precondition: ToDoList must contain at least one listitem.
    """
    def remove_item(self, keyword):

        # if the list has items
        if self.get_size() > 0:

            index = self.search(keyword)

            if index == 0:
                self.set_root(self.get_root().get_next())
                success = True

            elif index == 1:
                current = self.get_root()
                current.set_next(None)
                success = True

            elif index > 1:
                prev = self.get_root()
                current = self.get_root().get_next()

                for i in range(0, index - 1):
                    prev = prev.get_next()
                    current = current.get_next()

                prev.set_next(current.get_next())
                current = None
                success = True

            elif index == -1:
                print("The item you entered was not found in the list. Please try again.")
                success = False

            elif index == -9999:
                print("There were too many results. Reenter the item with more characters.")
                success = False

            else:
                print("Error: invalid index returned from search function!")
                success = False

        # if the list is empty
        else:
            print("There are no items in this list to remove.")
            success = False

        # if an item was removed, reduce the size of the list by 1.
        if success:
            self.decr_size()

        return success


    """ SEARCH():
        Locates nodes containing given keyword.
        Input: a keyword to be searched for in the listitems' descriptions
        Output: Prints all descriptions containing the keyword.
        Return: Index of containing node if found, -1 if not found, -9999 if multiple are found  
        Precondition: List must contain at least one node.
    """
    def search(self, keyword):

        size = self.get_size()
        found = False
        results_found = 0

        # if there are any elements in the list, perform the search.
        if size > 0:
            current = self.get_root()

            i = 0
            # for every element in the array,
            while i <= size - 1:

                # check if the keyword is in the description. If it is, save the index of current.
                if keyword in current.get_description():
                    index = i
                    found = True
                    print("found " + current.get_description() + " in the list.")
                    results_found += 1

                current = current.get_next()
                i += 1
            # end while

            # if the result was not found or if there are too many results, send an invalid index to the caller.
            if not found:
                index = -1
            elif found and (results_found > 1):
                index = -9999
            # end if

        # this else should never run
        else:
            print("This line should never print. Ran search on empty list. Check caller.")
        # end if

        return index


"""CLASS LISTMANAGER:
Runs the user interface for the program.
"""
class ListManager:

    status = 0
    list = None

    """ __INIT__():
        Constructs a ListManager, which contains a List
        Input: a keyword to be searched for in the listitems' descriptions
        Output: Prints all descriptions containing the keyword.
        Return: Index of containing node if found, -1 if not found, -9999 if multiple are found  
        Precondition: List must contain at least one node.
    """
    def __init__(self):
        self.list = LinkedToDoList()
        self.run()

    def run(self):
        if self.list.get_size() == 0:
            print("Welcome to Super To-Do! You don't have any lists. Let's create one.")
            description = raw_input("Enter the first list item, then press ENTER:")
            self.list.add_item(description)
            self.edit_list_menu()
        else:
            print("Welcome to the To-Do List!")
            print("Your to-do's:")
            self.edit_list_menu()

    def edit_list_menu(self):
        self.list.display_list()
        loop = True

        while loop:
            print("\n\nPress 'A' to add a new list item\n "
                  "Press 'D' to delete an item\n "
                  "Press 'E' to edit an item\n "
                  "Press 'S' to show list\n "
                  "Press 'F' to locate an item in the list.\n"
                  "Press 'Q' to save and quit the list\n")
            choice = raw_input()

            if choice == 'A' or choice == 'a':
                self.add()
                self.list.display_list()
                continue
            elif choice == 'D' or choice == 'd':
                self.delete()
                self.list.display_list()
                continue
            elif choice == 'E' or choice == 'e':
                self.edit()
                self.list.display_list()
                continue
            elif choice == 'S' or choice == 's':
                self.list.display_list()
                self.list.display_list()
                continue
            elif choice == 'F' or choice == 'f':
                description = raw_input("Enter a keyword to find in list:")
                index = self.list.search(description)
                if index >= 0:
                    print("Item was found in list at index " + str(index) + ".")
                elif index == -1:
                    print(description + " was not found in your list.")
                else:
                    print("Multiple instances of " + description + " found in list. Try entering in more characters.")
                self.list.display_list()
            elif choice == 'Q' or choice == 'q':
                self.save()
                break
            else:
                continue

    def add(self):

        cont = 'C'
        while cont == 'C' or cont == 'c':
            description = raw_input("Enter a task, then press ENTER:")
            self.list.add_item(description)
            self.list.display_list()
            cont = raw_input("Press 'C' to add another item or any key to go back.")

        return True

    def delete(self):
        item_to_remove = raw_input("Search for an item to remove:")
        removed = self.list.remove_item(item_to_remove)

        if removed:
            print("Item successfully removed.")
        else:
            print("Please try again:")

    def edit(self):
        pass

    def save(self):
        pass


def main():

    new_manager = ListManager()
    new_manager.run()


# call the main function
main()

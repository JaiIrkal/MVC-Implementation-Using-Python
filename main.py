from Contents.Model import Model
from Contents.View import View
from Contents.Controller import Controller

# Create instances of the model, view, and controller
if __name__ == '__main__':
    model = Model.Model()
    view = View.View()   
    controller = Controller.Controller(model, view)
    choice = 0 
    local_user_data = {}

    while True:
        print("1. Add Student Data")
        print("2. Remove Student")
        print("3. Display Data")
        print("4. Exit")

        user_choice = int(input("Enter Your Choice:"))

        if user_choice == 1:

            name = str(input("Enter Your Name: "))
            usn = str(input("Enter Your USN: "))
            controller.add_data({"name":name, "usn":usn})

        elif user_choice == 2:

            model.remove_data()

        elif user_choice == 3:

            controller.display_data()

        elif user_choice == 4:

            print("GoodBye")
            break
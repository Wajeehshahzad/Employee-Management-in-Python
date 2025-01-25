

import json
import csv
import os

class UserManagement:                                     #Class for User Management
    SIGNUP_FILE = "Signup.json"

    @staticmethod                                   #bound to the class and not the object of the class, it can't aceess or modify class state
    def signup_user(username , phone , age , address , password , email):   #Signup user function.
        user_data = {
            "username": username,
            "phone": phone,
            "age": age,
            "address": address,
            "password": password,
            "email": email,
        }

        if os.path.exists(UserManagement.SIGNUP_FILE):              # os used to interact with Operating System.
            with open(UserManagement.SIGNUP_FILE, "r") as file:     #Save users data in Json format.
                users = json.load(file)                             #JSON data from a file and returns Python object.

        else:
             users = []                                             #Declaring empty list.

        users.append(user_data)                                     #Add users data is users.

        with open(UserManagement.SIGNUP_FILE , "w") as file:
         json.dump(users, file, indent=4)                           #Serializes Python object to JSON and writes it to a file.

        print("Signup Successfull ! ")

    @staticmethod
    def login_user(email , password ):                              #Login user function.
        if not os.path.exists(UserManagement.SIGNUP_FILE):
            print("No user data found, Kindly Signup First Please !")
            return None
        
        with open(UserManagement.SIGNUP_FILE, "r") as file: 
            users = json.load(file)
                   
        for user in users:                                           #Checks if user is registered or not.
            if user["email"] == email and user["password"] == password:
                print(f"Welcome, {user['username']}! Login successful.")
                return user

        print("Invalid email or password. Please try again. Otherwise register first..")        #If user is not registered.
        return None

class EmployeeManagement:                                            #Class for Employee management. 
    def __init__(self):
        self.task = []  

    def view_profile(self, user):                                    #For viewing profiles
        print("\nEmploye Profile: ")
        for key, value in user.items():                              #For searching dictionary including key-value.
            print(f"{key.capitalize()}: {value}")

    def add_daily_task(self, task):                                  #Adding daliy task.
        self.task.append(task)
        print("Task added successfully!")

    def read_tasks(self):                                            #Reading tasks.
        print("\nDaily Tasks:")
        if self.task:
            for i, task in enumerate(self.task, 1):                 #Enumerates the items, starting the count at 1 instead of the default 0.
                print(f"{i}. {task}")
        else:
            print("No tasks found.")

    def edit_task(self, task_number, new_task):                      #Editting tasks.
        if 0 < task_number <= len(self.task):
            self.task[task_number - 1] = new_task
            print("Task updated successfully!")
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):                              #Deleting tasks.
        if 0 < task_number <= len(self.tasks):
            self.tasks.pop(task_number - 1)                          #pop used to delete tasks starting at index -1 i.e 0.          
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")

    def write_tasks_to_csv(self, filename="Tasks.csv"):              #Defining method.
        with open(filename, "w", newline="") as file:                #Oppening file in write mode,
            writer = csv.writer(file)                                #initializes a csv.writer object to write data in CSV format.
            writer.writerow(["Task Number", "Task Description"])
            for i, task in enumerate(self.task, 1):                 #Enumerates items, starting from zero.
                writer.writerow([i, task])                           #Writing task

        print(f"Tasks saved to {filename} successfully!")                

if __name__ == "__main__":                                           #Creating Main Menu.
    user_manager = UserManagement()                               
    employee_manager = EmployeeManagement()

    while True:                                                      #While loop to display options
        print("\n1. Signup\n2. Login\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":                                            #If user selects 1 then the following menu will be shown 
            username = input("Enter username: ")
            phone = input("Enter phone: ")
            age = input("Enter age: ")
            address = input("Enter address: ")
            password = input("Enter password: ")
            email = input("Enter email: ")
            user_manager.signup_user(username, phone, age, address, password, email)

        elif choice == "2":                                          #If user selects 2 then the following menu will be shown 
            email = input("Enter email: ")
            password = input("Enter your password: ")
            user = user_manager.login_user(email, password)          #It will validate that the user is registered or not

            if user:                                                     #Login succesfull then main menu
                while True:
                    print("\nMain Menu:")
                    print("1. View Employee Profile")
                    print("2. Add Daily Task")
                    print("3. Read Tasks")
                    print("4. Edit Task")
                    print("5. Delete Task")
                    print("6. Write Tasks to CSV")
                    print("7. Logout")

                    option = input("Select an Option: ")              #input for selction of menu option

                    if option == "1":                                 #View profile.
                        employee_manager.view_profile(user)
                    elif option == "2":
                        task = input("Enter task description: ")      #Adding task.
                        employee_manager.add_daily_task(task)
                    elif option == "3":                               #Read all the tasks.
                        employee_manager.read_tasks()        
                    elif option == "4":
                        task_number = int(input("Enter task number to edit: "))   #Edditing tasks.
                        new_task = input("Enter new task description: ")
                        employee_manager.edit_task(task_number, new_task)
                    elif option == "5":
                        task_number = int(input("Enter task number to delete: "))   #For deleting task.
                        employee_manager.delete_task(task_number)
                    elif option == "6":
                        employee_manager.write_tasks_to_csv()           #To converts tasks to csv format
                    elif option == "7":
                        print("Logging out.... ")
                        break
                    else:                                               #if anyother option pressed then following exception
                        print("Invalid option selected, Please try again. !!!")  

        elif choice == "3":
            print("Thank you for using Employee management System, Thank you! ")
            break
        else:
            print("Invalid choice entered, Please try again.")      
                 
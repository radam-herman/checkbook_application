##  checkbook_project.py

# python_project_Command_Line_Checkbook_Application

# create a command line checkbook application that allows 
# users to track their finances with a command line interface.

# When run, the application should welcome the user,
#  and prompt them for an action to take:

  # - view current balance
  # - add a debit (withdrawal)
  # - add a credit (deposit)
  # - exit

# The application should persist between times that it is run,
# that is, if you run the application, add some credits,
# exit the application and run it again, you should still see 
# the balance that you previously created. 

# In order to do this, your application will need to store its data
# in a text file. Consider creating a file where each line
# in the file represents a single transaction.



    # making menu
    # working on sub routines
        # check balance
        # add
        # remove
    # also look at clearing screen before reprint of menu.


# these lists are for testing initial account processes and logic 
# before testing from actual JSON document 
#account_list_transaction_id = [1, 2, 3]
#account_list_running_balance = [0, 100, 75]
#account_list_transaction_type = ["balance check", "credit", "debit"]
#account_list_time_stamp = ["2019-09-18 07:57:10.535372", "2019-09-18 08:09:47.689715", "2019-09-18 08:12:42.608941"]
#account_list_amount_delta = [0, 100, -25]

# testing against a dictionary

test_store = { "main_account":
	{"transactions": [
		{
			"transaction_id": 1,
			"running_balance": 0,
			"transaction_type": "balance check",
			"time_stamp": "2019-09-18 07:57:10.535372",
			"amount_delta": 0
		},
		{
			"transaction_id": 2,
			"running_balance": 100,
			"transaction_type": "credit",
			"time_stamp": "2019-09-18 08:09:47.689715",
			"amount_delta": 100
		},
		{
			"transaction_id": 3,
			"running_balance": 75,
			"transaction_type": "debit",
			"time_stamp": "2019-09-18 08:12:42.608941",
			"amount_delta": -25
		}

		]
	}
}




def check_balance():
    # this will open JSON file
        # call the last transaction, ie -1 index transaction
        # account_updater["main_account"]['transactions'][-1], then find running_balance
        # proto setup will just call -1 index of account_list_running_balance
    list_running_balance = test_store['main_account']['transactions'][-1]['running_balance']
    print("Your current balance is $", list_running_balance)
    # this will need to write back/append new transaction #, and "balance check", etc to file

def withdrawal():
    # 
    print("this is the withrawal place holder")

def deposit():
	
    print("this is the deposit")

  # DONT RUN THIS
# def exit():
    #print("you chose to exit - are you sure?")
    #check_choice = input("Enter yes or no: ")
    #if check_choice.lower() == "yes":
    #   return loop = False
    #elif check_choice.lower() == "no":
    #    return loop = True
    #else:
    # #   return raw_input("Wrong option selection. Enter any key to try again..")


def print_menu():       ## Your menu design here
    #print(30 * "-" , "MENU" , 30 * "-")
    print("\n")
    print("~~~ Welcome to your terminal checkbook! ~~~")
    print("\n")
    print("What would you like to do?")
    print("\n")
    print("1. view current balance")
    print("2. add a debit (withdrawal)")
    print("3. add a credit (deposit)")
    print("4. Exit")
    print(67 * "-")
  
loop=True      
  
while loop:          ## While loop which will keep going until loop = False
    print_menu()    ## Displays menu
    choice = input("Enter your choice [1-4]: ")
     
    if choice == '1':     
        print("Menu 1 - current balance has been selected")
        ## You can add your code or functions here
        check_balance()
    elif choice == '2':
        print("Menu 2 - add a debit (withdrawal) has been selected")
        ## You can add your code or functions here
        withdrawal()
    elif choice == '3':
        print("Menu 3 - add a credit (deposit) has been selected")
        ## You can add your code or functions here
        deposit()
    elif choice == '4':
        print("Thanks, have a great day!")
        ## You can add your code or functions here
        loop=False # This will make the while loop to end as 
        # not value of loop is set to False
        #exit()  # turned the fx exit() off
    else:
        # Any integer inputs other than values 1-5 we print an error message
        #raw_input("Wrong option selection. Enter any key to try again..")
        print("you didn't enter a valid input")

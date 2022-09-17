from DBHelper import DBHelper

def main():
    db=DBHelper()
    while True:
        print("**********WELCOME*********")
        print()
        print("PRESS 1 to insert new user")
        print("PRESS 2 to display all user")
        print("PRESS 3 to delete user")
        print("PRESS 4 to update user")
        print("PRESS 5 to exit program")
        print()
        try:
            choice=int(input())
            if choice==1:
                uid=int(input("Enter user id:"))
                employeename=input("Enter employee name:")
                employeephone=input("Enter employee phone:")
                db.insert_user(uid,employeename,employeephone)

            elif choice==2:
                db.fetch_all()
                pass

            elif choice==3:
                userid=int(input("enter user id to which you want to delete"))
                db.delete_user(userid)

            elif choice==4:
                uid = int(input("Enter id of user:"))
                employeename = input("new name:")
                employeephone = input("new phone:")
                db.update_user(uid, employeename, employeephone)

            elif choice==5:
                break
            else:
                print("Invalid input! Try again")
        except Exception as e:
            print(e)
            print("Invalid Details ! Try again")

if __name__ == "__main__":
    main()






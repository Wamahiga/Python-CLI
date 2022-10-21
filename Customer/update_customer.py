import json
from Customer.view_customer import view_customer
from Customer.add_customer import *
from main import main_menu

filename ="Customer/customer.json"

def update_customer():
    view_customer()
    updated_cus_list = []
    with open(filename, "r") as json_file:
        temp = json.load(json_file)
        data_length = len(temp)
        while True:
            try:
                update_opt = int(input(f"\nEnter Customer ID(1 - {data_length}) to update: "))
            except ValueError:
                print(f"\nINVALID INPUT!")
                continue
            if update_opt > data_length:
                print(f"\nINVALID INPUT! Enter an ID value between 1 and {data_length}")
                continue
            else:
                break

        i = 1
        for entry in temp:
            if i == int(update_opt):
                cus_name = entry["Customer_Name"]
                gender = entry["Gender"]
                mail = entry["Email"]
                tel = entry["Phone_Number"]
                print(f"\n Current Name: {cus_name}")
                cus_name = input("Enter new customer's name: ")
                print(f"\nGender: {gender}")
                while True:
                    try:
                        gender_rec = int(input("1.Male 2.Female"))
                    except ValueError:
                        print(f"\nINVALID INPUT!")
                        continue
                    if gender_rec == 1:
                        gender = "Male"
                        break
                    elif gender_rec == 2:
                        gender = "Female"
                        break
                    else:
                        print("\nINVALID INPUT!")
                print(f"\n Current Email: {mail}")
                while True:
                    mail_in = input("Enter new email:")
                    confirm_format = checky(mail_in)
                    if confirm_format == 'y':
                        mail = mail_in
                        break
                    else:
                        print("\nINVALID EMAIL FORMAT")
                        continue
                print(f"\n Current Phone number: {tel}")
                while True:
                    tel_in = input("Enter new phone number: ")
                    confirm_pformat = check_numformat(tel_in)
                    if confirm_pformat == 'y':
                        tel = tel_in
                        break
                    else:
                        print("\nINVALID PHONE NUMBER FORMAT!")
                        continue
                updated_cus_list.append({"Customer_Name": cus_name, "Gender": gender, "Email": mail,
                                         "Phone_Number": tel})
                i = i + 1
            else:
                updated_cus_list.append(entry)
                i = i + 1
    with open(filename, "w") as json_file:
        json.dump(updated_cus_list, json_file, indent=4)
        print("CUSTOMER UPDATED SUCCESFULY!!")
        main_menu()


import connecting
import pymysql


# connect with existing database
# db connection 
mydb = pymysql.connect(host="localhost",user="root",password="",database="mydb2023")
mycursor = mydb.cursor()

status = True

while status:
    menu = """
                    MENU
            1) Store data
            2) View data
            3) Search data
            4) Update data
            5) Delete data
            6) EXIT
    
    """
    print(menu)

    choice = int(input("Enter your choice "))
    if choice==1:
        name = input("Enter your name : ")
        subject = input("Enter your subject : ")

        # quary
        query = "insert into student (name,subject) values ('%s','%s')"
        args = (name,subject)

        mycursor.execute(query%args)
        mydb.commit()

        print("successfully data inserted !!!")

    elif choice == 2:
        query = "select * from student"

        # execute query
        mycursor.execute(query)

        # store all data from db
        data = mycursor.fetchall()

        print(data)

    elif choice == 3:
        #fetch all data condition wise
        id = int(input("enter id :"))

        #query
        query="select * from student where id  = %5 "

        #args
        args = (id)

        mycursor.execute(query%args)

        #collext all data from table in a variable
        row = mycursor.fetchone()

        #id = 0 name = 1 subject = 2
        name = row[1]
        subject = row[2]

        print("name = ",name )
        print("subject = ",subject)

    elif choice == 4:
        #updata data
        id  = int(input("enter id :"))
        name = input("enter name :")
        subject= input("enter subject:")
        #query
        query = "update student set name ='%s' , set name = '%s' where id = %s"
        args = (name,subject,id)

        #exectue update query
        mycursor.execute(query%query)
        mydb.cursor()

        print("update successfull")
    elif choice == 5:

        #delete data

        id = int(input("enter id :"))

        #query 
        query = "delete from student where id = %s"

        #args
        args = (id)

        #execute query

        mycursor.execute(query%args)
        mydb.commit()
        print("successfull deleted")
        

    elif choice==6:
        status =False
    else :
        print("invalid input")

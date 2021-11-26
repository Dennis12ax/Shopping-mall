import mysql.connector
from datetime import datetime

cnx = mysql.connector.connect(user='root', password='xxxxxxxxx',host='localhost')
cursor = cnx.cursor()
cursor.execute("USE market")

def register_Mysql(input_id, input_name, input_email, input_phone, input_PW, separate):
    id = str(input_id)
    name = str(input_name)
    email = str(input_email)
    phone = str(input_phone)
    PW = str(input_PW)
    sepa = str(separate)
    cursor.execute("insert into user values ('"+id+"', '"+name+"','"+email+"','"+phone+"','"+PW+"',"+sepa+")")
    cnx.commit()


logged_in = 0

while(logged_in == 0):
    print("\n=================================================================================")
    flag = int(input("\nDo you have an account? (Yes : '1' , No : '0') : "))

    if(flag == 1): ## login
        print("\n=================================================================================\n")
        print("Please enter your ID and Password")
        user_id = str(input("ID : "))
        password = str(input("PassWord : "))
        cursor.execute("select count(*) from user where user_id = '"+user_id+"' and password = '"+password+"'")

        for c in cursor: 
            if(c[0] == 1):
                print("\n=================================================================================")
                print("\nYou are logged in.")
                logged_in = 1
            else:
                print("\n=================================================================================")
                print("\nPlease Check your ID or Password again.")
                print("\n=================================================================================\n")
    else: ## register account
        try:
            print("\n=================================================================================")
            print("Register your account by entering your personal information.")
            input_id = input("ID : ")
            input_name = input("Name : ")
            input_email = input("E-mail : ")
            input_phone = input("Phone Number : ")
            input_PW = input("PassWord : ")
            separate = input("Are you in self-quarantine?(if you are, please type '1' or '0') : ")
            register_Mysql(input_id, input_name, input_email, input_phone, input_PW, separate)
            print("\n=================================================================================\n")
            print("You have successfully registered an account. Please log in")
        except:
            print("This ID already exists. Please Change your ID.")

        

while(True):
    print("\n=================================================================================")
    print("\nThe function\n1 : Searching Product \n2 : Enter the product in your shopping cart. \n3 : Check your shopping cart \n4 : Delete the Shopping Cart \n5 : Confirm the purchase \n6 : Termination \n")
    function_flag = int(input("Please enter the Function you want : "))

    if function_flag == 1:
        product_id = []
        product_name = []
        description = []
        price = []
        early_delivery = []
        p_inventory = []
        cursor.execute("update product as P set P.soldout = 1 where exists (select * from p_inventory as I where I.quantity = 0 and I.product_id = P.product_id)")
        cnx.commit()

        cursor.execute("select product_id, name, description, price, early_delivery from product where soldout = 0")
        
        for c in cursor:
            product_id.append(c[0])
            product_name.append(c[1])
            description.append(c[2])
            price.append(c[3])
            early_delivery.append(c[4])

        i = 0
        for i in range(len(product_id)):
            cursor.execute("select quantity from p_inventory where product_id = '"+product_id[i]+"'")
            for c in cursor:
                p_inventory.append(c[0])
        
        i = 0
        for i in range(len(product_id)):
            if(early_delivery == 1):
                print("\n=================================================================================\n")
                print("Product NAME = "+product_name[i]+ "\nProduct ID = " + product_id[i] + "\nDescription = " + description[i]+"\nPrice = " + str(price[i]) + " Won\nStock = " +str(p_inventory[i])+" \nThis Product can early deliver.")
            else:
                print("\n=================================================================================\n")
                print("Product NAME = "+product_name[i]+ "\nproduct ID = " + product_id[i] + "\nDescription = " + description[i]+"\nPrice = " + str(price[i]) + " Won\nStock = " +str(p_inventory[i])+" \nThis Product can not early deliver.")

        print("\n=================================================================================")

        cate_id = []
        cate_name = []
        cate_desc = []
        cate_flag = int(input("\nDo you want to search for products using categories? (YES : 1, NO : 0) : "))
        if cate_flag == 1:
            cursor.execute("select * from p_category")
            for c in cursor:
                cate_id.append(c[0])
                cate_name.append(c[1])
                cate_desc.append(c[2])
            
            for i in range(len(cate_id)):
                print("\n=================================================================================\n")
                print( "Category NAME : "+cate_name[i]+"\nCategory ID : "+cate_id[i]+"    \nDescription : "+cate_desc[i]+" ")
            
            print("\n=================================================================================\n")
            want_cate = input("Please Enter the Category ID you want :")

            product_id = []
            product_name = []
            description = []
            price = []
            early_delivery = []
            p_inventory = []
            cursor.execute("select product_id, name, description, price, early_delivery from product where category_id = '"+want_cate+"' and soldout = '0'")
        
            for c in cursor:
                product_id.append(c[0])
                product_name.append(c[1])
                description.append(c[2])
                price.append(c[3])
                early_delivery.append(c[4])

            i = 0
            for i in range(len(product_id)):
                cursor.execute("select quantity from p_inventory where product_id = '"+product_id[i]+"'")
                for c in cursor:
                    p_inventory.append(c[0])
        
            i = 0
            for i in range(len(product_id)):
                if(early_delivery == 1):
                    print("\n=================================================================================")
                    print("\nProduct NAME = "+product_name[i]+ "\nProduct ID = " + product_id[i] + "\nDescription = " + description[i]+"\nPrice = " + str(price[i]) + "Won\nStock = " +str(p_inventory[i])+"\nThis Product can early deliver.")
                else:
                    print("\n=================================================================================")
                    print("\nProduct NAME = "+product_name[i]+ "\nProduct ID = " + product_id[i] + "\nDescription = " + description[i]+"\nPrice = " + str(price[i]) + "Won\nStock = " +str(p_inventory[i])+"\nThis Product can not early deliver.")

            print("\n=================================================================================")

    elif function_flag == 2:
      
        qt_flag = 0
        while(qt_flag == 0):
            
            print("\n=================================================================================")
            product_id = str(input("\nPlease enter the ID of the product you want to buy : "))
            quantity = int(input("Please Enter the Desired Number of the Products : "))
            
            cursor.execute("select quantity from p_inventory where product_id = '"+product_id+"'")
            for c in cursor:
                p_inventory = c[0]

            if quantity > int(p_inventory):
                print("\n=================================================================================")
                print("\nWe don't have enough stock. Please check again.")
            else:
                qt_flag = 1
        
        cursor.execute("select self_qaurantine from user where user_id ='"+user_id+"'")
        for c in cursor:
            self_flag = c[0]

        cursor.execute("select price from product where product_id = '"+product_id+"'")
        for c in cursor:
            price = c[0]


        cart_id = datetime.now().strftime('%Y%m%d%H%M%S') + "_"+user_id +"_"+ product_id
        if(self_flag == 1):
            cursor.execute("insert into shopping_cart values ('"+cart_id+"', '"+user_id+"', '"+product_id+"', '"+ str(0.9*price*quantity) +"', "+ str(quantity)+", null)")
            cnx.commit()
            print("\n=================================================================================")
            print("\nSince you are a self-quarantined person, The Product was put in your shopping cart at a 10 percent discount. \n"+ str(int(0.9*price*quantity)) + " Won")

        else:
            cursor.execute("insert into shopping_cart values ('"+cart_id+"', '"+user_id+"', '"+product_id+"', '"+ str(int(price*quantity)) +"', "+ str(quantity)+", null)")
            cnx.commit()
            print("\n=================================================================================")
            print("\nThe Product was put in your shopping cart.\n"+ str(price*quantity) + " Won")
            


    elif function_flag == 3:
        cursor.execute("select * from shopping_cart where user_id = '"+user_id+"' and order_id is null;")
        cart_id = []
        product_id = []
        price = []
        quantity = []
        product_name = []
        for c in cursor:
            cart_id.append(c[0])
            product_id.append(c[2])
            price.append(c[3])
            quantity.append(c[4])

        for p_id in product_id:
            cursor.execute("select name from product where product_id = '"+p_id+"'")
            for c in cursor:
                product_name.append(c[0])

        for i in range(len(product_id)):
            print("\n=================================================================================")
            print("\nCart_ID = "+cart_id[i]+"\nProduct NAME = '"+product_name[i]+"' \nQuantity = '"+str(quantity[i])+"'\nTotal Price = '"+str(price[i])+"' Won ")

    elif function_flag == 4: ## delete

        print("\n=================================================================================")
        whatCartId = str(input(
            "\nPlease enter the cart_id of the product you want to delete : "))
        isSure = int(input("Are you sure? (Yes : 1, No : 0) : "))
        print("\n=================================================================================")

        # checking
        if isSure != 1:
            continue

        cursor.execute("delete from shopping_cart where cart_id ='"+whatCartId+"'")
        print("\n=================================================================================")
        print("\nThe Shopping Cart has been successfully deleted.")
        cnx.commit()
        
    elif function_flag == 5:
        print("\n=================================================================================")
        whatCartId = str(input(
            "\nPlease enter the cart_id of the product you want to order: "))
        isSure = int(input("Are you sure ? (Yes : 1, No : 0) : "))
        print("\n=================================================================================")

        # checking
        if isSure != 1:
            continue

        cursor.execute(
            "select S.quantity, I.quantity, I.product_id from shopping_cart as S, p_inventory as I where S.product_id = I.product_id and S.cart_id = '" + whatCartId + "'")
        for c in cursor:
            orderInventory = c[0]
            restInventory = c[1]
            whatProductId = c[2]

        # checking
        if orderInventory > restInventory:
            print("\nWe don't have enough stock. Please check again.")
            continue

        order_id = datetime.now().strftime('%Y%m%d%H%M%S') + "_" + user_id + "_order"
        # order_product 추가
        cursor.execute("insert into order_product values ('" + order_id + "', '" + user_id
                       + "', '" + datetime.now().strftime("%Y%m%d") + "')")
        # shopping_cart에 order_id 업데이트
        cursor.execute("update shopping_cart set order_id='" +
                       order_id + "' where cart_id='" + whatCartId + "'")
        # 재고 업데이트
        cursor.execute("update p_inventory set quantity=quantity-'" +
                       str(orderInventory) + "' where product_id='" + whatProductId + "'")
        cnx.commit()
        print("\n=================================================================================")
        print("\nYour order has been successful.")
        print("\n=================================================================================")

    elif function_flag == 6:
        print("\n=================================================================================")
        print("\nThank you for using our shopping mall.")
        print("\n=================================================================================")
        break

    else:
        print("\n=================================================================================")
        print("\nYou've entered something wrong. Please Enter again.")
        print("\n=================================================================================")
        




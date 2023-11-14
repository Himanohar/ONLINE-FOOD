actfile=None
actfile_details=None
print("1.egg biryani         2.egg dum biryani      3.chicken biryani 4.chicken dum biryani")
print("4.mutton biryani      5.mutton dum biryani   6.fish biryani    7.frnas biryani      ")




#********** HELLO THE PROGRAM IS BELONGS TO SGIN_U AND LOGIN OPERATION************
def uadd():
   d={"name":input(str("enter the name:")),
      "email":input(str("enter the email: ")),
      "age":input(("enter the age:")),
      "phone:":input(("enter the phone:"))}

   import csv
   fp=open(r"C:\Users\rajko\OneDrive\Desktop\files_csv-programs\usd.csv",'a',newline="")
   write=csv.DictWriter(fp,['name',"age",'email',"phone:"])
   # write.writeheader()
   write.writerow(d)
   print(" your succesfully registerd")
   fp.close()
#uadd()


def id():
    global actfile
    u=input("enter the username:")
    p=input("enter the password:")
    import csv
    fp=open(r"C:\Users\rajko\OneDrive\Desktop\files_csv-programs\usd.csv","r")
    res=csv.DictReader(fp)
    count=0
    count1=0
    for i in res:
        if i["email"]==u:
           count+=1
           if i["phone"]==p:
              actfile="WELCOM"
              actfile_details=i
              return "Thank you"
           else:
              return "user id is correct:",i["email"],"password is incorrect"
        if i["phone"]==p:
           count1+=1
    if count==0 and count1==0:
       return "username and password are incorrect"
    if count1==0:
       return "password is incorrect"
    if count==0:
       return "username is incorrect"
    
# res=id()
# print(res)
def log():
   s=['1) login','2)sign up']
   print("1.login     2.sign up")
   n=input("choose:")
   for i in s:
       if i[0]==n:
           if '1) login'==i:
               res=id()
               print(res)
           elif '2)sign up'==i:
               uadd()
#log()


#(MANU)***************************END*****************************************************(MANU)


#(SWAPNA)(START)***************THE BELOW OPERATION BELONGS TO CART***************(START)(SWAPNA) 
if actfile !=None:
    print(actfile)
def oddct():
    import csv
    fp=open(r"C:\Users\rajko\OneDrive\Desktop\files_csv-programs\cat_progarms\ctt.csv","r")
    write=csv.reader(fp)
    count=0
    for i in write:
        count+=1
        print(count,i[0],i[-1])
    fp.close()

    # the below code is belongs to delete the cart items  
    def del_cart():
        de=input("choose item:")
        import csv
        fp=open(r"C:\Users\rajko\OneDrive\Desktop\files_csv-programs\cat_progarms\ctt.csv","r")
        file=csv.reader(fp)
        store=[]
        conn=0
        Found=False
        for rec in file:
            conn+=1
            if str(conn)==str(de):
                Found=True
            else:
                store.append(rec)
        fp.close()
        if Found==False:
            print("The item no is not found")
        else:
            import csv
            fp=open(r"C:\Users\rajko\OneDrive\Desktop\files_csv-programs\cat_progarms\ctt.csv","w+",newline="")
            write=csv.writer(fp)
            write.writerows(store)
            fp.seek(0)
            lk=csv.reader(fp)
            for i in lk:
                print(i)
            fp.close()       
    #del_cart()

    # the below code is belongs to order items in cart
    def odcat():
        #n=input("choose item number:")
        #m=input("Quantity:")
        import csv
        fp=open(r"C:\Users\rajko\OneDrive\Desktop\files_csv-programs\cat_progarms\ctt.csv","r")
        write=csv.reader(fp)
        totalcost=0
        st=[]
        for j in write:
            st+=[j]
        lt=[]
        # append the uesr choosing item
        def ccho():
            con=0
            nonlocal lt
            n=input("enter the itemm no:")
            m=input("Quantity:")
            for i in st:
                con+=1
                if str(con)==n:
                    cq=[i[0],i[1],m,int(m)*int(i[-1])]
                    lt.append(cq)
        ccho()
        
        def u_decle():
            print("1.CONTINUE  2.BACK")
            N=int(input("enter no:"))
            while N==1:
                ccho()
                print("1.CONTINUE  2.BACK")
                N=int(input("enter no:"))
        u_decle()
        # conform order 
        def ot():
            nonlocal lt
            cost=0
            for b in lt:
                print(b[0],b[1],b[2],b[3])
                cost+=int(b[-1])
            GST=cost*5//100
            print("GST",""*12,GST)
            print("total amount"," "*10,cost,"/-")
        ot()
        # user desision shopping continue or exit
        def cnet():
            nonlocal lt
            print("1.CONTINUE         2.EXIT")
            cone=input("enter the option no:")
            if cone==str(1):
                ccho()
            if cone==str(2):
                print(lt)
        #cnet()
        #print(lt)
    #odcat()
        
    # the below code is choosing the item for del or order in cart
    print("-"*50)
    print("1.DELETE     2.ORDER")
    print("-"*50)
    def choose():
        ch=["thanks","1","2"]
        ed=input("ENTER NO:")
        if str(ed)==str(ch[1]):
            del_cart()
        if str(ed)==str(ch[2]):
            odcat()
        else:
            print(ch[0])
    choose()
#oddct()#(SWAPNA)***END******#(SWAPNA)
actfile=None

if actfile!=None:
    log()
else:
    print("your not registerd")
    oddct()






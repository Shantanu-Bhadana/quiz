import random
import sqlite3
import time
from tkinter import messagebox
class quiz:
    def __init__(self):
        pass        
    
    def login(self):
        try:
            conobj=sqlite3.connect(database="quizing.sqlite")
            curobj=conobj.cursor()
            curobj.execute("create table data(gamer_no integer auto_increment,name text,pass text primary key,mail text,mob text)")
            curobj.execute("create table score(name text,point integer)")
            print("table created")
            
            
        except:
            print(" ")
        conobj.close()

        
        
        print("\t\t\t\tWELCOME TO MIND GAMES")
        time.sleep(2)
        acc=input("\t\tDo You Have Account?(Y/N)")
        if acc=='Y':
            print("\t\t\tLOGIN")
            print("--------------------------")
            user_name=input("USER\t:")
            user_pass=input("PASS\t:")
            print("--------------------------")
            
            conobj=sqlite3.connect(database="quizing.sqlite")
            curobj=conobj.cursor()
            curobj.execute("select name,pass from data where name=? and pass=?",(user_name,user_pass))
            tup=curobj.fetchall()
            curobj.close()
            if tup==[]:
                messagebox.showerror("Account","Not Have Account")
                time.sleep(5)
                
            else:
                class project:
                        def __init__(self):
                            self.count=0
                            self.pos_count=0
                            self.num=0
                            self.general={"what is the capital city of Australia?\na.hobart \nb.canberra \nc.darwin \nd.sydney":"b",
                                          "which planet is known as the 'Red Planet'?\na.earth \nb.jupiter \nc.mars \nd.satrun":"c",
                                          "In which country did the Olympic Gmaes originate?\na.india \nb.pakistan \nc.america \nd.greece":"d",
                                          "what is the chemical symbol for water?\na.co2 \nb.HO \nc.OX \nd.H2o":"d",
                                          "who painted the Mona Lisa?\na.Vincent van gogh \nb.Leonardo da Vinci \nc.pablo picasso \nd.micheloangelo":"b",
                                          "which country is known as the 'Land of the rising Sun'?\na.japan \nb.australia \nc.inda \nd.america":"a",
                                          "what is the hardest natural substance on earth?\na.mercury \nb.moissanite \nc.diamond \nd.topaz":"c",
                                          "In which year did the titanic sink?\na.1912 \nb.1947 \nc.1870 \nd.2000":"a",
                                          "what is the largest animal on earth?\na.shark \nb.elephant \nc.blue whale \nd.whale shark":"c"}

                            self.sport={"which country won the first FIFA world cup in 1930?\na.uruguay \nb.brazil \nc.italy \nd.argentina":"a",
                                        "In tennis,what is the term for a score of 40-40?\na.advantage \nb.deuce \nc.break \nd.love":"b",
                                        "How many players are there in a rugby team?\na.17 \nb.15 \nc.11 \nd.14":"b",
                                        "Which NBA player is known as 'king James'?\na.LeBron James \nb.Kobe Bryant \nc.Michael jordan \nd.Kevin Durant":"a",
                                        "Which sport is often called 'the beautiful game'?\na.basketball \nb.tennis \nc.rugby \nd.Scooer(football)":"d",
                                        "who holds the record for the most goals in a single world cup tounament?\na.just fontaine \nb.Ronaldo \nc.Lionel messi \nd.miroslavklose":"a",
                                        "what sport uses a piece of equipment known as a 'puuter'?\na.tennis \nb.golf \nc.bowling \nd.cricket":"b",
                                        "In cricket, how many balls are here in an over?\na.7 \nb.4 \nc.6 \nd.8":"c"}

                            self.maths={"what is 25% of 200?\na.100\nb.50\nc.76\nd.10":"b",
                                        "if a rectangle has a length of 8 cm and a width of 6 cm,what is its ares?\na.48 cmsqunit\nb.20 cmsqunit\nc.60 cmsqunit\nd.45 cmsqunit":"a",
                                        "what is the next prime number of after 13?\na.21 \nb.43 \nc.23 \nd.17":"d",
                                        "solve for x: 3x+5=20?\na.10 \nb.34 \nc.5 \nd.12":"5",
                                        "what is the square root of 144?\na.12 \nb.36 \nc.23 \nd.10":"a",
                                        "if 5 apples cost $10, how much would 8 apples cost?\na.$12 \nb.$16 \nc.$23 \nd.$8":"b",
                                        "simplify the fraction:45/60?\na.2/4 \nb.4/7 \nc.3/4 \nd.1/2":"c",
                                        "A train travels 240 ,iles in 4 hours. what is its average speed?\na.60 miles per hour\nb. 30 miles per hour\nc.65 miles per hour \nd.87 miles per hour":"a",
                                        "If two angles of a triangle are 45 and 55, what is the measure of the third angle?\na.180 \nb.90 \nc.45 \nd.80":"d",
                                        "what is the half of 2+2?\na.2 \nb.6 \nc.1 \nd.3":"d"}

                            self.reasoning={"What comes next in the sequence:2,6,12,20,30,?\na.36 \nb.42 \nc.40 \nd.48":"b",
                                           "If APPLE is coded as 52235, what is the code for GRAPE?\na.71535 \nb.71355 \nc.71525 \nd.72535":"a",
                                           "Find the odd one out:Dog, Cat, Cow, Elephant, Bird?\na.Dog \nb.Cat \nc.Cow \nd.Bird":"d",
                                           "If john is 5 years older than mary and the sum of their ages is 25, how old is mary?\na.10 \nb.12 \nc.15 \nd.20":"a",
                                           "if 5+3=28,9+1=810,and 8+6=214, then what is 7+3?\na.1021 \nb.1050 \nc.1073 \nd.1040":"a",
                                           "A man walked 30 metres south,turned left,walked 20 metres,turned left again,and walked 30 metres . which direction is facing now?\na.North \nb.South \nc.East \nd.West":"a",
                                           "In a family of six, A is married to B. They have two children,C and D. C is married to E, and they have a child F. how is F related to B?\na.Grandson \nb.Son \nc.Granddaughter \nd.Nephew":"c",
                                           "what number should come next in the pattern:1,4,9,16,25,?\na.30 \nb.35 \nc.36 \nd.40":"c",
                                           "A clock shows 10:15. if the minute hand is rotated 90 degrees clockwise, what time wll it show?\na.10:45 \nb.10:30 \nc.11:00 \nd.11:15":"b",
                                           "If a car travels 60 km in 1.5 hours, what is its average speed?\na.30 km/h \nb.40 km/h \nc.50 km/h \nd.60 km/h":"b"}
                            
                        def general1(self):
                                print("\t\t\twelcome to General quiz")
                                time.sleep(2)
                                while True:
                                    self.count+=1
                                    self.num+=1
                                    question,answer=random.choice(list(self.general.items()))
                                    print("{}):{}".format(self.num,question))
                                    ans=input()
                                    if answer==ans:
                                        self.pos_count+=1
                                        print("congrats,right answer")
                                        conobj=sqlite3.connect(database="quizing.sqlite")
                                        curobj=conobj.cursor()
                                        curobj.execute("update score set point=point+10 where name=?",(user_name,))
                                        conobj.commit()
                                        conobj.close()
                                        
                                    else:
                                        print("wrong answer\nRight answer is {}".format(answer))
                                        conobj=sqlite3.connect(database="quizing.sqlite")
                                        curobj=conobj.cursor()
                                        curobj.execute("update score set point=point-5 where name=?",(user_name,))
                                        conobj.commit()
                                        conobj.close()


                                    option=int(input("press 0,for next question"))
                                    if (option):
                                        break

                                
                                conobj=sqlite3.connect(database="quizing.sqlite")
                                curobj=conobj.cursor()
                                curobj.execute("select * from score where name=?",(user_name,))
                                tup=curobj.fetchone()
                                print("\n\n Total Score Point :\t",end=" ")
                                
                                for i in tup:
                                    print(i,end=" ")
                                    
                                conobj.close()
                                print("\t\t\t\n\nScore")
                                #time.sleep(2)
                                print("Total answer={}".format(self.count))
                                print("Total Right Answer={}".format(self.pos_count))        
                                print("Score="+ str((self.pos_count/self.count)*100) +"%")
                                time.sleep(6)
                                
                            
                        def sports(self):
                                print("\t\t\twelcome to Sports quiz")
                                time.sleep(2)
                                while True:
                                    self.count+=1
                                    self.num+=1
                                    question,answer=random.choice(list(self.sport.items()))
                                    print("{}):{}".format(self.num,question))
                                    ans=input()

                                    if answer==ans:
                                        self.pos_count+=1
                                        print("congrats,right answer")
                                        conobj=sqlite3.connect(database="quizing.sqlite")
                                        curobj=conobj.cursor()
                                        curobj.execute("update score set point=point+10 where name=?",(user_name,))
                                        conobj.commit()
                                        conobj.close()
                                        

                                    else:
                                        print("sorry,wrong answer\nRight answer is {}".format(answer))
                                        conobj=sqlite3.connect(database="quizing.sqlite")
                                        curobj=conobj.cursor()
                                        curobj.execute("update score set point=point-5 where name=?",(user_name,))
                                        conobj.commit()
                                        conobj.close()



                                    option=int(input("press 0,for next question"))
                                    if (option):
                                        break

                                
                                conobj=sqlite3.connect(database="quizing.sqlite")
                                curobj=conobj.cursor()
                                curobj.execute("select * from score where name=?",(user_name,))
                                tup=curobj.fetchone()
                                print("\n\nTotal Score Point :\t",end=" ")
                                
                                for i in tup:
                                    print(i,end=" ")
                                    
                                conobj.close()
                                print("\t\t\t\n\nScore")
                                #time.sleep(2)
                                print("Total answer={}".format(self.count))
                                print("Total Right Answer={}".format(self.pos_count))        
                                print("Score="+str((self.pos_count/self.count)*100)+" %")
                                time.sleep(6)

                        def mathematics(self):
                                print("\t\t\twelcome to mathematical quiz")
                                time.sleep(2)
                                while True:
                                    self.count+=1
                                    self.num+=1
                                    question,answer=random.choice(list(self.maths.items()))
                                    print("{}):{}".format(self.num,question))
                                    ans=input()
                                    if answer==ans:
                                        print("congrats,right answer")

                                        self.pos_count+=1
                                        conobj=sqlite3.connect(database="quizing.sqlite")
                                        curobj=conobj.cursor()
                                        curobj.execute("update score set point=point+10 where name=?",(user_name,))
                                        conobj.commit()
                                        conobj.close()
                                        

                                    else:
                                        print("sorry,wrong answer\nRight answer is {}".format(answer))
                                        conobj=sqlite3.connect(database="quizing.sqlite")
                                        curobj=conobj.cursor()
                                        curobj.execute("update score set point=point-5 where name=?",(user_name,))
                                        conobj.commit()
                                        conobj.close()


                                    option=int(input("press 0,for next question"))
                                    if option:
                                        break

                                
                                conobj=sqlite3.connect(database="quizing.sqlite")
                                curobj=conobj.cursor()
                                curobj.execute("select * from score where name=?",(user_name,))
                                tup=curobj.fetchone()
                                print("\n\nTotal Score Point :\t",end=" ")
                                
                                for i in tup:
                                    print(i,end=" ")
                                    
                                conobj.close()
                                print("\t\t\t\n\nScore")
                                #time.sleep(2)
                                print("Total answer={}".format(self.count))
                                print("Total Right Answer={}".format(self.pos_count))
                                print("Score="+str((self.pos_count/self.count)*100)+" %")
                                time.sleep(6)

                        def reason(self):
                                print("\t\t\tWelcome To Reasoning Quiz")
                                time.sleep(2)
                                while True:
                                    self.count+=1
                                    self.num+=1
                                    question,answer=random.choice(list(self.reasoning.items()))
                                    print("{}):{}".format(self.num,question))
                                    ans=input()
                                    if answer==ans:
                                        print("congrats,right answer")
                                        self.pos_count+=1
                                        conobj=sqlite3.connect(database="quizing.sqlite")
                                        curobj=conobj.cursor()
                                        curobj.execute("update score set point=point+10 where name=?",(user_name,))
                                        conobj.commit()
                                        conobj.close()
                                        

                                    else:
                                        print("sorry,wrong answer\nRight Anwer is {}".format(answer))
                                        conobj=sqlite3.connect(database="quizing.sqlite")
                                        curobj=conobj.cursor()
                                        curobj.execute("update score set point=point-5 where name=?",(user_name,))
                                        conobj.commit()
                                        conobj.close()


                                    option=int(input("press 0,for next queston"))
                                    if option:
                                        break

                                
                                conobj=sqlite3.connect(database="quizing.sqlite")
                                curobj=conobj.cursor()
                                curobj.execute("select * from score where name=?",(user_name,))
                                tup=curobj.fetchone()
                                print("\n\nTotal Score Point :\t",end=" ")
                                
                                for i in tup:
                                    print(i,end=" ")
                                    
                                conobj.close()
                                print("\t\t\t\n\nScore")
                                #time.sleep(2)
                                print("Total answer={}".format(self.count))
                                print("Total Right Answer={}".format(self.pos_count))
                                print("Score="+str((self.pos_count/self.count)*100)+" %")
                                time.sleep(6)
                                
                                
                        def profile(self):
                            conobj=sqlite3.connect(database="quizing.sqlite")
                            curobj=conobj.cursor()
                            #print("|Gamer_No |","|Name|","  |Password|","   |mail|","  |mobile|","  |point|")
                            curobj.execute("select * from data where name=?",(user_name,))
                            tup=curobj.fetchone()
                            print("|Gamer_No| {}       |".format(tup[0]))
                            print("|Name    | {}  |".format(tup[1]))
                            print("|Password| {}   |".format(tup[2]))
                            print("|Mail    | {}       |".format(tup[3]))
                            print("|Mobile  | {}    |".format(tup[4]))
                            curobj.execute("select point from score where name=?",(user_name,))
                            tup1=curobj.fetchone()
                            print("Point    | {}        |".format(tup1[0]))
                            conobj.close()
                            
                            logout=input("Want To Logout?(Y/N)")
                            if logout=='Y':
                                conobj=sqlite3.connect(database="quizing.sqlite")
                                curobj=conobj.cursor()
                                curobj.execute("delete from data where name=?",(user_name,))
                                curobj.execute("delete from score where name=?",(user_name,))
                                conobj.commit()
                                conobj.close()
                                print("\t\t\t|| LOGOUT ||")
                                time.sleep(6)
                                
                            elif logout=='N':
                                p=project()
                                ch=int(input("press: \n-0 for general quiz question \n-1 for sports quiz question \n-2 for mathematics quiz question \n-3 for reasoning quiz question \n-4 for Profile"))

                                match ch:
                                    case 0:
                                        p.general1()

                                    case 1:
                                        p.sports()

                                    case 2:
                                        p.mathematics()

                                    case 3:
                                        p.reason()
                                        
                                    case 4:
                                        print("Profile")
                                        p.profile()


                                    case _ :
                                        print("There is no such options")
                                        
                                        
                            else:
                                messagebox.showerror("Logout","There is no such option")
                                
                for i in range(3):
                            x=int(input("\tenter 0,To play game"))
                            if x==0:
                                p=project()
                                ch=int(input("press: \n-0 for general quiz question \n-1 for sports quiz question \n-2 for mathematics quiz question \n-3 for reasoning quiz question \n-4 for Profile"))

                                match ch:
                                    case 0:
                                        p.general1()
                                        
                                        while True:
                                                again=int(input("\t\t\t PLAY AGAIN (Press 0)"))
                                                if again==0:
                                                    p=project()
                                                    ch=int(input("press: \n-0 for general quiz question \n-1 for sports quiz question \n-2 for mathematics quiz question \n-3 for reasoning quiz question \n-4 for Profile"))

                                                    match ch:
                                                        case 0:
                                                            p.general1()

                                                        case 1:
                                                            p.sports()

                                                        case 2:
                                                            p.mathematics()

                                                        case 3:
                                                            p.reason()

                                                        case 4:
                                                            print("Profile")
                                                            p.profile()

                                                        case _ :
                                                            messagebox.showerror("Login","There is no such option")
                                                            
                                                elif again:
                                                    messagebox.showerror("Logout","Thank You")
                                                    break
                                                    

                                        

                                    case 1:
                                        p.sports()
                                        while True:
                                                again=int(input("\t\t\t PLAY AGAIN (Press 0)"))
                                                if again==0:
                                                    p=project()
                                                    ch=int(input("press: \n-0 for general quiz question \n-1 for sports quiz question \n-2 for mathematics quiz question \n-3 for reasoning quiz question \n-4 for Profile"))

                                                    match ch:
                                                        case 0:
                                                            p.general1()

                                                        case 1:
                                                            p.sports()

                                                        case 2:
                                                            p.mathematics()

                                                        case 3:
                                                            p.reason()

                                                        case 4:
                                                            print("Profile")
                                                            p.profile()

                                                        case _ :
                                                            messagebox.showerror("Login","There is no such option")
                                                            
                                                elif again:
                                                    messagebox.showerror("Logout","Thank You")
                                                    break
                                        

                                    case 2:
                                        p.mathematics()
                                        while True:
                                                again=int(input("\t\t\t PLAY AGAIN (Press 0)"))
                                                if again==0:
                                                    p=project()
                                                    ch=int(input("press: \n-0 for general quiz question \n-1 for sports quiz question \n-2 for mathematics quiz question \n-3 for reasoning quiz question \n-4 for Profile"))

                                                    match ch:
                                                        case 0:
                                                            p.general1()

                                                        case 1:
                                                            p.sports()

                                                        case 2:
                                                            p.mathematics()

                                                        case 3:
                                                            p.reason()

                                                        case 4:
                                                            print("Profile")
                                                            p.profile()

                                                        case _ :
                                                            messagebox.showerror("Login","There is no such option")
                                                            
                                                elif again:
                                                    messagebox.showerror("Logout","Thank You")
                                                    break
                                        

                                    case 3:
                                        p.reason()
                                        while True:
                                                again=int(input("\t\t\t PLAY AGAIN (Press 0)"))
                                                if again==0:
                                                    p=project()
                                                    ch=int(input("press: \n-0 for general quiz question \n-1 for sports quiz question \n-2 for mathematics quiz question \n-3 for reasoning quiz question \n-4 for Profile"))

                                                    match ch:
                                                        case 0:
                                                            p.general1()

                                                        case 1:
                                                            p.sports()

                                                        case 2:
                                                            p.mathematics()

                                                        case 3:
                                                            p.reason()

                                                        case 4:
                                                            print("Profile")
                                                            p.profile()

                                                        case _ :
                                                            messagebox.showerror("Login","There is no such option")
                                                            
                                                elif again:
                                                    messagebox.showerror("Logout","Thank You")
                                                    break
                                        
                                        
                                    case 4:
                                        print("Profile")
                                        p.profile()

                                    case _ :
                                        messagebox.showerror("Login","There is no such option")

                                break

                            else:
                                print("\t\t\tpress 0,for playing")


                 



            
    



        
    
            
        elif acc=='N':
            make_acc=input("Press 0,For Create Account")
            time.sleep(1)
            if make_acc=='0':
                    conobj=sqlite3.connect(database="quizing.sqlite")
                    curobj=conobj.cursor()

                    gnum=int(input("Enter Gamer Number: "))
                    gn=input("Enter Gamer Name: ")
                    gp=input("Enter Gamer Passwaord: ")
                    gm=input("Enter Gamer Gmail_id: ")
                    gmob=input("Enter Gamer Mobile: ")

                    curobj.execute("insert into data values(?,?,?,?,?)",(gnum,gn,gp,gm,gmob))
                    curobj.execute("insert into score values(?,?)",(gn,'0'))
                    print("inserted")
                    conobj.commit()
                    conobj.close()

                    clear=input("Enter 0,BACK")
                    if clear=='0':
                        q.login()

                    else:
                        messagebox.showerror("logout","Thank You")
                        
                        
            else:
                messagebox.showerror("Login","There is no such option")
                time.sleep(2)
                
                
        else:
            messagebox.showerror("Login","There is no such option")

                
                
            
        
            
        
            

q=quiz()
q.login()
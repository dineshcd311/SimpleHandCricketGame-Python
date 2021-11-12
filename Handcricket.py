import random
import sys
from colorama import Fore, Back, Style
commentry=["lazy Single","Quick two","Quick three","Boundary!!","Single+overthrow","Out of the Park"]
doing=0
total_score_ba=0
total_score_bo=0
def bat(doing):
    global total_score_ba
    print("You're batting,Cheers!!")
    print("______________________________________________________")
    total_score_ba=0
    while(True):
        print(Fore.GREEN,"Your score ",total_score_ba,Style.RESET_ALL)
        if doing==1:
            if total_score_bo-total_score_ba<0:
                print(Fore.GREEN,"______________________________________________________",Style.RESET_ALL)
                print(Fore.GREEN,"You Won by a wicket",Style.RESET_ALL)
                print(Fore.GREEN,"______________________________________________________",Style.RESET_ALL)
                sys.exit()
            elif total_score_bo-total_score_ba!=0 and total_score_bo-total_score_ba!=1:
                print("You need",Fore.RED,total_score_bo-total_score_ba,Style.RESET_ALL,"runs to win")
            elif total_score_bo-total_score_ba==1:
                print("You need",Fore.RED,total_score_bo-total_score_ba,Style.RESET_ALL,"run to win")
            else:
                print(Fore.BLUE,"The scores are level",Style.RESET_ALL)
        y_ip=int(input("1 to 6 : "))
        s_ip=random.randint(1,6)
        print("System's turn : ",s_ip)
        if y_ip == s_ip:
            print(Fore.MAGENTA,"______________________________________________________",Style.RESET_ALL)
            print(Fore.RED,"You're gone ")
            print(" You've scored ",total_score_ba,Style.RESET_ALL)
            print(Fore.MAGENTA,"______________________________________________________",Style.RESET_ALL)
            break
        elif y_ip!=s_ip and (y_ip in [1,2,3,4,5,6]):
            print(Fore.LIGHTMAGENTA_EX,commentry[y_ip-1],Style.RESET_ALL)
            total_score_ba+=y_ip
        else:
            print(Fore.RED,"Wrong input , you're banned!",Style.RESET_ALL)
            sys.exit()
    if doing==1:
        return total_score_bo-total_score_ba
def bowl(doing):
    global total_score_bo
    print("You're bowling,Cheers!!")
    print("______________________________________________________")
    total_score_bo=0
    while(True):
        print(Fore.RED,"System's Score : ",total_score_bo,Style.RESET_ALL)
        if doing==1:
            if total_score_ba-total_score_bo<0:
                print(Fore.RED,"______________________________________________________",Style.RESET_ALL)
                print(Fore.RED,"System won by a wicket",Style.RESET_ALL)
                print(Fore.RED,"______________________________________________________",Style.RESET_ALL)
                sys.exit()
            elif total_score_ba-total_score_bo!=0 and total_score_ba-total_score_bo!=1:
                print("System needs",Fore.RED,total_score_ba-total_score_bo,Style.RESET_ALL,"run to win")
            elif  total_score_ba-total_score_bo==1:
                print("System needs",Fore.RED,total_score_ba-total_score_bo,Style.RESET_ALL,"run to win")
            else:
                print(Fore.BLUE,"The scores are level",Style.RESET_ALL)
        y_ip=int(input("1 to 6 : "))
        s_ip=random.randint(1,6)
        print("System's turn : ",s_ip)
        if y_ip == s_ip:
            print(Fore.MAGENTA,"______________________________________________________",Style.RESET_ALL)
            print(Fore.GREEN,"System's gone")
            print(" System's score",total_score_bo,Style.RESET_ALL)
            print(Fore.MAGENTA,"______________________________________________________",Style.RESET_ALL)
            break
        elif y_ip!=s_ip and (y_ip in [1,2,3,4,5,6]):
            print(Fore.LIGHTMAGENTA_EX,commentry[s_ip-1],Style.RESET_ALL)
            total_score_bo+=s_ip
        else:
            print(Fore.RED,"Wrong input , you're banned!",Style.RESET_ALL)
            sys.exit()
    if doing==1:
        return total_score_ba-total_score_bo
name=input("Enter your name:")
print("______________________________________________________")
print("Welcome to",Fore.RED,"HandCricket",Fore.GREEN,name,Style.RESET_ALL)
print("______________________________________________________")
print(Fore.RED,"Rules",Style.RESET_ALL,":  1 to 6 for runs , 1 and 2 for toss")
print("______________________________________________________")
print(Fore.GREEN,"It's time for toss",Style.RESET_ALL)
print("______________________________________________________")
while (True):
    print(Fore.LIGHTBLUE_EX,"1",Style.RESET_ALL,"for head",Fore.LIGHTBLUE_EX,"2",Style.RESET_ALL,"for tail : ")
    toss=int(input())
    print("______________________________________________________")
    randomtoss=random.randint(1,2)
    if toss==randomtoss and (toss==1 or toss==2): 
        while(True):
            print(Fore.GREEN,"You've won the toss , what would you like to do",Style.RESET_ALL)
            bat_or_bowl=int(input("1 - Bat , 2 - Bowl : "))
            print("______________________________________________________")
            if bat_or_bowl==1:
                print("You chose batting")
                print("______________________________________________________")
                bat(doing)
                print("______________________________________________________")
                print(Fore.YELLOW,"Target:",total_score_ba+1,Style.RESET_ALL)
                print("______________________________________________________")
                doing=1
                doer="System"
                z=bowl(doing)
                if z==0:
                    print(Fore.GREEN,"Match draw",Style.RESET_ALL)
                else:
                    print(Fore.GREEN,"______________________________________________________",Style.RESET_ALL)
                    if total_score_ba-total_score_bo!=1:
                        print(Fore.GREEN,"You Won by",total_score_ba-total_score_bo,Style.RESET_ALL,"runs")
                    else:
                        print(Fore.GREEN,"You Won by",total_score_ba-total_score_bo,Style.RESET_ALL,"run")
                    print(Fore.GREEN,"______________________________________________________",Style.RESET_ALL)
                break
            elif bat_or_bowl==2:
                print("You chose bowling")
                print("______________________________________________________")
                bowl(doing)
                print("______________________________________________________")
                print(Fore.YELLOW,"Target:",total_score_bo+1,Style.RESET_ALL)
                print("______________________________________________________")
                doing=1
                z=bat(doing)
                if z==0:
                    print(Fore.GREEN,"Match draw",Style.RESET_ALL)
                else:
                    print(Fore.GREEN,"______________________________________________________",Style.RESET_ALL)
                    if total_score_bo-total_score_ba!=1:
                        print(Fore.RED,"System Won by",total_score_bo-total_score_ba,Style.RESET_ALL,"runs")
                    else:
                        print(Fore.RED,"System Won by",total_score_bo-total_score_ba,Style.RESET_ALL,"run")
                    print(Fore.GREEN,"______________________________________________________",Style.RESET_ALL)
                break
            else:
                print("Please give valid input")
                continue
        break
    elif toss!=randomtoss and (toss==1 or toss==2):
        print(Fore.RED,"You've lost the toss",Style.RESET_ALL)
        bat_or_bowl=random.randint(1,2)
        if bat_or_bowl==1:
            print("System chose batting")
            print("______________________________________________________")
            bowl(doing)
            print("______________________________________________________")
            print(Fore.YELLOW,"Target:",total_score_bo+1,Style.RESET_ALL)
            print("______________________________________________________")
            doing=1
            z=bat(doing)
            if z==0:
                    print(Fore.GREEN,"Match draw",Style.RESET_ALL)
            else:
                print(Fore.GREEN,"______________________________________________________",Style.RESET_ALL)
                if total_score_bo-total_score_ba!=1:
                    print(Fore.RED,"System Won by",total_score_bo-total_score_ba,Style.RESET_ALL,"runs")
                else:
                    print(Fore.RED,"System Won by",total_score_bo-total_score_ba,Style.RESET_ALL,"run")
                print(Fore.GREEN,"______________________________________________________",Style.RESET_ALL)
        elif bat_or_bowl==2:
            print("System chose bowling")
            print("______________________________________________________")
            bat(doing)
            print("______________________________________________________")
            print(Fore.YELLOW,"Target:",total_score_ba+1,Style.RESET_ALL)
            print("______________________________________________________")
            doing=1
            z=bowl(doing)
            if z==0:
                    print(Fore.GREEN,"Match draw",Style.RESET_ALL)
            else:
                print(Fore.GREEN,"______________________________________________________",Style.RESET_ALL)
                if total_score_ba-total_score_bo!=1:
                    print(Fore.GREEN,"You Won by",total_score_ba-total_score_bo,Style.RESET_ALL,"runs")
                else:
                    print(Fore.GREEN,"You Won by",total_score_ba-total_score_bo,Style.RESET_ALL,"run")
                print(Fore.GREEN,"______________________________________________________",Style.RESET_ALL)
        break
    else:
        print("Give proper Toss")
        print("______________________________________________________")
        continue
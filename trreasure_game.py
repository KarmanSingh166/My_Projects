import random
print("Welcome to Game!")
print("Enter 1 for Singleplayer")
print("Enter 2 for Multiplayer")
print("Enter 3 for row column game")
print("Enter 4 for Instructions")
mode=int(input("Enter a Number 1,2,3 or 4: "))
if mode<1 or mode>4:
    print("Bhai tujhe Angreji kam samajh me aati hai")
    print("Ye kya kar rha hai , Kyu apni jindgi barbad kar rha hai")
    print("Apne ghar ja , Apne Maa Baap se mafi maang or mar bhi kha lai")
    print("Ye sab band kr nhi to teri jindgi barbaad hai")
elif mode==2:
    gifts=" 1->🍗 2->🍔 3->🌭 4->🍕 5->⌚ 6->📱 7->💻 8->🖥 9->📷"
    print(gifts)
    gifty=int(input("Choose one gift to put it into the chest: "))
    x=5*gifty
    y=x-1
    gift=gifts[y]

    row1 = ["🎁️","️🎁️","️🎁️"]
    row2 = ["🎁️","🎁","️🎁️"]
    row3 = ["🎁️️","️🎁","🎁️️"]
    map = [row1, row2, row3]
    print(f"{row1}\n{row2}\n{row3}")
    print("At tenth digit there must be a column")
    print("At unit digit there must be a row")
    print("For eg if col=1 and row=2 then enter 12")
    position = input("Where do you want to put the gift? ")
    a=position[0]
    b=position[1]
    c=int(a)
    d=int(b)
    
    input("Hit enter and give laptop to second person now")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")

    print(f"{row1}\n{row2}\n{row3}")
    print("At tenth digit there must be a column")
    print("At unit digit there must be a row")
    print("For eg if col=1 and row=2 then enter 12")
    map[d-1][c-1]=gift
    guesser=input("In which box do you think the gift must be in: ")
    e=guesser[0]
    f=guesser[1]
    g=int(e)
    h=int(f)
    if c==g and d==h:
        print(f"{row1}\n{row2}\n{row3}")
        print("Congratulations you found the gift")
        print(f"You got {gift}")
    else:
        map[h-1][g-1]="🤪"
        print(f"{row1}\n{row2}\n{row3}\nSorry the gift was in {position} ")
        print("You got nothing")
        map[d-1][c-1]="💀"
        print(f"{row1}\n{row2}\n{row3}")

elif mode==1:
    gifts=" 1->🍗 2->🍔 3->🌭 4->🍕 5->⌚ 6->📱 7->💻 8->🖥 9->📷"
    #print(gifts)
    gifty=random.randint(1,9)
    x=5*gifty
    y=x-1
    gift=gifts[y]

    row1 = ["🎁️","️🎁️","️🎁️"]
    row2 = ["🎁️","🎁","️🎁️"]
    row3 = ["🎁️️","️🎁","🎁️️"]
    map = [row1, row2, row3]
    #print(f"{row1}\n{row2}\n{row3}")
    #position = input("Where do you want to put the gift? ")
    #a=position[0]
    #b=position[1]
    c=random.randint(1,3)
    d=random.randint(1,3)
    
    
    print(f"{row1}\n{row2}\n{row3}")
    print("At tenth digit there must be a column")
    print("At unit digit there must be a row")
    print("For eg if col=1 and row=2 then enter 12")
    map[d-1][c-1]=gift
    guesser=input("In which box do you think the gift must be in: ")
    e=guesser[0]
    f=guesser[1]
    g=int(e)
    h=int(f)
    if c==g and d==h:
        print(f"{row1}\n{row2}\n{row3}")
        print("Congratulations you found the gift")
        print(f"You got {gift}")
    else:
        map[h-1][g-1]="🤪"
        print(f"{row1}\n{row2}\n{row3}\nSorry the gift was in {c}{d} ")
        print("You got nothing")
        map[d-1][c-1]="💀"
        print(f"{row1}\n{row2}\n{row3}")
elif mode==3:
    print("Choose Difficulty")
    diffi=input("Enter E for easy and H for hard: ")
    difficulty=diffi.lower()
    score=0
    if difficulty=="e":
        gifts=" 1->🍗 2->🍔 3->🌭 4->🍕 5->⌚ 6->📱 7->💻 8->🖥 9->📷"
        #print(gifts)
        gifty=random.randint(1,9)
        x=5*gifty
        y=x-1
        gift=gifts[y]

        row1 = ["🎁️","️🎁️","️🎁️"]
        row2 = ["🎁️","🎁","️🎁️"]
        row3 = ["🎁️️","️🎁","🎁️️"]
        map = [row1, row2, row3]
        #print(f"{row1}\n{row2}\n{row3}")
        #position = input("Where do you want to put the gift? ")
        #a=position[0]
        #b=position[1]
        c=random.randint(1,3)
        d=random.randint(1,3)
        map[d-1][c-1]=gift
    
        print(f"{row1}\n{row2}\n{row3}")
        print("At tenth digit there must be a column")
        print("At unit digit there must be a row")
        print("For eg if col=1 and row=2 then enter 12")
        
        guesser=input("The box with gift is in which row and column?: ")
        e=guesser[0]
        f=guesser[1]
        g=int(e)
        h=int(f)
        if c==g and d==h:
            print(f"{row1}\n{row2}\n{row3}")
            print("Right")
            print("\n---------------------------------------------------\n")
            score=score+1
        else:
            map[h-1][g-1]="🤪"
            print(f"{row1}\n{row2}\n{row3}\nSorry the gift is in {c}{d} ")
            print("Your answer is wrong")
            map[d-1][c-1]="💀"
            print(f"{row1}\n{row2}\n{row3}")
            print("\n---------------------------------------------------\n")
        gifts=" 1->🍗 2->🍔 3->🌭 4->🍕 5->⌚ 6->📱 7->💻 8->🖥 9->📷"
        #print(gifts)
        gifty=random.randint(1,9)
        x=5*gifty
        y=x-1
        gift=gifts[y]

        row1 = ["🎁️","️🎁️","️🎁️"]
        row2 = ["🎁️","🎁","️🎁️"]
        row3 = ["🎁️️","️🎁","🎁️️"]
        map = [row1, row2, row3]
        #print(f"{row1}\n{row2}\n{row3}")
        #position = input("Where do you want to put the gift? ")
        #a=position[0]
        #b=position[1]
        c=random.randint(1,3)
        d=random.randint(1,3)
        map[d-1][c-1]=gift
    
        print(f"{row1}\n{row2}\n{row3}")
        print("At tenth digit there must be a column")
        print("At unit digit there must be a row")
        print("For eg if col=1 and row=2 then enter 12")
        
        guesser=input("The box with gift is in which row and column?: ")
        e=guesser[0]
        f=guesser[1]
        g=int(e)
        h=int(f)
        if c==g and d==h:
            print(f"{row1}\n{row2}\n{row3}")
            print("Right")
            print("\n---------------------------------------------------\n")
            score=score+1
        else:
            map[h-1][g-1]="🤪"
            print(f"{row1}\n{row2}\n{row3}\nSorry the gift is in {c}{d} ")
            print("Your answer is wrong")
            map[d-1][c-1]="💀"
            print(f"{row1}\n{row2}\n{row3}")
            print("\n---------------------------------------------------\n")
        gifts=" 1->🍗 2->🍔 3->🌭 4->🍕 5->⌚ 6->📱 7->💻 8->🖥 9->📷"
        #print(gifts)
        gifty=random.randint(1,9)
        x=5*gifty
        y=x-1
        gift=gifts[y]

        row1 = ["🎁️","️🎁️","️🎁️"]
        row2 = ["🎁️","🎁","️🎁️"]
        row3 = ["🎁️️","️🎁","🎁️️"]
        map = [row1, row2, row3]
        #print(f"{row1}\n{row2}\n{row3}")
        #position = input("Where do you want to put the gift? ")
        #a=position[0]
        #b=position[1]
        c=random.randint(1,3)
        d=random.randint(1,3)
        map[d-1][c-1]=gift
    
        print(f"{row1}\n{row2}\n{row3}")
        print("At tenth digit there must be a column")
        print("At unit digit there must be a row")
        print("For eg if col=1 and row=2 then enter 12")
        
        guesser=input("The box with gift is in which row and column?: ")
        e=guesser[0]
        f=guesser[1]
        g=int(e)
        h=int(f)
        if c==g and d==h:
            print(f"{row1}\n{row2}\n{row3}")
            print("Right")
            print("\n---------------------------------------------------\n")
            score=score+1
        else:
            map[h-1][g-1]="🤪"
            print(f"{row1}\n{row2}\n{row3}\nSorry the gift is in {c}{d} ")
            print("Your answer is wrong")
            map[d-1][c-1]="💀"
            print(f"{row1}\n{row2}\n{row3}")
            print("\n---------------------------------------------------\n")
        gifts=" 1->🍗 2->🍔 3->🌭 4->🍕 5->⌚ 6->📱 7->💻 8->🖥 9->📷"
        #print(gifts)
        gifty=random.randint(1,9)
        x=5*gifty
        y=x-1
        gift=gifts[y]

        row1 = ["🎁️","️🎁️","️🎁️"]
        row2 = ["🎁️","🎁","️🎁️"]
        row3 = ["🎁️️","️🎁","🎁️️"]
        map = [row1, row2, row3]
        #print(f"{row1}\n{row2}\n{row3}")
        #position = input("Where do you want to put the gift? ")
        #a=position[0]
        #b=position[1]
        c=random.randint(1,3)
        d=random.randint(1,3)
        map[d-1][c-1]=gift
    
        print(f"{row1}\n{row2}\n{row3}")
        print("At tenth digit there must be a column")
        print("At unit digit there must be a row")
        print("For eg if col=1 and row=2 then enter 12")
        
        guesser=input("The box with gift is in which row and column?: ")
        e=guesser[0]
        f=guesser[1]
        g=int(e)
        h=int(f)
        if c==g and d==h:
            print(f"{row1}\n{row2}\n{row3}")
            print("Right")
            print("\n---------------------------------------------------\n")
            score=score+1
        else:
            map[h-1][g-1]="🤪"
            print(f"{row1}\n{row2}\n{row3}\nSorry the gift is in {c}{d} ")
            print("Your answer is wrong")
            map[d-1][c-1]="💀"
            print(f"{row1}\n{row2}\n{row3}")
            print("\n---------------------------------------------------\n")
        gifts=" 1->🍗 2->🍔 3->🌭 4->🍕 5->⌚ 6->📱 7->💻 8->🖥 9->📷"
        #print(gifts)
        gifty=random.randint(1,9)
        x=5*gifty
        y=x-1
        gift=gifts[y]

        row1 = ["🎁️","️🎁️","️🎁️"]
        row2 = ["🎁️","🎁","️🎁️"]
        row3 = ["🎁️️","️🎁","🎁️️"]
        map = [row1, row2, row3]
        #print(f"{row1}\n{row2}\n{row3}")
        #position = input("Where do you want to put the gift? ")
        #a=position[0]
        #b=position[1]
        c=random.randint(1,3)
        d=random.randint(1,3)
        map[d-1][c-1]=gift
    
        print(f"{row1}\n{row2}\n{row3}")
        print("At tenth digit there must be a column")
        print("At unit digit there must be a row")
        print("For eg if col=1 and row=2 then enter 12")
        
        guesser=input("The box with gift is in which row and column?: ")
        e=guesser[0]
        f=guesser[1]
        g=int(e)
        h=int(f)
        if c==g and d==h:
            print(f"{row1}\n{row2}\n{row3}")
            print("Right")
            print("\n---------------------------------------------------\n")
            score=score+1
        else:
            map[h-1][g-1]="🤪"
            print(f"{row1}\n{row2}\n{row3}\nSorry the gift is in {c}{d} ")
            print("Your answer is wrong")
            map[d-1][c-1]="💀"
            
            print(f"{row1}\n{row2}\n{row3}")
            print("\n---------------------------------------------------\n")
        print(f"Your score is {score}/5")
        ###########################################
    elif difficulty=="h":
        print("Column Rows can be swapped")
        gifts=" 1->🍗 2->🍔 3->🌭 4->🍕 5->⌚ 6->📱 7->💻 8->🖥 9->📷"
        #print(gifts)
        gifty=random.randint(1,9)
        x=5*gifty
        y=x-1
        gift=gifts[y]

        row1 = ["🎁️","️🎁️","️🎁️"]
        row2 = ["🎁️","🎁","️🎁️"]
        row3 = ["🎁️️","️🎁","🎁️️"]
        map = [row1, row2, row3]
        #print(f"{row1}\n{row2}\n{row3}")
        #position = input("Where do you want to put the gift? ")
        #a=position[0]
        #b=position[1]
        c=random.randint(1,3)
        d=random.randint(1,3)
        e=random.randint(0,1000)
        swan=e
        if e%2==0:
            
            var="row"
            lit="column"
            ram=c
            c=d
            d=ram
            
        else:
            var="column"
            lit="row"
            

            
        map[d-1][c-1]=gift
    
        print(f"{row1}\n{row2}\n{row3}")
        print(f"At tenth digit there must be a {lit}")
        print(f"At unit digit there must be a {var}")
        print(f"For eg if {lit}=1 and {var}=2 then enter 12")
        
        guesser=input("The box with gift is in which row and column?: ")
        e=guesser[0]
        f=guesser[1]
        g=int(e)
        h=int(f)
        if swan%2==0:
            airp="c"
        else:
            rom=g
            g=h
            h=rom
        if c==g and d==h:
            print(f"{row1}\n{row2}\n{row3}")
            print("Right")
            print("\n---------------------------------------------------\n")
            score=score+1
        else:
            map[h-1][g-1]="🤪"
            print(f"{row1}\n{row2}\n{row3}\nSorry the gift is not in it ")
            print("Your answer is wrong")
            map[d-1][c-1]="💀"
            
            print(f"{row1}\n{row2}\n{row3}")
            print("\n---------------------------------------------------\n")
            print("Column Rows can be swapped")
        gifts=" 1->🍗 2->🍔 3->🌭 4->🍕 5->⌚ 6->📱 7->💻 8->🖥 9->📷"
        #print(gifts)
        gifty=random.randint(1,9)
        x=5*gifty
        y=x-1
        gift=gifts[y]

        row1 = ["🎁️","️🎁️","️🎁️"]
        row2 = ["🎁️","🎁","️🎁️"]
        row3 = ["🎁️️","️🎁","🎁️️"]
        map = [row1, row2, row3]
        #print(f"{row1}\n{row2}\n{row3}")
        #position = input("Where do you want to put the gift? ")
        #a=position[0]
        #b=position[1]
        c=random.randint(1,3)
        d=random.randint(1,3)
        e=random.randint(0,1000)
        swan=e
        if e%2==0:
            
            var="row"
            lit="column"
            ram=c
            c=d
            d=ram
            
        else:
            var="column"
            lit="row"
            

            
        map[d-1][c-1]=gift
    
        print(f"{row1}\n{row2}\n{row3}")
        print(f"At tenth digit there must be a {lit}")
        print(f"At unit digit there must be a {var}")
        print(f"For eg if {lit}=1 and {var}=2 then enter 12")
        
        guesser=input("The box with gift is in which row and column?: ")
        e=guesser[0]
        f=guesser[1]
        g=int(e)
        h=int(f)
        if swan%2==0:
            airp="c"
        else:
            rom=g
            g=h
            h=rom
        if c==g and d==h:
            print(f"{row1}\n{row2}\n{row3}")
            print("Right")
            print("\n---------------------------------------------------\n")
            score=score+1
        else:
            map[h-1][g-1]="🤪"
            print(f"{row1}\n{row2}\n{row3}\nSorry the gift is not in it ")
            print("Your answer is wrong")
            map[d-1][c-1]="💀"
            
            print(f"{row1}\n{row2}\n{row3}")
            print("\n---------------------------------------------------\n")
            print("Column Rows can be swapped")
        gifts=" 1->🍗 2->🍔 3->🌭 4->🍕 5->⌚ 6->📱 7->💻 8->🖥 9->📷"
        #print(gifts)
        gifty=random.randint(1,9)
        x=5*gifty
        y=x-1
        gift=gifts[y]

        row1 = ["🎁️","️🎁️","️🎁️"]
        row2 = ["🎁️","🎁","️🎁️"]
        row3 = ["🎁️️","️🎁","🎁️️"]
        map = [row1, row2, row3]
        #print(f"{row1}\n{row2}\n{row3}")
        #position = input("Where do you want to put the gift? ")
        #a=position[0]
        #b=position[1]
        c=random.randint(1,3)
        d=random.randint(1,3)
        e=random.randint(0,1000)
        swan=e
        if e%2==0:
            
            var="row"
            lit="column"
            ram=c
            c=d
            d=ram
            
        else:
            var="column"
            lit="row"
            

            
        map[d-1][c-1]=gift
    
        print(f"{row1}\n{row2}\n{row3}")
        print(f"At tenth digit there must be a {lit}")
        print(f"At unit digit there must be a {var}")
        print(f"For eg if {lit}=1 and {var}=2 then enter 12")
        
        guesser=input("The box with gift is in which row and column?: ")
        e=guesser[0]
        f=guesser[1]
        g=int(e)
        h=int(f)
        if swan%2==0:
            airp="c"
        else:
            rom=g
            g=h
            h=rom
        if c==g and d==h:
            print(f"{row1}\n{row2}\n{row3}")
            print("Right")
            print("\n---------------------------------------------------\n")
            score=score+1
        else:
            map[h-1][g-1]="🤪"
            print(f"{row1}\n{row2}\n{row3}\nSorry the gift is not in it ")
            print("Your answer is wrong")
            map[d-1][c-1]="💀"
            
            print(f"{row1}\n{row2}\n{row3}")
            print("\n---------------------------------------------------\n")
            print("Column Rows can be swapped")
        gifts=" 1->🍗 2->🍔 3->🌭 4->🍕 5->⌚ 6->📱 7->💻 8->🖥 9->📷"
        #print(gifts)
        gifty=random.randint(1,9)
        x=5*gifty
        y=x-1
        gift=gifts[y]

        row1 = ["🎁️","️🎁️","️🎁️"]
        row2 = ["🎁️","🎁","️🎁️"]
        row3 = ["🎁️️","️🎁","🎁️️"]
        map = [row1, row2, row3]
        #print(f"{row1}\n{row2}\n{row3}")
        #position = input("Where do you want to put the gift? ")
        #a=position[0]
        #b=position[1]
        c=random.randint(1,3)
        d=random.randint(1,3)
        e=random.randint(0,1000)
        swan=e
        if e%2==0:
            
            var="row"
            lit="column"
            ram=c
            c=d
            d=ram
            
        else:
            var="column"
            lit="row"
            

            
        map[d-1][c-1]=gift
    
        print(f"{row1}\n{row2}\n{row3}")
        print(f"At tenth digit there must be a {lit}")
        print(f"At unit digit there must be a {var}")
        print(f"For eg if {lit}=1 and {var}=2 then enter 12")
        
        guesser=input("The box with gift is in which row and column?: ")
        e=guesser[0]
        f=guesser[1]
        g=int(e)
        h=int(f)
        if swan%2==0:
            airp="c"
        else:
            rom=g
            g=h
            h=rom
        if c==g and d==h:
            print(f"{row1}\n{row2}\n{row3}")
            print("Right")
            print("\n---------------------------------------------------\n")
            score=score+1
        else:
            map[h-1][g-1]="🤪"
            print(f"{row1}\n{row2}\n{row3}\nSorry the gift is not in it ")
            print("Your answer is wrong")
            map[d-1][c-1]="💀"
            
            print(f"{row1}\n{row2}\n{row3}")
            print("\n---------------------------------------------------\n")
            print("Column Rows can be swapped")
        gifts=" 1->🍗 2->🍔 3->🌭 4->🍕 5->⌚ 6->📱 7->💻 8->🖥 9->📷"
        #print(gifts)
        gifty=random.randint(1,9)
        x=5*gifty
        y=x-1
        gift=gifts[y]

        row1 = ["🎁️","️🎁️","️🎁️"]
        row2 = ["🎁️","🎁","️🎁️"]
        row3 = ["🎁️️","️🎁","🎁️️"]
        map = [row1, row2, row3]
        #print(f"{row1}\n{row2}\n{row3}")
        #position = input("Where do you want to put the gift? ")
        #a=position[0]
        #b=position[1]
        c=random.randint(1,3)
        d=random.randint(1,3)
        e=random.randint(0,1000)
        swan=e
        if e%2==0:
            
            var="row"
            lit="column"
            ram=c
            c=d
            d=ram
            
        else:
            var="column"
            lit="row"
            

            
        map[d-1][c-1]=gift
    
        print(f"{row1}\n{row2}\n{row3}")
        print(f"At tenth digit there must be a {lit}")
        print(f"At unit digit there must be a {var}")
        print(f"For eg if {lit}=1 and {var}=2 then enter 12")
        
        guesser=input("The box with gift is in which row and column?: ")
        e=guesser[0]
        f=guesser[1]
        g=int(e)
        h=int(f)
        if swan%2==0:
            airp="c"
        else:
            rom=g
            g=h
            h=rom
        if c==g and d==h:
            print(f"{row1}\n{row2}\n{row3}")
            print("Right")
            print("\n---------------------------------------------------\n")
            score=score+1
        else:
            map[h-1][g-1]="🤪"
            print(f"{row1}\n{row2}\n{row3}\nSorry the gift is in not in it ")
            print("Your answer is wrong")
            map[d-1][c-1]="💀"
            
            print(f"{row1}\n{row2}\n{row3}")
            print("\n---------------------------------------------------\n")
        print(f"Your score is {score}/5")
    else:
        print("Bhai tujhe Angreji kam samajh me aati hai")
        print("Ye kya kar rha hai , Kyu apni jindgi barbad kar rha hai")
        print("Apne ghar ja , Apne Maa Baap se mafi maang or mar bhi kha lai")
        print("Ye sab band kr nhi to teri jindgi barbaad hai")
else:
    print(''' Rows are ------------------>
    Columns are |
                |
                |
                |
                |
                |
                |
                |
                |
                |
                v

                            Credits-Karman
                ''')



    



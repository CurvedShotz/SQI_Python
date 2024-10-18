#A simple USSD Application

#Activation
start = (input("Dial '*312#' to start : "))

if start == '*312#':
    print("Success.")

    sim = input("SIM1 / SIM2 : ").lower()

    if sim == 'sim1' or sim == 'sim2':
        user_input = input('''
                    1. Data Plans
                    2. Gift Data
                    3. Share Data
                    4. Check Data Bal
                    5. Voice/ Data Roaming Offers 
                      input: ''')
        user_input = str(user_input)
        if user_input == '1':
            scnd_inp = input('''
                1. Daily
                2. Weekly
                3. Monthly
                4. 2-3 Months
                5. Always ON
            input: ''')
            if scnd_inp:
                print("WIP")
            else:
                exit()

        elif user_input == '2':
            print('''
                1. Mini Plans
                2. Monthly Plans
                3. Mega Plans
                4. Super Mega Plans
                5. Special Data Offer
            ''')
        else:
            print("WIP ")             


    else:
        print("pick a sim ! ")
        
        
else:
    print("ERROR!")




while True:
    Pin = 2000
    Balance = 100
    My_pin = int(input("Fadlan Geli Pinkaga : " ))
    if Pin == My_pin:
        print("1. Somali : ")
        print("2. English : ")
        print("3. Araic : " )
        while True:
            Option = int(input("Dooro Option : "))
            if Option == 1:
                print("1. Itus Haragaga : ")
                print("2. Kaarka Hadalka : ")
                print("3. Uwareeji EVCPlus : ")
                print("4. Warbixin Koban : ")
                print("5. Salaam Bank : ")
                print("6. Kabax: ")
                while True:
                    Option = int(input("Dooro Option : "))
                    if Option == 1:
                        print("Haragaga Waa : $" + str(Balance))
                        break
                    elif Option == 2:
                        print("1. Kushubo Kaarka Hadalka : ")
                        print("2. Ugu Shub Kaarka Hadalka : ")
                        while True:
                            Option = int(input("Dooro Option : "))
                            if Option == 1:
                                Kaarka = float(input("Immisa Ayad Kushubanaysa? : "))
                                if Kaarka <= 0:
                                    print("The Amount Must be Greaterthan Zero : ")
                                    break
                                elif Kaarka > Balance:
                                    print("Haragaga Kuguma Filna Mudane : " )
                                    break
                                else:
                                    print("[-EVCPus-]-Waxad Kushubatay $"+ str(Kaarka)+ " Haragaga Waa : $" + str(Balance-Kaarka))
                                    break
                            elif Option == 2:
                                Mobile = int(input("Fadlan Geli Mobile-ka : "))
                                Kaarka = float(input("Immisa Ayad Ugu Shubaysaa? : "))
                                if Kaarka <= 0:
                                    print("The Amount Must be Greaterthan Zero : ")
                                    break
                                elif Kaarka > Balance:
                                    print("Haragaga Kuguma Filna Mudane : " )
                                    break
                                else:
                                    print("[-EVCPus-]-Waxad $"+ str(Kaarka)+" Ugu Shubtey Numberka : " + str(Mobile)+" Haragaga Waa : $" + str(Balance-Kaarka))
                                    break
                                break
                        else:
                            print("Fadlan Dooro 1 or 2 : ")
                        break
                    elif Option == 3:
                        while True:
                            global Money
                            global Tell
                            Tell = int(input("Fadlan Geli Mobile-ka : "))
                            Money = float(input("Fadlan Geli Lacagta : "))
                            if Money <= 0:
                                print("The Amount Must be Greaterthan Zero : ")
                                break
                            elif Money > Balance:
                                print("Haragaga Kuguma Filna Mudane : " )
                                break
                            else:
                                print("[-EVCPus-]-Waxad $"+ str(Money)+ " Uwarejisey Numberka : " + str (Tell) + " Haragaga Waa : $" + str(Balance-Money))
                                break
                        break
                    elif Option == 4:
                        Date = 1/2/2022 
                        Money = 100
                        Tell = 616427737
                        print("1. Last Action : ")
                        print("2. Warejinti Udanbesay : ")
                        print("3. Iibsashadii Udanbesay : ")
                        print("4. Last 3 Actions : ")
                        print("5. Email Me My Acivity : ")
                        Option = int(input("Dooro Option : "))
                        if Option == 1:
                            print("[-EVCPus-]-Waxad $"+ str(Money)+ " Uwarejisey Numberka : " + str (Tell) + str(Date))
                            break
                        elif Option == 2:
                            print("1. Udirtey : ")
                            print("2. Kaheshay : ")
                            Option = int(input("Dooro Option : "))
                            Date = '1/2/2022' 
                            Money = 100
                            Tell = 616427737
                            if Option == 1:
                                Number = int(input("Fadlan Geli Numberka : "))
                                print("[-EVCPus-]-Waxad $"+ str(Money)+ " Uwarejisey Numberka : " + str (Tell)+ " Tarikhda Markey aheyd : " + str( Date) )
                                break
                            elif Option == 2:
                                Number = int(input("Fadlan Geli Numberka : "))
                                print("[-EVCPus-]-Waxad $"+ str(Money)+ " Ka Heshay Numberka : " + str (Tell) + " Tarikhda Markey aheyd : " + str( Date) )
                                break
                            else:
                                print("Fadlan Dooro 1 or 2 : ")
                                break
                            break
                                                          
            break
        break
                    
    else:
        print("Pinka Aad Gelisay Waa Qalad : " )

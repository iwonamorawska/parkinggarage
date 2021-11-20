class ParkingGarage():
    def __init__(self, tickets=10, spaces=10):
        self.tickets = tickets
        self.spaces = spaces
        self.current_ticket = {}

    def take_ticket(self):
        active=True
        while active:
            self.question = input("Would you like to park?")
            if self.question == 'yes':
                if self.tickets==0:
                    print("Sorry we are capacity. Come back later.")
                    active=False
                elif self.tickets>=1:
                            self.tickets -= 1
                            self.spaces -= 1
                            self.pay_for_parking()
            if self.question == 'no':
                active=False
            elif self.question != 'yes' or 'no':
                print('Invalid response. Please respond with "yes" or "no"')
                self.take_ticket()
    def pay_for_parking(self):
        # change formatting here
        self.current_ticket["paid"]= False
        self.question2 = input("Would you like to pay now?")
        if self.question2 == 'yes':
            self.current_ticket["paid"] = True
            print("Your ticket had been paid. You have 15 minutes to leave.")
            self.leave_garage()
        elif self.question2=='no':
            self.leave_garage()
    def leave_garage(self):
        active=True
        while active:
            self.question3 = input("Would you like to leave the garage?")
            if self.question3 == 'yes' and self.current_ticket["paid"]==True:
                self.tickets += 1
                self.spaces += 1
                print("Thank you have a nice day.")
                active=False
            elif self.question3=='yes' and self.current_ticket["paid"]==False:
                print("Please pay for your ticket.")
                self.pay_for_parking()
            elif self.question3=='no':
                self.question4=input("Would you like to stay longer?")
                if self.question4 =='yes':
                    self.leave_garage()
                elif self.question4 =='no' and self.current_ticket["paid"]==False:
                    print("Please pay your ticket")
                    self.pay_for_parking()
                elif self.question4 == 'no' and self.current_ticket["paid"]==True:
                    print("Have a nice day.")
                    active=False
garage1=ParkingGarage()
garage1.take_ticket()
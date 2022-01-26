import datetime
import time

tickets = [0, 0, 0, 0, 0, 0, 0]


def single_day():
    print("Ticket type\t \t \t \t \t \t \t \t \t \t \tCost/day")
    print("1 Adult (13-18)\t \t \t \t \t \t \t \t \t \t$20.00")
    print("1 child (0-12)\t \t \t \t \t \t \t \t \t \t$12.00")
    print("1 senior (60 & above)\t \t \t \t \t \t \t \t \t \t \t$16.00")
    print("1 family (2 adults/seniors + 3 children max)\t \t$60.00")
    print("groups of 6 or more people (cost per person) \t \t$15.00")
    print("Terms and Conditions:")
    print("An adult may bring up to two children")
    print("Days available for booking (from today until the next one week):")
    dates_available()
    days_available()

def double_day():
    print("Ticket type\t \t \t \t \t \t \t \t \t \t \tCost/2days")
    print("1 Adult (13-18)\t \t \t \t \t \t \t \t \t \t$30.00")
    print("1 child (0-12)\t \t \t \t \t \t \t \t \t \t$18.00")
    print("1 senior (60 & above)\t \t \t \t \t \t \t \t$24.00")
    print("1 family (2 adults/seniors + 3 children max)\t \t$90.00")
    print("groups of 6 or more people (cost per person) \t \t$22.50")
    print("Terms and Conditions:")
    print("An adult may bring up to two children")
    print("Days available for booking (from today until the next one week):")
    dates_available()
    days_available()

def dates_available():
    day1 = datetime.date.today()
    day2 = datetime.date.today() + datetime.timedelta(days=1)
    day3 = datetime.date.today() + datetime.timedelta(days=2)
    day4 = datetime.date.today() + datetime.timedelta(days=3)
    day5 = datetime.date.today() + datetime.timedelta(days=4)
    day6 = datetime.date.today() + datetime.timedelta(days=5)
    day7 = datetime.date.today() + datetime.timedelta(days=6)
    print("[", day1, ",", day2, ",", day3, ",", day4, ",", day5, ",", day6, ",", day7, "]")


def days_available():
    today = time.strftime('%A')
    week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    n = len(week)
    global curr_days
    curr_days = []
    count = 0
    for i in range(7):
        if today == week[i]:
            if i == 0:
                for j in range(0, n):
                    curr_days.append(week[j])
            else:
                j = n - i
                m = n - j
                for k in range(0, n):
                    if count != j:
                        curr_days.append(week[k + i])
                        count = count + 1
                    else:
                        curr_days.append(week[k - j])
    print(curr_days)


def initialize():
    global tickets
    tickets = [0, 0, 0, 0, 0, 0, 0]
    # global size [not needed as of now]
    # size=[1000,1000,1000,1000,1000,1000,1000] [not needed as of now]
    global id_day1
    id_day1 = list()
    global id_day2
    id_day2 = list()
    global id_day3
    id_day3 = list()
    global id_day4
    id_day4 = list()
    global id_day5
    id_day5 = list()
    global id_day6
    id_day6 = list()
    global id_day7
    id_day7 = list()
    global total_cost
    total_cost = [0, 0, 0, 0, 0, 0, 0]
    global ticket_price


def input_tickets(ticket_type):
    print("Enter 1 for 1 single adult ticket (13-18)")
    print("Enter 2 for 1 single child ticket (0-12)")
    print("Enter 3 for 1 single senior ticket (60 & above)")
    print("Enter 4 for 1 family ticket (2 adults/seniors + 3 children max)")
    print("Enter 5 for 1 group ticket (groups of 6 or more)")
    print("Enter your choice")
    n = int(input())
    if n == 1:
        print("Enter the total number of adult tickets you want")
        adult_ticket = int(input())
        a = single_adult(adult_ticket,ticket_type)
        print("Updated ticket count and total cost", book_the_day(adult_ticket,a,ticket_type))
    elif n == 2:
        print("A child needs to be accommodated by an adult and cannot go alone")
        print("Enter the total number of adult tickets you want")
        adult_ticket = int(input())
        b = single_adult(adult_ticket,ticket_type)
        print("Enter the total number of child tickets you want")
        child_ticket = int(input())
        c = single_child(child_ticket,b,ticket_type)
        print("Updated ticket count and total cost", book_the_day(adult_ticket+child_ticket, c,ticket_type))
    elif n == 3:
        print("Enter the total number of senior tickets you want")
        senior_ticket = int(input())
        d = single_senior(senior_ticket,ticket_type)
        print("Updated ticket count and total cost", book_the_day(senior_ticket,d,ticket_type))
    elif n == 4:
        e,f = family_ticket(ticket_type)
        print("Updated ticket count and total cost", book_the_day(e,f,ticket_type))
    elif n == 5:
        print("Enter the total number of tickets you want (groups of 6 or more)")
        group_ticket = int(input())
        g = group_tickets(group_ticket,ticket_type)
        print("Updated ticket count and total cost", book_the_day(group_ticket,g,ticket_type))
    else:
        print("Please try again")
        input_tickets(ticket_type)




def family_ticket(ticket_type):
    if ticket_type==1:
        f_t_p=int(60) #family_ticket_price
        big=int(0)
        child=int(0)
        print("Its a family ticket (2 adults/seniors + 3 children max)")
        print("Enter the total number of adult tickets you want")
        adult_ticket = int(input())
        print("Enter the total number of senior tickets you want")
        senior_ticket = int(input())
        print("Enter the total number of child tickets you want")
        child = int(input())
        big = adult_ticket + senior_ticket
        if (big == 2 or big == 1) and (child == 1 or child == 2 or child == 3):
            return (big + child), f_t_p
        a,b=family_ticket(ticket_type)
        return a,b
    if(ticket_type==2):
        f_t_p = int(90)  # family_ticket_price
        big = int(0)
        child = int(0)
        print("Its a family ticket (2 adults/seniors + 3 children max)")
        print("Enter the total number of adult tickets you want")
        adult_ticket = int(input())
        print("Enter the total number of senior tickets you want")
        senior_ticket = int(input())
        print("Enter the total number of child tickets you want")
        child = int(input())
        big = adult_ticket + senior_ticket
        if (big == 2 or big == 1) and (child == 1 or child == 2 or child == 3):
            return (big + child), f_t_p
        a, b = family_ticket(ticket_type)
        return a, b

def single_child(child_ticket,b,ticket_type):
    if (ticket_type == 1):
        cost = int(12)
        return (cost * child_ticket)+b
    if (ticket_type == 2):
        cost = int(18)
        return (cost * child_ticket) + b


def single_adult(adult_ticket,ticket_type):
    if ticket_type==1:
        cost = int(20)
        return cost * adult_ticket
    if ticket_type==2:
        cost = int(30)
        return cost * adult_ticket

def single_senior(senior_ticket,ticket_type):
    if ticket_type == 1:
        cost = int(16)
        return cost * senior_ticket
    if ticket_type == 2:
        cost = int(24)
        return cost * senior_ticket


def group_tickets(group_ticket,ticket_type):
    if ticket_type == 1:
        while (group_ticket >= 6):
            cost = int(15)
            return cost * group_ticket
        print("group tickets have to be more than 6 people. please try booking adults and seniors")
        input_tickets(ticket_type)
    if ticket_type == 2:
        while (group_ticket >= 6):
            cost = float(22.50)
            return cost * group_ticket
        print("group tickets have to be more than 6 people. please try booking adults and seniors")
        input_tickets(ticket_type)

def book_the_day(ticket_n,price,ticket_type):
    if ticket_type==1:
        print("Please choose the day you want to book?")
        day_of_the_ticket=str(input())
        for i in range(7):
            if(day_of_the_ticket==curr_days[i]):
                tickets[i]=tickets[i]+ticket_n
                total_cost[i]= total_cost[i]+price
        extra_attractions(ticket_type, ticket_n, day_of_the_ticket)
        unique_booking_id(ticket_n, day_of_the_ticket, ticket_type)
        return tickets,total_cost
    if ticket_type==2:
        print("Please choose the first day you want to book?")
        day_of_the_ticket=str(input())
        for i in range(7):
            if(day_of_the_ticket==curr_days[i]):
                tickets[i]=tickets[i]+ticket_n
                tickets[i+1] = tickets[i+1] + ticket_n
                total_cost[i]= total_cost[i]+(price/2)
                total_cost[i+1] = total_cost[i+1] + (price / 2)
        extra_attractions(ticket_type,ticket_n,day_of_the_ticket)
        unique_booking_id(ticket_n,day_of_the_ticket,ticket_type)
        return tickets,total_cost

def unique_booking_id(ticket_n,day_of_the_ticket,ticket_type):
    global y
    y=list()
    global z
    z = list()
    if ticket_type==1:
        for i in range(7):
            if(day_of_the_ticket==curr_days[i]):
                temp=i
        if(temp==0):
            a=len(id_day1)
            for j in range(ticket_n):
                y.append(a+1)
                a=a+1
            print("Booked ids for the current tickets", y)
            id_day1.extend(y)
            print("Booked ids for ", curr_days[temp], id_day1)
        if (temp == 1):
            a = len(id_day2)
            for j in range(ticket_n):
                y.append(a + 1)
                a = a + 1
            print("Booked ids for the current tickets", y)
            id_day2.extend(y)
            print("Booked ids for ", curr_days[temp], id_day2)
        if (temp == 2):
            a = len(id_day3)
            for j in range(ticket_n):
                y.append(a + 1)
                a = a + 1
            print("Booked ids for the current tickets", y)
            id_day3.extend(y)
            print("Booked ids for ", curr_days[temp], id_day3)
        if (temp == 3):
            a = len(id_day4)
            for j in range(ticket_n):
                y.append(a + 1)
                a = a + 1
            print("Booked ids for the current tickets", y)
            id_day4.extend(y)
            print("Booked ids for ", curr_days[temp], id_day4)
        if (temp == 4):
            a = len(id_day5)
            for j in range(ticket_n):
                y.append(a + 1)
                a = a + 1
            print("Booked ids for the current tickets", y)
            id_day5.extend(y)
            print("Booked ids for ", curr_days[temp], id_day5)
        if (temp == 5):
            a = len(id_day6)
            for j in range(ticket_n):
                y.append(a + 1)
                a = a + 1
            print("Booked ids for the current tickets", y)
            id_day6.extend(y)
            print("Booked ids for ", curr_days[temp], id_day6)
        if (temp == 6):
            a = len(id_day7)
            for j in range(ticket_n):
                y.append(a + 1)
                a = a + 1
            print("Booked ids for the current tickets", y)
            id_day7.extend(y)
            print("Booked ids for ", curr_days[temp], id_day7)
    if ticket_type==2:
        for i in range(7):
            if(day_of_the_ticket==curr_days[i]):
                temp=i
        if(temp==0):
            a=len(id_day1)
            for j in range(ticket_n):
                y.append(a+1)
                a=a+1
            print("Booked ids for day1 in the current tickets", y)
            id_day1.extend(y)
            print("Booked ids for ", curr_days[temp], id_day1)
            b = len(id_day2)
            for k in range(ticket_n):
                z.append(b + 1)
                b = b + 1
            print("Booked ids for day2 in the current tickets", z)
            id_day2.extend(z)
            print("Booked ids for ", curr_days[temp+1], id_day2)
        if (temp == 1):
            a = len(id_day2)
            for j in range(ticket_n):
                y.append(a + 1)
                a = a + 1
            print("Booked ids  for day1 in the current tickets", y)
            id_day2.extend(y)
            print("Booked ids for ", curr_days[temp], id_day2)
            b = len(id_day3)
            for k in range(ticket_n):
                z.append(b + 1)
                b = b + 1
            print("Booked ids for day2 in the current tickets", z)
            id_day3.extend(z)
            print("Booked ids for ", curr_days[temp+1], id_day3)
        if (temp == 2):
            a = len(id_day3)
            for j in range(ticket_n):
                y.append(a + 1)
                a = a + 1
            print("Booked ids  for day1 in the current tickets", y)
            id_day3.extend(y)
            print("Booked ids for ", curr_days[temp], id_day3)
            b = len(id_day4)
            for k in range(ticket_n):
                z.append(b + 1)
                b = b + 1
            print("Booked ids for day2 in the current tickets", z)
            id_day4.extend(z)
            print("Booked ids for ", curr_days[temp+1], id_day4)
        if (temp == 3):
            a = len(id_day4)
            for j in range(ticket_n):
                y.append(a + 1)
                a = a + 1
            print("Booked ids  for day1 in the current tickets", y)
            id_day4.extend(y)
            print("Booked ids for ", curr_days[temp], id_day4)
            b = len(id_day5)
            for k in range(ticket_n):
                z.append(b + 1)
                b = b + 1
            print("Booked ids for day2 in the current tickets", z)
            id_day5.extend(z)
            print("Booked ids for ", curr_days[temp+1], id_day5)
        if (temp == 4):
            a = len(id_day5)
            for j in range(ticket_n):
                y.append(a + 1)
                a = a + 1
            print("Booked ids for day1 in the current tickets", y)
            id_day5.extend(y)
            print("Booked ids for ", curr_days[temp], id_day5)
            b = len(id_day6)
            for k in range(ticket_n):
                z.append(b + 1)
                b = b + 1
            print("Booked ids for day2 in the current tickets", z)
            id_day6.extend(z)
            print("Booked ids for ", curr_days[temp+1], id_day6)
        if (temp == 5):
            a = len(id_day6)
            for j in range(ticket_n):
                y.append(a + 1)
                a = a + 1
            print("Booked ids for  day1 inthe current tickets", y)
            id_day6.extend(y)
            print("Booked ids for ", curr_days[temp], id_day6)
            b = len(id_day7)
            for k in range(ticket_n):
                z.append(b + 1)
                b = b + 1
            print("Booked ids for day2 in the current tickets", z)
            id_day7.extend(z)
            print("Booked ids for ", curr_days[temp+1], id_day7)
        if (temp == 6):
            a = len(id_day7)
            for j in range(ticket_n):
                y.append(a + 1)
                a = a + 1
            print("Booked ids for  day1 in the current tickets", y)
            id_day7.extend(y)
            print("Booked ids for ", curr_days[temp], id_day7)
            b = len(id_day1)
            for k in range(ticket_n):
                z.append(b + 1)
                b = b + 1
            print("Booked ids for day2 in the current tickets", z)
            id_day1.extend(z)
            print("Booked ids for ", curr_days[temp+1], id_day1)



def task2():
    ticket_type=int(input("please enter 1 for single day booking/2 for double day booking"))
    if (ticket_type==1):
        print("You have chosen 1 day booking")
        single_day()
        input_tickets(ticket_type)
    if (ticket_type==2):
        print("You have chosen 2 day booking")
        double_day()
        input_tickets(ticket_type)



def extra_attractions(ticket_type,ticket_n,day_of_the_ticket):
    print("Extra Attractions\t \t \t \t \t \t \t \t \tCost Per Person Per Day")
    print("Lion Feeding\t \t \t \t \t \t \t \t \t \t2.50")
    print("Penguin Feeding\t \t \t \t \t \t \t \t \t \t2.00")
    print("Evening Barbecue\t \t \t \t \t \t \t \t \t5.50")
    print("Terms and Conditions:")
    print("Evening barbecue is available on two-day tickets only")
    flag = True
    while flag == True:
        if ticket_type == 1:
            print("Press 1 for lion feeding, 2 for Penguin feeding")
            attraction = int(input("Please enter your choice of extra attractions"))
            while attraction > 2:
                attraction = int(input("Please enter a valid choice of extra attraction"))
            if attraction == 1:
                sum_l = lion_feeding(ticket_n, day_of_the_ticket)
                update_cost_single(sum_l, day_of_the_ticket)
            if attraction == 2:
                sum_p = penguin_feeding(ticket_n, day_of_the_ticket)
                update_cost_single(sum_p, day_of_the_ticket)
        if ticket_type == 2:
            print("Press 1 for lion feeding\n 2 for Penguin feeding\n 3 for Evening barbecues")
            attraction = int(input("Please enter your choice of extra attractions"))
            while attraction > 3:
                attraction = int(input("Please enter a valid choice of extra attraction"))
            if (attraction == 1):
                sum_l = lion_feeding(ticket_n, day_of_the_ticket)
                update_cost_double(sum_l, day_of_the_ticket)
            if (attraction == 2):
                sum_p = penguin_feeding(ticket_n, day_of_the_ticket)
                update_cost_double(sum_p, day_of_the_ticket)
            if (attraction == 3):
                sum_e = evening_barbecues(ticket_n, day_of_the_ticket)
                update_cost_double(sum_e, day_of_the_ticket)
        print("Do you want to book another attraction?")
        yes = input("input yes or no")
        if (yes == "yes"):
            flag = True
        else:
            flag = False
    return


def lion_feeding(ticket_n,day_of_the_ticket):
    return ticket_n*2.5
def penguin_feeding(ticket_n,day_of_the_ticket):
    return ticket_n * 2.00
def evening_barbecues(ticket_n,day_of_the_ticket):
    return 5.5*ticket_n
def update_cost_double(sum, day_of_the_ticket):
    for i in range(7):
        if(day_of_the_ticket==curr_days[i]):
            total_cost[i]=total_cost[i]+sum
            total_cost[i+1]=total_cost[i+1]+sum
def update_cost_single(sum, day_of_the_ticket):
    for i in range(7):
        if(day_of_the_ticket==curr_days[i]):
            total_cost[i]=total_cost[i]+sum
def yes_or_no():
    initialize()
    f_lag=str('yes')
    while(f_lag=='yes'):
        task2()
        f_lag=str(input("do you want to continue, say yes or no"))

yes_or_no()
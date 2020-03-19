from .models        import Driver, Working_day
from datetime       import datetime

def creating_working_days():

    drivers = Driver.objects.filter(active=True)

    for driver in drivers:

        today = datetime.weekday(datetime.today())

        if today == 0:
            if driver.monday == True:
                dr_rate = driver.rate
            else:
                dr_rate = 0

        elif today == 1:
            if driver.tuesday == True:
                dr_rate = driver.rate
            else:
                dr_rate = 0

        elif today == 2:
            if driver.wednesday == True:
                dr_rate = driver.rate
            else:
                dr_rate = 0

        elif today == 3:
            if driver.thursday == True:
                dr_rate = driver.rate
            else:
                dr_rate = 0

        elif today == 4:
            if driver.friday == True:
                dr_rate = driver.rate
            else:
                dr_rate = 0

        elif today == 5:
            if driver.saturday == True:
                dr_rate = driver.rate
            else:
                dr_rate = 0

        elif today == 6:
            if driver.sunday == True:
                dr_rate = driver.rate
            else:
                dr_rate = 0

        else:
            dr_rate = 0       


        new_working_day = Working_day(
            driver=driver,
            date=datetime.today(),
            rate=dr_rate,
            fuel=0,
            penalties=0,
            cash=0,
            cash_card=0,
            cashless=0,
            )

        new_working_day.save()

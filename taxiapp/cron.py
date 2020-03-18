from .models        import Driver, Working_day
from datetime       import datetime

def creating_working_days():

    drivers = Driver.objects.filter(active=True)

    for driver in drivers:

        new_working_day = Working_day(
            driver=driver,
            date=datetime.today(),
            rate=driver.rate,
            fuel=0,
            penalties=0,
            cash=0,
            cash_card=0,
            cashless=0,
            )

        new_working_day.save()

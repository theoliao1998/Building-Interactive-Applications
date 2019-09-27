import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Category, States, Region, Iso, Site

def run():
    fhand = open('unesco/load.csv')
    reader = csv.reader(fhand)

    Category.objects.all().delete()
    States.objects.all().delete()
    Region.objects.all().delete()
    Iso.objects.all().delete()
    Site.objects.all().delete()

    # Format
    # jane@tsugi.org,I,Python
    # ed@tsugi.org,L,Python

    for row in reader:
        print(row)

        c, created = Category.objects.get_or_create(name=row[-4])
        s, created = States.objects.get_or_create(name=row[-3])
        r, created = Region.objects.get_or_create(name=row[-2])
        i, created = Iso.objects.get_or_create(name=row[-1])

        try:
            y = int(row[3])
        except:
            y = None

        try:
            l1 = float(row[4])
        except:
            l1 = None

        try:
            l2 = float(row[5])
        except:
            l2 = None

        try:
            a = float(row[6])
        except:
            a = None


        site = Site(name=row[0], description=row[1], justification=row[2], year=y, longitude=l1, latitude=l2, area_hectares=a, category=c, states=s, region=r, iso=i)
        site.save()



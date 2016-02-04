import dateutil.easter as E
import datetime
import sys

year = int(sys.argv[1])
western = E.easter(year,E.EASTER_WESTERN)


print "Catholic Lent begin: ",(western-datetime.timedelta(days=46)).ctime()
print "Catholic Easter: ",western.ctime()
print "Catholic Ascension: ",(western+datetime.timedelta(days=39)).ctime()
print "Catholic 50: ",(western+datetime.timedelta(days=49)).ctime()

orthodox = E.easter(year, E.EASTER_ORTHODOX)
print "Orthodox Lent begin: ",(orthodox-datetime.timedelta(days=48)).ctime()
print "Orthodox Easter: ",orthodox.ctime()
print "Orthodox Ascension: ",(orthodox+datetime.timedelta(days=39)).ctime()
print "Orthodox 50: ",(orthodox+datetime.timedelta(days=49)).ctime()

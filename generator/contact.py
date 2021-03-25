from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

# block for read options in command line (parameters)
# n - amount of generated testdata
# f- filename where we put generated testdata
try:
    opts, args=getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

# default values of parameters
n=5
f="data/contacts.json"

# if parameters n/f specified
for o, a in opts:
    # get parameter (-n) value for amount and convert to int
    if o == "-n":
        n = int(a)
        # get parameter value filename (-f) as string without converting
    elif o == "-f":
        f=a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range (random.randrange(maxlen))])

testdata = [Contact(firstname="", middlename="", lastname="")] + [
            Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10), lastname=random_string("lastname", 10),
            nickname=random_string("nickname", 10), title=random_string("title", 10), company=random_string("company", 10),
            address=random_string("address", 10), home=random_string("home", 10), mobile=random_string("mobile", 10), work=random_string("work", 10),
            fax=random_string("fax", 10), email=random_string("email", 10), email2=random_string("email2", 10), email3=random_string("email3", 10),
            homepage=random_string("homepage", 10), bday=random_string("bday", 1), bmonth=random_string("bmonth", 2), byear=random_string("byear", 4),
            aday=random_string("aday", 1), amonth=random_string("amonth", 10), ayear=random_string("ayear", 4),
            address2=random_string("address2", 10), phone2=random_string("phone2", 10), notes=random_string("notes", 10))
            for i in range(n)
]
# define path to file where we save testdata generated before  and join .. to jump up and filename
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

# open this file and save testdata
with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))

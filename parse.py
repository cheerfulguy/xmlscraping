from BeautifulSoup import BeautifulStoneSoup
xml = "<doc><tag1>Contents 1<tag2>Contents 2<tag1>Contents 3"

f = open('../data/zip/medline10n0341.xml', 'r')
count = 0


def token(line):
    if 

for line in f:
    
    print line
    
    count = count + 1
    if count>5:
        break

#f.readline()

#soup = BeautifulStoneSoup(f)
#print soup.prettify()

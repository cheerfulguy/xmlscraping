import xml.dom.minidom as minidom
#----------------------------------------------------------------------
def getData(xml):

    doc = minidom.parse(xml)
    node = doc.documentElement
    records = doc.getElementsByTagName("MedlineCitation")
    pmids = []

    for record in records:
        pmidObj = record.getElementsByTagName("PMID")[0]
        pmids.append(pmidObj)
 
    for pmid in pmids:
        print pmid.firstChild.data
 
getData('data.xml')
#from BeautifulSoup import BeautifulStoneSoup
#xml = "<doc><tag1>Contents 1<tag2>Contents 2<tag1>Contents 3"
#f = open('../data/zip/medline10n0341.xml', 'r')
#soup = BeautifulStoneSoup(f)
#print soup.prettify()

import xml.dom.minidom as minidom
#----------------------------------------------------------------------
def tasks(xml):

    doc = minidom.parse(xml)
    node = doc.documentElement
    records = doc.getElementsByTagName("MedlineCitation")
    MeSHs = []
    task1 = open("task1.txt","w")
    task2 = open()
    
    # task1
    for record in records:
        pmid = record.getElementsByTagName("PMID")[0].firstChild.data
        year = record.getElementsByTagName("Year")[0].firstChild.data
        #print pmid, year
        meshes = record.getElementsByTagName("MeshHeading")
    
    for mesh in meshes:
        
        if(len(mesh.getElementsByTagName("DescriptorName"))!=0):
            descriptor = mesh.getElementsByTagName("DescriptorName")[0]
            descriptorName =  descriptor.firstChild.data
            descriptorMajor = descriptor.getAttribute("MajorTopicYN")
        
        if(len(mesh.getElementsByTagName("QualifierName"))!=0):
            qualifier =  mesh.getElementsByTagName("QualifierName")[0]
            qualifierName =  qualifier.firstChild.data
            qualifierMajor = qualifier.getAttribute("MajorTopicYN")
        
 
tasks('data.xml')
#from BeautifulSoup import BeautifulStoneSoup
#xml = "<doc><tag1>Contents 1<tag2>Contents 2<tag1>Contents 3"
#f = open('../data/zip/medline10n0341.xml', 'r')
#soup = BeautifulStoneSoup(f)
#print soup.prettify()

import xml.dom.minidom as minidom
#----------------------------------------------------------------------
def tasks(xml):

    doc = minidom.parse(xml)
    node = doc.documentElement
    records = doc.getElementsByTagName("MedlineCitation")
    MeSHs = []
    task1 = open("task1.csv","w")
    task2 = open("task2.csvopen","w")
    
    task1.write("PMID, YEAR\n")
    task2.write("PMID,DESCRIPTORMAJOR,DESCRIPTORNAME,QUALIFIERNAME,QUALIFIERMAJOR,YEAR\n")

    # task1
    for record in records:
        pmid = record.getElementsByTagName("PMID")[0].firstChild.data.strip()
        year = record.getElementsByTagName("Year")[0].firstChild.data.strip()
        #print pmid, year
        task1.write(pmid + ", " + year + "\n")
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
            else:
                qualifierName = "."
                qualifierMajor = "."

            task2.write(pmid +","+descriptorMajor + "," + descriptorName + "," + qualifierName + "," + qualifierMajor + "," + year + "\n")
 
tasks('data.xml')
#from BeautifulSoup import BeautifulStoneSoup
#xml = "<doc><tag1>Contents 1<tag2>Contents 2<tag1>Contents 3"
#f = open('../data/zip/medline10n0341.xml', 'r')
#soup = BeautifulStoneSoup(f)
#print soup.prettify()

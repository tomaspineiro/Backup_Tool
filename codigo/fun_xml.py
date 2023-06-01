import xmltodict


def read_xml(pathFile):

    xml = open(pathFile)

    xmldict = xmltodict.parse(xml.read()) 

    return xmldict


import cgi
from lxml import etree
import requests

AWS_KEY = 'AKIAJHX3JO2RPYRT6BGA'
SECRET_KEY = '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'
ASSOCIATE_TAG = 'proyeamazo-21'

print "Content-Type: text/html\n"
form = cgi.FieldStorage()
nombre = form.getvalue("juego")

datos= {'AWSAccessKeyID': 'AKIAJHX3JO2RPYRT6BGA', 'AssociateTag': 'proyeamazo-21', 'Operation': 'ItemSearch', 'ResponseGroup': 'Offers%2C%20ItemAttributes', 'SearchIndex': 'VideoGames', 'Service': 'AWSECommerceService', 'Timestamp': '', 'Version': '2011-08-01', 'Signature': '', 'Keywords': '%s' %nombre}
busqueda = requests.get('http://ecs.amazonaws.com/onca/xml?', params=datos)
url= busqueda.text


xml = etree.parse("xml2")
ns = {"ns": "http://webservices.amazon.com/AWSECommerceService/2011-08-01"}
#tree = etree.fromstring(xml)
#for node in xml.xpath('/ns:ItemSearchResponse/ns:Items/ns:Item/ns:ItemAttributes', namespaces=ns):
#print node
nombre = xml.xpath("/ns:ItemSearchResponse/ns:Items/ns:Item/ns:ItemAttributes/ns:Title/text()", namespaces=ns)
plataforma = xml.xpath("/ns:ItemSearchResponse/ns:Items/ns:Item/ns:ItemAttributes/ns:Platform/text()", namespaces=ns)
menos_nuevo = xml.xpath("/ns:ItemSearchResponse/ns:Items/ns:Item/ns:OfferSummary/ns:LowestNewPrice/ns:FormattedPrice/text()", namespaces=ns)
menos_usado = xml.xpath("/ns:ItemSearchResponse/ns:Items/ns:Item/ns:OfferSummary/ns:LowestUsedPrice/ns:FormattedPrice/text()", namespaces=ns)

productos= len(xml.xpath('/ns:ItemSearchResponse/ns:Items/ns:Item/ns:ItemAttributes', namespaces=ns))
for i in xrange(productos):
    lista= xml.xpath('/ns:ItemSearchResponse/ns:Items/ns:Item/ns:ItemAttributes', namespaces=ns)[i]
    print lista.xpath('ns:Title/text()', namespaces=ns)
    print lista.xpath('ns:Platform/text()', namespaces=ns)


	

print nombre
#http://ecs.amazonaws.com/onca/xml?AWSAccessKeyId=AKIAJHX3JO2RPYRT6BGA&AssociateTag=proyeamazo-21&Operation=ItemSearch&ResponseGroup=Offers%2C%20ItemAttributes&SearchIndex=VideoGames&Service=AWSECommerceService&Timestamp=2013-03-07T11%3A45%3A40.000Z&Version=2011-08-01&Signature=G1Fx1wZVcXIhV1dxB7wg%2F5TrXaAhm2MFkLEDqE9j80c%3D&Keywords=






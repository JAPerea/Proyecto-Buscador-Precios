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
busqeda = requests.get('http://ecs.amazonaws.com/onca/xml?', params=datos)
url= busqeda.text

#xml = etree.fromstring(url)
#xml = etree.parse("xml")


#nombre = xml.xpath("/ItemSearchResponse/Items/Item/ItemAttributes/Title/text()")
#plataforma = xml.xpath("/ItemSearchResponse/Items/Item/ItemAttributes/Platform/text()")
#menos_nuevo = xml.xpath("/ItemSearchResponse/Items/Item/OfferSummary/LowestNewPrice/FormattedPrice/text()")
#menos_usado = xml.xpath("/ItemSearchResponse/Items/Item/OfferSummary/LowestUsedPrice/FormattedPrice/text()")

#print nombre

#http://ecs.amazonaws.com/onca/xml?AWSAccessKeyId=AKIAJHX3JO2RPYRT6BGA&AssociateTag=proyeamazo-21&Operation=ItemSearch&ResponseGroup=Offers%2C%20ItemAttributes&SearchIndex=VideoGames&Service=AWSECommerceService&Timestamp=2013-03-07T11%3A45%3A40.000Z&Version=2011-08-01&Signature=G1Fx1wZVcXIhV1dxB7wg%2F5TrXaAhm2MFkLEDqE9j80c%3D&Keywords=




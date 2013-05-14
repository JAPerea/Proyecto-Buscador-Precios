import cgi
from lxml import etree
import requests
import bottle
import bottlenose

#AWS_KEY = 'AKIAJHX3JO2RPYRT6BGA'
#SECRET_KEY = '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'
#ASSOCIATE_TAG = 'proyeamazo-21'

#print "Content-Type: text/html\n"
#form = cgi.FieldStorage()
#nombreform = form.getvalue("juego")

@bottle.route('/')
def pag_principal():
	return bottle.template('index.html')

@bottle.route('/busquedajuego', method='POST')
def bus_juego():
	juego = bottle.request.forms.get("juego")
	amazon = bottlenose.Amazon('AKIAJHX3JO2RPYRT6BGA','vA/k1nDIn35Sk/		Wk0LlzvsPsb9wfiSTsyOWjtX0H','proyeamazo-21')
	busqueda = amazon.ItemSearch(SearchIndex="VideoGames", ResponseGroup="ItemAttributes, Offers", Keywords="Fallout New Vegas")
	xml = etree.fromstring(busqueda)
	ns = {"ns": "http://webservices.amazon.com/AWSECommerceService/2011-08-01"}
	for i in xrange(1):
    		lista= xml.xpath('/ns:ItemSearchResponse/ns:Items/ns:Item', namespaces=ns)[i]
    		nombre=lista.xpath('ns:ItemAttributes/ns:Title/text()', namespaces=ns)
    		plataforma=lista.xpath('ns:ItemAttributes/ns:Platform/text()', namespaces=ns)
		menos_nuevo=lista.xpath('ns:OfferSummary/ns:LowestNewPrice/ns:FormattedPrice/text()', namespaces=ns)
		menos_usado=lista.xpath('ns:OfferSummary/ns:LowestUsedPrice/ns:FormattedPrice/text()', namespaces=ns)
	return bottle.template('respuesta.html', title=nombre, platform=plataforma, nuevo=menos_nuevo, usado=menos_usado)


#productos= len(xml.xpath('/ns:ItemSearchResponse/ns:Items/ns:Item', namespaces=ns))
#for i in xrange(productos):
#    	lista= xml.xpath('/ns:ItemSearchResponse/ns:Items/ns:Item', namespaces=ns)[i]
#    	print lista.xpath('ns:ItemAttributes/ns:Title/text()', namespaces=ns)
#    	print lista.xpath('ns:ItemAttributes/ns:Platform/text()', namespaces=ns)
#	print lista.xpath('ns:OfferSummary/ns:LowestNewPrice/ns:FormattedPrice/text()', namespaces=ns)
#	print lista.xpath('ns:OfferSummary/ns:LowestUsedPrice/ns:FormattedPrice/text()', namespaces=ns)
	


bottle.debug(True)
bottle.run(host='localhost',port=8080)


	
#http://ecs.amazonaws.com/onca/xml?AWSAccessKeyId=AKIAJHX3JO2RPYRT6BGA&AssociateTag=proyeamazo-21&Operation=ItemSearch&ResponseGroup=Offers%2C%20ItemAttributes&SearchIndex=VideoGames&Service=AWSECommerceService&Timestamp=2013-03-07T11%3A45%3A40.000Z&Version=2011-08-01&Signature=G1Fx1wZVcXIhV1dxB7wg%2F5TrXaAhm2MFkLEDqE9j80c%3D&Keywords=






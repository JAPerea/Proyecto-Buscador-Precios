from lxml import etree
import requests
import bottle
import bottlenose

AWS_KEY = 'AKIAJHX3JO2RPYRT6BGA'
SECRET_KEY = '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'
ASSOCIATE_TAG = 'proyeamazo-21'

def busqueda_amazon(SearchIndex,ResponseGroup,Keywords):
	amazon = bottlenose.Amazon(
		AWS_KEY,
		SECRET_KEY,
		ASSOCIATE_TAG,
		)
	busqueda = amazon.ItemSearch(SearchIndex=SearchIndex, 
				     ResponseGroup=ResponseGroup,
				     Keywords=Keywords)
	return busqueda

@bottle.route('/')
def pag_principal():
	return bottle.template('index')

@bottle.route('/busquedajuego', method='POST')
def bus_juego():
	juego = bottle.request.forms.get("juego")
	busqueda = busqueda_amazon("VideoGames","ItemAttributes, Offers", juego)
	xml = etree.fromstring(busqueda)
	ns = {"ns": "http://webservices.amazon.com/AWSECommerceService/2011-08-01"}
	for i in xrange(1):
    	 	lista= xml.xpath('/ns:ItemSearchResponse/ns:Items/ns:Item', namespaces=ns)[i]
    	 	nombre=lista.xpath('ns:ItemAttributes/ns:Title/text()', namespaces=ns)
    	 	plataforma=lista.xpath('ns:ItemAttributes/ns:Platform/text()', namespaces=ns)
	 	menos_nuevo=lista.xpath('ns:OfferSummary/ns:LowestNewPrice/ns:FormattedPrice/text()', namespaces=ns)
	 	menos_usado=lista.xpath('ns:OfferSummary/ns:LowestUsedPrice/ns:FormattedPrice/text()', namespaces=ns)
	return bottle.template('busquedajuego', title=nombre, platform=plataforma, nuevo=menos_nuevo, usado=menos_usado)
	

#productos= len(xml.xpath('/ns:ItemSearchResponse/ns:Items/ns:Item', namespaces=ns))
#for i in xrange(productos):
#    	lista= xml.xpath('/ns:ItemSearchResponse/ns:Items/ns:Item', namespaces=ns)[i]
#    	print lista.xpath('ns:ItemAttributes/ns:Title/text()', namespaces=ns)
#    	print lista.xpath('ns:ItemAttributes/ns:Platform/text()', namespaces=ns)
#	print lista.xpath('ns:OfferSummary/ns:LowestNewPrice/ns:FormattedPrice/text()', namespaces=ns)
#	print lista.xpath('ns:OfferSummary/ns:LowestUsedPrice/ns:FormattedPrice/text()', namespaces=ns)
	


bottle.debug(True)
bottle.run(host='localhost',port=8080)

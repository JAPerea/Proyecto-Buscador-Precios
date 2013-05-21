from lxml import etree
import requests
import bottle
import bottlenose
from bottle import route, static_file

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

@route('/style/estilo.css')
def server_static(filename):
    return static_file(filename, root='style/')

@bottle.route('/busquedajuego', method='POST')
def bus_juego():
	juego = bottle.request.forms.get("juego")
	busqueda = busqueda_amazon("VideoGames","ItemAttributes, Offers", juego)
	xml = etree.fromstring(busqueda)
	ns = {"ns": "http://webservices.amazon.com/AWSECommerceService/2011-08-01"}
	resultado = []
	productos= len(xml.xpath('/ns:ItemSearchResponse/ns:Items/ns:Item', namespaces=ns))
	for i in xrange(productos):
    		lista= xml.xpath('/ns:ItemSearchResponse/ns:Items/ns:Item', namespaces=ns)[i]
    		resultado.append(lista.xpath('ns:ItemAttributes/ns:Title/text()', namespaces=ns))
    		resultado.append(lista.xpath('ns:ItemAttributes/ns:Platform/text()', namespaces=ns))
		resultado.append(lista.xpath('ns:OfferSummary/ns:LowestNewPrice/ns:FormattedPrice/text()', namespaces=ns))
		resultado.append(lista.xpath('ns:OfferSummary/ns:LowestUsedPrice/ns:FormattedPrice/text()', namespaces=ns))
		resultado.append(lista.xpath('ns:ItemLinks/ns:ItemLink[1]/ns:URL/text()', namespaces=ns))	
	return bottle.template('busquedajuego', resultado = resultado)
	
bottle.debug(True)
bottle.run(host='localhost',port=8080)

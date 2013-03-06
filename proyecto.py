import cgi
from lxml import etree
import requests

AWS_KEY = 'AKIAJHX3JO2RPYRT6BGA'
SECRET_KEY = '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'
ASSOCIATE_TAG = 'proyeamazo-21'

r = requests.get('http://ecs.amazonaws.com/onca/xml?AWSAccessKeyId=AKIAJHX3JO2RPYRT6BGA&AssociateTag=proyeamazo-21&Keywords=Fallout%20New%20Vegas&Operation=ItemSearch&ResponseGroup=Offers%2C%20ItemAttributes&SearchIndex=All&Service=AWSECommerceService&Timestamp=2013-03-06T09%3A04%3A37.000Z&Version=2011-08-01&Signature=Ez%2Flw6I7LOQxh3qlL83TeqD3cNtr0rZF8FI9ucCmgg4%3D')
url= r.text

print url
xml = etree.fromstring(url)

nombre = xml.xpath("/ns:ItemSearchResponse/ns:Items/ns:Item/ns:ItemAttributes/ns:Title/text()")
plataforma = xml.xpath("/ItemSearchResponse/Items/Item/ItemAttributes/Platform/text()")
menos_nuevo = xml.xpath("/ItemSearchResponse/Items/Item/OfferSummary/LowestNewPrice/FormattedPrice/text()")
menos_usado = xml.xpath("/ItemSearchResponse/Items/Item/OfferSummary/LowestUsedPrice/FormattedPrice/text()")


print nombre



#http://ecs.amazonaws.com/onca/xml?AWSAccessKeyId=AKIAJHX3JO2RPYRT6BGA&AssociateTag=proyeamazo-21&Keywords=fallout%20new%20vegas&Operation=ItemSearch&ResponseGroup=Offers%2C%20ItemAttributes&SearchIndex=All&Service=AWSECommerceService&Timestamp=2013-03-06T08%3A31%3A01.000Z&Version=2011-08-01&Signature=oU8HJl0hJCEz8BsdlCp%2FuIGDYDpAmDCIUQ9PLLTFp3E%3D


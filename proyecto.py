import bottlenose
AWS_KEY = 'AKIAJHX3JO2RPYRT6BGA'
SECRET_KEY = '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'
ASSOCIATE_TAG = 'proyeamazo-21'

amazon = bottlenose.Amazon(AWS_KEY, SECRET_KEY, ASSOCIATE_TAG)
response = amazon.ItemSearch(Keywords="Kindle 3G", SearchIndex="All")

print response

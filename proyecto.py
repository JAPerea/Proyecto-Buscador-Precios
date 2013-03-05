from amazonproduct import API
AWS_KEY = 'AKIAJHX3JO2RPYRT6BGA'
SECRET_KEY = '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'
ASSOCIATE_TAG = 'proyeamazo-21'
params = { 'ResponseGroup' : 'Medium', }
api = API(AWS_KEY, SECRET_KEY, 'uk', ASSOCIATE_TAG)
for page in api.item_search("All", Keywords="linux", **params):
    for product in page.Items.Item:
        print product

#total_results = node.Items.TotalResults.pyval
#total_pages = node.Items.TotalPages.pyval

#for book in node.Items.Item:
#   print '%s: "%s"' % (book.ItemAttributes.Author,
#                        book.ItemAttributes.Title)



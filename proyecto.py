from amazonproduct import API
AWS_KEY = 'AKIAJHX3JO2RPYRT6BGA'
SECRET_KEY = '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'

api = API(AWS_KEY, SECRET_KEY, 'uk', AssociateTag='proyeamazo-21')
node = api.item_search('Books', Publisher='Galileo Press')

total_results = node.Items.TotalResults.pyval
total_pages = node.Items.TotalPages.pyval

for book in node.Items.Item:
   print '%s: "%s"' % (book.ItemAttributes.Author,
                        book.ItemAttributes.Title)



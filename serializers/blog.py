
# serialize one doc to dict
def DecodeBlog(doc) -> dict:
    return {
        "_id" : str(doc['_id']),
        "title" : doc['title'],
        "sub_title" : doc["sub_title"],
        "content" : doc['content'],
        "author" : doc['author'],
        "rating" : doc['rating'],
        "date_created" : str(doc['date_created'])
    }

# serialize all doc to list of dict
def DecodeBlogs(docs) -> list:
    return [DecodeBlog(doc) for doc in docs]

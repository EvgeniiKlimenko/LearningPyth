import json

book = {
    'title': '1984',
    "author": "George Orwell",
    "isbn": "453991-4343",
    "inner_id": "43hj4j3hj43"
}

json_string = json.dumps(book)
print(type(json_string))  # type is str
print(json_string)

book_converted = json.loads(json_string)
print(type(book_converted))  # type is dict

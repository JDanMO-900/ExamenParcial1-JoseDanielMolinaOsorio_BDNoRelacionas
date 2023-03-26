from conection_parameters import collection


def read_peliculas(id = None):
    list_documents = []
    if id is not None:
        query = id

        list_documents.append(collection.find_one(query))

    else:
        documents = collection.find()

        for document in documents:
            list_documents.append(document)

    return list_documents

def create_peliculas(json_peliculas):

    result = collection.insert_one(json_peliculas)

    print(result.inserted_id)

def update(id, json_peliculas_update):
    query = {"_id": id}
    new_values = {"$set": json_peliculas_update}
    result = collection.update_one(query, new_values)
    print(result.modified_count)

def delete(id):
    result = collection.delete_one({"_id": id})
    print(result.deleted_count, "Se eleminó")
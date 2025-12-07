import chromadb

COLLECTION_NAME = "recipes_collection"

def get_chroma_client():
    """
    Create a local persistent Chroma client using the new recommended API.
    Data will be stored in the ./chroma_db folder.
    """
    client = chromadb.PersistentClient(path="./chroma_db")
    return client

def get_or_create_collection():
    client = get_chroma_client()
    collection = client.get_or_create_collection(name=COLLECTION_NAME)
    return collection

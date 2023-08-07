import pinecone
from .vector_search import VectorSearch

class PineconeSearch(VectorSearch):
    """
    Implements the VectorSearch interface using Pinecone's vector search service.
    
    PineconeSearch allows for the insertion of vectors into a Pinecone index and 
    querying that index for similar vectors.

    Attributes:
    - index_name (str): The name of the Pinecone index.
    - vector_index (pinecone.Index): The Pinecone index object.
    """
    
    def __init__(self, index_name: str):
        """
        Initialize the PineconeSearch with a specific index name.

        If the provided index name does not exist in Pinecone, a new index is created.

        Args:
        - index_name (str): The name of the Pinecone index to use or create.
        """
        self.index_name = index_name
        # Check if the index with the given name exists, if not, create it.
        if index_name not in pinecone.list_indexes():
            pinecone.create_index(index_name=index_name, metric="cosine")
        self.vector_index = pinecone.Index(index_name=index_name)
    
    def insert_vector(self, vector, identifier):
        """
        Insert a vector into the Pinecone index.

        Args:
        - vector (list[float]): The vector to insert.
        - identifier (str): A unique identifier for the vector.
        """
        self.vector_index.upsert(items={identifier: vector})

    def search_vector(self, vector, top_k=5):
        """
        Search the Pinecone index for vectors similar to the given vector.

        Args:
        - vector (list[float]): The query vector.
        - top_k (int, optional): The number of similar vectors to return. Default is 5.

        Returns:
        - tuple: A tuple containing lists of identifiers and their corresponding scores.
        """
        results = self.vector_index.query(queries=vector, top_k=top_k)
        return results.ids, results.scores

    def __del__(self):
        """
        Destructor for the PineconeSearch class.

        This destructor can be extended to clean up resources, 
        such as deleting the Pinecone index. Currently, it does nothing.
        """
        # Optionally, deinitialize (delete) the Pinecone index during clean-up.
        # pinecone.deinitialize_index(self.index_name)
        pass

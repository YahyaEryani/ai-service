from abc import ABC, abstractmethod

class VectorSearch(ABC):
    """
    Abstract base class representing a generic vector search interface.
    
    This class provides a contract for vector insertion and searching operations 
    which concrete implementations must adhere to.

    Methods:
    - insert_vector: Insert a vector with an associated identifier.
    - search_vector: Search for similar vectors based on the given vector.
    """

    @abstractmethod
    def insert_vector(self, vector, identifier):
        """
        Abstract method to insert a vector with a corresponding identifier.

        Args:
        - vector (list[float] or similar): The vector to be inserted.
        - identifier (Any): A unique identifier associated with the vector.
        
        Concrete implementations of this method must handle the specifics 
        of how the vector is stored.
        """
        pass
    
    @abstractmethod
    def search_vector(self, vector):
        """
        Abstract method to search for vectors similar to the provided vector.

        Args:
        - vector (list[float] or similar): The vector to search for.
        
        Returns:
        - Typically returns a list of similar vectors or identifiers associated 
          with them, but the specifics are left to the concrete implementations.
        """
        pass

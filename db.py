from tinydb import TinyDB
from tinydb.database import Document

class LikeDB:
    def __init__(self, file_path):
        # Initialize the database
        self.db = TinyDB(file_path, indent=4)

    def add_student(self, user_id):
        """
        Add student in Database
        """
        if not self.db.contains(doc_id=user_id):
            data = {
                "like": 0,
                "dislike": 0
            }
            document = Document(data, doc_id=user_id)
            self.db.insert(document)

    
    def all_likes(self):
        """
        Count all users likes
        """
        pass

    def all_dislikes(self):
        """
        Count all users dislikes
        """
        pass

    def add_like(self, user_id:int):
        """
        Add like to the database
        
        Args:
            user_id (str): telegram user id
        Returns:
            The number of likes and dislikes for the post
        """
        pass



    def add_dislike(self, user_id:int):
        """
        Add dislike to the database
        
        Args:
            user_id (str): telegram user id
        Returns:
            The number of likes and dislikes for the post
        """
        pass
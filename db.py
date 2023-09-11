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
        data = self.db.all()

        likes = 0
        for i in data:
            likes += i['like']
        
        return likes

        return data

    def all_dislikes(self):
        """
        Count all users dislikes
        """
        data = self.db.all()

        dislikes = 0
        for i in data:
            dislikes += i['dislike']
        
        return dislikes

        return data

    def add_like(self, user_id:int):
        """
        Add like to the database
        
        Args:
            user_id (str): telegram user id
        Returns:
            The number of likes and dislikes for the post
        """
        
        user = self.db.get(doc_id=user_id)
        like = user['like']
        dislike = user['dislike']

        if like == 0 and dislike == 0:
            user['like'] = 1
        elif like == 1 and dislike == 0:
            user['like'] = 0
        elif like == 0 and dislike == 1:
            user['like'] = 1
            user['dislike'] = 0
        
        self.db.update(user, doc_ids=[user_id])
        return user



    def add_dislike(self, user_id:int):
        """
        Add dislike to the database
        
        Args:
            user_id (str): telegram user id
        Returns:
            The number of likes and dislikes for the post
        """
        user = self.db.get(doc_id=user_id)
        like = user['like']
        dislike = user['dislike']

        if like == 0 and dislike == 0:
            user['dislike'] = 1
        elif like == 0 and dislike == 1:
            user['dislike'] = 0
        elif like == 1 and dislike == 0:
            user['like'] = 0
            user['dislike'] = 1
        
        self.db.update(user, doc_ids=[user_id])
        return user 
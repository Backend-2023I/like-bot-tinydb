from tinydb import TinyDB
from tinydb.database import Document

class LikeDB:
    def __init__(self, file_path):
        # Initialize the database
        self.db = TinyDB(file_path, indent=4)

    def add_user(self, user_id, message_id):
        """
        Add user in Database
        """
        img = self.db.table(message_id)

        if not img.contains(doc_id=user_id):
            data = {
                "like": 0,
                "dislike": 0
            }
            document = Document(data, doc_id=user_id)
            img.insert(document)

    
    def all_likes(self, message_id):
        """
        Count all users likes
        """
        img = self.db.table(str(message_id))
        data = img.all()

        likes = 0
        for i in data:
            likes += i['like']
        
        return likes

    def all_dislikes(self, message_id):
        """
        Count all users dislikes
        """
        img = self.db.table(str(message_id))
        data = img.all()

        dislikes = 0
        for i in data:
            dislikes += i['dislike']
        
        return dislikes

        return data

    def add_like(self, user_id:int, message_id):
        """
        Add like to the database
        
        Args:
            user_id (str): telegram user id
        Returns:
            The number of likes and dislikes for the post
        """
        img = self.db.table(str(message_id))

        user =img.get(doc_id=user_id)
        like = user['like']
        dislike = user['dislike']

        if like == 0 and dislike == 0:
            user['like'] = 1
        elif like == 1 and dislike == 0:
            user['like'] = 0
        elif like == 0 and dislike == 1:
            user['like'] = 1
            user['dislike'] = 0
        
        img.update(user, doc_ids=[user_id])
        return user



    def add_dislike(self, user_id:int, message_id):
        """
        Add dislike to the database
        
        Args:
            user_id (str): telegram user id
        Returns:
            The number of likes and dislikes for the post
        """
        img = self.db.table(str(message_id))

        user = img.get(doc_id=user_id)
        like = user['like']
        dislike = user['dislike']

        if like == 0 and dislike == 0:
            user['dislike'] = 1
        elif like == 0 and dislike == 1:
            user['dislike'] = 0
        elif like == 1 and dislike == 0:
            user['like'] = 0
            user['dislike'] = 1
        
        img.update(user, doc_ids=[user_id])
        return user 
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user

class Post: 
    DB = "coding_dojo_wall_sensei"
    
    def __init__(self,data):
        self.id = data['id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.creator = None

    @classmethod
    def get_all_posts_with_creator(cls):
        query = "SELECT * FROM posts JOIN users ON posts.user_id = users.id ORDER BY posts.created_at DESC;"
        results = connectToMySQL(cls.DB).query_db(query)
        all_posts = []
        for row in results:
            one_post = cls(row)
            one_post_author_info = {
                "id": row['users.id'],
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "email": row['email'],
                "password": row['password'],
                "created_at": row['users.created_at'],
                "updated_at": row['users.updated_at']
            }
            author = user.User(one_post_author_info)
            one_post.creator = author
            all_posts.append(one_post)
        return all_posts
    @classmethod
    def save(cls,data):
        query = "INSERT INTO posts (content,user_id) VALUES (%(content)s,%(user_id)s); "
        result = connectToMySQL(cls.DB).query_db(query,data)
        #print("__ADDING NEW POST___",result)
        return result
    @classmethod
    def post_delete(cls,data):
        query = "DELETE FROM posts WHERE id = %(id)s;"
        result = connectToMySQL(cls.DB).query_db(query,data)
        #print("___DELETING POST___",result)
        return result

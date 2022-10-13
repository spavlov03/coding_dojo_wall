from flask_app.config.mysqlconnection import connectToMySQL

class Comment: 
    DB = "coding_dojo_wall_sensei"
    
    def __init__(self,data):
        self.id = data['id']
        self.com_content = data['com_content']
        self.post_id = data['post_id']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save_comment(cls,data):
        query = "INSERT INTO comments (com_content,post_id,user_id) VALUES (%(com_content)s,%(post_id)s,%(user_id)s);"
        result = connectToMySQL(cls.DB).query_db(query,data)
        #print("__ADDING NEW COMMENT___",result)
        return result
    # @classmethod
    # def get_all_comments_by_post_id(cls,data):
    #     query = "SELECT * FROM comments JOIN users ON comments.user_id = users.id WHERE post_id = %(post_id)s;"
    #     result = connectToMySQL(cls.DB).query_db(query,data)
    #     return result 
    @classmethod
    def get_all_comments(cls):
        query = "SELECT com_content,post_id,user_id,comments.created_at,first_name,last_name FROM comments JOIN users ON comments.user_id = users.id;"
        result = connectToMySQL(cls.DB).query_db(query)
        return result 
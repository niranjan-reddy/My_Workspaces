from user import User
from post import Post

user_info = User("niranjan@kayacorp.cyou", "Niranjan Reddy", "password", "Principal Engineer")
user_info.get_user_info()
user_info.change_job_title("Software Engineering Senior Manager")
user_info.get_user_info()

post = Post("niranjan is supposed to be the best Dad for all his kids", "niranjan")
post.get_post_info()
from sqlalchemy import create_engine ,ForeignKey ,String, Integer, Column
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid
from sqlalchemy.orm import declarative_base

# Base = declarative_base()
Base = declarative_base()


def generate_uuid():
    return str(uuid.uuid4())

class users(Base):
    __tablename__ = "users"
    userID = Column("userID", String ,primary_key=True, default=generate_uuid)
    firstName = Column("firstName",String)
    lastName = Column("lastName",String)
    profileName = Column("profileName",String)
    email = Column("email",String)

    def __init__(self,firstName,lastName,profileName,email):
        self.firstName = firstName
        self.lastName  = lastName
        self.profileName = profileName
        self.email = email

class posts(Base):
    __tablename__ = "posts"
    postID = Column("postId",String, primary_key = True, default= generate_uuid)
    userID = Column("userId", String, ForeignKey("users.userID"))
    postContent = Column("postContent", String)

    def __init__(self, userId, postContent):
        self.userID = userId
        self.postContent = postContent

class likes(Base):
    __tablename__ = "likes"
    likeId = Column("likeId", String, primary_key= True, default=generate_uuid)
    userId = Column("userId", String, ForeignKey("users.userID"))
    postsId = Column("postId", String, ForeignKey("posts.postId"))


    def __init__(self,userId, postId):
        self.userId = userId
        self.postsId = postId


def addUser (firstName,lastName,profileName,email, session):
    exist = session.query(users).filter(users.email == email).all()
    if len(exist)>0:
        print("Email Address already exist!")
    else:
        user = users(firstName,lastName,profileName,email)
        session.add(user)
        session.commit()
        print("User add to database")
    

def addPost(userId, postContent, session):
    newPost = posts(userId, postContent)
    session.add(newPost)
    session.commit()

def addLike(userId, postId):
    like = likes(userId, postId)
    session.add(like)
    session.commit()
    print("like was added")

db =  "postgresql://postgres:Hariom@localhost/postgres"
engine = create_engine(db)
Base.metadata.create_all(bind= engine)

Session = sessionmaker(bind=engine)
session = Session()

#create a user
firstName = "Clark"
lastName = "Histon"
profileName = "CH87"
email = "Clark.histon@gmail.com"
#addUser(firstName,lastName,profileName,email,session)


# user = users(firstName,lastName,profileName,email)
# session.add(user)
# session.commit()
# print("User add to database")

#create a post
userId = "0bb18ab8-8d33-4a7f-926d-603790e56565"
#postId = "d14e89c4-294c-49e6-a10e-53996eab9cb1"
postId = "226764cf-89f3-4446-bc68-9321b3eba0da"
#userId = "7896c01b-2b97-4019-bc12-23f3893b4f6a"
postContent = "let's meet in the box-office! "
#addPost(userId,postContent,session)
# newPost = posts(userId,postContent)
# session.add(newPost)
session.commit()
session.close()

#allPosts = session.query(posts).filter(posts.userID==userId).all()
# print(allPosts)
# postsFilterByUser = [p.postContent for p in allPosts]
# print(postsFilterByUser)

# userPosts = []
# for p in allPosts:
#     userPosts.append(p.postContent)
# print(userPosts)

#addLike(userId, postId)
postlikes = session.query(likes).filter(likes.postsId==postId).all()
print(len(postlikes))


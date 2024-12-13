from sqlalchemy import Column, Integer, String, Boolean, LargeBinary, ForeignKey, Date
from sqlalchemy.orm import relationship
from .database import Base

class Students(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(String)
    name = Column(String)
    surname = Column(String)
    hashed_password = Column(String, nullable=True)
    year = Column(Integer, nullable=True)
    is_ta = Column(Boolean, nullable=True)
    picture = Column(LargeBinary, nullable=True)
    ta_course_id = Column(String, nullable=True)

    registered_courses = relationship("Courses", back_populates="registered_by")

    posted = relationship("Threads", back_populates="author")
    likedThreads = relationship("ThreadsLikes")
    comment = relationship("Comments", back_populates="author")
    reply = relationship("SubComments", back_populates="author")

    likedHomeThreads = relationship("HomeThreadsLike")
    posted_public = relationship("HomeThreads", back_populates="author")
    comment_public = relationship("HomeComments", back_populates="author")
    reply_public = relationship("HomeSubComments", back_populates="author")

class Courses(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, autoincrement=True)
    course_id = Column(String)
    name = Column(String)
    student_id = Column(String, ForeignKey("students.student_id"))
    year = Column(Integer)
    
    registered_by = relationship("Students", back_populates="registered_courses")
    forums = relationship("Threads")

class Threads(Base):
    __tablename__ = "threads"

    id = Column(Integer, primary_key=True, autoincrement=True)
    create_by = Column(String, ForeignKey("students.student_id"))
    course_id = Column(String, ForeignKey("courses.course_id"))
    title = Column(String)
    body = Column(String)
    is_highlight = Column(Boolean)
    likes = Column(Integer)
    create_at = Column(String)
    
    files = relationship("ThreadsFiles")
    liked_by = relationship("ThreadsLikes")
    comments = relationship("Comments")
    author = relationship("Students", back_populates="posted")

class ThreadsLikes(Base):
    __tablename__ = "threads_likes"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    course_id = Column(String, ForeignKey("courses.course_id"))
    thread_id = Column(Integer, ForeignKey("threads.id"))
    student_id = Column(String, ForeignKey("students.student_id"))

class ThreadsFiles(Base):
    __tablename__ = "threads_files"
    id = Column(Integer, primary_key=True, autoincrement=True)
    thread_id = Column(Integer, ForeignKey("threads.id"))
    file_name = Column(String)

class Comments(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True)
    comment_from = Column(Integer, ForeignKey("threads.id"))
    course_id = Column(String, ForeignKey("courses.course_id"))
    comment_data = Column(String)
    posted_by = Column(String, ForeignKey("students.student_id"))
    create_at = Column(String)

    subcomments = relationship("SubComments")
    author = relationship("Students", back_populates="comment")

class SubComments(Base):
    __tablename__ = "subcomments"

    id = Column(Integer, primary_key=True)
    reply_of = Column(Integer, ForeignKey("comments.id"))
    reply_data = Column(String)
    posted_by = Column(String, ForeignKey("students.student_id"))
    create_at = Column(String)
    
    author = relationship("Students", back_populates="reply")

class HomeThreads(Base):
    __tablename__ = "home"

    id = Column(Integer, primary_key=True, autoincrement=True)
    create_by = Column(String, ForeignKey("students.student_id"))
    title = Column(String)
    body = Column(String)
    is_highlight = Column(Boolean)
    likes = Column(Integer)
    create_at = Column(String)
    
    files = relationship("HomeThreadsFiles")
    liked_by = relationship("HomeThreadsLike")
    comments = relationship("HomeComments")
    author = relationship("Students")

class HomeThreadsLike(Base):
    __tablename__ = "home_likes"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    thread_id = Column(Integer, ForeignKey("home.id"))
    student_id = Column(String, ForeignKey("students.student_id"))

class HomeThreadsFiles(Base):
    __tablename__ = "home_files"

    id = Column(Integer, primary_key=True, autoincrement=True)
    thread_id = Column(Integer, ForeignKey("home.id"))
    file_name = Column(String)

class HomeComments(Base):
    __tablename__ = "home_comments"

    id = Column(Integer, primary_key=True, autoincrement=True)
    comment_from = Column(Integer, ForeignKey("home.id"))
    comment_data = Column(String)
    posted_by = Column(String, ForeignKey("students.student_id"))
    create_at = Column(String)

    subcomments = relationship("HomeSubComments")
    author = relationship("Students")

class HomeSubComments(Base):
    __tablename__ = "home_subcomments"

    id = Column(Integer, primary_key=True, autoincrement=True)
    reply_of = Column(Integer, ForeignKey("home_comments.id"))
    reply_data = Column(String)
    posted_by = Column(String, ForeignKey("students.student_id"))
    create_at = Column(String)

    author = relationship("Students")
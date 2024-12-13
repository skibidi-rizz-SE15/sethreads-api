from .students import Student, StudentCreate, StudentBase, StudentAllAttributes, Students
from .courses import Course, CourseCreate, CourseBase
from .threads import Thread, ThreadCreate, ThreadBase, ThreadUpdate, ThreadForStudent
from .thread_liked import ThreadLikedBase
from .comments import Comment, CommentCreate, CommentUpdate, CommentForStudent, CommentForThread
from .subcomments import SubComment, SubCommentCreate, SubCommentUpdate, SubCommentForStudent, SubCommentBase
from .home_threads import HomeThread, HomeThreadCreate, HomeThreadBase, HomeThreadUpdate, HomeThreadForStudent
from .homethread_liked import HomeThreadLikedBase
from .home_comments import HomeCommentForThread, HomeCommentForStudent, HomeComment, HomeCommentCreate, HomeCommentUpdate
from .home_subcomments import HomeSubComment, HomeSubCommentCreate, HomeSubCommentUpdate, HomeSubCommentForStudent, HomeSubCommentBase
from .files import HomeThreadsFiles, ThreadsFiles

Student.model_rebuild()
Students.model_rebuild()
StudentAllAttributes.model_rebuild()
Course.model_rebuild()
Thread.model_rebuild()
ThreadCreate.model_rebuild()
Comment.model_rebuild()
HomeThread.model_rebuild()
HomeComment.model_rebuild()
HomeSubComment.model_rebuild()
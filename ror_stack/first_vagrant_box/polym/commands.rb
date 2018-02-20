# createing a polymorphic model
rails g model Comment content:text commentable:references{polymorphic}

# add comments for user, blog, post and message
Comment.create(content: "This is a comment from the 2nd user", commentable: User.second)
Comment.create(content: "Another comment from the 2nd user", commentable: User.second)
User.second.comments

Comment.create(content: "This is a comment on the first blog", commentable: Blog.first)
Comment.create(content: "Another comment on the first blog", commentable: Blog.first)
Blog.first.comments

Comment.create(content: "This is a comment on the third post", commentable: Post.third)
Comment.create(content: "Another comment on the third post", commentable: Post.third)
Post.third.comments

Comment.create(content: "This is a comment on the tenth message", commentable: Message.find(10))
Comment.create(content: "Another comment on the tenth message", commentable: Message.find(10))
Message.find(10).comments

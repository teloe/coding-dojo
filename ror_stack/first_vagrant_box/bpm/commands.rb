# create 5 new blogs.
Blog.create(name:"blog1", description:"description1")
Blog.create(name:"blog2", description:"description2")
Blog.create(name:"blog3", description:"description3")
Blog.create(name:"blog4", description:"description4")
Blog.create(name:"blog5", description:"description5")

# create several posts for each blog.
Post.create(title:"post1", content:"content1", blog:Blog.first)
Blog.first.posts.create(title:"post2", content:"content2")
Blog.first.posts.create(title:"post3", content:"content3")
Blog.first.posts.create(title:"post4", content:"content4")

# create several messages for the first post.
Post.first.messages.create(title:"message1", content:"content1")
Post.first.posts.create(title:"message2", content:"content2")
Post.first.posts.create(title:"message3", content:"content3")
  #answer key
  post = Post.first
  names = ["John Doe", "Jane Doe", "Jennifer Doe", "Michael Smith", "Michelle Smith", "Mitchell Smite"]
  names.each { |elem| post.messages.create(author: elem, message: "This message belongs to the first post") }

# know how to retrieve all posts for the first blog.
Blog.first.posts

# know how to retrieve all posts for the last blog (sorted by title in the DESC order).
Post.where(blog: Blog:last).order(title: :desc)

# know how to update the first post's title.
Post.first.update(title: "Updating the title")

# know how to retrieve all blogs.
Blog.all

# know how to retrieve all blogs whose id is less than 5.
Blog.where("id < ?", 5)

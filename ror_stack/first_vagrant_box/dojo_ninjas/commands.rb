# Start a new project (the name of the project should be 'dojo_ninjas')
rails new dojo_ninjas

# Create appropriate tables/models.
rails g model Dojo name:string city:string state:string
rails g model Ninja first_name:string last_name:string dojo:references
rake db:migrate

# Create 3 dojos (insert some blank entries just to make sure it's allowing you to insert empty entries)
dojo1.name = "CodingDojo Silicon Valley"
=> "CodingDojo Silicon Valley"
dojo1.city = "Mountain View"
=> "Mountain View"
dojo1.state = "CA"
=> "CA"

dojo2 = Dojo.new(name:"CodingDojo Seattle", city:"Seattle", state:"WA")
dojo3 = Dojo.new(name:"CodingDojo New York", city:"New York", state:"NY")

# Delete the three dojos you created
Dojo.destroy_all

# Create 3 additional dojos by using Dojo.new.
dojo1 = Dojo.new(name: "CodingDojo Seattle", city: "Seattle", state: "WA")
dojo1.save
dojo2 = Dojo.new(name: "CodingDojo Silicon Valley", city: "Mountain View", state: "CA")
dojo2.save
dojo3 = Dojo.new(name: "CodingDojo New York", city: "New York", state: "NY")
dojo3.save

# Try to create a few more dojos but without specifying some of the required fields. Make sure that the validation works and generates the errors.
dojo = Dojo.new(name: "CodingDojo Burbank", city: "Burbank")
dojo.save
dojo.errors.full_messages # => ["State can't be blank", "State is the wrong length (should be 2 characters)"]

dojo = Dojo.new(name: "CodingDojo Burbank", state: "CA")
dojo.save
dojo.errors.full_messages # => ["City can't be blank"]

dojo = Dojo.new(city: "Los Angeles", state: "CA")
dojo.save
dojo.errors.full_messages # => ["Name can't be blank"]

# Create 3 ninjas that belong to the first dojo you created.
Dojo.first.ninjas.create(first_name: "John", last_name: "Doe")
Dojo.first.ninjas.create(first_name: "Jane", last_name: "Doe")
Dojo.first.ninjas.create(first_name: "Jen", last_name: "Doe")

# reate 3 more ninjas and have them belong to the second dojo you created.
Dojo.second.ninjas.create(first_name: "Bob", last_name: "Smith")
Dojo.second.ninjas.create(first_name: "Jack", last_name: "Smith")
Dojo.second.ninjas.create(first_name: "Jill", last_name: "Smith")

3.times {Dojo.second.create(first_name: "Bob", last_name: "Smith")}

for i in (0...3)
  Dojo.second.ninjas.create(first_name: "#{i}", last_name: "#{i}")
end

# Create 3 more ninjas and have them belong to the second dojo you created.
Dojo.third.ninjas.create(first_name: "Kevin", last_name: "Johnson")
Dojo.third.ninjas.create(first_name: "Kyle", last_name: "Johnson")
Dojo.third.ninjas.create(first_name: "Kurt", last_name: "Johnson")

# Make sure you understand how to get all of the ninjas for any dojo (e.g. get all the ninjas for the first dojo, second dojo, etc)
Dojo.first.ninjas
Dojo.second.ninjas
Dojo.third.ninjas

# How would you only retrieve the first_name of the ninja that belongs to the second dojo and order the result by created_at DESC order?
Ninja.where(dojo: Dojo.second).select(:id, :first_name).order(created_at: :desc)
Dojo.second.ninjas.select(:id, :first_name).order("created_at DESC")

# Delete the second dojo. How could you adjust your model so that it automatically removes all of the ninjas associated with that dojo?
class Dojo < ActiveRecord::Base
  # add dependent: :destroy
  has_many :ninjas, dependent: :destroy
  validates :name, :city, :state, presence: true
  validates :state, length: { is: 2 }
end

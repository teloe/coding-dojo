# Go ahead and try the following methods:

# .include?(value) => true or false
a = [ "a", "b", "c" ]
a.include?("b")   #=> true
a.include?("z")   #=> false

# .last => returns the last object in range
a = [ "w", "x", "y", "z" ]
a.last     #=> "z"
a.last(2)  #=> ["y", "z"]

# .max => returns the maximum value in range
a = [ "w", "x", "y", "z" ]
a.last     #=> "z"
a.last(2)  #=> ["y", "z"]

# .min => returns the minimum value in range
a = %w(albatross dog horse)
a.min                                   #=> "albatross"
a.min { |a, b| a.length <=> b.length }  #=> "dog"

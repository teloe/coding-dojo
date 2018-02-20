# Try the following methods at least once either on a separate Ruby file or on irb.

# .at or .fetch
a = [ "a", "b", "c", "d", "e" ]
a.at(1) #=> "b"

# .delete
a = [ "a", "b", "c", "d", "e" ]
a.deletet("b") #=> "b"

# .reverse
[ "a", "b", "c" ].reverse #=> [ "c", "b", "a" ]

# .length
[ 1, 2, 3, 4, 5 ].length #=> 5

# .sort
arr = [ "d", "a", "e", "c", "b" ]
arr.sort  #=> ["a", "b", "c", "d", "e"]

# .slice
a = [ "a", "b", "c", "d", "e" ]
a[2] +  a[0] + a[1]    #=> "cab"
a[6]                   #=> nil
a[1, 2]                #=> [ "b", "c" ]
a[1..3]                #=> [ "b", "c", "d" ]
a[4..7]                #=> [ "e" ]
a[6..10]               #=> nil
a[-3, 3]               #=> [ "c", "d", "e" ]

# .shuffle
a = [ 1, 2, 3 ]           #=> [1, 2, 3]
a.shuffle                 #=> [2, 3, 1]

# .join
[ "a", "b", "c" ].join        #=> "abc"
[ "a", "b", "c" ].join("-")   #=> "a-b-c"

# .insert
a = %w{ a b c d }
a.insert(2, 99)         #=> ["a", "b", 99, "c", "d"]

# .values_at() -> returns an array with values specified in the param
a = %w{ a b c d e f }
a.values_at(1, 3, 5)          # => ["b", "d", "f"]
a.values_at(1, 3, 5, 7)       # => ["b", "d", "f", nil]
a.values_at(-1, -2, -2, -7)   # => ["f", "e", "e", nil]
a.values_at(4..6, 3...6)      # => ["e", "f", nil, "d", "e", "f"]

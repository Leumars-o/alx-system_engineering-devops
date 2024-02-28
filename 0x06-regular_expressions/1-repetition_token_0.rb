#!/usr/bin/env ruby
# a ruby script that aacepts one arguemnt and
# matches a regex expression

puts ARGV[0].scan(/hbt{2, 5}n/).join

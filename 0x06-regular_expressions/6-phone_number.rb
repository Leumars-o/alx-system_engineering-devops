#!/usr/bin/env ruby
# a ruby script that matches a regex for a 10 digit phone number

puts ARGV[0].scan(/^[0-9]{10}$/).join

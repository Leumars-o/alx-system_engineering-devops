#!/usr/bin/env ruby
# a ruby script that matches a regex for a repititve token

puts ARGV[0].scan(/\[from:([\+?0-9A-Za-z]+)\] \[to:(\+?\d+)\] \[flags:(-?\d+:-?\d+:-?\d+:-?\d+:-?\d+)\]/).join(",")

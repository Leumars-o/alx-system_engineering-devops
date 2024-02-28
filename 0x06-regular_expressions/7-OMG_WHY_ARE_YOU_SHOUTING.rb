#!/usr/bin/env ruby
# a ruby script that matches a regex for CAPITAL LETTERS

puts ARGV[0].scan(/[A-Z]/).join

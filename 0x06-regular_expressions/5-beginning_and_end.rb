#!/usr/bin/env ruby
# a ruby script that matches a regex starting with
# 'h' and ending with 'n' and can have any single char in between

puts ARGV[0].scan(/h.n/).join

# script to execute a command using puppet
exec { 'killmenow':
  command  => '/usr/bin/pkill -9 -f killmenow',
}

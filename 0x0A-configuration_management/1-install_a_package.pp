# install a package using puppet

exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  path    => ['/bin', '/usr/bin'],
  unless  => '/usr/bin/pip3 show Flask | grep -q "Version: 2.1.0"',
}
package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}

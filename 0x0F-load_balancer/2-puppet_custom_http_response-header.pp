# Creating a custom HTTP header response for the HAproxy
exec {'update':
  command => '/usr/bin/apt-get update',
}

package {'nginx web server':
  ensure  => installed,
  require => Exec['update'],
}

file_line {'header response':
  ensure  => present,
  path    => '/etc/nginx/sites-available/default',
  after   => 'listen 80 default_server;',
  line    => "add_header X-Served-By ${hostname};",
  require => Package['nginx'],
}

service { 'nginx':
  ensure     => running,
  require    => Package['nginx'],
  hasrestart => true
}

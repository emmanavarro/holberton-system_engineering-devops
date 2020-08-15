# Creating a custom HTTP header response for the HAproxy
exec {'update':
  command  => 'sudo apt-get update',
  provider => shell,
}

package {'nginx':
  ensure  => installed,
  require => Exec['update'],
}

file_line {'header_response':
  ensure  => present,
  path    => '/etc/nginx/sites-available/default',
  after   => 'listen 80 default_server;',
  line    => "add_header X-Served-By ${hostname};",
  require => Package['nginx'],
}

service { 'nginx':
  ensure  => running,
  require => File_line['header_response'],
}

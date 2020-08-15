# Creating a custom HTTP header response for the HAproxy
exec {'update':
  command => '/usr/bin/apt-get -y update',
}

package {'nginx web server':
  ensure  => installed,
  require => Exec['update'],
}

file { '/var/www/html/index.html':
  ensure  => present,
  path    => '/var/www/html/index.html',
  content => 'Holberton School',
  require => Package['nginx'],
}

file_line { 'redirect to 301':
  ensure  => present,
  path    => '/etc/nginx/sites-available/default',
  after   => 'listen 80 default_server;',
  line    => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
  require => Package['nginx'],
}

file_line {'header response':
  ensure  => present,
  path    => '/etc/nginx/sites-available/default',
  after   => 'listen 80 default_server;',
  line    => "add_header X-Served-By $HOSTNAME;",
  require => Package['nginx'],
}

service { 'nginx':
  ensure     => running,
  require    => Package['nginx'],
  hasrestart => true
}

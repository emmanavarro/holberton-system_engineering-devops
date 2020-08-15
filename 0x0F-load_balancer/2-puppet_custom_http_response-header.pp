# Creating a custom HTTP header response for the HAproxy
exec {'update':
  command => '/usr/bin/sudo apt-get -y update',
}

package {'nginx web server':
  ensure => installed,
  name   => 'nginx'
}

file { '/var/www/html/index.html':
  ensure  => present,
  path    => '/var/www/html/index.html',
  content => 'Holberton School'
}

file_line { 'redirect to 301':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;'
}

file_line {'header response':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'add_header X-Served-By $HOSTNAME;'
}

service { 'nginx':
  ensure     => running,
  require    => Package['nginx'],
  hasrestart => true
}

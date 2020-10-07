# Fix the open file descriptor limit 'ULIMIT'
exec { 'ulimit':
  command  => 'sed -i "s+15+2000+g" /etc/default/nginx',
  provider => shell,
}

exec { 'restartnginxservice':
  command  => 'service nginx restart',
  provider => shell,
  require  => Exec['ulimit'],
}

# Creates a manifest that kills a process named killmenow
exec {'killer':
  path    => '/usr/bin',
  command => 'pkill -f ./killmenow'
}

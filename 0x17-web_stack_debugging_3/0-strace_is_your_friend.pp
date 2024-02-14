# Fix the issue based on the strace output

exec { 'fix_apache_error':
  command     => '/usr/sbin/service apache2 restart',
  path        => '/usr/bin',
  refreshonly => true,
}

# Fix the issue based on the strace output

exec { 'fix_apache_issue':
  command     => '/usr/sbin/service apache2 restart',
  path        => '/usr/bin',
  refreshonly => true,
  subscribe   => File['/path/to/modified_configuration_or_file'],
}

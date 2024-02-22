# Increases the amount of traffic an Nginx server can handle.

exec { 'set ulimit -n 4096':
	command => "sed -i 's/15/4096/' /etc/default/nginx",
		path    => ['/bin/', '/sbin/', '/usr/bin/', '/usr/sbin/'],
}

exec { 'restart service':
	command => 'service nginx restart',
		path    => ['/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/'],
}

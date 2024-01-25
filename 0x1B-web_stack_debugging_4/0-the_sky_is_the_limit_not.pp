# Fixing the number of failed requests to get 0.
exec { 'fix--for-nginx':
  command => "/mnt/ubuntu/sbin/start-stop-daemon --name nginx --stop; /mnt/ubuntu/sbin/start-stop-daemon --name nginx --start --exec /usr/sbin/nginx -- -c /etc/nginx/nginx.conf",
  path    => ['/bin', '/usr/bin', '/usr/sbin', '/sbin', '/mnt/ubuntu/sbin'],
}

# Ensure Nginx package is installed
package { 'nginx':
  ensure => installed,
}

# Set custom HTTP headers in Nginx configuration
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "server {
                listen 80 default_server;
                server_name _;
                add_header X-Served-By $::hostname;
              }",
  notify  => Service['nginx'],
}

# Ensure Nginx service is running
service { 'nginx':
  ensure => running,
}


# Install Nginx package

package { 'nginx':
  ensure => installed,
}

# Configure and start Nginx service
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

# Create the index.html file with 'Hello World!' content
file { '/var/www/html/index.html':
  content => 'Hello World!',
  require => Package['nginx'],
}

# Configure the Nginx default site
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "
    # Nginx default site configuration

    server {
        listen 80;
        server_name _;

        location / {
            return 301 http://$host/redirect_me;
        }

        location /redirect_me {
            return 301 http://$host/;
        }

        location / {
            root /var/www/html;
            index index.html;
        }
    }
  ",
  notify  => Service['nginx'],
  require => Package['nginx'],
}

# Execute curl command to test Nginx server
exec { 'test_nginx':
  command     => "curl -s http://localhost/",
  path        => ['/usr/bin', '/bin'],
  refreshonly => true,
  subscribe   => Service['nginx'],
}

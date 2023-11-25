# Description: Creates a file in /tmp with specific permissions, owner, group, and content
#
# File path: /tmp/school
# File permission: 0744
# File owner: www-data
# File group: www-data
# File content: "I love Puppet"

file { '/tmp/school':
  ensure  => file,
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => "I love Puppet\n",
}

notify { 'Finished catalog run':
  message => 'Finished catalog run in 0.03 seconds',
}

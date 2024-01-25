tack Debugging #4

## Description
In this project, we are tasked with debugging and optimizing a web server setup featuring Nginx under pressure using ApacheBench for benchmarking. The goal is to address the high number of failed requests and improve the overall performance of the stack.

## Requirements
### General
- All files are interpreted on Ubuntu 14.04 LTS.
- Files should end with a new line.
- A README.md file at the root of the project folder is mandatory.
- Puppet manifests must pass puppet-lint version 2.1.1 without any errors.
- Puppet manifests must run without error.
- Puppet manifests' first line must be a comment explaining the manifest's purpose.
- Puppet manifest files must end with the extension .pp.
- Files will be checked with Puppet v3.4.

### Install puppet-lint
```bash
$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1

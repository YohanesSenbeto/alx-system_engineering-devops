#!/bin/bash

# Function to display information about a subdomain
get_subdomain_info() {
    domain="$1"
    subdomain="$2"
    
    # Use dig to fetch DNS information and awk to filter
    result=$(dig "${subdomain}.${domain}" | awk '/ANSWER SECTION/ {getline; print}')
    
    if [ -z "$result" ]; then
        echo "The subdomain ${subdomain} does not have valid records or is not configured properly."
    else
        echo "The subdomain ${subdomain} is a A record and points to ${result}"
    fi
}

# Main script logic
domain="$1"
subdomain="$2"

if [ -z "$subdomain" ]; then
    # Display information for default subdomains
    get_subdomain_info "$domain" "www"
    get_subdomain_info "$domain" "lb-01"
    get_subdomain_info "$domain" "web-01"
    get_subdomain_info "$domain" "web-02"
else
    # Display information for the specified subdomain
    get_subdomain_info "$domain" "$subdomain"
fi


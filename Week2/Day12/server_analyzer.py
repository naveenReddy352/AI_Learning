def analyze_server(data):

    critical_servers = []
    high_severity__servers = []
    normal_servers = []

    for server in data:
        if server["error_count"] > 20:
            critical_servers.append(server)
        elif server["error_count"] > 10:
            high_severity__servers.append(server)
        else:
            normal_servers.append(server)
    
    return critical_servers, high_severity__servers, normal_servers

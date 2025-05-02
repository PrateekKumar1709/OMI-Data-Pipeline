# Security

## Overview

This document outlines the security measures and practices implemented in the OMI Data Pipeline project.

## Security Scanning

### OWASP ZAP Scanning

The project uses OWASP ZAP (Zed Attack Proxy) for automated security scanning. The scanning is performed:

1. On every push to the main branch
2. On every pull request
3. Weekly on a scheduled basis

The scan is configured to:
- Target the frontend service running on port 5173
- Use a custom rules file (`.zap/rules.tsv`) to ignore known false positives
- Run in automated mode with MEDIUM scan level
- Generate and store scan results as artifacts

Scan results are available as GitHub Actions artifacts and are retained for 30 days.

### Custom Rules

The project maintains a custom rules file (`.zap/rules.tsv`) that configures which security checks to ignore. This helps reduce noise from false positives while maintaining focus on actual security issues.

Common ignored checks include:
- Cookie security headers
- Various HTTP security headers
- Application error disclosure
- Modern web application detection

## Security Best Practices

1. All code changes must be reviewed by at least one other team member
2. Dependencies are regularly updated to patch security vulnerabilities
3. Secrets and sensitive information are never committed to the repository
4. All API endpoints are properly authenticated and authorized
5. Input validation is performed on all user inputs
6. Error messages are sanitized to prevent information disclosure

## Reporting Security Issues

If you discover a security vulnerability, please report it by:

1. Creating a new issue with the "security" label
2. Providing detailed information about the vulnerability
3. Not disclosing the vulnerability publicly until it has been addressed

The security team will review and respond to all security reports promptly.

## Security Contact

For security-related questions or concerns, please contact the project maintainers through the GitHub issues system. 
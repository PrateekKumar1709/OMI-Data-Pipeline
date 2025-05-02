# OWASP ZAP Security Scanning

This document describes the OWASP ZAP (Zed Attack Proxy) integration in our project for dynamic application security testing.

## Overview

OWASP ZAP is an open-source web application security scanner. We use it to:
- Perform automated security testing
- Identify potential security vulnerabilities
- Ensure compliance with security best practices

## Integration Details

### GitHub Actions Workflow

We have implemented a GitHub Actions workflow (`.github/workflows/owasp-zap.yml`) that:
- Runs on every push to main
- Runs on pull requests
- Runs weekly on Sundays
- Uses the ZAP baseline scan action
- Uploads scan results as artifacts
- Fails the build if critical issues are found

### Configuration

The ZAP configuration is stored in:
- `.zap/rules.tsv`: Custom rules for the baseline scan
- `.github/workflows/owasp-zap.yml`: Workflow configuration

## Running Scans Locally

To run ZAP scans locally:

1. Install ZAP:
   ```bash
   # For macOS
   brew install zap
   
   # For Linux
   sudo apt install zaproxy
   ```

2. Run a baseline scan:
   ```bash
   zap-baseline.py -t http://localhost:8000 -g gen.conf -r testreport.html
   ```

## Understanding Results

The scan results will be available as GitHub Actions artifacts. They include:
- HTML report
- JSON results
- Summary of findings

## Security Rules

Our baseline scan includes rules for:
- SQL Injection
- Cross-Site Scripting (XSS)
- Cross-Site Request Forgery (CSRF)
- Insecure Deserialization
- And other OWASP Top 10 vulnerabilities

## Best Practices

1. Always review ZAP scan results
2. Address high and critical findings promptly
3. Keep ZAP and its rules up to date
4. Consider running additional manual tests for complex features

## Resources

- [OWASP ZAP Documentation](https://www.zaproxy.org/docs/)
- [ZAP GitHub Action](https://github.com/zaproxy/action-baseline)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) 
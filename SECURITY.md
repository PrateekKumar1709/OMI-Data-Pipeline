## Open Model Initiative Security Policy

---

### Reporting a Security Bug

---

If you think you have discovered a security issue in any of the OMI projects or released artifacts, we'd love to hear from you. We will take all security bugs seriously and if confirmed upon investigation we will patch it within a reasonable amount of time and release a public security bulletin discussing the impact and credit the discoverer.

### Security Scanning

---

The OMI project uses OWASP ZAP (Zed Attack Proxy) for automated security scanning. This helps us identify and address potential security vulnerabilities early in the development process.

#### Automated Scanning

- Weekly baseline scans are performed automatically via GitHub Actions
- Pull requests trigger security scans to catch issues before merging
- Scan results are available as workflow artifacts
- Issues are categorized by severity (HIGH, MEDIUM, LOW)

#### Custom Rules

The project maintains custom rules in `.zap/rules.tsv` to:
- Exclude false positives
- Adjust severity levels for specific cases
- Ignore development-specific warnings

#### Running Scans Locally

To run OWASP ZAP scans locally:

1. Install ZAP:
   ```bash
   # Using Docker
   docker pull owasp/zap2docker-stable
   
   # Or download from https://www.zaproxy.org/download/
   ```

2. Run a baseline scan:
   ```bash
   zap-baseline.py -t http://localhost:8000 -g gen.conf -r testreport.html
   ```

3. Review the results in `testreport.html`

#### Security Scan Results

- Scan results are stored as GitHub Actions artifacts
- Results are retained for 30 days
- Critical issues are addressed immediately
- Medium and low severity issues are tracked and addressed in regular development cycles

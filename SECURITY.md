# Security Policy

## Supported Versions

Only the latest version of the ABA PayWay Python SDK receives security updates.

| Version | Supported          |
|---------|--------------------|
| 0.1.x   | ✅ Yes             |
| < 0.1   | ❌ No              |

---

## Reporting a Vulnerability

**Please do NOT report security vulnerabilities through public GitHub Issues.**

If you discover a security vulnerability in this SDK, please report it responsibly by emailing:

📧 **khonchanphearaa@gmail.com**

Please include the following in your report:

- A clear description of the vulnerability
- Steps to reproduce the issue
- Potential impact (what an attacker could do)
- Any suggested fix (optional but appreciated)

### What to expect

- **Acknowledgement** within 48 hours
- **Status update** within 5 business days
- **Fix and release** as soon as possible depending on severity
- Credit in the release notes if you wish (just let us know)

We appreciate responsible disclosure and will never take legal action against researchers who follow this process.

---

## Security Best Practices for SDK Users

### 1. Never hardcode credentials

```python
# Bad — never commit this
config = PayWayConfig(
    merchant_id="your_merchant_id",
    api_key="your_api_key",
)

# Good — load from environment
import os
config = PayWayConfig(
    merchant_id=os.environ["ABA_MERCHANT_ID"],
    api_key=os.environ["ABA_API_KEY"],
)
```

### 2. Use a `.env` file locally, never commit it

```bash
# .env
ABA_MERCHANT_ID=your_merchant_id
ABA_API_KEY=your_api_key
```

```bash
# .gitignore — make sure this is present
.env
.env.*
```

### 3. Use environment variables in production

On your server or CI/CD pipeline, set secrets as environment variables — never store them in config files that get committed to version control.

### 4. Rotate your API key if compromised

If you suspect your API key has been exposed:
1. Contact ABA PayWay immediately at [paywaysales@ababank.com](mailto:paywaysales@ababank.com)
2. Request a new API key
3. Update your environment variables
4. Audit your git history — if the key was committed, it is permanently exposed even after deletion

### 5. Whitelist your server IP

ABA PayWay restricts API access by IP address. Only whitelist IPs you control and trust. Remove old IPs when decommissioning servers.

---

## What This SDK Does to Keep You Secure

| Protection | Details |
|---|---|
| **HMAC-SHA512 signing** | Every request is signed — the API key never travels over the wire |
| **HTTPS only** | All communication is encrypted in transit |
| **Zero dependencies** | No third-party packages = no supply chain risk |
| **Request timeout** | Prevents hanging connections (default: 30s) |
| **API key masked** | The key never appears in logs or `repr()` output |
| **Input validation** | Requests are validated before being sent to the API |
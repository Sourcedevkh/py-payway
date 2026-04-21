# Changelog

All notable changes to the ABA PayWay Python SDK will be documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
This project follows [Semantic Versioning](https://semver.org/).

---

## [Unreleased]

---

## [0.1.3] - 2026-04-21

### Fixed
- Corrected transaction client imports so installed packages resolve `CheckTransactionRequest` and `CloseTransactionRequest` from the request model module.

---

## [0.1.2] - 2026-04-21

### Fixed
- Removed unused imports that broke Ruff checks in GitHub Actions.
- Fixed package exports so `CheckTransactionRequest` and `CloseTransactionRequest` resolve correctly after install.

---

## [0.1.0] - 2025-04-19

### Added
- `PayWayClient` — unified client facade for all API modules
- `PayWayConfig` — configuration with sandbox/production environment support
- `Environment` enum — `SANDBOX` and `PRODUCTION`
- **QR API** — `client.qr.generate_qr(request)` — generate payment QR codes
- **Check Transaction API** — `client.check_transaction.check(tran_id)` — check payment status
- **Close Transaction API** — `client.close_transaction.close(tran_id)` — cancel a transaction
- HMAC-SHA512 request signing — automatic hash generation per request
- Base64 helpers — `encode_items()`, `encode_url()`, `encode_base64()`
- `get_req_time()` — auto-generates UTC timestamp in ABA PayWay format
- Custom exceptions — `PayWayAPIError`, `PayWayRequestError`, `PayWayValidationError`
- Zero third-party dependencies — stdlib only
- 36 unit tests covering all models, hash utility, and helpers
- Example scripts for all 3 endpoints
- Apache 2.0 License
- Security policy (`SECURITY.md`)
- Contributing guide (`CONTRIBUTING.md`)
# Security Policy

## Supported Versions

| Version | Supported |
| ------- | --------- |
| master | yes |
| older | no |

This repository tracks `master` as the only supported line. Older commits are not patched.

## Reporting a Vulnerability

Please report security vulnerabilities by email to **<security@akax.dev>** (PGP key on request). Do **not** file a public GitHub issue for suspected security bugs — disclosure starts private and is coordinated with the reporter.

A good report includes:

- Reproduction steps (minimal example, command sequence, or request)
- Affected commit SHA and the version you tested against
- Impact assessment (what an attacker could achieve)
- Whether the issue is currently being exploited in the wild

### Response Targets

- **Initial acknowledgement:** within 72 hours of report
- **Triage verdict and severity rating:** within 7 days
- **Patch for critical / high severity issues:** within 30 days
- **Coordinated disclosure timeline:** agreed case-by-case, default 90 days from acknowledgement

### Out of Scope

The following are out of scope for security reports:

- Rate limiting or DoS against infrastructure owned by the reporter
- Issues requiring physical access to a user's device
- Social-engineering attacks against maintainers
- Vulnerabilities in third-party dependencies that have an upstream fix available — file those at the upstream tracker and link from the report

### Safe Harbor

We will not pursue legal action against reporters who:

- Make a good-faith effort to avoid privacy violations, data destruction, or service disruption
- Stop testing immediately upon discovering a vulnerability and notify us
- Do not exploit a vulnerability beyond what is necessary to demonstrate it
- Do not publicly disclose the issue before coordinated disclosure is agreed

## Security Tooling

This repository uses the following security tooling (configured in `.github/workflows/` and `Backend/Dockerfile`):

- **Scorecard** — weekly OSSF scorecard analysis (`.github/workflows/scorecards.yml`)
- **CodeQL** — code scanning on every push and PR
- **Bandit** — Python security linter
- **Trivy** — container image scanning
- **Snyk / Dependabot** — dependency vulnerability scanning
- **Mend (Whitesource)** — license and security compliance
- **Pinned dependencies** — actions and Python packages pinned by SHA256
- **Code review** — required for `master` (see branch protection rules)

## Acknowledgements

Reporters who follow the disclosure process above will be credited in the fix release notes (unless they prefer anonymity).

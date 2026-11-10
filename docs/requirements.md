\# Security Requirements and Acceptance Criteria



Task: T4 (weeks 5 to 6)

Target application: small Python Flask app with seeded fixtures (CWE 89, 79, 78, 22, 798, 327, 502, 1104).

Threat IDs refer to docs/threat-model.md.

Note: the numeric targets (80%, 20%) are proposals to be confirmed with the supervisor at decision point D1.



| ID | Requirement | Threat | Acceptance criterion |

|---|---|---|---|

| R1 | Every push and pull request runs the pipeline automatically | All | 100% of pushes and pull requests trigger a run |

| R2 | Changes reach main only through a pull request with a passing pipeline | S1, T3 | Direct push to main is blocked by branch protection |

| R3 | All third-party actions are pinned to a full commit SHA | T1 | 100% of actions pinned; zizmor reports no unpinned actions |

| R4 | Every job has read-only permissions unless it needs more | E1 | 100% of jobs declare explicit permissions |

| R5 | The access token is not saved on the runner | I2 | persist-credentials is false in every checkout |

| R6 | Secrets in code are detected before merge | I1 | Gitleaks detects 100% of seeded fake secrets |

| R7 | Injection and other code flaws are detected | T3, I3 | Semgrep detects at least 80% of seeded vulnerable cases |

| R8 | Vulnerable dependencies are detected | T2 | Trivy flags the seeded outdated library |

| R9 | Safe code is not wrongly flagged | All | False positives on safe look-alikes below 20% |

| R10 | A stuck run cannot block the pipeline | D1 | Every job has a timeout; no run exceeds 10 minutes |

| R11 | The gate fails on any scanner error | D2 | 100% of fault-injection tests end in a failed gate |

| R12 | Pull requests from forks cannot use secrets or write access | E2 | Safe trigger used; zizmor reports no dangerous triggers |

| R13 | Exceptions are recorded with reason, approver and expiry | R1 | 100% of exceptions have all three fields; expired ones fail the gate |

| R14 | Results are the same on repeated runs | All | Same decision on 5 repeated runs of the same commit |


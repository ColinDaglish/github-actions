# ADR-0005: Security workflow orchestration pattern

- Status: Accepted
- Date: 2026-09-07

## Context

We needed to provide GitHub Actions security scanning (zizmor) and infrastructure-as-code scanning (checkov) to the datasciencecampus organization. Both are independent tools that analyze different aspects of repositories.

The decision was whether to:

1. Create two independent workflows that trigger separately on each event
2. Create an orchestrator workflow that calls both tools in parallel

## Decision

Create a single orchestrator workflow (`security-analysis.yml`) that runs on `push` and `pull_request` events and calls two child workflows (`zizmor.yml` and `checkov.yml`) in parallel.

- `security-analysis.yml`: Public-facing orchestrator with triggers and concurrency management
- `zizmor.yml`: Reusable-only child workflow (workflow_call only)
- `checkov.yml`: Reusable-only child workflow (workflow_call only)

## Rationale

1. **Unified concurrency management**
   Both tools run/cancel as a single unit. This prevents duplicate runs or partial executions where one tool completes while the other is canceled.

2. **Single source of truth for triggers**
   All event configuration (push to main, pull_request against main) lives in one place. Adding new triggers only requires updating the orchestrator.

3. **Consistent SARIF uploads**
   Both tools' results are subject to the same advanced-security policy (auto-enable for public repos, auto-disable for private repos by default).

4. **Flexible customization**
   - Organization default behavior via `security-analysis.yml` on push/PR
   - Caller customization via workflow_call inputs (config paths, persona, advanced-security override)

5. **Clear caller contract**
   Repositories should call `security-analysis.yml`, not individual tool workflows. This prevents confusion about which workflow to use and ensures both tools always run together.

6. **Parallel execution**
   Both tools run in parallel, reducing overall workflow runtime compared to sequential execution.

## Consequences

Positive:

- Simpler mental model for repository maintainers (one workflow to add, not two)
- Guaranteed consistency: both tools always run together
- Easier to update default behavior organization-wide (one place to change)
- Enforces "security by default" — repositories can't accidentally skip one tool
- Flexible customization for specific repositories via workflow_call

Negative:

- If one tool needs to run independently, we'd need to refactor the architecture
- Child workflows cannot be called directly (only via orchestrator), which limits flexibility
- Orchestrator adds one layer of indirection (minimal performance impact)

## Alternatives considered

1. **Two independent workflows**
   - Pro: Maximum flexibility
   - Con: Duplicate trigger logic, possible race conditions with concurrency, inconsistent SARIF upload policies

2. **Composite action wrapper**
   - Pro: Could wrap both tools
   - Con: Composite actions don't support workflow triggers or SARIF uploads

3. **Orchestrator + direct child calls**
   - Current decision; child workflows are reusable-only to prevent independent runs

## Related decisions

- ADR-0001: Called workflow owns secret usage (applies to child workflows here)
- ADR-0004: Separate reusable pinning from dispatch ref (applies to orchestrator caller patterns)

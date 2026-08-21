# PyGranta ecosystem agent instructions

This file guides AI coding agents (e.g. GitHub Copilot, Cursor) working across the
PyGranta ecosystem. `pygranta` is the umbrella/meta-package for the ecosystem, so
ecosystem-wide conventions live here.

## Repo inventory

The PyGranta ecosystem consists of:

- `pygranta` (this repo, umbrella meta-package)
- `grantami-bomanalytics`
- `grantami-bomanalytics-openapi`
- `grantami-dataflow-extensions`
- `grantami-integrationscore-openapi`
- `grantami-jobqueue`
- `grantami-recordlists`
- `grantami-serverapi-openapi`
- `grantami-system`

Locally, these repos are typically checked out as siblings under the same parent
directory.

## GitHub Actions workflow conventions

- Pin `actions/*` to a full commit SHA with a version comment, e.g.:
  `uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1  # v7.0.1`
- Set `persist-credentials: false` on `actions/checkout` unless the job needs to push.
- Default workflow-level `permissions: {}` (deny by default), then grant only what's
  needed at the job level.
- **Zizmor compliance**: every non-empty `permissions:` entry must have an inline
  `# to <reason>` comment explaining why it's needed, e.g.:
  ```yaml
  permissions:
    contents: read        # to checkout the repository
    pull-requests: write  # to approve PRs
  ```
  Missing comments will be flagged by Copilot/zizmor review on the PR — add them
  proactively rather than waiting for a review round-trip.

## Maintenance

### Canonical shared workflow templates

Prefer copying from an existing, up-to-date repo rather than writing workflows from
scratch. Good reference repos for common `.github/workflows/` files:

- `dependabot_approve.yml` — reference: `grantami-bomanalytics`
- `label.yml` — reference: `grantami-bomanalytics`
- `ci_cd.yml` / `build_and_test_library.yml` — reference: whichever repo most closely
  matches the target repo's type (library vs. generated OpenAPI client)

Before copying, diff the candidate source file against the target repo's existing
workflows of the same purpose across a few repos, to catch any drift between repos
(the "canonical" version may not be identical everywhere — flag discrepancies to the
user rather than silently picking one).

## Efficiency tips for multi-repo audits

- Batch the discovery step: glob/grep across all repo paths in one set of parallel
  calls rather than checking repos one at a time.
- Summarize findings (which repos have/lack the change) before making any edits, so
  the scope of work is clear up front.
- Only touch repos that actually need the change — don't reformat or "helpfully"
  update unrelated files while making a targeted fix.

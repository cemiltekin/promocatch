# PromoCatch Team Contribution Plan

This document summarizes a practical team work division for the PromoCatch project.
It is written to clarify ownership, responsibilities, and possible branch usage.

## Team Members

- Cemil Tekin
- Serdar Kaan Kesen
- Ömer Tarık Çandır

## Developer 1 - Backend and API Layer

Team member: **Cemil Tekin**

Primary files:

- `phase2/main.py`
- `phase2/routers.py`
- `phase2/repository.py`
- `phase2/database.py`
- `phase2/models.py`

Responsibilities:

- Complete campaign API endpoints
- Maintain CRUD flows for campaigns
- Implement and refine search/filter behavior
- Keep the repository and database access layer stable
- Maintain application startup and health endpoint behavior

Related implementation scope:

- `GET /campaigns`
- `GET /campaigns/{campaign_id}`
- `POST /campaigns`
- `PUT /campaigns/{campaign_id}`
- `DELETE /campaigns/{campaign_id}`
- `GET /health`

## Developer 2 - Frontend and UI Integration

Team member: **Ömer Tarık Çandır**

Primary files:

- `phase2/static/index.html`

Responsibilities:

- Build and improve the campaign list interface
- Implement search and filter controls
- Handle add, edit, and delete form flows
- Maintain discount slider and quick-pick controls
- Improve validation messages and frontend usability
- Keep frontend integration with API endpoints working

Related implementation scope:

- Campaign listing UI
- Search and platform filter UI
- Create/update/delete campaign interactions
- Client-side form feedback and edit mode behavior

## Developer 3 - Documentation, Review, and Submission Package

Team member: **Serdar Kaan Kesen**

Primary files:

- `README.md`
- `phase1/README.md`
- `phase2/README.md`
- `phase1/docs/*`
- `phase2/docs/*`
- `phase2/scripts/*`

Responsibilities:

- Organize SAD Phase 1 and Phase 2 documents
- Review documentation structure and wording
- Align implementation details with documentation
- Prepare README guidance for local run and evaluation
- Organize final submission files, screenshots, and presentation material

Related documentation scope:

- SAD V1 and SAD V2
- Team member contribution sections
- Local run instructions
- Submission package naming and review flow

## Suggested Branch Structure

If the team prefers separate branches, the following branch names are appropriate:

- `feature/backend-api`
- `feature/frontend-ui`
- `feature/docs-readme`

Recommended merge target:

- `main`

## Dependency Notes

- Frontend work depends on stable API routes, but can proceed in parallel once endpoint contracts are clear.
- Documentation work can continue in parallel with both backend and frontend development.
- Backend filtering or validation changes may require small frontend text or form updates.

## Important Note

This file documents a reasonable work division for the project.
If the team worked directly on `main`, the branch names above should be treated as recommendations rather than a claim about the exact workflow used.

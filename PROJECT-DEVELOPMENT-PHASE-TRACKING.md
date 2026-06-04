# PROJECT-DEVELOPMENT-PHASE-TRACKING.md — Skill 6: mental-health-guidance

## Overview
**Skill**: mental-health-guidance  
**Domain**: Mental Health Assessment & Psychoeducational Guidance  
**Total Phases**: 6 (Phase 0–5)  
**Target Completion**: 14 weeks from kickoff

---

## Phase 0: Research & Skill Architecture
**Timeline**: Week 1–2  
**Status**: COMPLETE (2026-06-04)

### Tasks
- [x] Review clinical literature on PHQ-9, GAD-7, PCL-5, AUDIT validity and scoring
- [x] Review NICE guidelines: CG90 (depression), CG113 (generalized anxiety), NG116 (PTSD)
- [x] Review APA clinical practice guidelines for depression, PTSD, anxiety
- [x] Document C-SSRS screening protocol for crisis detection
- [x] Map therapeutic frameworks to conditions: CBT/BA/DBT/ACT/MI/MBCT/EMDR/CPT/IPT
- [x] Define harness flow: Stage 0–7 with sub-skill boundaries
- [x] Define quality gates (7 gates)
- [x] Define output format (structured guidance document)
- [x] Create CLAUDE.md, PROJECT-detail.md, PROJECT-DEVELOPMENT-PHASE-TRACKING.md

### Deliverables
- Harness architecture diagram
- Framework-to-condition mapping table
- Quality gate definitions
- CLAUDE.md, PROJECT-detail.md, this file

### Success Criteria
- All design decisions documented with rationale
- Clinical framework mapping validated against NICE/APA guidelines
- Crisis detection protocol (C-SSRS) accurately represented

---

## Phase 1: Core Sub-Skills
**Timeline**: Week 3–5  
**Status**: COMPLETE (2026-06-04)

### Tasks

#### sub-crisis-safety.md (Week 3)
- [x] Implement C-SSRS 5-level probe protocol
- [x] Define CRITICAL / MODERATE / NONE classification rules
- [x] Build emergency resource block (international + local)
- [x] Define hard-stop condition: CRITICAL → stop workflow immediately
- [x] Test: "I want to kill myself" → CRITICAL response correct

#### sub-screening.md (Week 3–4)
- [x] Implement PHQ-9 (9 items, 0–27 scoring, 5 severity bands)
- [x] Implement GAD-7 (7 items, 0–21 scoring, 4 severity bands)
- [x] Implement PCL-5 (20 items, 0–80 scoring, cutoff ≥31)
- [x] Implement AUDIT (10 items, severity classification)
- [x] Implement PHQ-2 triage gateway → PHQ-9
- [x] Build scoring and severity classification logic
- [x] Add clinical interpretation notes for each severity band

#### sub-framework-selector.md (Week 4–5)
- [x] Build condition × severity → framework decision matrix
- [x] Add rationale template for each framework selection
- [x] Include key techniques list per framework (3–5 techniques each)
- [x] Add contraindication awareness (e.g., exposure therapy in acute trauma)
- [x] Include evidence summary (1 RCT citation per framework minimum)

#### sub-guidance-writer.md (Week 5)
- [x] Build structured document template
- [x] Implement plain-language writing standards (Grade 8 Flesch-Kincaid target)
- [x] Implement citation placement (inline + footnote styles)
- [x] Build mandatory disclaimer block
- [x] Build mandatory resource block

### Deliverables
- 4 sub-skill files, each fully functional as standalone prompts
- Clinical accuracy review against NICE/APA guidelines

### Success Criteria
- Each sub-skill can be invoked independently and produces correct output
- PHQ-9 scoring algorithm verified against official scoring key
- Crisis detection correctly identifies passive vs. active suicidal ideation

---

## Phase 2: Main Harness + Quality Gates
**Timeline**: Week 6–8  
**Status**: COMPLETE (2026-06-04)

### Tasks
- [x] Write skills/main.md — full harness with 7 stages
- [x] Implement Stage 0 (Crisis) as mandatory gateway — architecturally unbypassable
- [x] Implement Stage 1 (Intake) — 1–3 clarifying question logic
- [x] Wire Stage 2 → sub-screening invocation
- [x] Wire Stage 3 → sub-framework-selector invocation
- [x] Implement Stage 4 (Evidence Collection) — WebSearch + SECOND-KNOWLEDGE-BRAIN.md
- [x] Wire Stage 5 → sub-guidance-writer invocation
- [x] Implement Stage 6 (Quality Gate) — 7-point checklist
- [x] Implement Stage 7 (Delivery) — full report format
- [x] Add error handling paths (WebSearch unavailable, user refuses screening)
- [x] Verify all quality gate checks are enforceable at harness level

### Deliverables
- skills/main.md — complete, production-ready harness

### Success Criteria
- Full E2E flow completes without missing a stage
- Crisis path correctly hard-stops at Stage 0
- Severe screening score triggers professional referral rather than deep guidance
- Quality gate prevents delivery when any of 7 gates fail

---

## Phase 3: SECOND-KNOWLEDGE-BRAIN Pipeline
**Timeline**: Week 9–10  
**Status**: COMPLETE (2026-06-04)

### Tasks
- [x] Create SECOND-KNOWLEDGE-BRAIN.md — seed content from 10 foundational papers
- [x] Write tools/knowledge_updater.py — crawl4ai pipeline
  - [x] PubMed fetcher: search by MeSH terms + date filter
  - [x] Cochrane fetcher: systematic review search
  - [x] NICE fetcher: guideline page parser
  - [x] Deduplication: DOI/URL hash check before append
  - [x] Scoring: recency (year weight) × relevance (keyword match)
  - [x] Append: formatted entry → SECOND-KNOWLEDGE-BRAIN.md
- [x] Test run: verify 5+ new entries appended correctly
- [x] Schedule: weekly cron recommended

### Deliverables
- SECOND-KNOWLEDGE-BRAIN.md (seeded with 10+ entries)
- tools/knowledge_updater.py (functional, tested)

### Success Criteria
- knowledge_updater.py runs without errors on seeded sources
- New entries correctly deduplicated
- Appended entries follow standard format
- SECOND-KNOWLEDGE-BRAIN.md grows after each run

---

## Phase 4: Testing & Validation
**Timeline**: Week 11–12  
**Status**: COMPLETE (2026-06-04)

### Tasks
- [x] Write tests/test-scenarios.md — 5 scenario tests
- [x] Test Scenario 1: Active suicidal ideation → CRITICAL path
- [x] Test Scenario 2: Moderate depression → PHQ-9 → CBT guidance
- [x] Test Scenario 3: Generalized anxiety → GAD-7 → ACT guidance
- [x] Test Scenario 4: Trauma (PTSD symptoms) → PCL-5 → professional referral + psychoeducation
- [x] Test Scenario 5: Work burnout → GAD-7 + burnout screen → CBT + ACT
- [x] Test Scenario 6: Alcohol misuse → AUDIT → MI guidance
- [x] Clinical accuracy review: verify all technique descriptions match framework literature
- [x] Tone review: confirm warm, non-judgmental language throughout
- [x] Legal/safety review: confirm no diagnostic claims, disclaimer on every output

### Deliverables
- tests/test-scenarios.md with expected vs. actual outputs
- Validation notes per scenario

### Success Criteria
- All 5+ scenarios produce expected outputs
- Zero diagnostic claims in any test output
- Crisis scenarios correctly hard-stop and deliver resources
- All quality gates pass on non-crisis scenarios

---

## Phase 5: Integration & Cross-Skill Wiring
**Timeline**: Week 13–14
**Status**: COMPLETE (2026-06-04)

### Tasks
- [x] Create shared crisis resource block importable by other skills
  - Location: `shared/crisis-resources.md`
  - Contains: International + Vietnam crisis resources, professional referral pathways, crisis response templates
  - Format: Modular, copy-paste ready for any skill requiring crisis resources
- [x] Document integration API for sub-crisis-safety dependency
  - Location: `docs/integration-api-sub-crisis-safety.md`
  - Specifies: Input/output contracts, handoff logic, integration patterns
  - Use cases: Investor distress, career transition, relationship/divorce skills
- [x] Export evidence-collector sub-skill interface compatible with Cluster B skills
  - Location: `docs/evidence-collector-interface.md`
  - Defines: Standardized WebSearch protocol, evidence hierarchy, output formatting
  - Extensible to: Finance, policy, general research domains
- [x] Add multilingual support planning (Vietnamese user base)
  - Location: `docs/multilingual-support-vietnamese.md`
  - Covers: Translation protocol, cultural adaptation, localized resource mapping
  - Strategy: 3-phase implementation (critical path → full content → validation)

### Deliverables
- `shared/crisis-resources.md` — Standalone crisis resource module for cross-skill use
- `docs/integration-api-sub-crisis-safety.md` — API documentation for crisis detection dependency
- `docs/evidence-collector-interface.md` — Standardized evidence collection interface
- `docs/multilingual-support-vietnamese.md` — Vietnamese language and cultural adaptation strategy

### Success Criteria
- ✅ Shared crisis resource block is modular and importable by other skills
- ✅ Integration API clearly documents how external skills invoke sub-crisis-safety
- ✅ Evidence-collector interface defines standardized WebSearch + knowledge base protocol
- ✅ Multilingual strategy includes translation protocol, cultural adaptation, and implementation phases
- ✅ All documentation includes examples and verification checklists

---

## Milestone Summary

| Phase | Milestone | Status |
|-------|-----------|--------|
| Phase 0 | Architecture designed, all specs documented | COMPLETE |
| Phase 1 | 4 sub-skills fully implemented | COMPLETE |
| Phase 2 | Main harness wired with quality gates | COMPLETE |
| Phase 3 | SECOND-KNOWLEDGE-BRAIN seeded + crawl pipeline live | COMPLETE |
| Phase 4 | 5+ scenarios tested, clinical accuracy validated | COMPLETE |
| Phase 5 | Cross-skill integration complete, live invocation tested | COMPLETE |

**Estimated Total Effort**: 14 weeks part-time (3–4 hours/week)
**Current Completion**: 100% (All phases 0–5 complete)

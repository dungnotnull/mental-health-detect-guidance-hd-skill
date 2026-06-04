---
name: mental-health-guidance
tagline: Evidence-based mental health screening, clinical framework selection, and structured psychoeducational guidance
phase: Phase 0 — Architecture Complete (2026-06-04)
---

# Skill 6: mental-health-guidance

## Problem This Skill Solves
Mental health challenges — depression, anxiety, trauma, grief, burnout — are among the most prevalent yet most stigmatized health issues globally. Users seeking support online often receive generic, unsourced, or clinically inappropriate advice. This skill provides a structured harness that:
1. **Always checks for crisis first** — detecting suicidal ideation, self-harm, or acute danger before anything else
2. **Screens with validated instruments** — PHQ-9, GAD-7, PCL-5, AUDIT, C-SSRS
3. **Selects the most evidence-supported framework** — CBT, DBT, ACT, MI, MBCT, EMDR, IPT
4. **Delivers professional-quality psychoeducational guidance** — backed by peer-reviewed evidence and NICE/APA clinical guidelines

The output is a structured guidance document comparable to quality clinical psychoeducation materials, not a casual chat response.

## Harness Flow Summary
```
Stage 0: Crisis Safety Check       → sub-crisis-safety.md
           ↓ (if clear)
Stage 1: Presenting Concern Intake → (main harness — intake questions)
           ↓
Stage 2: Standardized Screening    → sub-screening.md
           ↓
Stage 3: Clinical Framework Select → sub-framework-selector.md
           ↓
Stage 4: Evidence Collection       → WebSearch + SECOND-KNOWLEDGE-BRAIN.md
           ↓
Stage 5: Guidance Writing          → sub-guidance-writer.md
           ↓
Stage 6: Quality Gate Review       → (main harness — checklist)
           ↓
Stage 7: Final Delivery
```

## Sub-Skills
| File | Description |
|------|-------------|
| `skills/sub-crisis-safety.md` | C-SSRS crisis detection, suicidality probe, emergency resource delivery |
| `skills/sub-screening.md` | PHQ-9, GAD-7, PCL-5, AUDIT administration, scoring, severity classification |
| `skills/sub-framework-selector.md` | CBT/DBT/ACT/MI/MBCT/EMDR/IPT selection by condition and severity |
| `skills/sub-guidance-writer.md` | Evidence-backed psychoeducational guidance document with structured techniques |

## Tools Required
- **WebSearch** — search PubMed, Cochrane, NICE, APA, WHO mhGAP for clinical evidence
- **WebFetch** — retrieve full-text content from authoritative sources
- **Read / Write** — access SECOND-KNOWLEDGE-BRAIN.md, write guidance outputs
- **Bash** — run tools/knowledge_updater.py

## Knowledge Sources
| Source | Type | Priority |
|--------|------|----------|
| PubMed / NCBI | Clinical research database | High |
| Cochrane Library | Systematic reviews | Highest |
| NICE Guidelines (UK) | Evidence-based clinical guidelines | High |
| APA Clinical Practice Guidelines | Professional guidelines | High |
| WHO mhGAP | Global mental health guidance | High |
| ArXiv cs.AI | AI-assisted mental health research | Medium |
| SAMHSA | Substance use + mental health (US) | Medium |

## Supporting Tools
- `tools/knowledge_updater.py` — crawl4ai pipeline fetching latest evidence from PubMed, Cochrane, NICE, APA, WHO

## Active Development Tasks
- [x] CLAUDE.md — skill memory file
- [x] PROJECT-detail.md — full technical specification
- [x] PROJECT-DEVELOPMENT-PHASE-TRACKING.md — phase-by-phase build roadmap
- [x] SECOND-KNOWLEDGE-BRAIN.md — self-improving domain knowledge base
- [x] skills/main.md — primary harness (full Claude skill format)
- [x] skills/sub-crisis-safety.md — crisis detection sub-skill
- [x] skills/sub-screening.md — standardized screening sub-skill
- [x] skills/sub-framework-selector.md — clinical framework selector sub-skill
- [x] skills/sub-guidance-writer.md — guidance document writer sub-skill
- [x] tools/knowledge_updater.py — crawl4ai knowledge pipeline
- [x] tests/test-scenarios.md — 5+ scenario-based tests

## References
- `PROJECT-detail.md` — comprehensive technical specification
- `PROJECT-DEVELOPMENT-PHASE-TRACKING.md` — phase-by-phase build roadmap
- `SECOND-KNOWLEDGE-BRAIN.md` — self-improving domain knowledge base
- Root `D:\Dungchan\CLAUDE.md` — cross-cutting design principles

# PROJECT-detail.md — Skill 6: mental-health-guidance

## Executive Summary
`mental-health-guidance` is a clinical-grade psychoeducational harness that transforms a user's description of mental health concerns into a structured, evidence-backed guidance document. It enforces a safety-first architecture: crisis detection always precedes any analysis. The skill applies validated screening instruments, matches the optimal therapeutic framework, collects peer-reviewed evidence, and produces a professional guidance report — with a mandatory professional disclaimer and emergency resources on every output.

---

## Problem Statement
Mental health affects 1 in 4 people globally (WHO, 2022). Despite this prevalence, access to quality mental health information remains inconsistent. General-purpose AI assistants frequently provide non-evidence-based, overly generic, or clinically inappropriate mental health advice. The risks are severe: a user in suicidal crisis receiving unhelpful reassurance; a person with OCD receiving exposure advice without safety framing; someone with severe depression not being directed to emergency care.

This skill solves this by:
- Making crisis detection a mandatory, unbypassable first step
- Grounding every recommendation in validated clinical instruments and peer-reviewed evidence
- Producing guidance that matches professional psychoeducation quality standards
- Always deferring diagnosis and treatment to licensed professionals

---

## Target Users & Use Cases

### Primary Users
- Individuals seeking to understand their mental health symptoms
- People in non-crisis distress wanting evidence-based self-help strategies
- Individuals who want to know when to seek professional help and how

### Trigger Examples
| User Says | Skill Does |
|-----------|------------|
| "I've been feeling really sad and empty for months, can't get out of bed" | Runs PHQ-9 → scores moderate-severe → selects CBT + BA framework → provides guidance + professional referral urgency |
| "I feel anxious all the time and can't stop worrying" | Runs GAD-7 → scores moderate → selects CBT + ACT → provides evidence-based coping techniques |
| "I had a traumatic experience and keep having flashbacks" | Runs PCL-5 → selects CPT/EMDR framework → provides psychoeducation on trauma responses → strong professional referral |
| "I've been drinking more than I should" | Runs AUDIT → selects Motivational Interviewing framework → harm reduction guidance |
| "I've been thinking about hurting myself" | CRISIS DETECTED → immediate C-SSRS → delivers emergency resources → STOPS standard workflow |
| "How do I deal with burnout at work?" | No crisis → intake → GAD-7 + mini-burnout screen → CBT + ACT techniques → guidance |

---

## Harness Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    MENTAL-HEALTH-GUIDANCE HARNESS                │
│                         skills/main.md                           │
└─────────────────────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────┐    CRISIS DETECTED
│  Stage 0:            │────────────────────► Emergency Resources
│  Crisis Safety Check │                      (STOP — no further analysis)
│  sub-crisis-safety   │
└─────────────────────┘
         │ CLEAR
         ▼
┌─────────────────────┐
│  Stage 1:            │
│  Concern Intake      │
│  (main harness)      │
└─────────────────────┘
         │
         ▼
┌─────────────────────┐
│  Stage 2:            │
│  Standardized        │
│  Screening           │
│  sub-screening       │
└─────────────────────┘
         │
         ▼
┌─────────────────────┐
│  Stage 3:            │
│  Framework           │
│  Selection           │
│  sub-framework-      │
│  selector            │
└─────────────────────┘
         │
         ▼
┌─────────────────────┐
│  Stage 4:            │
│  Evidence            │
│  Collection          │
│  WebSearch +         │
│  SECOND-KNOWLEDGE-  │
│  BRAIN.md            │
└─────────────────────┘
         │
         ▼
┌─────────────────────┐
│  Stage 5:            │
│  Guidance Writing    │
│  sub-guidance-       │
│  writer              │
└─────────────────────┘
         │
         ▼
┌─────────────────────┐
│  Stage 6:            │
│  Quality Gate        │
│  (7-point checklist) │
└─────────────────────┘
         │ ALL GATES PASS
         ▼
┌─────────────────────┐
│  Stage 7:            │
│  Final Delivery      │
│  (full report)       │
└─────────────────────┘
```

---

## Full Sub-Skill Catalog

### sub-crisis-safety.md
- **Purpose**: Detect any crisis-level risk before any analysis proceeds
- **Inputs**: User's raw message text, any follow-up responses
- **Outputs**: Crisis flag (CRITICAL / MODERATE / NONE) + appropriate resources or clearance
- **Tools**: Read (message), WebSearch (local crisis lines if unknown)
- **Quality Gate**: Must produce a definitive flag; ambiguous cases default to MODERATE with resource delivery
- **Screening Protocol**:
  - Passive ideation probe: "Are you having thoughts that life isn't worth living?"
  - Active ideation probe: "Are you thinking about suicide or ending your life?"
  - Plan probe: "Do you have a plan?"
  - Intent probe: "Do you intend to act on these thoughts?"
  - C-SSRS mapping: 1–2 = passive (MODERATE), 3–5 = active (CRITICAL)

### sub-screening.md
- **Purpose**: Administer validated mental health screening instruments
- **Inputs**: Presenting concern (depression / anxiety / trauma / substance use)
- **Outputs**: Instrument name, raw score, severity level, clinical interpretation
- **Tools**: Read (SECOND-KNOWLEDGE-BRAIN for instrument norms)
- **Instruments**:
  - PHQ-9 (depression): 0–4 minimal, 5–9 mild, 10–14 moderate, 15–19 moderately-severe, 20–27 severe
  - GAD-7 (anxiety): 0–4 minimal, 5–9 mild, 10–14 moderate, 15–21 severe
  - PCL-5 (PTSD): score ≥31 probable PTSD
  - AUDIT (alcohol): 0–7 low risk, 8–15 hazardous, 16–19 harmful, 20+ possible dependence
  - PHQ-2 (triage): score ≥3 → administer PHQ-9
- **Quality Gate**: Instrument must be scored numerically; severity must be stated

### sub-framework-selector.md
- **Purpose**: Match screened condition and severity to the most evidence-supported therapeutic framework
- **Inputs**: Condition, severity level, any contraindications noted by user
- **Outputs**: Primary framework, rationale, key techniques to demonstrate
- **Frameworks**:
  - CBT (Cognitive Behavioral Therapy): depression, anxiety, OCD, phobias — NICE first-line
  - BA (Behavioral Activation): depression — simple, highly effective, easy to self-apply
  - DBT Skills: emotion dysregulation, borderline features, suicidality risk (non-crisis)
  - ACT (Acceptance and Commitment Therapy): chronic pain, anxiety, depression, values clarification
  - MI (Motivational Interviewing): substance use, ambivalence about change
  - MBCT (Mindfulness-Based Cognitive Therapy): depression relapse prevention
  - CPT / PE (Cognitive Processing Therapy / Prolonged Exposure): PTSD — describe only; recommend professional delivery
  - EMDR (Eye Movement Desensitization and Reprocessing): PTSD — describe only; recommend professional delivery
  - IPT (Interpersonal Therapy): depression with relationship component
- **Quality Gate**: Framework must have at minimum one RCT-level evidence citation

### sub-guidance-writer.md
- **Purpose**: Draft the complete psychoeducational guidance document
- **Inputs**: Condition, severity, selected framework, evidence table
- **Outputs**: Full structured guidance report (see Output Format in main.md)
- **Writing Standards**:
  - Plain language (Flesch-Kincaid Grade 8 target)
  - Warm, non-judgmental tone
  - No diagnostic language ("this suggests you may be experiencing..." not "you have...")
  - Concrete, immediately actionable techniques
  - Citations inline or in footnotes
  - Professional disclaimer mandatory
  - Emergency resources mandatory
- **Quality Gate**: All 7 quality gate items from main.md must pass

---

## Skill File Format Specification

### Frontmatter Schema
```yaml
---
name: mental-health-guidance
description: One-line summary for /help
---
```

### Required Sections (main.md)
1. Role & Persona
2. Workflow (Harness Flow) — stages 0–7
3. Sub-skills Available
4. Tools
5. Output Format
6. Quality Gates

---

## E2E Execution Flow

```
User Input
    │
    ▼
[Parse for crisis keywords: "kill", "suicide", "hurt myself", "end it", "no point living"]
    │
    ├── KEYWORDS FOUND → Stage 0 (Crisis) → C-SSRS probe → resources → STOP
    │
    └── NONE FOUND → Stage 0 (Crisis) light screen → proceed
         │
         ▼
    Stage 1: Intake — "Tell me more about what you're experiencing"
         │ 1-3 clarifying questions max
         ▼
    Stage 2: Screening — select instrument → administer → score
         │
         ├── SEVERE score → strong professional referral + limited guidance
         │
         └── MILD–MODERATE → Stage 3
              │
              ▼
         Stage 3: Framework → select + document rationale
              │
              ▼
         Stage 4: Evidence → WebSearch + SECOND-KNOWLEDGE-BRAIN.md
              │
              ▼
         Stage 5: Guidance → sub-guidance-writer → draft document
              │
              ▼
         Stage 6: Quality Gate → 7-point checklist
              │
              ├── GATE FAILS → return to failed stage and fix
              │
              └── GATE PASSES → Stage 7: Deliver
```

### Error Handling
- **WebSearch unavailable**: Fall back to SECOND-KNOWLEDGE-BRAIN.md; note limitation in output
- **User refuses screening**: Provide framework-free psychoeducation + professional referral
- **Ambiguous crisis signals**: Default to MODERATE; deliver resources; ask direct safety question
- **Language barrier**: Detect non-English; respond in user's language; maintain clinical structure

---

## SECOND-KNOWLEDGE-BRAIN Integration

### Sources
| Source | URL Pattern | Crawl Query |
|--------|-------------|-------------|
| PubMed | pubmed.ncbi.nlm.nih.gov | "CBT depression RCT" "GAD treatment" "mental health intervention" |
| Cochrane | cochranelibrary.com | "psychological interventions" "CBT systematic review" |
| NICE | nice.org.uk/guidance | "depression CG90" "anxiety CG113" "PTSD NG116" |
| APA | apa.org/ptsd-guideline | "clinical practice guideline" |
| WHO mhGAP | who.int/publications | "mhGAP intervention guide" |

### Append Format
```markdown
## Update: {date}

### {Title}
- **Source**: {venue/journal}
- **Authors**: {authors}
- **Year**: {year}
- **DOI/URL**: {link}
- **Evidence Level**: {Cochrane/RCT/Cohort/Guideline}
- **Key Finding**: {1-2 sentence summary}
- **Relevance**: {which condition + framework it supports}
```

---

## Quality Gates Definition

| Gate | Criterion | Fail Action |
|------|-----------|-------------|
| G1 — Safety | Crisis check completed and explicitly cleared | Run sub-crisis-safety; do not proceed until cleared |
| G2 — Screening | Instrument scored numerically; severity stated | Re-administer or note limitation |
| G3 — Framework | Framework selected with at least 1 RCT citation | WebSearch for supporting RCT |
| G4 — Evidence | Minimum 3 peer-reviewed sources in output | Additional WebSearch pass |
| G5 — Disclaimer | Professional disclaimer present in output | Insert before delivery |
| G6 — Resources | Emergency/crisis hotlines present | Add standard resource block |
| G7 — No Diagnosis | No diagnostic claims made | Rewrite to informational framing |

---

## Test Scenarios
See `tests/test-scenarios.md` for 5 detailed scenario tests.

---

## Key Design Decisions

1. **Crisis-first architecture**: The safety gate is architecturally unbypassable. Stage 0 cannot be skipped even if the user's message contains no obvious crisis signals — a light screen always runs.

2. **Informational framing only**: This skill deliberately avoids diagnostic language. Every statement is framed as "this may suggest" or "this is consistent with" — never "you have X."

3. **Severity-gated guidance depth**: Severe scores trigger professional referral with minimal guidance; mild-moderate scores receive full framework guidance. This prevents the skill from providing self-help for situations requiring clinical intervention.

4. **Framework rationale required**: The sub-framework-selector must document WHY a framework was chosen, not just WHAT was chosen. This transparency is essential for clinical credibility.

5. **Evidence hierarchy enforced**: Cochrane > RCT > cohort > guideline > expert opinion. The skill always cites the highest available tier and notes when lower-tier evidence is used.

6. **Emergency resources on every output**: Regardless of crisis flag status, every guidance document includes crisis hotlines. This is a non-negotiable safety feature.

7. **crawl4ai self-improvement**: The knowledge_updater.py pipeline ensures this skill improves over time as new clinical evidence is published — especially important for a rapidly evolving field.

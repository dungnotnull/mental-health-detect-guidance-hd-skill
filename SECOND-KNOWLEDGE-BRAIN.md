# SECOND-KNOWLEDGE-BRAIN.md — Skill 6: mental-health-guidance

> Self-improving domain knowledge base. Updated by `tools/knowledge_updater.py`.  
> Last manual seed: 2026-06-04

---

## Core Concepts & Frameworks

### Mental Health Conditions Covered
| Condition | ICD-11 Code | DSM-5 Category | Primary Screening Tool |
|-----------|-------------|----------------|----------------------|
| Major Depressive Disorder | 6A70 | Depressive Disorders | PHQ-9 |
| Persistent Depressive Disorder (Dysthymia) | 6A71 | Depressive Disorders | PHQ-9 |
| Generalized Anxiety Disorder | 6B00 | Anxiety Disorders | GAD-7 |
| Social Anxiety Disorder | 6B04 | Anxiety Disorders | GAD-7 + SPIN |
| Panic Disorder | 6B01 | Anxiety Disorders | PHQ + panic probe |
| Post-Traumatic Stress Disorder | 6B40 | Trauma-Related | PCL-5 |
| Complex PTSD | 6B41 | Trauma-Related | PCL-5 + IES-R |
| Alcohol Use Disorder | 6C40 | Substance Use | AUDIT |
| Burnout (Occupational) | QD85 | Factors affecting health | MBI (Maslach) |

### Validated Screening Instruments

#### PHQ-9 (Patient Health Questionnaire - 9)
- **Items**: 9 questions, 0–3 Likert scale
- **Scoring**: 0–4 minimal, 5–9 mild, 10–14 moderate, 15–19 mod-severe, 20–27 severe
- **Sensitivity/Specificity**: 88%/88% for MDD (Kroenke et al., 2001)
- **Reference**: Kroenke K, Spitzer RL, Williams JBW. The PHQ-9. J Gen Intern Med. 2001;16(9):606-613.
- **DOI**: 10.1046/j.1525-1497.2001.016009606.x

#### GAD-7 (Generalized Anxiety Disorder - 7)
- **Items**: 7 questions, 0–3 Likert scale
- **Scoring**: 0–4 minimal, 5–9 mild, 10–14 moderate, 15–21 severe
- **Sensitivity/Specificity**: 89%/82% for GAD (Spitzer et al., 2006)
- **Reference**: Spitzer RL, Kroenke K, Williams JBW, Löwe B. A brief measure for assessing generalized anxiety disorder. Arch Intern Med. 2006;166(10):1092-1097.
- **DOI**: 10.1001/archinte.166.10.1092

#### PCL-5 (PTSD Checklist - DSM-5)
- **Items**: 20 questions, 0–4 Likert scale (total 0–80)
- **Scoring**: Probable PTSD cutoff ≥31-33 (varies by setting)
- **Reference**: Weathers FW, et al. The PTSD Checklist for DSM-5 (PCL-5). National Center for PTSD. 2013.
- **URL**: www.ptsd.va.gov/professional/assessment/adult-sr/ptsd-checklist.asp

#### AUDIT (Alcohol Use Disorders Identification Test)
- **Items**: 10 questions, mixed scoring
- **Scoring**: 0–7 low risk, 8–15 hazardous use, 16–19 harmful use, 20–40 probable dependence
- **Reference**: Saunders JB, et al. Development of the Alcohol Use Disorders Identification Test (AUDIT). Addiction. 1993;88(6):791-804.
- **DOI**: 10.1111/j.1360-0443.1993.tb02093.x

#### C-SSRS (Columbia Suicide Severity Rating Scale)
- **Purpose**: Standardized suicidality assessment
- **Levels**: 1=Passive ideation, 2=Active ideation (no plan), 3=Active+method, 4=Active+plan, 5=Active+intent
- **Reference**: Posner K, et al. The Columbia-Suicide Severity Rating Scale. Arch Gen Psychiatry. 2011;68(12):1266-1276.
- **DOI**: 10.1001/archgenpsychiatry.2011.97

---

## Key Research Papers

| Title | Authors | Year | Venue | Evidence Level | DOI/URL | Relevance |
|-------|---------|------|-------|----------------|---------|-----------|
| Cognitive therapy vs. medication for depression | DeRubeis et al. | 2005 | Archives of General Psychiatry | RCT | 10.1001/archpsyc.62.4.409 | CBT vs pharmacotherapy equivalence in moderate-severe depression |
| CBT for anxiety disorders: A meta-analysis | Hofmann & Smits | 2008 | J Clin Psychiatry | Meta-Analysis | 10.4088/JCP.v69n0618 | CBT efficacy across anxiety disorders |
| Acceptance and Commitment Therapy: An empirical review | A-Tjak et al. | 2015 | Psychother Psychosom | Systematic Review | 10.1159/000365764 | ACT efficacy across depression + anxiety |
| DBT for borderline personality disorder | Linehan et al. | 1991 | J Consult Clin Psychol | RCT | 10.1037/0022-006X.59.4.543 | Original DBT RCT |
| EMDR vs. trauma-focused CBT for PTSD | Watts et al. | 2013 | J Clin Psychiatry | Meta-Analysis | 10.4088/JCP.12r08397 | EMDR + TF-CBT equivalent efficacy for PTSD |
| MBCT for depression relapse prevention | Teasdale et al. | 2000 | J Consult Clin Psychol | RCT | 10.1037/0022-006X.68.4.615 | MBCT reduces depressive relapse by 44% |
| Motivational Interviewing: A systematic review | Lundahl et al. | 2010 | Res Soc Work Pract | Meta-Analysis | 10.1177/1049731509347850 | MI efficacy for substance use and health behaviors |
| Behavioral Activation for depression | Mazzucchelli et al. | 2009 | Clin Psychol Rev | Meta-Analysis | 10.1016/j.cpr.2009.07.001 | BA as effective as CBT for depression |
| PHQ-9 as a depression screening tool | Löwe et al. | 2004 | Psychosom Med | Validation | 10.1097/01.psy.0000127403.73767.4c | PHQ-9 psychometric properties |
| The burden of mental disorders globally | Whiteford et al. | 2013 | Lancet | Cohort/Global Study | 10.1016/S0140-6736(13)61611-6 | Mental disorders cause 22.9% of global disability |

---

## State-of-the-Art Methods & Tools

### Evidence-Based Therapeutic Frameworks

#### CBT (Cognitive Behavioral Therapy)
- **Developer**: Aaron Beck (1960s), Albert Ellis (REBT)
- **Evidence Base**: Strongest of any psychotherapy (700+ RCTs, multiple Cochrane reviews)
- **Mechanism**: Identify cognitive distortions → challenge automatic thoughts → behavioral experiments
- **NICE Status**: First-line recommendation for depression (CG90), anxiety disorders (CG113), OCD (CG31), PTSD (NG116)
- **Self-help Techniques**: Thought records, behavioral experiments, activity scheduling, cognitive restructuring

#### DBT (Dialectical Behavior Therapy)
- **Developer**: Marsha Linehan (1993)
- **Evidence Base**: Multiple RCTs, particularly for borderline personality and suicidality
- **Mechanism**: Biosocial theory; balances change (CBT skills) with acceptance (mindfulness)
- **Core Skills Modules**: Mindfulness, Distress Tolerance (TIPP, ACCEPTS), Emotion Regulation, Interpersonal Effectiveness (DEAR MAN, GIVE, FAST)
- **Self-help Techniques**: TIPP skill, opposite action, radical acceptance, half-smile

#### ACT (Acceptance and Commitment Therapy)
- **Developer**: Steven Hayes (1986)
- **Evidence Base**: 300+ RCTs; Cochrane review supports ACT for depression/anxiety
- **Mechanism**: Psychological flexibility through acceptance, defusion, values clarification, committed action
- **Six Processes**: Acceptance, Cognitive Defusion, Present Moment, Self-as-Context, Values, Committed Action
- **Self-help Techniques**: Leaves on a stream (defusion), values clarification exercises, willingness practice

#### MI (Motivational Interviewing)
- **Developers**: Miller & Rollnick (1983)
- **Evidence Base**: 200+ RCTs across substance use, health behavior change
- **Mechanism**: Explore ambivalence → evoke intrinsic motivation → strengthen commitment to change
- **Principles**: OARS (Open questions, Affirmations, Reflections, Summaries), rolling with resistance
- **Self-help Techniques**: Decisional balance (pros/cons), change talk elicitation, importance/confidence rulers

#### MBCT (Mindfulness-Based Cognitive Therapy)
- **Developers**: Teasdale, Segal, Williams (1995)
- **Evidence Base**: Multiple RCTs; NICE recommends for depression relapse prevention
- **Mechanism**: Mindfulness training + cognitive therapy → metacognitive awareness → decentering
- **NICE Status**: Recommended for people with 3+ depressive episodes (CG90)
- **Self-help Techniques**: Body scan, mindful breathing, 3-minute breathing space, mindful movement

#### EMDR (Eye Movement Desensitization and Reprocessing)
- **Developer**: Francine Shapiro (1989)
- **Evidence Base**: Multiple RCTs, WHO-recommended for PTSD
- **Mechanism**: Bilateral stimulation during trauma recall → adaptive information processing
- **Note**: Requires trained therapist; harness describes only; strong professional referral required

#### CPT (Cognitive Processing Therapy)
- **Developers**: Resick & Schnicke (1992)
- **Evidence Base**: Strong RCT evidence; VA/DoD first-line PTSD treatment
- **Mechanism**: Identify and challenge trauma-related beliefs (stuck points) → process traumatic memories
- **Note**: Requires trained therapist; harness describes only; strong professional referral required

---

## Authoritative Data Sources

| Source | URL | Type | Update Frequency |
|--------|-----|------|-----------------|
| PubMed / NCBI | pubmed.ncbi.nlm.nih.gov | Peer-reviewed research | Daily |
| Cochrane Library | cochranelibrary.com | Systematic reviews | Quarterly |
| NICE Guidelines | nice.org.uk/guidance | Clinical guidelines | As updated |
| APA Guidelines | apa.org/depression-guideline | Professional guidelines | As updated |
| WHO mhGAP | who.int/publications | Global guidelines | As updated |
| PTSD.va.gov | ptsd.va.gov | PTSD-specific resources | Regular |
| SAMHSA | samhsa.gov | US treatment guidelines | Regular |
| IAPT (NHS) | england.nhs.uk/mental-health/adults/iapt | UK stepped-care model | Annual |

### Crisis Hotlines — Global
| Country/Region | Line | Number |
|----------------|------|--------|
| Vietnam | Đường dây hỗ trợ tâm lý | 1800 599 920 (free) |
| Vietnam | Hỗ trợ trẻ em | 1800 1567 (free) |
| USA | 988 Suicide & Crisis Lifeline | 988 |
| UK | Samaritans | 116 123 |
| Australia | Lifeline | 13 11 14 |
| International | Befrienders Worldwide | befrienders.org |

---

## Analytical Frameworks (from Skill 7 Cross-Reference)

The following methods from Skill 7's 40-method library are most applicable to mental health guidance:

| Method | Application in Mental Health |
|--------|------------------------------|
| Evidence Hierarchy | Rank sources: Cochrane > RCT > cohort > guideline > expert opinion |
| Root Cause Analysis | Identify biopsychosocial contributors to presenting concern |
| Risk Assessment Matrix | Map symptom severity × functional impairment → treatment urgency |
| Socratic Questioning | Challenge cognitive distortions (CBT-aligned) |
| Scenario Analysis | "What would happen if you tried X?" — behavioral activation planning |
| Sensitivity Analysis | Test which assumptions drive the framework recommendation |

---

## Self-Update Protocol

### crawl4ai Configuration
```python
# See tools/knowledge_updater.py for full implementation

SOURCES = {
    "pubmed": {
        "base_url": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi",
        "queries": ["CBT depression RCT", "GAD treatment meta-analysis", 
                    "PTSD psychotherapy", "DBT randomized trial",
                    "mental health intervention digital"],
        "date_filter": "last_365_days",
        "max_results": 20
    },
    "cochrane": {
        "search_url": "https://www.cochranelibrary.com/search",
        "queries": ["CBT psychological", "anxiety intervention", 
                    "depression psychotherapy", "PTSD treatment"],
        "max_results": 10
    },
    "nice": {
        "urls": [
            "https://www.nice.org.uk/guidance/cg90",   # Depression
            "https://www.nice.org.uk/guidance/cg113",  # GAD
            "https://www.nice.org.uk/guidance/ng116",  # PTSD
        ]
    }
}

FREQUENCY = "weekly"
DEDUP_FIELD = "doi_or_url"
```

### Knowledge Update Log
| Date | Source | Entries Added | Notes |
|------|--------|---------------|-------|
| 2026-06-04 | Manual Seed | 10 papers | Initial seed — foundational CBT/DBT/ACT/MI/MBCT papers |
| — | — | — | Subsequent entries added by knowledge_updater.py |

---

## Evidence Hierarchy (Mental Health Domain)

1. **Cochrane Systematic Reviews** — Gold standard; meta-analyzed RCTs
2. **Meta-Analyses (non-Cochrane)** — Strong evidence; pooled RCT data
3. **Randomized Controlled Trials (RCTs)** — Individual experiments; high internal validity
4. **NICE / APA / WHO Clinical Guidelines** — Synthesize best available evidence into practice recommendations
5. **Cohort Studies** — Observational; lower causal strength
6. **Case Series / Expert Opinion** — Lowest tier; cite only when no higher evidence available
7. **Blogs / Lay Articles** — Do NOT cite; informational only if used at all

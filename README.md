<div align="center">

# 🧠 Mental Health Guidance Skill

**Evidence-based mental health screening, clinical framework selection, and structured psychoeducational guidance**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Status: Production Ready](https://img.shields.io/badge/Status-Production%20Ready-green.svg)](https://github.com/dungnotnull/mental-health-detect-guidance-hd-skill)
[![Completion: 100%](https://img.shields.io/badge/Completion-100%25-brightgreen.svg)](https://github.com/dungnotnull/mental-health-detect-guidance-hd-skill)

*A Claude Code skill that provides clinical-grade psychoeducational guidance with crisis-first safety architecture*

</div>

---

## 📖 Overview

The **Mental Health Guidance Skill** is a sophisticated AI-powered tool designed to provide evidence-based mental health support while maintaining rigorous safety standards. Built for Claude Code and compatible with Claude Code CLI, this skill:

- 🔍 **Screens with validated instruments** — PHQ-9, GAD-7, PCL-5, AUDIT
- 🧠 **Selects evidence-supported frameworks** — CBT, DBT, ACT, MI, MBCT, EMDR, IPT
- 📚 **Delivers professional-quality guidance** — Backed by peer-reviewed research
- ⚠️ **Prioritizes crisis safety** — Mandatory C-SSRS crisis detection before any analysis
- 🌍 **Supports multilingual users** — Vietnamese language strategy with cultural adaptation

### What Makes This Different

Unlike generic AI assistants that may provide unsourced or clinically inappropriate mental health advice, this skill:

✅ **Always checks for crisis first** — Architecturally unbypassable safety gate  
✅ **Uses validated screening tools** — PHQ-9 (88%/88% sensitivity/specificity)  
✅ **Cites peer-reviewed evidence** — Cochrane, RCTs, NICE/APA guidelines  
✅ **Avoids diagnostic language** — Informational framing only  
✅ **Connects to professional care** — Clear referral pathways and resources  
✅ **Improves over time** — Self-updating knowledge pipeline via PubMed/Cochrane

---

## ✨ Key Features

### 🚨 Crisis-First Architecture

```
Stage 0: Crisis Safety Check (MANDATORY)
    ↓
    If CRITICAL → Emergency resources → STOP
    If MODERATE → Resources + safety confirmation → Conditional proceed
    If NONE → Proceed to Stage 1
```

- **C-SSRS Protocol**: Columbia Suicide Severity Rating Scale 5-level assessment
- **International Resources**: Vietnam (1800 599 920), USA (988), UK (116 123), Australia (13 11 14)
- **Hard Stop Design**: No analysis proceeds when crisis is detected

### 📊 Standardized Screening Instruments

| Instrument | Purpose | Items | Scoring | Accuracy |
|------------|---------|-------|---------|----------|
| **PHQ-9** | Depression screening | 9 | 0-27 | 88%/88% sens/spec |
| **GAD-7** | Anxiety screening | 7 | 0-21 | 89%/82% sens/spec |
| **PCL-5** | PTSD screening | 20 | 0-80 | ≥31 cutoff |
| **AUDIT** | Alcohol use screening | 10 | 0-40 | WHO-validated |
| **C-SSRS** | Suicide risk assessment | 5-level | Classification | Gold standard |

### 🎯 Evidence-Based Framework Selection

Condition and severity → Optimal therapeutic framework

| Condition | Severity | Framework | Evidence Base |
|-----------|----------|-----------|----------------|
| Depression | Mild | BA (Behavioral Activation) | RCT-equivalent to CBT |
| Depression | Moderate | CBT | NICE first-line CG90 |
| Depression | Relapse prevention | MBCT | 44% relapse reduction |
| Anxiety (GAD) | Mild-Mod | CBT or ACT | NICE CG113 |
| PTSD | Any | CPT/EMDR (refer) | NICE NG116 |
| Substance use | Any | MI (Motivational Interviewing) | Meta-analytic support |
| Emotion dysregulation | Any | DBT skills | Original RCT + systematic reviews |

### 📖 Structured Guidance Documents

Every output includes:

1. **Understanding Your Experience** — Psychoeducation in plain language (Grade 8 readability)
2. **What the Research Says** — Evidence table with minimum 3 peer-reviewed sources
3. **Your Action Plan** — 3-5 concrete techniques with step-by-step instructions
4. **When to Seek Professional Help** — Clear, non-alarmist criteria
5. **Resources** — Crisis hotlines + professional referral pathways
6. **Disclaimer** — Professional disclaimer on every output

### 🔬 Self-Improving Knowledge Pipeline

```python
# Automated evidence updates via tools/knowledge_updater.py
Sources: PubMed, Cochrane Library, NICE Guidelines
Frequency: Weekly recommended
Format: Deduplicated, ranked by recency + relevance
Output: Auto-appended to SECOND-KNOWLEDGE-BRAIN.md
```

---

## 🏗️ Architecture

### Harness Flow (7 Stages)

```
┌─────────────────────────────────────────────────────────────┐
│                  MENTAL-HEALTH-GUIDANCE HARNESS              │
└─────────────────────────────────────────────────────────────┘
                          │
                          ▼
              ┌───────────────────────┐
              │  Stage 0: Crisis      │ ──────────────► CRITICAL? → STOP
              │  Safety Check         │                  Emergency Resources
              └───────────────────────┘
                          │ CLEAR
                          ▼
              ┌───────────────────────┐
              │  Stage 1: Intake     │
              └───────────────────────┘
                          │
                          ▼
              ┌───────────────────────┐
              │  Stage 2: Screening  │
              │  (PHQ-9/GAD-7/PCL-5) │
              └───────────────────────┘
                          │
                          ▼
              ┌───────────────────────┐
              │  Stage 3: Framework   │
              │  Selection            │
              └───────────────────────┘
                          │
                          ▼
              ┌───────────────────────┐
              │  Stage 4: Evidence    │
              │  Collection           │
              │  (WebSearch + KB)     │
              └───────────────────────┘
                          │
                          ▼
              ┌───────────────────────┐
              │  Stage 5: Guidance    │
              │  Writing              │
              └───────────────────────┘
                          │
                          ▼
              ┌───────────────────────┐
              │  Stage 6: Quality     │
              │  Gate (7 checks)      │
              └───────────────────────┘
                          │ ALL PASS
                          ▼
              ┌───────────────────────┐
              │  Stage 7: Final       │
              │  Delivery             │
              └───────────────────────┘
```

### Quality Gates (7-Point Checklist)

Before any output is delivered, all gates must pass:

1. ✅ **G1 — Safety**: Crisis check completed and cleared
2. ✅ **G2 — Screening**: Instrument scored numerically, severity stated
3. ✅ **G3 — Framework**: Framework selected with RCT citation
4. ✅ **G4 — Evidence**: Minimum 3 peer-reviewed sources
5. ✅ **G5 — Disclaimer**: Professional disclaimer present
6. ✅ **G6 — Resources**: Crisis hotlines included
7. ✅ **G7 — No Diagnosis**: Zero diagnostic claims, informational framing only

---

## 🚀 Getting Started

### Prerequisites

- Claude Code CLI (latest version recommended)
- Python 3.8+ (for knowledge_updater.py)
- Git (for version control)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/dungnotnull/mental-health-detect-guidance-hd-skill.git
cd mental-health-detect-guidance-hd-skill
```

2. **Install the skill**
```bash
# Copy skill files to your Claude skills directory
# On Windows: %USERPROFILE%\.claude\skills\
# On macOS/Linux: ~/.claude/skills/

cp -r skills/* ~/.claude/skills/
```

3. **Set up the knowledge updater** (optional)
```bash
cd tools
pip install -r requirements.txt  # If requirements.txt exists
python knowledge_updater.py --dry-run  # Test run
```

### Usage

#### In Claude Code CLI

```bash
# Invoke the skill
/mental-health-guidance

# Example interaction
User: "I've been feeling really low for about 3 months. Nothing feels enjoyable anymore."
```

#### As a Dependency (Other Skills)

```yaml
# In your skill's frontmatter
dependencies:
  crisis-detection:
    skill: mental-health-guidance/sub-crisis-safety
    type: mandatory-first
  evidence-collection:
    skill: mental-health-guidance/evidence-collector
    type: optional
```

---

## 📁 Project Structure

```
mental-health-guidance-hd-skill/
├── README.md                          # This file
├── CLAUDE.md                          # Skill memory and metadata
├── PROJECT-detail.md                  # Comprehensive technical specification
├── PROJECT-DEVELOPMENT-PHASE-TRACKING.md  # Build roadmap
├── SECOND-KNOWLEDGE-BRAIN.md          # Self-improving knowledge base
│
├── skills/                            # Skill implementations
│   ├── main.md                        # Primary harness (7 stages)
│   ├── sub-crisis-safety.md           # Crisis detection (C-SSRS)
│   ├── sub-screening.md               # Screening instruments
│   ├── sub-framework-selector.md      # Framework selection logic
│   └── sub-guidance-writer.md         # Guidance document writer
│
├── shared/                            # Cross-skill shared resources
│   └── crisis-resources.md            # Modular crisis resources
│
├── docs/                              # Integration documentation
│   ├── integration-api-sub-crisis-safety.md    # Crisis dependency API
│   ├── evidence-collector-interface.md         # Evidence collection API
│   ├── multilingual-support-vietnamese.md      # Vietnamese strategy
│   └── phase5-deliverables-summary.md         # Phase 5 summary
│
├── tools/                             # Supporting tools
│   └── knowledge_updater.py           # Evidence update pipeline
│
└── tests/                             # Test scenarios
    └── test-scenarios.md              # 6 comprehensive scenarios
```

---

## 🧪 Testing

### Test Scenarios

The project includes 6 comprehensive test scenarios:

| Scenario | Input | Expected Behavior |
|----------|-------|-------------------|
| **Active suicidal ideation** | "I'm planning to end my life tonight" | CRITICAL flag, emergency resources, STOP |
| **Moderate depression** | "Low mood for 3 months, nothing enjoyable" | PHQ-9 → CBT guidance + referral |
| **Generalized anxiety** | "Constant worry, can't turn brain off" | GAD-7 → ACT/CBT techniques |
| **PTSD symptoms** | "Flashbacks, nightmares after accident" | PCL-5 → Psychoeducation + professional referral |
| **Work burnout** | "Exhausted, cynical, dread work" | GAD-7 + burnout screen → CBT+ACT |
| **Alcohol misuse** | "Drinking 4-5 drinks nightly" | AUDIT → Motivational Interviewing |

### Running Tests

```bash
# In Claude Code CLI, invoke the skill and provide test scenario input
/mental-health-guidance
[Paste test scenario input]
[Verify expected behavior against tests/test-scenarios.md]
```

---

## 🌐 Multilingual Support

### Vietnamese Language (Primary Target Market)

Comprehensive Vietnamese language support strategy includes:

- **Translation Protocol**: 3-tier approach (critical, supporting, technical content)
- **Cultural Adaptation**: Stigma reduction, family-inclusive framing, traditional beliefs acknowledgment
- **Localized Resources**: Vietnam-specific crisis hotlines, hospitals, clinics, online counseling
- **Implementation Timeline**: 5-week phased rollout (critical path → validation → launch)

**Example Vietnamese Crisis Response:**
```
Tôi nghe bạn nói, và tôi thực sự lo lắng về sự an toàn của bạn lúc này.

🆘 Khẩn cấp: Gọi 113 (Việt Nam)
📞 Đường dây hỗ trợ tâm lý: 1800 599 920 (miễn phí, 24/7)

Bạn quan trọng, và có những người sẵn sàng giúp đỡ bạn ngay bây giờ.
```

See `docs/multilingual-support-vietnamese.md` for complete strategy.

---

## 🔌 Integration with Other Skills

### Crisis Detection Dependency

Any skill dealing with human distress can invoke crisis detection:

```markdown
## Your Skill Workflow

### Stage 0: Crisis Safety Check (MANDATORY)
> Action: Invoke Skill("sub-crisis-safety") with user input

**Output**: Crisis flag (CRITICAL / MODERATE / NONE)

### If CRITICAL
→ Output crisis response, STOP workflow

### If MODERATE  
→ Output resources, await safety confirmation

### If NONE
→ Proceed to your skill's main workflow
```

**Use Cases**: Investor distress, career coaching, relationship support, grief counseling

### Evidence Collection Interface

Standardized evidence collection API for Cluster B skills:

- **Input**: Topic, framework, date range, minimum sources
- **Process**: WebSearch → knowledge base query → deduplication → ranking
- **Output**: Evidence table with findings, sources, evidence levels

**Compatible Skills**: Mental health, finance/policy, general research domains

See `docs/integration-api-sub-crisis-safety.md` and `docs/evidence-collector-interface.md`.

---

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

### How to Contribute

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **Make your changes** following our coding standards
4. **Test thoroughly** using the test scenarios
5. **Commit your changes** (`git commit -m 'Add amazing feature'`)
6. **Push to the branch** (`git push origin feature/amazing-feature`)
7. **Open a Pull Request**

### Contribution Guidelines

- **Clinical accuracy**: All mental health content must be evidence-based
- **Citation required**: New techniques/frameworks must include peer-reviewed citations
- **Safety first**: Never compromise crisis detection or safety gates
- **Plain language**: Maintain Grade 8 readability for user-facing content
- **Cultural sensitivity**: Consider multilingual and cultural factors

### Areas for Contribution

- **Additional languages**: Translation and cultural adaptation for new markets
- **New frameworks**: Evidence-based therapeutic approaches not yet included
- **Resource expansion**: Country-specific crisis resources and professional referrals
- **Technique library**: Additional self-help techniques with step-by-step instructions
- **Knowledge pipeline**: Improvements to evidence collection and update automation

---

## 📊 Evidence Base

### Knowledge Sources

| Source | Type | Priority | Update Frequency |
|--------|------|----------|------------------|
| PubMed / NCBI | Clinical research database | High | Daily |
| Cochrane Library | Systematic reviews | Highest | Quarterly |
| NICE Guidelines (UK) | Clinical guidelines | High | As updated |
| APA Guidelines | Professional guidelines | High | As updated |
| WHO mhGAP | Global mental health guidance | High | As updated |

### Current Knowledge Base

- **10+ foundational papers** seeded in SECOND-KNOWLEDGE-BRAIN.md
- **Evidence hierarchy**: Cochrane > Meta-Analysis > RCT > Guideline > Cohort
- **Automated updates**: Via tools/knowledge_updater.py

### Key Research References

- DeRubeis et al. (2005) — CBT vs medication for depression
- Hofmann & Smits (2008) — CBT for anxiety meta-analysis
- A-Tjak et al. (2015) — ACT empirical review
- Linehan et al. (1991) — DBT original RCT
- Mazzucchelli et al. (2009) — BA meta-analysis
- Teasdale et al. (2000) — MBCT relapse prevention

---

## 🛡️ Safety & Ethics

### Safety Principles

1. **Crisis-first architecture** — Safety gate is architecturally unbypassable
2. **Informational framing only** — No diagnostic language ("may suggest" not "you have")
3. **Severity-gated guidance** — Severe scores get professional referral, minimal self-help
4. **Resources on every output** — Crisis hotlines always present
5. **Professional disclaimer** — Clear that this is not a substitute for professional care

### Clinical Safeguards

- **PTSD**: No exposure exercises; describe CPT/EMDR, refer to trained therapist
- **Severe depression**: Limited guidance, strong professional referral
- **Active suicidality**: Immediate crisis response, no analysis
- **Substance dependence**: Medical referral, withdrawal safety warning

### Limitations

This skill:
- Does NOT provide diagnosis or treatment
- Does NOT replace professional mental health care
- Does NOT handle emergency crises (call emergency services)
- Does NOT provide crisis counseling (directs to crisis lines)

---

## 📜 License

This project is licensed under the MIT License — see the LICENSE file for details.

**Summary**: You are free to use, modify, and distribute this software, with attribution.

---

## 🙏 Acknowledgments

### Clinical References

- **C-SSRS**: Columbia Suicide Severity Rating Scale (Posner et al., 2011)
- **NICE Guidelines**: CG90 (Depression), CG113 (Anxiety), NG116 (PTSD)
- **APA Guidelines**: Clinical Practice Guidelines for various disorders
- **WHO mhGAP**: Mental Health Gap Action Programme

### Screening Instruments

- **PHQ-9**: Kroenke K, Spitzer RL, Williams JBW. J Gen Intern Med. 2001
- **GAD-7**: Spitzer RL, Kroenke K, Williams JBW, Löwe B. Arch Intern Med. 2006
- **PCL-5**: Weathers FW, et al. National Center for PTSD. 2013
- **AUDIT**: Saunders JB, et al. Addiction. 1993

### Therapeutic Frameworks

- **CBT**: Aaron Beck (1960s), Albert Ellis (REBT)
- **DBT**: Marsha Linehan (1993)
- **ACT**: Steven Hayes (1986)
- **MI**: Miller & Rollnick (1983)
- **MBCT**: Teasdale, Segal, Williams (1995)
- **EMDR**: Francine Shapiro (1989)
- **CPT**: Resick & Schnicke (1992)

### Tools & Resources

- Built for [Claude Code](https://claude.com/claude-code)
- Evidence sources: PubMed, Cochrane Library, NICE, APA, WHO
- Crisis resources: Befrienders Worldwide, IASP, national crisis lines

---

## 📞 Support & Resources

### Crisis Resources (24/7)

| Country | Hotline | Website |
|---------|---------|---------|
| 🇻🇳 Vietnam | 1800 599 920 | befrienders.org |
| 🇺🇸 USA | 988 | 988lifeline.org |
| 🇬🇧 UK | 116 123 | samaritans.org |
| 🇦🇺 Australia | 13 11 14 | lifeline.org.au |

### Professional Help

- **Primary care doctor** — First point of contact for referral
- **BetterHelp** — betterhelp.com (online therapy)
- **Talkspace** — talkspace.com (online therapy)
- **Psychology Today** — psychologytoday.com (therapist directory)

### Project Support

- **GitHub Issues**: [Report bugs or request features](https://github.com/dungnotnull/mental-health-detect-guidance-hd-skill/issues)
- **Documentation**: See PROJECT-detail.md for comprehensive technical specs
- **Clinical questions**: Consult licensed mental health professionals

---

## 🌟 Star History

If you find this project useful, please consider giving it a star ⭐

[![Star History Chart](https://api.star-history.com/svg?repos=dungnotnull/mental-health-detect-guidance-hd-skill&type=Date)](https://star-history.com/#dungnotnull/mental-health-detect-guidance-hd-skill&Date)

---

<div align="center">

**Built with ❤️ for accessible, evidence-based mental health support**

*Remember: You are not alone. Help is available.*

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Status: Production Ready](https://img.shields.io/badge/Status-Production%20Ready-green.svg)](https://github.com/dungnotnull/mental-health-detect-guidance-hd-skill)

</div>

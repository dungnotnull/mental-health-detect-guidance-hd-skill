# Evidence Collector Interface — Cluster B Skills Standard

> **Version**: 1.0
> **Last Updated**: 2026-06-04
> **Compatible With**: Any skill requiring evidence-backed guidance
> **Purpose**: Standardized evidence collection API for consistent, high-quality source attribution across skills

---

## Overview

The Evidence Collector Interface defines a **standardized protocol** for:
1. Running WebSearch queries across authoritative sources
2. Querying domain-specific knowledge bases
3. Retrieving and formatting evidence citations
4. Building evidence tables for structured outputs

Skills using this interface gain:
- Consistent citation formatting
- Evidence hierarchy enforcement
- Deduplication across sources
- Standardized output for user-facing documents

### Compatible Skills (Cluster B)

| Skill | Domain | Evidence Sources |
|-------|--------|------------------|
| mental-health-guidance | Mental health | PubMed, Cochrane, NICE, APA, WHO |
| research-first-reasoning | General research | ArXiv, Google Scholar, institutional repositories |
| investment-policy-guide | Finance/Policy | SEC, academic finance journals, regulatory bodies |
| [Future skill] | [Domain] | [Domain-specific sources] |

---

## Quick Start: Minimal Integration

### Step 1: Define Your Evidence Sources

```yaml
# In your skill's frontmatter
evidence_sources:
  primary:
    - name: PubMed
      url: pubmed.ncbi.nlm.nih.gov
      type: peer_reviewed
      priority: high
    - name: Cochrane Library
      url: cochranelibrary.com
      type: systematic_review
      priority: highest
  secondary:
    - name: Clinical Guidelines
      url: nice.org.uk/guidance
      type: guideline
      priority: medium
```

### Step 2: Invoke Evidence Collection

```markdown
## Evidence Collection Stage

> Action: Collect evidence for [condition/topic] using standardized protocol

### Query Pattern
```
"{topic}" "{framework}" randomized controlled trial OR meta-analysis OR systematic review {date_range}
```

### Minimum Sources
- 3 peer-reviewed sources required
- Prioritize: Cochrane > Meta-Analysis > RCT > Guideline > Cohort
```

### Step 3: Format Output

```markdown
## Evidence Table

| Finding | Source | Evidence Level | Year |
|---------|--------|----------------|------|
| [1-2 sentence summary] | Author, Year, Journal | [Cochrane/RCT/Guideline] | [Year] |
| ... | ... | ... | ... |
```

---

## Full API Specification

### Input Contract

```yaml
evidence_request:
  topic:
    type: string
    required: true
    description: "Primary condition/concept to research"
    example: "depression CBT"

  framework:
    type: string
    required: false
    description: "Therapeutic framework or intervention type"
    example: "cognitive behavioral therapy"

  date_range:
    type: string
    required: false
    default: "2018-2024"
    description: "Publication year filter for WebSearch"

  min_sources:
    type: integer
    required: false
    default: 3
    description: "Minimum number of sources required"

  evidence_hierarchy:
    type: array
    required: false
    default: ["cochrane", "meta_analysis", "rct", "guideline", "cohort"]
    description: "Preferred evidence types in priority order"

  knowledge_base_path:
    type: string
    required: false
    description: "Path to domain-specific knowledge base (e.g., SECOND-KNOWLEDGE-BRAIN.md)"
```

### Output Contract

```yaml
evidence_response:
  sources:
    type: array
    description: "List of collected evidence sources"
    items:
      title:
        type: string
        example: "CBT for depression: A meta-analysis"

      authors:
        type: string
        example: "Hofmann SG, et al."

      year:
        type: string
        example: "2012"

      journal:
        type: string
        example: "J Clin Psychiatry"

      doi:
        type: string
        example: "10.4088/JCP.12r08291"

      url:
        type: string
        example: "https://pubmed.ncbi.nlm.nih.gov/23060076/"

      evidence_level:
        type: string
        enum: ["cochrane", "meta_analysis", "rct", "guideline", "cohort", "expert_opinion"]
        example: "meta_analysis"

      key_finding:
        type: string
        example: "CBT is effective for depression with large effect sizes (g=0.83)"

      relevance:
        type: string
        example: "CBT efficacy for depression"

  evidence_table:
    type: markdown
    description: "Formatted markdown table for user-facing output"

  summary:
    type: string
    description: "2-3 sentence synthesis of collective findings"
```

---

## Evidence Hierarchy Standard

### Priority Levels (Highest to Lowest)

| Level | Description | Examples | Weight |
|-------|-------------|----------|--------|
| **Cochrane** | Cochrane Library systematic reviews | "Cochrane Database of Systematic Reviews" | 5 |
| **Meta-Analysis** | Non-Cochrane meta-analyses | Psychological Bulletin meta-analyses | 4.5 |
| **RCT** | Randomized controlled trials | "J Clin Psychiatry", "Lancet" RCTs | 4 |
| **Guideline** | Clinical practice guidelines | NICE, APA, WHO guidelines | 3.5 |
| **Cohort** | Observational longitudinal studies | Large cohort studies | 2.5 |
| **Expert Opinion** | Position papers, consensus statements | Professional association statements | 1.5 |

### Source Quality Rules

```markdown
## Evidence Quality Rules

1. **Deduplication**: If same paper appears from multiple sources, count once
2. **Recency weighting**: Prefer recent sources (last 5 years) for fast-moving domains
3. **Citation required**: Every claim in final output must trace to a source
4. **Minimum threshold**: Do not deliver output if <3 sources collected
5. **Level notation**: Always state evidence level in output table
```

---

## WebSearch Query Patterns by Domain

### Mental Health (mental-health-guidance)

```yaml
query_templates:
  - "{condition} {framework} randomized controlled trial OR meta-analysis 2018-2024"
  - "NICE guideline {condition} site:nice.org.uk"
  - "{framework} efficacy {condition} systematic review"
  - "APA clinical practice guideline {condition}"

examples:
  - "depression cognitive behavioral therapy randomized controlled trial 2018-2024"
  - "PTSD trauma-focused therapy systematic review"
  - "generalized anxiety disorder ACT meta-analysis"
```

### Finance/Policy (investment-policy-guide)

```yaml
query_templates:
  - "{policy} impact investment randomized controlled trial OR natural experiment"
  - "{market_segment} behavioral finance experimental study"
  - "{regulation} capital market efficiency empirical study"
  - "SEC guidance {topic} site:sec.gov"

examples:
  - "ESG fund performance empirical study"
  - "retail investor behavior bias experiment"
  - "transaction costs market efficiency study"
```

### General Research (research-first-reasoning)

```yaml
query_templates:
  - "{topic} systematic review OR meta-analysis"
  - "{topic} randomized controlled trial OR experiment"
  - "{topic} longitudinal study OR cohort"
  - "arXiv {topic} site:arxiv.org"

examples:
  - "attention span digital media systematic review"
  - "remote work productivity empirical study"
```

---

## Knowledge Base Integration

### Standard Knowledge Base Format

Skills using this interface should maintain a knowledge base in this format:

```markdown
# {DOMAIN}-KNOWLEDGE-BASE.md

## Update: {date}

### {Paper Title}
- **Source**: {Journal/Venue}
- **Authors**: {Authors}
- **Year**: {Year}
- **DOI/URL**: {Link}
- **Evidence Level**: {Cochrane/RCT/etc.}
- **Key Finding**: {1-2 sentence summary}
- **Relevance**: {Which framework/condition this supports}
```

### Querying the Knowledge Base

```python
# Pseudocode for knowledge base query
def query_knowledge_base(topic, framework, min_sources=3):
    relevant_entries = []

    for entry in knowledge_base:
        if topic.lower() in entry['title'].lower():
            if framework and framework.lower() in entry['relevance'].lower():
                relevant_entries.append(entry)

    # Sort by evidence level (Cochrane first)
    relevant_entries.sort(key=lambda x: evidence_weight[x['evidence_level']], reverse=True)

    return relevant_entries[:min_sources]
```

### Hybrid Approach (WebSearch + Knowledge Base)

```markdown
## Evidence Collection Protocol

### Step 1: Check Knowledge Base
- Query domain-specific knowledge base for {topic} + {framework}
- Extract pre-cached entries matching relevance criteria

### Step 2: Fill Gaps with WebSearch
- If knowledge base returns < {min_sources}, run WebSearch
- Use query patterns for domain-specific sources
- Deduplicate against knowledge base entries (DOI matching)

### Step 3: Merge and Rank
- Combine knowledge base + WebSearch results
- Rank by evidence hierarchy (Cochrane first)
- Select top {min_sources} for output

### Output Format
- Build evidence table from merged results
- All sources formatted with standard citation fields
```

---

## Output Formatting Standards

### Evidence Table Format

```markdown
## What the Research Says

| Finding | Source | Evidence Level | Year |
|---------|--------|----------------|------|
| CBT is effective for depression with large effect sizes (Hedges' g = 0.83) and is recommended as first-line treatment | Hofmann et al., 2012, J Clin Psychiatry | Meta-Analysis | 2012 |
| Behavioral Activation is equally effective to CBT for depression and simpler to deliver | Mazzucchelli et al., 2009, Clin Psychol Rev | Meta-Analysis | 2009 |
| NICE guideline CG90 recommends CBT and BA for moderate depression | NICE, 2022, Clinical Guideline CG90 | Guideline | 2022 |

**Summary**: Taken together, these studies indicate that CBT and BA are both evidence-based approaches for depression, with CBT having the strongest evidence base across multiple meta-analyses.
```

### Inline Citation Format

```markdown
## Text with Citations

Cognitive Behavioral Therapy (CBT) has demonstrated strong efficacy for depression across numerous studies (Hofmann et al., 2012). A comprehensive meta-analysis of 115 studies found large effect sizes (Hedges' g = 0.83), supporting CBT as a first-line intervention (Hofmann et al., 2012). The NICE guideline CG90 explicitly recommends CBT for moderate to severe depression (NICE, 2022).

### Reference List (Optional Footnote Format)
1. Hofmann SG, et al. The Efficacy of CBT: A Review of Meta-analyses. J Clin Psychiatry. 2012.
2. Mazzucchelli T, et al. Behavioral Activation Treatment for Depression. Clin Psychol Rev. 2009.
3. National Institute for Health and Care Excellence. Depression in Adults (CG90). 2022.
```

---

## Integration Example for New Skills

### Example: Investment-Policy-Guide Skill

```markdown
## Evidence Collection (Using Standard Interface)

### Sources Defined
```yaml
evidence_sources:
  primary:
    - Journal of Finance
    - Review of Financial Studies
    - SSRN
  secondary:
    - SEC.gov
    - CFA Institute Research Foundation
```

### Query Invocation
```
WebSearch: "ESG fund performance randomized controlled trial OR natural experiment 2018-2024"
WebSearch: "retail investor behavior bias experiment OR field study"
WebSearch: "SEC guidance ESG disclosure site:sec.gov"
```

### Output Table
```markdown
## What the Research Says

| Finding | Source | Evidence Level | Year |
|---------|--------|----------------|------|
| ESG funds do not underperform conventional funds after fees | Broadstock et al., 2021, Review of Finance | Empirical Study | 2021 |
| Retail investors exhibit home bias and attention bias | Barber & Odean, 2008, J Finance | Experimental | 2008 |
| SEC disclosure guidance improves ESG reporting comparability | SEC, 2024, Guidance Document | Regulatory | 2024 |
```
```

---

## Error Handling

### If WebSearch Unavailable

```markdown
## Fallback Protocol

If WebSearch is unavailable or errors:
1. Use knowledge base entries only
2. Note limitation in output: "Evidence sources limited to pre-cached knowledge base"
3. If knowledge base has <3 sources: deliver output with caveat and recommend manual research
4. Never fabricate sources or citations
```

### If Insufficient Sources Found

```markdown
## Insufficient Sources Protocol

If WebSearch returns <3 sources:
1. Broaden search query (remove framework filter, expand date range)
2. If still <3 sources after 2 attempts: deliver with caveat
3. Caveat text: "Limited evidence available. Current findings based on {N} sources. Recommend consulting additional research."

### NEVER:
- Invent citations
- Use non-peer-reviewed blogs as sources
- Proceed without acknowledging source limitation
```

---

## Testing Your Integration

### Verification Checklist

- [ ] WebSearch queries use domain-specific patterns
- [ ] Evidence hierarchy is enforced in output
- [ ] Minimum 3 sources collected before output
- [ ] All citations include: authors, year, journal, DOI/URL
- [ ] Evidence table uses standard markdown format
- [ ] Knowledge base is queried before WebSearch (if available)
- [ ] Deduplication logic prevents duplicate sources
- [ ] Error handling prevents source fabrication

### Test Cases

| Input Topic | Expected Sources | Expected Table Format |
|-------------|------------------|----------------------|
| depression CBT | PubMed meta-analyses, Cochrane reviews, NICE CG90 | Standard markdown table with 3+ rows |
| ESG performance | Finance journal empirical studies, SEC guidance | Standard markdown table with 3+ rows |
| [Your domain] | [Domain-specific sources] | Standard markdown table |

---

## Versioning and Updates

### API Versioning

This is v1.0 of the Evidence Collector Interface. Future versions will maintain backward compatibility.

### Update Protocol

When updating your skill's evidence collection:
1. Check for new authoritative sources in your domain
2. Update query patterns to reflect current terminology
3. Refresh knowledge base with recent entries (last 12 months)
4. Maintain evidence hierarchy priority order

---

## Support and Examples

### Reference Implementations
- `mental-health-guidance` — Mental health domain (PubMed, Cochrane, NICE)
- `tools/knowledge_updater.py` — Automated knowledge base pipeline
- `SECOND-KNOWLEDGE-BRAIN.md` — Knowledge base format example

### For New Domains

When adding a new domain to the Cluster B skill family:
1. Define authoritative sources for the domain
2. Create domain-specific WebSearch query patterns
3. Initialize domain knowledge base with 10+ foundational papers
4. Test evidence collection produces 3+ sources consistently

---

**Standardization Principle**: All Cluster B skills should produce evidence tables in the same format, ensuring users receive consistent, high-quality source attribution regardless of domain.

---

*End of Evidence Collector Interface Specification*

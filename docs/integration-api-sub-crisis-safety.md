# Integration API: sub-crisis-safety as a Dependency

> **Version**: 1.0
> **Last Updated**: 2026-06-04
> **Skill**: mental-health-guidance / sub-crisis-safety
> **Purpose**: Enable any skill to invoke crisis detection without loading the full harness

---

## Overview

The `sub-crisis-safety` sub-skill can be invoked as a **standalone dependency** by any skill that needs to:
1. Detect crisis-level content before proceeding with its own workflow
2. Classify user risk (CRITICAL / MODERATE / NONE)
3. Deliver appropriate emergency resources when needed
4. Receive a clear signal on whether to continue or halt processing

### Why Use This Dependency?

| Use Case | Example Skills |
|----------|----------------|
| Investor distress detection | Skill analyzing portfolio losses, bankruptcy risk |
| Entrepreneurial failure stress | Skill coaching through startup setbacks |
| Career transition anxiety | Skill supporting layoffs, career pivots |
| Relationship/divorce distress | Skill navigating separation, custody issues |
| Grief and loss counseling | Skill processing bereavement, major loss |
| Academic/examination pressure | Skill supporting students under extreme stress |

**Any skill dealing with human distress should run crisis screening first.**

---

## Quick Start: Minimal Integration

### Step 1: Add Dependency Declaration

In your skill's frontmatter or first section:

```yaml
---
name: your-skill-name
description: Your skill description

dependencies:
  crisis-detection:
    skill: mental-health-guidance/sub-crisis-safety
    type: mandatory-first  # Must run before any other processing
    output-variables: [crisis-flag, user-safe-to-continue]
---
```

### Step 2: Invoke at Entry Point

At the **very start** of your skill's workflow, before any analysis:

```markdown
## Entry Point: Crisis Safety Check

> Action: Invoke Skill("sub-crisis-safety") with user's input message

**Input**: User's raw message text
**Output**: Crisis flag (CRITICAL / MODERATE / NONE) + response

### Handoff Logic
- **CRITICAL**: Output crisis response immediately. STOP your skill's workflow.
- **MODERATE**: Output resources + acknowledgment. Await user confirmation of safety.
- **NONE**: Log "Safety gate cleared" → proceed to your skill's main workflow.
```

### Step 3: Handle the Output

```markdown
## Crisis Response Handling

### If Crisis Flag = CRITICAL
```
[Your skill STOPS here — do not proceed to main workflow]
```

### If Crisis Flag = MODERATE
```
[Your skill AWIITS user confirmation: "Are you safe to continue?"]
→ If user confirms safe: proceed to main workflow
→ If user declines: redirect to crisis resources, stop workflow
```

### If Crisis Flag = NONE
```
[Your skill proceeds normally]
```
```

---

## Full API Specification

### Input Contract

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_message` | string | Yes | Raw user input text |
| `conversation_history` | array | No | Prior conversation turns (helps detect escalating distress) |

### Output Contract

```json
{
  "crisis_flag": "CRITICAL | MODERATE | NONE",
  "response_template": "string (pre-formatted response to user)",
  "classification_detail": {
    "cssrs_level": "1-5",
    "signals_detected": ["array of crisis keywords/themes"],
    "recommended_action": "stop | await-confirmation | proceed"
  },
  "handoff_signal": "STOP | AWAIT_USER | PROCEED"
}
```

### Classification Reference

| Flag | C-SSRS Level | Description | Your Skill Should |
|------|-------------|-------------|-------------------|
| CRITICAL | 3–5 | Active ideation + method/plan/intent | STOP immediately |
| MODERATE | 1–2 | Passive ideation, hopelessness | Deliver resources, await confirmation |
| NONE | 0 | No crisis signals detected | Proceed normally |

---

## Integration Patterns by Use Case

### Pattern A: High-Stress Scenarios (Investor Distress, Career Crisis)

**When to use**: Your domain involves significant life stressors that can trigger crisis.

```markdown
## Workflow for [Your Skill]

### Stage 0: Mandatory Crisis Check (UNBYPASSABLE)
1. Invoke `sub-crisis-safety` with user input
2. If CRITICAL: halt, output resources
3. If MODERATE: output resources + "Are you safe to continue?"
4. If NONE or user confirms safe: proceed to Stage 1

### Stage 1: [Your normal workflow begins here]
...
```

**Example**: User says "I lost everything in the market crash. I'm thinking about ending it."
→ `sub-crisis-safety` flags CRITICAL
→ Your skill outputs crisis response and does NOT proceed to portfolio analysis.

---

### Pattern B: Moderate Stress Scenarios (Career Coaching, Academic Support)

**When to use**: Your domain involves stress but typically below acute crisis threshold.

```markdown
## Workflow for [Your Skill]

### Pre-Processing: Crisis Screen
Invoke `sub-crisis-safety` if user message contains:
- "hopeless", "give up", "can't take it", "end it", "no point"
- References to self-harm, suicide, death
- Expressions of worthlessness, being a burden

### Screen Negative → Proceed normally
### Screen Positive → Follow crisis protocol (Pattern A)
```

**Example**: User says "I'm so stressed about this exam. I feel like giving up."
→ `sub-crisis-safety` flags MODERATE (passive ideation)
→ Your skill offers resources + asks if safe to continue studying.

---

### Pattern C: Minimal Overhead (General Purpose Skills)

**When to use**: Your skill rarely encounters crisis but wants safety coverage.

```markdown
## Crisis Safety Gate

Before responding to any user message:
1. Quick keyword scan: [kill myself, suicide, end my life, hurt myself]
2. If ANY match → invoke `sub-crisis-safety`
3. Else → proceed normally

**Note**: This is a light screen only. Full `sub-crisis-safety` invocation is safer and recommended for any skill dealing with emotional content.
```

---

## Resource Reuse

### Use Shared Crisis Resources

After receiving a CRITICAL or MODERATE flag, your skill can either:
1. Use the pre-formatted response from `sub-crisis-safety` output (recommended), OR
2. Use the shared crisis resource block at `shared/crisisis-resources.md`

### Custom Resource Integration

If your skill has domain-specific crisis resources (e.g., financial distress hotlines):

```markdown
## Crisis Response (Domain-Specific)

### General Crisis Resources
[Import from shared/crisis-resources.md]

### Domain-Specific Resources
- **Financial Distress Hotline**: [your number]
- **Bankruptcy Support Services**: [your resources]
```

---

## Error Handling

### If sub-crisis-safety Invocation Fails

```markdown
## Fallback Protocol

If `sub-crisis-safety` is unavailable or errors:
1. Default to MODERATE classification (safety-first)
2. Output generic crisis resources from shared block
3. Ask user direct safety question: "Are you safe right now?"
4. Do NOT proceed to main workflow until user confirms safety
```

### If User Refuses Safety Question

```markdown
## Non-Cooperative User Protocol

If user will not answer safety questions:
1. Assume MODERATE risk (safety-first default)
2. Provide crisis resources
3. State: "I can't continue without knowing you're safe. Please reach out to [crisis line]"
4. Halt workflow
```

---

## Testing Your Integration

### Test Cases to Verify

| Test Input | Expected Flag | Expected Your Skill Behavior |
|------------|--------------|------------------------------|
| "I want to kill myself" | CRITICAL | STOP; show resources; no analysis |
| "I've been feeling hopeless lately" | MODERATE | Show resources; await confirmation |
| "I'm stressed about my presentation" | NONE | Proceed to your normal workflow |
| "I lost my job and don't see a point" | MODERATE | Show resources; await confirmation |

### Verification Checklist

- [ ] Your skill invokes crisis check BEFORE any analysis
- [ ] CRITICAL flag causes immediate workflow halt
- [ ] MODERATE flag triggers resource delivery + safety question
- [ ] NONE flag allows normal workflow continuation
- [ ] Crisis resources are present in all CRITICAL/MODERATE outputs
- [ ] Your skill never proceeds to analysis when CRITICAL is detected

---

## Language Considerations

### Non-English User Input

The `sub-crisis-safety` sub-skill is English-optimized. For multilingual skills:

```markdown
## Multilingual Crisis Detection

### If User Input is Non-English
1. Use language detection on user message
2. If not English:
   - Translate user message to English (for crisis keyword detection)
   - Run `sub-crisis-safety` on translated text
   - Present crisis response in USER'S LANGUAGE using localized resources

### Vietnamese Example
User says: "Tôi chán đời quá, muốn tự tử"
→ Translate to English: "I'm tired of life, want to commit suicide"
→ Run `sub-crisis-safety` → flags CRITICAL
→ Respond in Vietnamese with Vietnamese crisis resources (1800 599 920)
```

---

## Versioning and Updates

### API Versioning

This documentation describes API v1.0. Future versions will maintain backward compatibility where possible.

### Update Protocol

When `sub-crisis-safety` is updated:
1. Check this integration API document for breaking changes
2. Update your skill's handoff logic if classification levels change
3. Verify crisis resource block updates (phone numbers may change)

### Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-06-04 | Initial API specification |

---

## Support and Questions

### For Implementation Help
- Reference: `skills/sub-crisis-safety.md` for full protocol
- Resources: `shared/crisis-resources.md` for resource templates
- Context: `PROJECT-detail.md` for architecture rationale

### Clinical Safety Questions
If you are uncertain whether your skill should use crisis detection:
- Default to YES (safety-first principle)
- Any skill dealing with human distress, loss, failure, or high stress should use this dependency

---

**Remember**: The cost of a false negative (missing a crisis) is unacceptably high. When in doubt, invoke the crisis safety check.

---

*End of Integration API Documentation*

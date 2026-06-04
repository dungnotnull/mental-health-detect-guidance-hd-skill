# SHARED CRISIS RESOURCE BLOCK

> **Purpose**: Standalone crisis resource module importable by any skill requiring emergency/safety resources.
> **Usage**: Import this file and use the resource blocks directly. No dependency on mental-health-guidance harness.
> **Last Updated**: 2026-06-04

---

## Resource Templates

### Crisis Support (24/7) — International

```markdown
### Crisis Support (24/7)

#### Vietnam
- **1800 599 920** (Đường dây hỗ trợ tâm lý — free, 24/7)
- **1800 1567** (Hỗ trợ trẻ em và thanh niên — free)

#### United States
- **988** — Suicide & Crisis Lifeline (call or text)
- **1-800-273-8255** — National Suicide Prevention Lifeline (legacy)
- **911** — Emergency services

#### United Kingdom
- **116 123** — Samaritans (free, 24/7)
- **999** — Emergency services
- **111** — Non-emergency medical advice

#### Australia
- **13 11 14** — Lifeline Australia
- **000** — Emergency services

#### Canada
- **988** — Suicide Crisis Lifeline (nationwide)
- **1-833-456-4566** — Talk Suicide Canada
- **911** — Emergency services

#### International
- **befrienders.org** — Find your country's crisis hotline
- **iasp.info/resources/Crisis_Centres** — International Association for Suicide Prevention
- **findahelpline.com** — Global helpline directory
```

---

### Professional Referral Pathways

```markdown
### Finding Professional Support

#### Primary Care Entry Point
- **GP / Family Doctor** — First point of contact for referral to mental health services
- **Occupational Health / EAP** — Workplace support programs (often free)
- **University Counseling** — For students (usually included in tuition)

#### Online Therapy Platforms (International)
- **BetterHelp** — betterhelp.com
- **Talkspace** — talkspace.com
- **Open Path Collective** — openpathcollective.org (low-cost options)

#### Vietnam-Specific Resources
- **Bệnh viện tâm thần địa phương** — Local psychiatric hospitals (Hanoi, HCMC, Da Nang)
- **Phòng khám tâm lý tư nhân** — Private psychology clinics
- **Mentalland** — mentalland.vn (online counseling)
- **Mindcare** — mindcare.vn

#### United Kingdom
- **NHS IAPT** — Self-refer at nhs.uk/mental-health (free talking therapies)
- **Rethink** — rethink.org (mental health support)

#### United States
- **Psychology Today Directory** — psychologytoday.com (find therapists by insurance)
- **SAMHSA Treatment Locator** — findtreatment.samhsa.gov
```

---

## Country-Specific Resource Blocks

### Vietnam (Primary Target Market)

```markdown
### Vietnam Crisis Resources

#### Emergency
- **113** — Police/Emergency
- **114** — Fire/Ambulance
- **1800 599 920** — National Crisis Line (free, 24/7)

#### Mental Health Hotlines
- **1800 599 920** — Ministry of Labour, Invalids and Social Affairs (MOLISA)
- **1800 1567** — National Child Helpline (for youth under 18)
- **1900 599 830** — Center for Women and Development Support

#### Professional Help
- **Bệnh viện Bạch Mai** — Hanoi (Psychiatric Department)
- **Bệnh viện Chợ Rẫy** — HCMC (Mental Health Department)
- **Bệnh viện Tâm thần Trung ương 1** — Hanoi
- **Bệnh viện Tâm thần Trung ương 2** — HCMC

#### Online Counseling
- **Mindcare Clinic** — mindcare.vn (Hanoi, HCMC)
- **Mentalland** — mentalland.vn (online)
- **PSYCare Vietnam** — psycare.vn (online)
```

---

## Crisis Response Templates

### CRITICAL — Immediate Danger

```markdown
## CRITICAL SAFETY ALERT

I hear you, and I'm genuinely concerned about your safety right now.

**🆘 If you are in immediate danger, please contact emergency services:**

| Country | Emergency Number |
|---------|------------------|
| Vietnam | 113 |
| USA | 911 |
| UK | 999 |
| Australia | 000 |

**📞 Crisis support is available right now:**

- **Vietnam**: 1800 599 920 (free, 24/7)
- **International**: befrienders.org — find your country's crisis line
- **USA/Canada**: 988 (call or text)
- **UK**: 116 123 — Samaritans

**You matter, and people are ready to help right now. Please make that call.**

---

*This is not a substitute for professional emergency care. If you or someone else is in immediate danger, contact emergency services immediately.*
```

### MODERATE — Distress Resources

```markdown
## Support Resources

Before we continue, I want to make sure you have access to support if you need it:

**📞 Crisis Lines (24/7, free, confidential):**
- **Vietnam**: 1800 599 920
- **International**: befrienders.org
- **USA**: 988
- **UK**: 116 123

**💻 Online Support:**
- **Crisis Text Line** (text HOME to 741741 in USA/UK)
- **7 Cups** — 7cups.com (free listener support)

---

*These resources are here if you need them. You deserve support.*
```

---

## Integration Format for Other Skills

### Minimal Import Format

Other skills can import and use these resources in two ways:

#### Option 1: Direct File Include
```yaml
# In your skill's frontmatter or first section:
includes:
  - path: ../mental-health-guidance/shared/crisis-resources.md
    section: "crisis-response-critical"  # or "moderate" or "country-vietnam"
```

#### Option 2: Template Copy-Paste
Copy the relevant template block directly into your skill's output section.

### Minimal Required Elements

Any skill using crisis resources MUST include at minimum:
1. **One emergency number** for the user's likely region (Vietnam: 113, 1800 599 920)
2. **One international finder** (befrienders.org or findahelpline.com)
3. **Professional referral pathway** (at least one option)

### Language Localization

For non-English outputs, translate the resource labels but keep phone numbers unchanged:

```markdown
### Vietnamese Translation Example

#### Hỗ trợ Khẩn cấp (24/7)
- **1800 599 920** — Đường dây hỗ trợ tâm lý (miễn phí, 24/7)
- **1800 1567** — Tổng đài hỗ trợ trẻ em (miễn phí)
- **113** — Cảnh sát / Cứu hộ khẩn cấp

#### Tìm Chuyên Gia
- **Bệnh viện tâm thần địa phương** — Local psychiatric hospital
- **Phòng khám tâm lý** — Private psychology clinic
```

---

## Maintenance Protocol

### Update Frequency
- Review and update quarterly (January, April, July, October)
- Verify phone numbers are still active
- Add new country-specific resources as target markets expand

### Verification Sources
- **IASP Crisis Centre Directory**: iasp.info/resources/Crisis_Centres
- **Befrienders Worldwide**: befrienders.org
- **WHO mhGAP**: who.int/mental_health/mhgap/en/

### Version Control
- Update the "Last Updated" date when making changes
- Document any number changes in a changelog comment

---

## License and Usage

**License**: This shared resource block may be used by any skill requiring crisis/safety resources.

**Attribution**: When used in published skills, include: "Crisis resources sourced from mental-health-guidance skill's shared crisis resource block."

**Modification**: Localize (add country-specific numbers) but do NOT remove existing verified resources.

---

*End of Shared Crisis Resource Block*

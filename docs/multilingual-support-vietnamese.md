# Multilingual Support: Vietnamese Language Strategy

> **Version**: 1.0
> **Last Updated**: 2026-06-04
> **Target Language**: Vietnamese (Tiếng Việt)
> **Primary User Base**: Vietnam-based users seeking mental health guidance
> **Scope**: Translation, cultural adaptation, resource localization

---

## Overview

Vietnam is the **primary target market** for the mental-health-guidance skill. Vietnamese users need:
1. Full skill workflow available in Vietnamese
2. Culturally appropriate framing of mental health concepts
3. Local crisis resources and professional referral pathways
4. Respectful handling of stigma and cultural attitudes toward mental health

### Vietnam Mental Health Context

| Factor | Consideration | Skill Adaptation |
|--------|--------------|------------------|
| **Stigma** | Mental health is highly stigmatized; seeking help is viewed as weakness | Use non-pathologizing language; emphasize "support" not "treatment" |
| **Family focus** | Family honor and reputation are central | Include family-inclusive approaches; address family concerns |
| **Traditional beliefs** | Spiritual/bodily imbalance concepts common | Acknowledge traditional views while presenting evidence-based approaches |
| **Resource access** | Limited mental health infrastructure outside major cities | Provide tiered guidance: self-help → local clinics → urban hospitals |
| **Language** | Northern/Southern dialect differences; formal/informal registers | Use standard Northern Vietnamese (Hanoi-based) with inclusive terms |

---

## Translation Protocol

### Tier 1: Core Content Translation (Priority 1)

**Must translate for Phase 1 Vietnamese launch:**

```yaml
tier1_translations:
  crisis_detection:
    - C-SSRS probe questions (all 5 levels)
    - CRITICAL/MODERATE/NONE response templates
    - All crisis hotline numbers and descriptions

  screening_instruments:
    - PHQ-9 questions and response options
    - GAD-7 questions and response options
    - PCL-5 core 5-item screen
    - Scoring instructions and severity bands

  framework_names:
    - CBT (Liệu pháp Nhận thức Hành vi)
    - ACT (Liệu pháp Chấp nhận và Cam kết)
    - DBT (Liệu pháp Hành vi Biện chứng)
    - MI (Phỏng vấn Động cơ)
    - MBCT (Liệu pháp Chánh niệm Nhận thức)

  technique_instructions:
    - All step-by-step technique descriptions
    - "How to do it" sections for each technique
    - Tip/example text for techniques
```

### Tier 2: Supporting Content (Priority 2)

**Translate for enhanced user experience:**

```yaml
tier2_translations:
  guidance_sections:
    - "Understanding Your Experience" psychoeducation
    - "What the Research Says" evidence summaries
    - "When to Seek Professional Help" criteria

  resources:
    - All Vietnam-specific professional referrals
    - Hospital and clinic names and descriptions
    - Online counseling platform names and URLs

  disclaimers:
    - Professional disclaimer block
    - Safety/emergency disclaimer language
```

### Tier 3: Technical Content (Priority 3)

**Keep in English with Vietnamese summaries:**

```yaml
tier3_translations:
  evidence_tables:
    - Keep source citations in English (author names, journals)
    - Translate "Finding" column to Vietnamese
    - Add Vietnamese summary after English table

  clinical_references:
    - Keep instrument names in English with Vietnamese translation
    - Example: "PHQ-9 (Bảng kiểm tra trầm cảm - 9 mục)"
```

---

## Cultural Adaptation Guidelines

### Principle 1: Reduce Stigma Through Language

**English (Direct)** → **Vietnamese (Adapted)**

| English Concept | Literal Vietnamese | Culturally Adapted Vietnamese |
|----------------|-------------------|------------------------------|
| "Mental illness" | "Bệnh tâm thần" (too stigmatizing) | "Vấn đề sức khỏe tâm thần" or "Khó khăn về tâm lý" |
| "Depression" | "Trầm cảm" (acceptable, but heavy) | "Cảm giác buồn chán" or "Trầm cảm (light use)" |
| "Therapy" | "Trị liệu" (medical term) | "Hỗ trợ tâm lý" or "Đàm phán tâm lý" |
| "Diagnosis" | "Chẩn đoán" (medical) | "Đánh giá" or "Hiểu rõ hơn về" |
| "Treatment" | "Điều trị" (disease-focused) | "Hỗ trợ" or "Phương pháp cải thiện" |

### Principle 2: Family-Inclusive Framing

```markdown
## Vietnamese Adaptation: Family Context

### Instead of (English):
"You may be experiencing depression. Here are self-help techniques."

### Use (Vietnamese):
"Bạn đang trải qua những cảm giác khó khăn. Điều này không có gì là đáng xấu hổ. Nhiều người cũng trải qua điều này. Các phương pháp sau có thể giúp bạn cảm thấy tốt hơn — và bạn có thể chia sẻ với người thân nếu bạn cảm thấy thoải mái."

### Key adaptations:
- Add "Không có gì là đáng xấu hổ" (There is nothing to be ashamed of)
- Include "Nhiều người cũng trải qua điều này" (Many people experience this too) — normalization
- Add optional family sharing: "bạn có thể chia sẻ với người thân" (you can share with loved ones)
```

### Principle 3: Respect Traditional Beliefs

```markdown
## Vietnamese Adaptation: Traditional Beliefs

### Acknowledge, Don't Dismiss

Sometimes Vietnamese users attribute mental health to:
- "Hên xui" (luck/fate)
- "Tâm linh" (spiritual causes)
- "Mất cân bằng âm dương" (yin-yang imbalance)

### Response Pattern:

"Bên cạnh các yếu tố tâm lý mà khoa học đã chứng minh, nhiều người cũng quan niệm rằng sức khỏe liên quan đến các yếu tố tâm linh hoặc sự cân bằng trong cơ thể. Các phương pháp dưới đây dựa trên nghiên cứu khoa học quốc tế, và bạn hoàn toàn có thể kết hợp với những cách bạn tin tưởng nếu nó giúp bạn cảm thấy tốt hơn."

### Translation:
"Alongside psychological factors proven by science, many people also believe health relates to spiritual factors or balance in the body. The methods below are based on international scientific research, and you can absolutely combine them with approaches you trust if they help you feel better."

### Key:
- Validate traditional beliefs ("nhiều người cũng quan niệm")
- Don't dismiss ("bạn hoàn toàn có thể kết hợp")
- Maintain scientific integrity ("dựa trên nghiên cứu khoa học")
```

### Principle 4: Appropriate Formality Levels

Vietnamese has complex pronoun systems. Use:

| Context | Pronoun System | When to Use |
|---------|----------------|-------------|
| **Standard skill responses** | "Bạn - Bạn" (You - You) | Default for general guidance |
| **Crisis/emergency** | "Bạn - Tôi" (You - I) | Maintain professional distance while being caring |
| **Very formal** | "Quý vị - Tôi" (You - I) | Medical/clinical contexts (rare in this skill) |

**Avoid**: "Anh - Em" (older brother - younger sibling) or familial terms unless user initiates.

---

## Localized Resource Mapping

### Vietnam Crisis Resources (Translated)

```markdown
### Vietnamese Crisis Resources — Translated

#### Tài nguyên Khẩn cấp (24/7)

**Việt Nam:**
- **1800 599 920** — Đường dây hỗ trợ tâm lý (miễn phí, 24/7)
- **1800 1567** — Tổng đài hỗ trợ trẻ em và thanh niên (miễn phí)
- **113** — Cảnh sát / Cứu hộ khẩn cấp

**Quốc tế:**
- **befrienders.org** — Tìm đường dây hỗ trợ tại quốc gia của bạn

#### Tìm Chuyên Gia Tại Việt Nam

**Bệnh viện tâm thần (Tại các thành phố lớn):**
- **Hà Nội:** Bệnh viện Tâm thần Trung ương 1, Bệnh viện Bạch Mai (Khoa Tâm thần)
- **TP. Hồ Chí Minh:** Bệnh viện Tâm thần Trung ương 2, Bệnh viện Chợ Rẫy (Khoa Sức khỏe Tâm thần)
- **Đà Nẵng:** Bệnh viện Tâm thần Đà Nẵng

**Phòng khám tâm lý tư nhân:**
- **Mindcare Clinic** — mindcare.vn (Hà Nội, TP. Hồ Chí Minh)
- **Mentalland** — mentalland.vn (hỗ trợ trực tuyến)
- **PSYCare Vietnam** — psycare.vn (hỗ trợ trực tuyến)

**Nền tảng tư vấn trực tuyến:**
- **BetterHelp** — betterhelp.com (nền tảng quốc tế)
- **Talkspace** — talkspace.com (nền tảng quốc tế)
```

### Professional Referral Language (Vietnamese)

```markdown
### Vietnamese Professional Referral Script

**Instead of (English):**
"You should see a therapist. Here's how to find one."

**Use (Vietnamese):**
"Nếu bạn cảm thấy những khó khăn này ảnh hưởng đến cuộc sống hàng ngày của bạn (công việc, gia đình, giấc ngủ), việc nói chuyện với một chuyên gia sức khỏe tâm thần có thể rất hữu ích. Tại Việt Nam, bạn có thể:

1. **Đến bệnh viện:** Các bệnh viện tâm thần tại Hà Nội, TP. Hồ Chí Minh, Đà Nẵng có các bác sĩ chuyên khoa
2. **Phòng khám tư:** Các phòng khám tâm lý tư nhân (Mindcare, Mentalland) có thể hỗ trợ đặt hẹn
3. **Hỗ trợ trực tuyến:** Các nền tảng như BetterHelp cho phép bạn nói chuyện với chuyên gia từ nhà

Bạn không cần phải một mình đối mặt với điều này. Xin hãy tìm kiếm sự hỗ trợ khi bạn cần."
```

---

## Implementation Strategy

### Phase 1: Critical Path Translation (Week 1-2)

**Priority: Launch-safe Vietnamese experience**

```yaml
phase1_tasks:
  week1:
    - Translate crisis detection probes (C-SSRS 5 levels)
    - Translate crisis response templates (CRITICAL/MODERATE/NONE)
    - Translate PHQ-9 and GAD-7 questions with scoring
    - Verify translated crisis resources (phone numbers active)

  week2:
    - Translate framework selection rationale templates
    - Translate 5 core techniques from CBT/ACT/DBT
    - Test end-to-end Vietnamese workflow with mock user input
    - Vietnamese language review by native speaker
```

### Phase 2: Full Content Translation (Week 3-4)

```yaml
phase2_tasks:
  week3:
    - Translate all psychoeducation sections ("Understanding Your Experience")
    - Translate evidence table findings (keep citations in English)
    - Translate technique reference bank (50+ techniques)
    - Translate "When to Seek Professional Help" section

  week4:
    - Translate disclaimer blocks
    - Translate all resource descriptions
    - Cultural adaptation review (stigma, family, traditional beliefs)
    - Full integration testing with Vietnamese user scenarios
```

### Phase 3: Validation and Launch (Week 5)

```yaml
phase3_tasks:
  week5:
    - Clinical accuracy review of translated content
    - Cultural appropriateness review by Vietnamese mental health professional
    - User testing with 5+ Vietnamese speakers
    - Final refinements and launch preparation
```

---

## Testing Approach

### Test Scenarios for Vietnamese

| Scenario | Input (Vietnamese) | Expected Behavior |
|----------|-------------------|-------------------|
| **Crisis** | "Tôi muốn tự tử. Tôi có kế hoạch rồi." | CRITICAL flag; Vietnamese crisis response; 1800 599 920 displayed |
| **Depression** | "Tôi buồn lắm, không muốn làm gì cả. Đã 3 tháng rồi." | PHQ-9 in Vietnamese; CBT/BA techniques in Vietnamese |
| **Anxiety** | "Tôi lo lắng suốt, không ngủ được." | GAD-7 in Vietnamese; ACT/CBT techniques in Vietnamese |
| **Stigma** | "Tôi sợ người nhà biết sẽ suy nghĩ về tôi." | Family-inclusive response; stigma-reduction language |
| **Traditional** | "Tôi nghĩ do tôi mất cân bằng âm dương." | Validate belief + present scientific approaches |

### Language Quality Checks

```markdown
## Vietnamese Translation Quality Checklist

- [ ] No machine translation artifacts (Google Translate quirks)
- [ ] Appropriate formality level (Bạn/Bạn standard)
- [ ] Crisis language is clear and direct (no euphemisms)
- [ ] Technique instructions are actionable and specific
- [ ] Clinical terms translated accurately (PHQ-9, CBT, etc.)
- [ ] Phone numbers and URLs are correct for Vietnam
- [ ] Stigma-reduction language present throughout
- [ ] Family-inclusive framing used where appropriate
- [ ] Traditional beliefs acknowledged when mentioned
- [ ] Professional disclaimer is legally appropriate in Vietnamese context
```

---

## Technical Implementation

### Language Detection and Routing

```markdown
## Multilingual Workflow

### Step 1: Language Detection
On first user message, detect language:
- If Vietnamese detected (confidence >80%): switch to Vietnamese mode
- If English or other: default to English mode, offer Vietnamese option

### Step 2: Language Preference Storage
Store user's language preference for session duration.

### Step 3: Content Routing
All subsequent invocations use language-specific content:
- Crisis detection: Use Vietnamese probes
- Screening: Use Vietnamese instrument questions
- Framework selection: Use Vietnamese rationale templates
- Techniques: Use Vietnamese instructions

### Step 4: Resource Localization
Always present crisis and professional resources matching user's language/location.
```

### File Structure for Vietnamese

```yaml
vietnam_localization:
  translations:
    - skills/vi/sub-crisis-safety-vi.md
    - skills/vi/sub-screening-vi.md
    - skills/vi/sub-framework-selector-vi.md
    - skills/vi/sub-guidance-writer-vi.md

  resources:
    - shared/crisis-resources-vi.md (Vietnamese resources)

  knowledge_base:
    - SECOND-KNOWLEDGE-BRAIN-VI.md (Vietnamese summaries of evidence)
```

---

## Cultural Sensitivity Notes

### Topics Requiring Extra Care

| Topic | Cultural Consideration | Vietnamese Adaptation |
|-------|----------------------|----------------------|
| **Suicide** | Highly stigmatized; brings shame to family | Use direct but caring language; emphasize family support resources |
| **Medication** | Many Vietnamese prefer herbal/traditional remedies | Acknowledge traditional approaches; present medication as one option among others |
| **Family conflict** | Family harmony is paramount; speaking against family is taboo | Frame as "improving family communication" not "confronting family" |
| **Work stress** | Overwork is often seen as unavoidable/dutiful | Validate work pressures while suggesting boundaries; acknowledge cultural expectations |
| **Help-seeking** | Asking for help is seen as weakness | Reframe as "seeking support is wise/courageous"; normalize help-seeking |

### Phrases to Avoid in Vietnamese

| Avoid | Use Instead | Reason |
|-------|-------------|--------|
| "Bạn bị trầm cảm" (You have depression) | "Bạn đang trải qua những cảm giác buồn chán" (You're going through sad feelings) | "Bị" (have/contract) is disease-focused and stigmatizing |
| "Bạn cần trị liệu" (You need therapy) | "Việc tìm hỗ trợ có thể giúp bạn" (Finding support can help you) | "Cần" (need) is directive; offer support instead |
| "Đừng lo lắng" (Don't worry) | "Cảm giác lo lắng là bình thường" (Feeling worried is normal) | Dismissive; validate instead |
| "Hãy nghĩ tích cực" (Think positively) | "Có những cách để đối diện với suy nghĩ tiêu cực" (There are ways to face negative thoughts) | Toxic positivity; acknowledge difficulty |

---

## Maintenance and Updates

### Translation Review Schedule

- **Quarterly**: Review translated content for accuracy and cultural appropriateness
- **After major updates**: When English content changes significantly, update Vietnamese translation
- **User feedback integration**: Incorporate user feedback on Vietnamese language clarity

### Vietnamese Mental Health Resource Updates

- **Biannually**: Verify Vietnam crisis hotlines are still active
- **Annually**: Update hospital/clinic resource lists
- **As needed**: Add new online counseling platforms serving Vietnam

---

## Success Metrics

### Vietnamese Launch Success Criteria

| Metric | Target | Measurement |
|--------|--------|-------------|
| **Translation accuracy** | ≥95% accurate by native speaker review | Professional Vietnamese translator assessment |
| **Cultural appropriateness** | Zero culture clashes in user feedback | User testing + feedback monitoring |
| **Resource accessibility** | All Vietnam phone numbers active | Quarterly verification |
| **User comprehension** | ≥90% of Vietnamese users report understanding guidance clearly | User survey |
| **Stigma reduction** | Users report feeling less ashamed after using skill | Qualitative user feedback |

---

## Examples: Side-by-Side Translations

### Example 1: Crisis Response

**English:**
```
I hear you, and I'm genuinely concerned about your safety right now.

Please reach out for immediate support:

🆘 Emergency: Call 113 (Vietnam) or go to your nearest emergency room
📞 Vietnam Crisis Line: 1800 599 920 (free, 24/7)

You matter, and people are there to help right now. Please make that call.
```

**Vietnamese:**
```
Tôi nghe bạn nói, và tôi thực sự lo lắng về sự an toàn của bạn lúc này.

Xin hãy tìm kiếm sự hỗ trợ ngay lập tức:

🆘 Khẩn cấp: Gọi 113 (Việt Nam) hoặc đến phòng cấp cứu gần nhất
📞 Đường dây hỗ trợ tâm lý Việt Nam: 1800 599 920 (miễn phí, 24/7)

Bạn quan trọng, và có những người sẵn sàng giúp đỡ bạn ngay bây giờ. Xin hãy gọi cho họ.
```

### Example 2: Technique Instruction

**English (CBT Thought Record):**
```
**How to do it** (step-by-step):
1. Write down the situation that triggered a difficult emotion
2. Identify the automatic thought that went through your mind
3. Challenge this thought: Is it 100% true? What evidence is against it?
4. Write a more balanced thought that fits the facts better
```

**Vietnamese (CBT Thought Record):**
```
**Cách thực hiện** (từng bước):
1. Viết lại tình huống đã触发 cảm xúc khó khăn
2. Xác định suy nghĩ tự động xuất hiện trong đầu bạn
3. Thách thức suy nghĩ này: Nó hoàn toàn đúng không? Có bằng chứng nào chống lại nó không?
4. Viết một suy nghĩ cân bằng hơn phù hợp với sự thật hơn
```

---

## Launch Readiness Checklist

### Before Vietnamese Language Launch

- [ ] All Tier 1 content translated and reviewed
- [ ] Crisis detection works accurately in Vietnamese
- [ ] Screening instruments (PHQ-9, GAD-7) validated in Vietnamese
- [ ] All Vietnam crisis resources verified active
- [ ] Cultural adaptation reviewed by Vietnamese mental health professional
- [ ] 5+ Vietnamese speakers have tested the skill end-to-end
- [ ] Stigma-reduction language present throughout
- [ ] Family-inclusive framing used where appropriate
- [ ] Traditional beliefs acknowledged in guidance
- [ ] Error handling supports Vietnamese language
- [ ] Disclaimer blocks legally appropriate for Vietnamese context

---

**Remember**: Vietnam is the primary market. A Vietnamese-language experience that is culturally sensitive, clinically accurate, and stigma-aware is essential for this skill's success.

---

*End of Multilingual Support Strategy (Vietnamese)*

# Home Mobile Responsive Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make the Home page responsive for 375px mobile and fluid in the full 744px->375px range without breaking desktop/744 behavior.

**Architecture:** Keep the current Vue SFC structure and implement a class-based responsive layer inside `Home.vue` scoped styles. Replace fragile positional media selectors with explicit section hooks and fluid CSS values (`clamp`) for intermediate widths, then apply exact 375 overrides. Keep review controls and the 3rd-section gradient aligned with existing desktop/744 behavior.

**Tech Stack:** Vue 3 SFC, scoped CSS, Tailwind utility classes already present in templates, Vite build.

---

### Task 1: Stabilize Home Section Hooks (Remove Positional Fragility)

**Files:**
- Modify: `frontend/src/views/Home.vue`
- Test: `frontend/src/views/Home.vue` (template compilation via build)

- [ ] **Step 1: Write the failing check (current fragility proof)**

Run: `npm run build`

Then manually confirm that current responsive behavior depends on positional selectors in `Home.vue` (`section:first-of-type`, `section:nth-of-type(...)`) and `!important`, which is fragile for further edits.

Expected: build passes, but responsive CSS structure is brittle and hard to evolve.

- [ ] **Step 2: Add explicit class hooks to Home sections and key containers**

Update `frontend/src/views/Home.vue` template by adding class hooks (keep existing attributes untouched).

```vue
<section
  class="home-hero"
  className="w-full h-[52.625rem] max-sm:h-full absolute top-0 left-0 bg-center bg-cover pb-16 max-sm:px-4"
  :style="{ backgroundImage: 'url(' + heroImage + ')' }"
>
  <div class="home-hero__content" className="mt-[566px] max-sm:mt-[314px] max-sm:px-4 px-8">
    ...
  </div>
</section>

<section
  class="home-about"
  className="bg-blue-600 px-8 z-[6] py-16 max-sm:py-2 w-full rounded-2xl relative translate-y-[835px] mt-[-16px] max-sm:translate-y-[648px]"
>
  <div class="home-about__head" ...>...</div>
  <div class="home-about__stats" ...>...</div>
</section>

<section
  class="home-services"
  className="bg-neutral-200 px-8 z-20 py-16 max-sm:py-2 w-full rounded-2xl relative translate-y-[825px] mt-[-16px] max-sm:translate-y-[640px]"
>
  <div class="home-services__promo" className="flex justify-end flex-col priemka h-[40.4375rem] w-full rounded-2xl text-neutral-100 p-8 mb-10">
    ...
  </div>
  <div class="home-services__grid" class="grid grid-cols-3 justify-items-center gap-8 max-[1328px]:grid-cols-2 max-[1328px]:justify-items-stretch max-[744px]:gap-[0.625rem]">
    ...
  </div>
</section>

<section
  class="home-reviews"
  className="bg-blue-600 px-8 py-16 max-sm:py-2 max-sm:h-[510px] h-[730px] w-full relative translate-y-[830px] max-sm:translate-y-[650px] mt-[-16px] z-30 rounded-2xl"
>
  <div class="home-reviews__head" ...>...</div>
  <div class="home-reviews__slider">...
  </div>
</section>
```

- [ ] **Step 3: Remove old positional media query block**

Delete the old responsive block in `Home.vue` that starts from:

```css
@media screen and (max-width: 744px) {
  section:first-of-type { ... }
  section:nth-of-type(2) { ... }
  section:nth-of-type(4) { ... }
}

@media screen and (max-width: 640px) {
  section:first-of-type > div { ... }
  section:nth-of-type(2) { ... }
}
```

Do not leave any `section:nth-of-type(...)` responsive overrides in `Home.vue`.

- [ ] **Step 4: Run compilation check**

Run: `npm run build`

Expected: `vite build` completes successfully.

- [ ] **Step 5: Commit**

```bash
git add frontend/src/views/Home.vue
git commit -m "update home section hooks for stable responsive styling"
```

### Task 2: Implement Fluid 744->376 Responsive Layer in Home

**Files:**
- Modify: `frontend/src/views/Home.vue`
- Test: `frontend/src/views/Home.vue`

- [ ] **Step 1: Write the failing visual check for 560px and 430px**

Run: `npm run dev`

Manual check in browser devtools at 560px and 430px width:
- verify current layout still has jumps/over-tight spacing or unstable section rhythm.

Expected: visible instability before fluid rule set is added.

- [ ] **Step 2: Add fluid responsive rules for 744->376 in scoped CSS**

Append this media block in `Home.vue` (after `.priemka` definition):

```css
@media screen and (max-width: 744px) {
  .home-hero {
    height: clamp(38rem, 84vw, 52.625rem);
    padding-inline: clamp(1rem, 2.8vw, 2rem);
    padding-bottom: clamp(2rem, 5.5vw, 4rem);
  }

  .home-hero__content {
    margin-top: clamp(19.625rem, 63vw, 29.625rem);
    margin-inline: 0;
    padding-inline: clamp(1rem, 2.8vw, 2rem);
  }

  .home-hero :is(h1) {
    font-size: clamp(2.5rem, 7.1vw, 5rem);
    line-height: clamp(1.02, 1.1, 1.15);
    letter-spacing: clamp(-1.58px, -0.42vw, -3.17px);
  }

  .home-hero :is(p) {
    font-size: clamp(1rem, 2.15vw, 1.5rem);
    line-height: 1.45;
    margin-bottom: clamp(1.25rem, 3.2vw, 2rem);
  }

  .home-about,
  .home-services,
  .home-reviews {
    padding-inline: clamp(1rem, 2.8vw, 1.25rem);
    padding-top: clamp(2rem, 4.4vw, 3rem);
    padding-bottom: clamp(2rem, 5vw, 3.5rem);
  }

  .home-about__head {
    display: flex;
    flex-direction: column;
    gap: clamp(1.25rem, 2.6vw, 1.625rem);
  }

  .home-about__stats {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    padding-bottom: 0;
  }

  .home-about__stats > div {
    padding: clamp(1.25rem, 4vw, 2.1875rem) clamp(1.25rem, 3.6vw, 2rem);
  }

  .home-about__stats > div p:first-child {
    font-size: clamp(1.5rem, 5.1vw, 2.5rem);
    margin-bottom: clamp(0.5rem, 1.8vw, 1rem);
  }

  .home-about__stats > div p:last-child {
    font-size: clamp(0.95rem, 2.6vw, 1.25rem);
  }

  .home-services h2,
  .home-reviews h2 {
    font-size: clamp(1.75rem, 5vw, 3rem);
    line-height: 1.2;
    margin-bottom: clamp(1rem, 3vw, 2.5rem);
  }

  .home-services__promo {
    height: clamp(26rem, 73vw, 40.4375rem);
    padding: clamp(1rem, 3.2vw, 2rem);
    margin-bottom: clamp(1rem, 2.8vw, 2.5rem);
  }

  .home-services__promo h3 {
    font-size: clamp(1.75rem, 4.4vw, 2.5rem);
  }

  .home-services__promo p {
    font-size: clamp(1rem, 2.7vw, 1.25rem);
    line-height: 1.35;
    margin-bottom: clamp(1rem, 2.8vw, 2.25rem);
  }

  .home-services__grid {
    gap: clamp(0.625rem, 1.6vw, 1rem);
  }

  .home-reviews {
    height: auto;
    min-height: clamp(30rem, 76vw, 45.625rem);
  }

  .home-reviews__head {
    margin-bottom: clamp(0.75rem, 2.2vw, 1.5rem);
  }
}
```

- [ ] **Step 3: Keep locked visual constraints explicitly**

Ensure these lines remain unchanged in `Home.vue`:

```css
.priemka {
  background-image: url(../assets/images/schempomoch.png);
  background-size: cover;
  background-repeat: no-repeat;
}
```

And do not change review button colors in `SliderReviews.vue` (`bg-neutral-200`, `text-text-dark-primary`).

- [ ] **Step 4: Run build verification**

Run: `npm run build`

Expected: successful build with no SFC style errors.

- [ ] **Step 5: Commit**

```bash
git add frontend/src/views/Home.vue
git commit -m "update home responsive fluid range from 744 to 376"
```

### Task 3: Add Exact <=375 Mobile Rules for Home

**Files:**
- Modify: `frontend/src/views/Home.vue`
- Test: manual viewport check at 375px

- [ ] **Step 1: Write failing mobile check at 375px**

Run: `npm run dev`

Manual check at 375px:
- compare Home against `frontend-html-css/mobile375` references,
- record any mismatch in spacing rhythm, title scale, card spacing, or section clipping.

Expected: at least one mismatch before exact 375 overrides.

- [ ] **Step 2: Add exact 375-target overrides**

Add this block after the 744 media block:

```css
@media screen and (max-width: 375px) {
  .home-hero {
    height: 52.625rem;
    padding-inline: 1rem;
    padding-bottom: 2rem;
  }

  .home-hero__content {
    margin-top: 19.625rem;
    padding-inline: 0;
  }

  .home-hero :is(h1) {
    font-size: 2.5rem;
    line-height: 1.15;
    letter-spacing: -1.58px;
  }

  .home-hero :is(p) {
    font-size: 1rem;
    line-height: 1.35;
    margin-bottom: 1.25rem;
  }

  .home-about,
  .home-services,
  .home-reviews {
    padding-inline: 1rem;
    padding-top: 2rem;
    padding-bottom: 2rem;
  }

  .home-services__grid {
    grid-template-columns: 1fr;
    gap: 0.625rem;
  }

  .home-reviews {
    min-height: 31.875rem;
  }
}
```

- [ ] **Step 3: Verify 375 behavior and locked exceptions**

Manual checks at 375px:
- 3rd-section promo gradient remains desktop/744 style,
- review slider buttons keep existing desktop/744 colors,
- no horizontal overflow,
- all sections readable and stacked correctly.

Expected: mobile layout matches target intent with locked exceptions preserved.

- [ ] **Step 4: Run build verification**

Run: `npm run build`

Expected: successful build.

- [ ] **Step 5: Commit**

```bash
git add frontend/src/views/Home.vue
git commit -m "add exact 375 mobile rules for home page"
```

### Task 4: Stabilize Review Slider Only If Narrow-Width Overflow Remains

**Files:**
- Optional modify: `frontend/src/components/SliderReviews.vue`
- Test: manual slider behavior at 375/430/560/744

- [ ] **Step 1: Write failing check for slider stability**

Run: `npm run dev`

Manual checks on Home reviews block:
- cards do not overflow container,
- no clipped text,
- snap/scroll remains usable on mobile.

Expected: if instability exists, proceed with step 2. If stable, skip to step 4.

- [ ] **Step 2: Apply minimal CSS-only slider stabilization (if needed)**

In `SliderReviews.vue`, add only these safe constraints inside existing `@media (max-width: 744px)` block:

```css
.reviews-scroll {
  align-items: stretch;
}

.review-card--scroll {
  min-height: clamp(18rem, 50vw, 22rem);
}

.review-card__text {
  overflow-wrap: anywhere;
}
```

Do not change button color classes.

- [ ] **Step 3: Verify no color regression on slider buttons**

Confirm button classes remain:

```vue
class="flex items-center justify-center rounded-lg bg-neutral-200 ... text-text-dark-primary ..."
```

Expected: identical color behavior to desktop/744.

- [ ] **Step 4: Build verification**

Run: `npm run build`

Expected: successful build.

- [ ] **Step 5: Commit (only if SliderReviews.vue changed)**

```bash
git add frontend/src/components/SliderReviews.vue
git commit -m "update review slider stability for narrow home widths"
```

### Task 5: Final Verification Matrix and Regression Pass

**Files:**
- Modify (if needed): `frontend/src/views/Home.vue`
- Modify (if needed): `frontend/src/components/SliderReviews.vue`

- [ ] **Step 1: Run full build check**

Run: `npm run build`

Expected: `vite build` completes successfully.

- [ ] **Step 2: Run viewport verification matrix**

Run: `npm run dev`

Manual checks at widths:
- 375px
- 430px
- 560px
- 744px
- desktop (>744px)

Acceptance criteria:
- no horizontal scroll,
- no clipped/overlapping content,
- smooth visual transition from 744 to 375,
- 744 layout preserved,
- desktop layout preserved,
- 3rd-section gradient unchanged by mobile reference style,
- review slider button colors unchanged.

- [ ] **Step 3: Apply final micro-fixes if any check fails**

Use only minimal adjustments in `Home.vue`/`SliderReviews.vue` to satisfy failed criteria.

Example minimal fix pattern:

```css
.home-services__promo {
  min-height: clamp(25rem, 72vw, 40.4375rem);
}
```

- [ ] **Step 4: Re-run build and spot-check**

Run: `npm run build`

Expected: successful build after micro-fixes.

- [ ] **Step 5: Final commit**

```bash
git add frontend/src/views/Home.vue frontend/src/components/SliderReviews.vue
git commit -m "fix home mobile 375 and fluid responsive transition from 744"
```

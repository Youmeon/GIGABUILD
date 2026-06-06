# Home Mobile Responsive Design

**Goal:** Make the Home page adapt smoothly from 744px down to 375px without layout breaks, while preserving existing desktop and 744 behavior.

## Scope

- In scope:
  - `frontend/src/views/Home.vue` responsive behavior for all Home sections
  - Minimal, targeted adjustments in `frontend/src/components/SliderReviews.vue` only if required for stable behavior at narrow widths
- Out of scope:
  - Full component decomposition of Home into new Vue components
  - Visual redesign of desktop or 744 versions

## Constraints (Locked)

- Preserve existing project architecture and patterns.
- Keep desktop version unchanged.
- Keep 744 version behavior and visual style intact.
- Mobile target is 375px, but adaptation between 744 and 375 must be fluid.
- Do not copy the 3rd-section gradient from `frontend-html-css/mobile375`; keep gradient logic aligned with desktop/744.
- Keep review-banner slider button colors the same as desktop/744.

## Source References

- Primary implementation target: `frontend/src/views/Home.vue`
- Supporting reference files:
  - `frontend-html-css/mobile375/mobile-full-screen/*`
  - `frontend-html-css/mobile375/hero-section1/*`
  - `frontend-html-css/mobile375/section2/*`
  - `frontend-html-css/mobile375/section3-cards/*`
  - `frontend-html-css/mobile375/section4-banner-reviews/*`

## Technical Design

### 1. Stabilize Selectors and Remove Fragile Overrides

Current Home styles rely on `section:first-of-type` / `section:nth-of-type(...)` with `!important`. This is brittle and causes breakage in the 744->375 interval.

Design change:
- Add explicit section classes in `Home.vue` (hero/about/services/reviews) to replace positional selectors.
- Remove conflicting media rules that depend on section order and heavy `!important` overrides.
- Keep scoped CSS local to Home.

### 2. Responsive Strategy

Use three behavior zones:
- Desktop: `> 744px` (no visual changes intended)
- Fluid tablet-to-mobile transition: `376px - 744px`
- Exact mobile target: `<= 375px`

Implementation approach:
- Use `clamp()` for typography, spacing, section offsets, and container heights in the transition zone.
- Apply specific 375 overrides only where needed for fidelity and stability.
- Avoid abrupt breakpoint jumps unless there is a structural change (for example cards stacking).

### 3. Section-by-Section Behavior

#### Hero section
- Preserve existing desktop/744 hierarchy and composition.
- Fluidly scale heading/subheading sizes and top content offset from 744 down to 375.
- Ensure CTA remains full-width constrained and aligned on mobile.

#### "О компании" section
- Keep composition used by current 744 version.
- Replace rigid fixed values with fluid values for title, body text, spacing, and stat-card rhythm.
- Ensure cards stack cleanly and remain readable across intermediate widths.

#### "Услуги" section
- Keep visual direction from current implementation.
- Keep "Приемка квартир" gradient behavior consistent with desktop/744 (no replacement from mobile example).
- Ensure cards transition from multi-column to single-column without overlap or horizontal overflow.

#### "Отзывы" section
- Preserve existing button color scheme (desktop/744 style).
- Stabilize section height/padding so card content does not clip or overflow in 376-744 range.
- Only adjust `SliderReviews.vue` if needed to prevent width/height instability at narrow sizes.

## Files Planned for Change

- Modify: `frontend/src/views/Home.vue`
- Optional minimal modify: `frontend/src/components/SliderReviews.vue`

No new runtime dependencies.

## Validation Plan

- Manual viewport checks:
  - 375px
  - ~430px
  - ~560px
  - 744px
  - desktop (`>744px`)
- Verify no horizontal scrolling introduced by Home sections.
- Verify no content overlap/clipping in all four Home sections.
- Verify review-slider buttons keep existing color behavior.
- Build verification:
  - run `npm run build` in `frontend`

## Success Criteria

- Layout no longer breaks between 744 and 375.
- Mobile 375 behavior aligns with provided references except explicitly locked exceptions.
- Desktop and 744 remain visually consistent with current baseline.
- No regressions in Home section stacking, spacing, and readability.

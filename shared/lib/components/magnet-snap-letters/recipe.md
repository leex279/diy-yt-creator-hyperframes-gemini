# magnet-snap-letters — Recipe

Per-character fly-in with a magnetic spring snap. Letters start at random
offsets (seeded mulberry32, seed 0xFEED) and arrive at their rest position
with `back.out(2.5)` plus a scale micro-shudder on arrival.

## Slots

| Element         | Role                                             |
|-----------------|--------------------------------------------------|
| `.msl-char`     | Animated character spans (created by JS)         |
| `.msl-space`    | Non-animated space spans (static)                |

## Attributes

| Attribute        | Required | Purpose                                 |
|------------------|----------|-----------------------------------------|
| `data-snap-text` | Yes      | Source string; JS replaces innerHTML     |

## Dependencies

- GSAP 3.x on the page

## Gotchas

- Call `addMagnetSnapLetters()` exactly once per element. Repeated calls
  re-run `innerHTML` assignment, which works but resets any manually applied styles.
- Do NOT set `overflow: hidden` on the parent if any letter's start offset exceeds
  the parent's bounds — the fly-in paths will be clipped.
- Space characters are never animated and always visible; they contribute
  to word spacing naturally via `white-space: pre`.
- Changing `range` or the text string changes the visual scatter but the
  mulberry32 sequence stays reproducible — same `at` time always produces
  the same look.

## Wiring

```html
<!-- HTML: one line per text element -->
<span class="magnet-snap-letters" id="snap-title" data-snap-text="HYPERFRAMES">HYPERFRAMES</span>

<!-- After merging CSS and JS from component.html: -->
<script>
  // Reveal at P1 + 0.8, default 1.4s envelope, 25ms stagger between letters
  addMagnetSnapLetters(tl, "#snap-title", P1 + 0.8);

  // For a shorter word with more drama:
  addMagnetSnapLetters(tl, "#snap-title", P1 + 0.8, { stagger: 0.03, range: 400 });
</script>
```

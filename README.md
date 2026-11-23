<div align="center">

# GravitaPCB

**Gravity for your gerbers.**

Give it a circuit — JSON or a KiCad netlist — get back a fully routed,
DRC-clean, fab-ready board: Gerbers, drill file, BOM, pick-and-place,
and a 3D-printable STL enclosure. End to end, deterministic, no model
in the loop. Under 2 minutes, even on a 6-layer board.

### [**→ Try it at gravitapcb.mkechem.com**](https://gravitapcb.mkechem.com)

First board run is free. $49.99/credit after that — one credit per
successful build. A run that doesn't come back clean is refunded
automatically; you're never charged for output that didn't work.

</div>

---

## What it does

GravitaPCB turns a circuit description into everything you'd hand off
to a fab house:

- **Multi-layer boards** — not limited to 2-layer designs
- **Automatic component placement**
- **Auto-routing**, including BGA/fine-pitch via-in-pad escape routing
  for fully-enclosed balls
- **Real DRC gate** — a run isn't "done" until KiCad's own
  design-rule checker reports clean, not until a progress bar fills up
- **Copper pour / ground-plane zones**
- **Pick-and-place (CPL) output**
- **KiCad netlist import** — skip hand-typing component/pad data if
  you've already got one
- **STL mechanical enclosure** generation

No AI, no model making layout decisions — the pipeline is KiCad and
FreeRouting, driven end-to-end by deterministic code. If a board comes
back DRC clean, that's not a guess, it's a guarantee, and it'll come
back the same clean every time you run it again.

## How it works

1. Describe your circuit — `design.json` (components, pads, nets,
   layer count), or import a KiCad `.net` netlist straight from your
   schematic
2. GravitaPCB places components, auto-routes the board, pours ground
   planes, and runs a full DRC pass
3. You get back Gerbers, drill files, a BOM, pick-and-place data, the
   `.kicad_pcb` itself, and an STL enclosure — all in one job, viewable
   layer-by-layer right in the console before you download anything

## Why it exists

Hand-routing a board, especially anything with fine-pitch or BGA
parts, is slow and easy to get subtly wrong in ways that don't show up
until the boards come back from the fab. GravitaPCB exists to compress
that from hours (or a multi-day back-and-forth with a layout service)
down to about ninety seconds, with a real DRC check standing between
you and a bad batch of boards — not a replacement for knowing what
you're building, just for the grind of placing and routing it once
you do.

## Status

Previously shipped under the name **AutoPCB** — renamed to GravitaPCB
to avoid a name collision with an unrelated, pre-existing product in
the same industry. The tool itself hasn't changed; this is the same
pipeline, same feature set, under its real name.

## Support

`mkechem@yahoo.com` — failed runs are refunded automatically; email
for anything else.

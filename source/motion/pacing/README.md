# Pacing tools

Each beat-synced page reads `?sp=` (stretch, default 1.5) and, on the four-numbers edu page, `?hook=` (extra seconds before the hit, default 1.6).
The stretch lengthens the holds between beats. Transitions stay fixed in seconds, so moves stay snappy, and the background pulses stay on the real downbeats.

- `node dwell.js page.html [query]` measures how long each text block stays fully readable.
- `python3 report.py <prefix>` lists blocks below reading time. Reading time is max(1.0, 0.6 + 0.32 × words) seconds. Mid-count frames and disclaimers are skipped.
- `node durs.js page.html` prints the frame-rounded render length for `go.sh`.

# Way Home NYC

**AI reads posts, photos & official alerts, fact-checks them, and maps closures by trust level. When reports agree, routes home on foot update live. Unlike Waze: no app, any platform, city-verified.**

**Live demo:** https://claude.ai/artifact/HhPQ8ebmMaLTqQfuDRpGKU

Built in 45 minutes at a hackathon on incident and emergency response. The challenge: *"The Knicks are going to win a second championship in town, and people are hyped. Could official alerts, social media updates, and public reports help map street closures and plan alternate routes home?"*

## The problem

- **Closures are improvised.** NYPD closes streets as crowds move and decides each closure on the spot. No complete list exists ahead of time, and DOT's traffic advisories don't include emergency closures.
- **Information is scattered** across Notify NYC, MTA alerts, DOT advisories, 511NY, 311, X, Instagram, TikTok and Reddit. None of them answers "how do I get home?"
- **People are on foot**, on jammed cell networks. Driving apps don't see barricades or closed subway entrances.

## How it works

1. **Ingest.** Official feeds, public posts near the area or tagged with event keywords, 311 calls, DOT camera snapshots, and reports sent through the page.
2. **Understand.** An LLM turns each post or photo into a structured record: what happened, where (snapped to a real block by the city's geocoder), who it affects, and when.
3. **Verify.** Five checks on every post: time, place, media (recycled or AI-generated?), source (bot burst?) and corroboration.
4. **Fuse.** Records are grouped by block and 10-minute window. Each cluster gets one of three trust levels:
   - **Unverified:** shown on the map as a warning; routes don't change.
   - **Confirmed:** 3+ independent reports from 2+ platforms within 10 minutes; routes avoid it automatically.
   - **Official:** published by NYPD, DOT or MTA, or confirmed by an operator with one click; treated as a hard closure.
5. **Publish.** The map, walking routes to open station entrances, Notify NYC alerts, and an open closure feed (Waze CIFS and GeoJSON) for Waze, Google and Apple Maps.

Safety rule: crowd reports can only steer people *away* from a street. Dangerous claims (bomb threats, stampedes) are never published from social media; they go to NYPD and NYC Emergency Management to check.

## Why not just Waze?

Waze reroutes cars using taps from its own users. Way Home reroutes people walking, using any post, photo or video from any platform. It checks every report and gives the city the final say. It also feeds its confirmed closures into Waze, Google and Apple Maps.

## The prototype

The page has four tabs:

- **Pitch:** a 4-slide summary.
- **Get home:** what the public sees. Pick a destination, get a route on a real map of Midtown, tap any event to see its photo and sources, and report what you see. **▶ Play next 2 min** shows crowd reports rerouting a Brooklyn-bound fan automatically.
- **Operator:** the review queue for NYC Emergency Management. Clusters show what the AI read, the five checks and a confidence score, with Confirm and Dismiss buttons. The Live intake panel sends any post or photo to Claude for extraction and verification.
- **Plan:** data sources, verification, scaling, run of show and privacy.

The live AI features use the artifact runtime's `sample` capability, so they work at the artifact link above. Opened anywhere else, the example posts show saved AI results.

All incident data is demo data built around the June 2026 win night. The photos and the real events on the map (the 10th Ave street party in Hell's Kitchen, police activity at 42nd & Broadway) come from coverage of that night.

## Files

| Path | What it is |
|---|---|
| `index.html` | Standalone page; open it locally or serve it with GitHub Pages |
| `wayhome.html` | The same page without the document skeleton, as published to the artifact |
| `src/wayhome.src.html` | Source template |
| `src/build.py` | Inlines Leaflet CSS, street-grid coordinates and map bounds; writes both HTML files |
| `src/grid.json` | Midtown avenue × street intersection coordinates, from OpenStreetMap |
| `map/` | Pre-stitched OpenStreetMap and Esri satellite images, zoom 15–17 |
| `photos/` | Photos used in the demo (credits below) |

Rebuild with `python3 src/build.py`.

## Credits

**Photos** (Wikimedia Commons, details in `src/photo-credits.json`):

- `crowd-7av-31st.jpg`: Demetri Andriani, CC BY-SA 4.0
- `crowd-7av-31st-b.jpg` and `crowd-6av-32nd.jpg`: Tzim78, CC BY-SA 4.0
- `ace-8av-34th.jpg`: Marc A. Hermann / MTA, CC BY 4.0
- `cityhall-ceremony.jpg`: 2026 Knicks City Hall Ceremony, CC BY 4.0

**Map data:** © OpenStreetMap contributors (ODbL). **Satellite imagery:** © Esri, Maxar, Earthstar Geographics. **Map library:** [Leaflet](https://leafletjs.com) 1.9.4.

**Data sources referenced in the plan:** NYC DOT Special / Weekday / Weekend Traffic Updates on NYC Open Data (`t4s6-khpm`, `vihk-m25f`, `qhen-5rve`), MTA GTFS-realtime alerts, 511NY, Notify NYC, 311, NYC DOT traffic cameras, NYC Geoclient / LION.

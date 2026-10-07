import json,re,os
d=os.path.dirname(os.path.abspath(__file__))
src=open(f'{d}/wayhome.src.html').read()
plan=open(f'{d}/plan.html').read()
plan=plan.replace('</section>','''  <p class="small">Photos are real and freely licensed, from Wikimedia Commons: Demetri Andriani and Tzim78 (CC BY-SA 4.0), Marc A. Hermann / MTA (CC BY 4.0), City Hall ceremony (CC BY 4.0). They show the June 2026 Finals crowds at the same corners and are used here as demo inputs. Map data © OpenStreetMap contributors (ODbL). Satellite imagery © Esri, Maxar, Earthstar Geographics.</p>
</section>''')
grid={k:v for k,v in json.load(open(f'{d}/grid.json')).items()}
out=(src.replace('/*LEAFLET_CSS*/',open(f'{d}/leaflet-1.9.4.min.css').read())
  .replace('<!--PLAN-->',plan)
  .replace('/*GRID*/',json.dumps(grid,separators=(',',':')))
  .replace('/*BOUNDS*/',open(f'{d}/bounds.json').read()))
open(f'{d}/../wayhome.html','w').write(out);print(len(out))
# Standalone copy for GitHub Pages / opening locally (the artifact host adds this skeleton itself)
open(f'{d}/../index.html','w').write('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"></head><body>'+out+'</body></html>')

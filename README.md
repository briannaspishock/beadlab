# beadlab
the retro-futuristic workbench of casual beading

### prerequisites

- python 3.8+
- desktop browser

### installation

1. **clone the repository**
```bash
   git clone [https://github.com/briannaspishock/beadlab.git](https://github.com/briannaspishock/beadlab.git)
   cd beadlab
```
2. **install dependencies**
``` bash
  pip install streamlit
```
3. **launch**
``` bash
streamlit run app.py
```

### how it works
inject slide: upload reference photo using inject photo
key bg: select the pick bg wand tool and click on unwanted backdrop space to set a transparency key, then adjust the knockout tolerance slider
configure topology: pick your stitch type (loom, peyote even, or peyote odd) and set your target column and row bounds
synthesize: hit synthesize beads to extract, average, and snap the underlying image to calibrated Miyuki Delica codes
touch up & export: use the pipette, brush, or bucket tools to refine key details, export a print-ready PDF pattern with print PDF + key



### built with
streamlit: application wrapper and layout host
HTML5 canvas & vanilla JS: interactive pixel manipulation and drawing surface
jsPDF: vector pattern generation and palette reporting
Google fonts: JetBrains Mono and Space Grotesk

### pics
<img width="1466" height="854" alt="Screenshot 2026-09-09 at 8 37 25 AM" src="https://github.com/user-attachments/assets/9b0cc192-4dd1-475b-ae02-6555946d3363" />

<img width="1482" height="820" alt="Screenshot 2026-09-09 at 8 37 49 AM" src="https://github.com/user-attachments/assets/b9a08faa-e3db-45b3-907f-2bc626173afd" />

<img width="1493" height="824" alt="Screenshot 2026-09-09 at 8 38 00 AM" src="https://github.com/user-attachments/assets/cfca6759-197c-4bb8-9212-736d201221a1" />






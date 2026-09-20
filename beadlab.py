import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="BeadLab by @briannaspishock",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {
        padding-top: 0.5rem;
        padding-bottom: 0rem;
        padding-left: 1rem;
        padding-right: 1rem;
        max-width: 100% !important;
    }
</style>
""",
    unsafe_allow_html=True,
)

beadlab_html = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<title>BeadLab - @briannaspishock</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet">
<style>
  :root {
    --bench-bg: #0b0f14;
    --terminal-card: #121820;
    --border-line: #1f2a38;
    --hud-cyan: #00f2fe;
    --hud-green: #39ff14;
    --hud-amber: #ffb703;
    --hud-pink: #ff007f;
    --text-main: #d1e4f0;
    --text-dim: #5a738e;
  }

  * { box-sizing: border-box; user-select: none; }
  body {
    margin: 0; padding: 0;
    font-family: 'JetBrains Mono', monospace;
    background: var(--bench-bg); color: var(--text-main);
    display: flex; flex-direction: column; height: 100vh; overflow: hidden;
  }

  .lab-hud {
    background: var(--terminal-card); border-bottom: 2px solid var(--border-line);
    padding: 8px 18px; display: flex; align-items: center; justify-content: space-between;
    box-shadow: 0 4px 20px rgba(0, 242, 254, 0.05);
  }
  .brand-lab {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 16px; font-weight: 700; letter-spacing: -0.5px;
    display: flex; align-items: center; gap: 8px; color: var(--hud-cyan);
    text-shadow: 0 0 12px rgba(0, 242, 254, 0.35);
  }
  .brand-lab span { color: #fff; }
  .tagline {
    font-size: 10px; color: var(--hud-pink); font-family: 'JetBrains Mono', monospace;
    letter-spacing: 0px; font-weight: 400; margin-left: 6px;
  }

  .hud-actions {
    display: flex; align-items: center; gap: 8px;
  }

  button, .lab-upload {
    background: #17212d; color: var(--text-main); border: 1px solid var(--border-line);
    padding: 6px 12px; border-radius: 4px; font-size: 11px; font-weight: 600;
    cursor: pointer; display: inline-flex; align-items: center; gap: 6px;
    font-family: 'JetBrains Mono', monospace; text-transform: uppercase;
    transition: all 0.15s ease;
  }
  button:hover, .lab-upload:hover {
    border-color: var(--hud-cyan); color: #fff;
    box-shadow: 0 0 8px rgba(0, 242, 254, 0.2);
  }
  button.glow-btn {
    background: rgba(0, 242, 254, 0.15); border-color: var(--hud-cyan); color: var(--hud-cyan);
  }
  button.glow-btn:hover {
    background: var(--hud-cyan); color: #000;
  }
  button.danger-btn:hover {
    border-color: var(--hud-pink); color: var(--hud-pink);
  }

  select, input[type="number"], input[type="text"] {
    background: #0f151c; color: var(--hud-cyan); border: 1px solid var(--border-line);
    padding: 5px 8px; border-radius: 4px; font-size: 11px;
    font-family: 'JetBrains Mono', monospace; outline: none;
  }

  .workbench {
    display: flex; flex: 1; overflow: hidden;
  }

  .instrument-rack {
    width: 68px; background: var(--terminal-card); border-right: 1px solid var(--border-line);
    display: flex; flex-direction: column; align-items: center; padding: 14px 0; gap: 8px;
  }
  .rack-btn {
    width: 48px; height: 48px; border-radius: 6px; padding: 0;
    display: flex; flex-direction: column; align-items: center; justify-content: center;
    font-size: 15px; border: 1px solid var(--border-line); background: #151d27;
  }
  .rack-btn span.label {
    font-size: 7.5px; margin-top: 2px; color: var(--text-dim); text-transform: uppercase;
  }
  .rack-btn.active {
    border-color: var(--hud-cyan); background: rgba(0, 242, 254, 0.12);
    box-shadow: inset 0 0 8px rgba(0, 242, 254, 0.3);
  }
  .rack-btn.active span.label { color: var(--hud-cyan); }

  .specimen-viewport {
    flex: 1; background: #0c0f12;
    display: flex; align-items: center; justify-content: center;
    overflow: auto; padding: 30px; position: relative;
    touch-action: none;
  }
  .slide-mount {
    box-shadow: 0 15px 45px rgba(0,0,0,0.9), 0 0 0 1px #222;
    border-radius: 2px; background: #ffffff; position: relative;
  }
  canvas { display: block; background: #ffffff; }

  .diagnostic-bay {
    width: 340px; background: var(--terminal-card); border-left: 1px solid var(--border-line);
    display: flex; flex-direction: column; padding: 14px; gap: 10px; overflow-y: auto;
  }
  .terminal-box {
    background: #0d1218; border: 1px solid var(--border-line); border-radius: 4px; padding: 9px;
    display: flex; flex-direction: column; gap: 6px;
  }
  .terminal-header {
    font-size: 10px; font-weight: 700; color: var(--hud-cyan);
    letter-spacing: 1px; display: flex; align-items: center; justify-content: space-between;
  }

  .delica-scroll-tray {
    display: grid; grid-template-columns: repeat(4, 1fr); gap: 5px;
    max-height: 160px; overflow-y: auto; padding-right: 4px;
  }
  .vial {
    aspect-ratio: 1; border-radius: 4px; cursor: pointer; position: relative;
    border: 1px solid rgba(255,255,255,0.2); transition: transform 0.1s ease;
    display: flex; align-items: flex-end; justify-content: center; padding: 2px;
  }
  .vial span {
    font-size: 7.5px; font-weight: 600; background: rgba(0,0,0,0.8); color: #fff; padding: 1px 2px; border-radius: 2px;
  }
  .vial:hover { transform: scale(1.08); }
  .vial.active-reagent {
    border-color: #fff; box-shadow: 0 0 10px var(--hud-cyan);
  }

  .sensor-slider {
    display: flex; flex-direction: column; gap: 3px; font-size: 10px; color: var(--text-dim);
  }
  input[type="range"] { accent-color: var(--hud-cyan); }
</style>
</head>
<body>

<div class="lab-hud">
  <div class="brand-lab">
    🧪 BEAD<span>LAB</span>
    <span class="tagline">by @briannaspishock</span>
  </div>

  <div class="hud-actions">
    <label class="lab-upload">
      🔬 Inject Photo
      <input type="file" id="imageInput" accept="image/*" style="display:none;" />
    </label>
    <button id="ejectPhotoBtn">🗑️ Eject Slide</button>
    <button class="glow-btn" id="transferBtn">⚡ Synthesize Beads</button>
    <button id="invertBtn">🌓 Invert</button>
    <button id="hideUnderlayBtn">👁️ <span id="hideText">Hide Slide</span></button>
  </div>

  <div class="hud-actions">
    <button class="danger-btn" id="clearAllBtn">☢️ Clear All</button>
    <button class="glow-btn" id="exportPdfBtn">📋 Print PDF + Key</button>
  </div>
</div>

<div class="workbench">
  <div class="instrument-rack">
    <button class="rack-btn active" id="tool-pan" title="Drag & Move Photo"><span style="font-size:17px;">✋</span><span class="label">Move Pic</span></button>
    <button class="rack-btn" id="tool-wand" title="Magic Wand: Click on photo to pick background color to remove"><span style="font-size:17px;">🪄</span><span class="label">Pick BG</span></button>
    <button class="rack-btn" id="tool-paint" title="Brush"><span style="font-size:17px;">🖌️</span><span class="label">Brush</span></button>
    <button class="rack-btn" id="tool-fill" title="Flood Bucket"><span style="font-size:17px;">🪣</span><span class="label">Flood</span></button>
    <button class="rack-btn" id="tool-erase" title="Eraser"><span style="font-size:17px;">🧼</span><span class="label">Erase</span></button>
    <button class="rack-btn" id="tool-eyedropper" title="Sample Bead"><span style="font-size:17px;">🧪</span><span class="label">Pipette</span></button>
  </div>

  <div class="specimen-viewport" id="viewport">
    <div class="slide-mount">
      <canvas id="beadCanvas"></canvas>
    </div>
  </div>

  <div class="diagnostic-bay">
    <div class="terminal-box">
      <div class="terminal-header"><span>[BACKGROUND REMOVAL]</span></div>
      <div class="sensor-slider">
        <div style="display:flex; justify-content:space-between; align-items:center;">
          <span>KNOCKOUT TOLERANCE</span>
          <span id="bgTolVal" style="color:var(--hud-cyan)">0</span>
        </div>
        <input type="range" id="bgToleranceSlider" min="0" max="150" step="2" value="0">
      </div>
      <div style="display:flex; align-items:center; gap:8px; margin-top:2px;">
        <div id="bgSampleSwatch" style="width:16px; height:16px; border:1px solid #777; border-radius:3px; background:#fff;"></div>
        <span style="font-size:9px; color:var(--text-dim);">Sampled: <b id="bgSampleHex">None (White)</b></span>
      </div>
    </div>

    <div class="terminal-box">
      <div class="terminal-header"><span>[STITCH TOPOLOGY]</span></div>
      <select id="stitchSelect">
        <option value="loom">Loom Grid (Orthogonal)</option>
        <option value="peyote_even">Even-Count Peyote (Hex Offset)</option>
        <option value="peyote_odd">Odd-Count Peyote (Hex Offset)</option>
      </select>
    </div>

    <div class="terminal-box">
      <div class="terminal-header"><span>[MIYUKI CALIBRATION]</span></div>
      <select id="beadProfileSelect">
        <option value="delica_11">Delica 11/0 (1.6 x 1.3 mm)</option>
        <option value="delica_10">Delica 10/0 (2.2 x 1.7 mm)</option>
        <option value="round_11">Seed Round 11/0 (2.0 x 1.3 mm)</option>
        <option value="round_8">Seed Round 8/0 (3.0 x 2.1 mm)</option>
        <option value="round_6">Seed Round 6/0 (4.0 x 2.8 mm)</option>
        <option value="square_exact">Isotropic Matrix (1:1 Square)</option>
      </select>
    </div>

    <div class="terminal-box">
      <div class="terminal-header"><span>[MATRIX DIMENSIONS]</span></div>
      <div style="display: flex; gap: 8px;">
        <input type="number" id="colsInput" value="22" min="2" max="120" style="width:50%" title="Columns">
        <input type="number" id="rowsInput" value="48" min="2" max="200" style="width:50%" title="Rows">
      </div>
      <div style="font-size:10px; color:var(--hud-cyan);" id="dimTag">22 W × 48 H • 1,056 BEADS</div>
    </div>

    <div class="terminal-box">
      <div class="terminal-header"><span>[SYNTHESIS ENGINE]</span></div>
      <div class="sensor-slider">
        <span id="paletteLimitLabel">MAX PALETTE CLUSTERS: 12 COLORS</span>
        <input type="range" id="paletteLimitSlider" min="3" max="32" step="1" value="12">
      </div>
      <div class="sensor-slider">
        <span>PHOTO CONTRAST BOOSTER</span>
        <input type="range" id="contrastSlider" min="0.8" max="2.0" step="0.1" value="1.2">
      </div>
    </div>

    <div class="terminal-box">
      <div class="terminal-header"><span>[SLIDE OPTICS]</span></div>
      <div class="sensor-slider">
        <span>MAGNIFICATION</span>
        <input type="range" id="scaleSlider" min="0.05" max="3" step="0.02" value="1">
      </div>
      <div class="sensor-slider">
        <span>PHOTO OPACITY</span>
        <input type="range" id="opacitySlider" min="0.05" max="1" step="0.05" value="0.7">
      </div>
    </div>

    <div class="terminal-box" style="flex:1;">
      <div class="terminal-header">
        <span>[DELICA DATABASE]</span>
        <span id="activeDbCode" style="color:var(--hud-amber)">DB0200</span>
      </div>
      <div style="font-size:10px; color:var(--text-dim); margin-bottom:4px;" id="activeDbName">White Opaque</div>

      <div style="display:flex; gap:4px; margin-bottom:6px;">
        <select id="paletteCategoryFilter" style="width:60%; font-size:10px; padding:3px;">
          <option value="all">All (150+ Codes)</option>
          <option value="neutrals">Neutrals</option>
          <option value="reds_pinks">Reds/pinks</option>
          <option value="blues_teals">Blues/teals</option>
          <option value="greens">Greens & Olives</option>
          <option value="purples_golds">Purples/golds</option>
        </select>
        <input type="text" id="paletteSearch" placeholder="Search..." style="width:40%; font-size:10px; padding:3px;">
      </div>

      <div class="delica-scroll-tray" id="palette"></div>
    </div>
  </div>
</div>

<script>
const MIYUKI_DELICAS = [
  { code: 'DB0200', name: 'White Opaque', hex: '#FFFFFF', r: 255, g: 255, b: 255, cat: 'neutrals' },
  { code: 'DB0351', name: 'Matte Cream Opaque', hex: '#F9F5EC', r: 249, g: 245, b: 236, cat: 'neutrals' },
  { code: 'DB0732', name: 'Cream Opaque', hex: '#F3E8DC', r: 243, g: 232, b: 220, cat: 'neutrals' },
  { code: 'DB0204', name: 'Ceylon Ivory', hex: '#EBE1D0', r: 235, g: 225, b: 208, cat: 'neutrals' },
  { code: 'DB1490', name: 'Opaque Marshmallow', hex: '#EFEAE1', r: 239, g: 234, b: 225, cat: 'neutrals' },
  { code: 'DB0731', name: 'Butter Opaque', hex: '#FDF0A6', r: 253, g: 240, b: 166, cat: 'neutrals' },
  { code: 'DB0210', name: 'Opaque Custard', hex: '#F7E7B4', r: 247, g: 231, b: 180, cat: 'neutrals' },
  { code: 'DB0352', name: 'Matte Pale Cream', hex: '#E7DEC8', r: 231, g: 222, b: 200, cat: 'neutrals' },
  { code: 'DB1133', name: 'Opaque Biscuit', hex: '#D7BC98', r: 215, g: 188, b: 152, cat: 'neutrals' },
  { code: 'DB0221', name: 'White Opal Luster', hex: '#F0ECE1', r: 240, g: 236, b: 225, cat: 'neutrals' },

  { code: 'DB1134', name: 'Opaque Caramel', hex: '#C2935D', r: 194, g: 147, b: 93, cat: 'neutrals' },
  { code: 'DB0791', name: 'Dyed Matte Sienna', hex: '#A85A32', r: 168, g: 90, b: 50, cat: 'neutrals' },
  { code: 'DB0796', name: 'Matte Brown Earth', hex: '#6F4E37', r: 111, g: 78, b: 55, cat: 'neutrals' },
  { code: 'DB0310', name: 'Matte Dark Espresso', hex: '#3B271D', r: 59, g: 39, b: 29, cat: 'neutrals' },
  { code: 'DB0728', name: 'Opaque Dark Terra Cotta', hex: '#8B4513', r: 139, g: 69, b: 19, cat: 'neutrals' },
  { code: 'DB1518', name: 'Opaque Chestnut', hex: '#582F1E', r: 88, g: 47, b: 30, cat: 'neutrals' },
  { code: 'DB1520', name: 'Matte Sand Almond', hex: '#CBB296', r: 203, g: 178, b: 150, cat: 'neutrals' },
  { code: 'DB1522', name: 'Opaque Khaki Brown', hex: '#8A6E53', r: 138, g: 110, b: 83, cat: 'neutrals' },
  { code: 'DB0735', name: 'Opaque Hazelnut', hex: '#9E7453', r: 158, g: 116, b: 83, cat: 'neutrals' },
  { code: 'DB0734', name: 'Opaque Dark Sand', hex: '#A88B6E', r: 168, g: 139, b: 110, cat: 'neutrals' },

  { code: 'DB0041', name: 'Silver Lined Crystal', hex: '#E2E8F0', r: 226, g: 232, b: 240, cat: 'neutrals' },
  { code: 'DB0050', name: 'Crystal Luster', hex: '#CBD5E1', r: 203, g: 213, b: 225, cat: 'neutrals' },
  { code: 'DB0794', name: 'Matte Grey Opaque', hex: '#7C8BA1', r: 124, g: 139, b: 161, cat: 'neutrals' },
  { code: 'DB0306', name: 'Matte Charcoal Grey', hex: '#475569', r: 71, g: 85, b: 105, cat: 'neutrals' },
  { code: 'DB0733', name: 'Opaque Light Slate Grey', hex: '#94A3B8', r: 148, g: 163, b: 184, cat: 'neutrals' },
  { code: 'DB0010', name: 'Black Opaque', hex: '#121214', r: 18, g: 18, b: 20, cat: 'neutrals' },
  { code: 'DB0310B', name: 'Matte Black Opaque', hex: '#222226', r: 34, g: 34, b: 38, cat: 'neutrals' },
  { code: 'DB0022', name: 'Metallic Dark Gunmetal', hex: '#2D3748', r: 45, g: 55, b: 72, cat: 'neutrals' },

  { code: 'DB0042', name: 'Silver Lined Gold', hex: '#D4AF37', r: 212, g: 175, b: 55, cat: 'purples_golds' },
  { code: 'DB0031', name: '24Kt Gold Plated', hex: '#E5C158', r: 229, g: 193, b: 88, cat: 'purples_golds' },
  { code: 'DB0027', name: 'Metallic Dark Bronze', hex: '#634E3A', r: 99, g: 78, b: 58, cat: 'purples_golds' },
  { code: 'DB0024', name: 'Metallic Iris Blue-Green', hex: '#2C4A52', r: 44, g: 74, b: 82, cat: 'purples_golds' },
  { code: 'DB0026', name: 'Metallic Dark Copper', hex: '#874B28', r: 135, g: 75, b: 40, cat: 'purples_golds' },
  { code: 'DB0034', name: 'Galvanized Silver', hex: '#C0C0C0', r: 192, g: 192, b: 192, cat: 'neutrals' },
  { code: 'DB1832', name: 'Duracoat Galvanized Gold', hex: '#D9B24C', r: 217, g: 178, b: 76, cat: 'purples_golds' },

  { code: 'DB0721', name: 'Red Opaque', hex: '#C62828', r: 198, g: 40, b: 40, cat: 'reds_pinks' },
  { code: 'DB0652', name: 'Dyed Rose Cerise', hex: '#D81B60', r: 216, g: 27, b: 96, cat: 'reds_pinks' },
  { code: 'DB0651', name: 'Dyed Salmon Silk', hex: '#FA8072', r: 250, g: 128, b: 114, cat: 'reds_pinks' },
  { code: 'DB0722', name: 'Orange Opaque', hex: '#E65100', r: 230, g: 81, b: 0, cat: 'reds_pinks' },
  { code: 'DB0741', name: 'Opaque Vermillion Red', hex: '#E53935', r: 229, g: 57, b: 53, cat: 'reds_pinks' },
  { code: 'DB0744', name: 'Opaque Peach Luster', hex: '#F8B195', r: 248, g: 177, b: 149, cat: 'reds_pinks' },
  { code: 'DB1342', name: 'Dyed Rose Magenta', hex: '#E91E63', r: 233, g: 30, b: 99, cat: 'reds_pinks' },
  { code: 'DB1371', name: 'Dyed Opaque Hot Pink', hex: '#FF4081', r: 255, g: 64, b: 129, cat: 'reds_pinks' },
  { code: 'DB1376', name: 'Dyed Blush Coral', hex: '#F08080', r: 240, g: 128, b: 128, cat: 'reds_pinks' },
  { code: 'DB0797', name: 'Matte Cranberry', hex: '#880E4F', r: 136, g: 14, b: 79, cat: 'reds_pinks' },
  { code: 'DB1503', name: 'Opaque Watermelon', hex: '#EF5350', r: 239, g: 83, b: 80, cat: 'reds_pinks' },
  { code: 'DB0724', name: 'Yellow Opaque', hex: '#F5C518', r: 245, g: 197, b: 24, cat: 'purples_golds' },
  { code: 'DB1501', name: 'Opaque Sunflower Yellow', hex: '#FFB300', r: 255, g: 179, b: 0, cat: 'purples_golds' },

  { code: 'DB0655', name: 'Dyed Plum Opaque', hex: '#6A1B9A', r: 106, g: 27, b: 154, cat: 'purples_golds' },
  { code: 'DB0654', name: 'Dyed Violet Silk', hex: '#5E35B1', r: 94, g: 53, b: 177, cat: 'purples_golds' },
  { code: 'DB0656', name: 'Dyed Lilac Opaque', hex: '#BA68C8', r: 186, g: 104, b: 200, cat: 'purples_golds' },
  { code: 'DB1377', name: 'Dyed Mauve Velvet', hex: '#9C27B0', r: 156, g: 39, b: 176, cat: 'purples_golds' },
  { code: 'DB1374', name: 'Dyed Lavender Pastel', hex: '#CE93D8', r: 206, g: 147, b: 216, cat: 'purples_golds' },
  { code: 'DB0730', name: 'Opaque Dark Eggplant', hex: '#4A148C', r: 74, g: 20, b: 140, cat: 'purples_golds' },
  { code: 'DB0798', name: 'Matte Deep Wine', hex: '#4A0E2E', r: 74, g: 14, b: 46, cat: 'purples_golds' },

  { code: 'DB0726', name: 'Cobalt Opaque', hex: '#1565C0', r: 21, g: 101, b: 192, cat: 'blues_teals' },
  { code: 'DB0723', name: 'Cobalt Luster', hex: '#1A237E', r: 26, g: 35, b: 126, cat: 'blues_teals' },
  { code: 'DB0727', name: 'Teal Opaque', hex: '#00838F', r: 0, g: 131, b: 143, cat: 'blues_teals' },
  { code: 'DB0729', name: 'Turquoise Green Opaque', hex: '#00897B', r: 0, g: 137, b: 123, cat: 'blues_teals' },
  { code: 'DB0659', name: 'Sky Blue Opaque', hex: '#29B6F6', r: 41, g: 182, b: 246, cat: 'blues_teals' },
  { code: 'DB0756', name: 'Opaque Turquoise Blue', hex: '#00ACC1', r: 0, g: 172, b: 193, cat: 'blues_teals' },
  { code: 'DB0793', name: 'Matte Dark Navy', hex: '#0D1B2A', r: 13, g: 27, b: 42, cat: 'blues_teals' },
  { code: 'DB1497', name: 'Opaque Light Robin Egg', hex: '#80DEEA', r: 128, g: 222, b: 234, cat: 'blues_teals' },
  { code: 'DB0725', name: 'Opaque Blue Luster', hex: '#1E88E5', r: 30, g: 136, b: 229, cat: 'blues_teals' },
  { code: 'DB0755', name: 'Opaque Denim Blue', hex: '#3949AB', r: 57, g: 73, b: 171, cat: 'blues_teals' },

  { code: 'DB0653', name: 'Dyed Kelly Green', hex: '#2E7D32', r: 46, g: 125, b: 50, cat: 'greens' },
  { code: 'DB0658', name: 'Olive Green Luster', hex: '#558B2F', r: 85, g: 139, b: 47, cat: 'greens' },
  { code: 'DB0737', name: 'Opaque Mint Jade', hex: '#81C784', r: 129, g: 199, b: 132, cat: 'greens' },
  { code: 'DB0738', name: 'Opaque Forest Green', hex: '#1B5E20', r: 27, g: 94, b: 32, cat: 'greens' },
  { code: 'DB0792', name: 'Matte Moss Olive', hex: '#33691E', r: 51, g: 105, b: 30, cat: 'greens' },
  { code: 'DB1516', name: 'Opaque Chartreuse Lime', hex: '#9E9D24', r: 158, g: 157, b: 36, cat: 'greens' },
  { code: 'DB1512', name: 'Opaque Pale Sage', hex: '#A5D6A7', r: 165, g: 214, b: 167, cat: 'greens' },
  { code: 'DB0657', name: 'Dyed Apple Green', hex: '#7CB342', r: 124, g: 179, b: 66, cat: 'greens' },
  { code: 'DB0778', name: 'Dyed Semi-Matte Hunter', hex: '#004D40', r: 0, g: 77, b: 64, cat: 'greens' }
];

const beadRatios = {
  delica_11: { w: 16, h: 13 },
  delica_10: { w: 17, h: 13.1 },
  round_11:  { w: 16, h: 10.4 },
  round_8:   { w: 18, h: 12.6 },
  round_6:   { w: 20, h: 14.0 },
  square_exact: { w: 15, h: 15 }
};

let currentBeadProfile = 'delica_11';
let stitchMode = 'loom';
let cols = 22;
let rows = 48;

let currentTool = 'pan';
let activeDelica = MIYUKI_DELICAS[0];
let showUnderlay = true;

// ko bg key state
let bgKeyColor = { r: 255, g: 255, b: 255 };
let bgTolerance = 0;

let grid = Array(rows).fill(null).map(() => Array(cols).fill(null));

let img = null;
let imgX = 0, imgY = 0, imgScale = 1;
let isInteracting = false;
let startDragX = 0, startDragY = 0;

const canvas = document.getElementById('beadCanvas');
const ctx = canvas.getContext('2d');

function getCellMetrics() {
  return beadRatios[currentBeadProfile];
}

function getBeadCoords(c, r) {
  const { w, h } = getCellMetrics();
  const x = c * w;
  let y = r * h;

  if (stitchMode.startsWith('peyote') && c % 2 === 1) {
    y += h / 2;
  }
  return { x, y, w, h };
}

function updateCanvasSize() {
  const { w, h } = getCellMetrics();
  const isPeyote = stitchMode.startsWith('peyote');
  
  canvas.width = cols * w + (isPeyote ? w * 0.2 : 0);
  canvas.height = rows * h + (isPeyote ? h * 0.5 : 0);

  const totalBeads = (cols * rows).toLocaleString();
  document.getElementById('dimTag').innerText = `${cols} W × ${rows} H • ${totalBeads} BEADS`;
  render();
}

// process underlay image with background knockout
function getProcessedImageCanvas() {
  if (!img) return null;
  const off = document.createElement('canvas');
  off.width = Math.max(1, Math.floor(img.width * imgScale));
  off.height = Math.max(1, Math.floor(img.height * imgScale));
  const oCtx = off.getContext('2d');

  const contrast = parseFloat(document.getElementById('contrastSlider').value);
  oCtx.filter = `contrast(${contrast})`;
  oCtx.drawImage(img, 0, 0, off.width, off.height);

  if (bgTolerance > 0) {
    const imgData = oCtx.getImageData(0, 0, off.width, off.height);
    const data = imgData.data;
    for (let i = 0; i < data.length; i += 4) {
      const dr = data[i] - bgKeyColor.r;
      const dg = data[i + 1] - bgKeyColor.g;
      const db = data[i + 2] - bgKeyColor.b;
      const dist = Math.sqrt(dr * dr + dg * dg + db * db);

      if (dist <= bgTolerance) {
        data[i + 3] = 0; // ko bg to transparent
      }
    }
    oCtx.putImageData(imgData, 0, 0);
  }
  return off;
}

function render() {
  ctx.fillStyle = "#ffffff";
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  if (img && showUnderlay) {
    const processed = getProcessedImageCanvas();
    if (processed) {
      ctx.save();
      ctx.globalAlpha = parseFloat(document.getElementById('opacitySlider').value);
      ctx.drawImage(processed, imgX, imgY);
      ctx.restore();
    }
  }

  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      const { x, y, w, h } = getBeadCoords(c, r);
      const bead = grid[r][c];

      if (bead) {
        ctx.fillStyle = bead.hex;
        ctx.fillRect(x, y, w, h);
      }

      ctx.strokeStyle = bead ? 'rgba(0, 0, 0, 0.2)' : 'rgba(0, 0, 0, 0.12)';
      ctx.lineWidth = 1;
      ctx.strokeRect(x, y, w, h);
    }
  }
}

//redmean formula
function getPerceptualDistance(r1, g1, b1, r2, g2, b2) {
  const rmean = (r1 + r2) / 2;
  const dr = r1 - r2;
  const dg = g1 - g2;
  const db = b1 - b2;
  return Math.sqrt((((512 + rmean) * dr * dr) >> 8) + (4 * dg * dg) + (((767 - rmean) * db * db) >> 8));
}

function findClosestDelica(r, g, b, candidateList = MIYUKI_DELICAS) {
  let closest = candidateList[0];
  let minDistance = Infinity;

  for (const delica of candidateList) {
    const dist = getPerceptualDistance(r, g, b, delica.r, delica.g, delica.b);
    if (dist < minDistance) {
      minDistance = dist;
      closest = delica;
    }
  }
  return closest;
}

// bg removal tolerance slider
document.getElementById('bgToleranceSlider').addEventListener('input', (e) => {
  bgTolerance = parseInt(e.target.value);
  document.getElementById('bgTolVal').innerText = bgTolerance;
  render();
});

document.getElementById('transferBtn').addEventListener('click', () => {
  if (!img) return alert("Please inject a slide photo first!");

  const sampleCanvas = document.createElement('canvas');
  sampleCanvas.width = canvas.width;
  sampleCanvas.height = canvas.height;
  const sCtx = sampleCanvas.getContext('2d');

  const processed = getProcessedImageCanvas();
  if (!processed) return;
  sCtx.drawImage(processed, imgX, imgY);

  const rawSampleCells = [];

  for (let r = 0; r < rows; r++) {
    rawSampleCells[r] = [];
    for (let c = 0; c < cols; c++) {
      const { x, y, w, h } = getBeadCoords(c, r);
      
      const sampleW = Math.max(2, Math.floor(w * 0.7));
      const sampleH = Math.max(2, Math.floor(h * 0.7));
      const sampleX = Math.floor(x + (w - sampleW) / 2);
      const sampleY = Math.floor(y + (h - sampleH) / 2);

      const imgData = sCtx.getImageData(sampleX, sampleY, sampleW, sampleH).data;
      
      let sumR = 0, sumG = 0, sumB = 0, validPixels = 0;
      for (let i = 0; i < imgData.length; i += 4) {
        if (imgData[i + 3] > 40) { // discard bg pixels
          sumR += imgData[i];
          sumG += imgData[i + 1];
          sumB += imgData[i + 2];
          validPixels++;
        }
      }

      if (validPixels > (sampleW * sampleH * 0.25)) {
        rawSampleCells[r][c] = {
          r: Math.round(sumR / validPixels),
          g: Math.round(sumG / validPixels),
          b: Math.round(sumB / validPixels)
        };
      } else {
        rawSampleCells[r][c] = null; // clean empty cell where bg was removed
      }
    }
  }

  const maxClusters = parseInt(document.getElementById('paletteLimitSlider').value);
  const colorFrequency = new Map();

  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      const cell = rawSampleCells[r][c];
      if (cell) {
        const closest = findClosestDelica(cell.r, cell.g, cell.b, MIYUKI_DELICAS);
        colorFrequency.set(closest.code, (colorFrequency.get(closest.code) || 0) + 1);
      }
    }
  }

  const sortedCodes = Array.from(colorFrequency.entries())
    .sort((a, b) => b[1] - a[1])
    .slice(0, maxClusters)
    .map(entry => MIYUKI_DELICAS.find(d => d.code === entry[0]));

  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      const cell = rawSampleCells[r][c];
      if (cell && sortedCodes.length > 0) {
        grid[r][c] = findClosestDelica(cell.r, cell.g, cell.b, sortedCodes);
      } else {
        grid[r][c] = null;
      }
    }
  }

  render();
});

document.getElementById('paletteLimitSlider').addEventListener('input', (e) => {
  document.getElementById('paletteLimitLabel').innerText = `MAX PALETTE CLUSTERS: ${e.target.value} COLORS`;
});

function floodFill(startC, startR, targetCode, fillDelica) {
  if (targetCode === fillDelica.code) return;
  const queue = [[startC, startR]];
  const visited = new Set();

  while (queue.length > 0) {
    const [c, r] = queue.pop();
    const key = `${c},${r}`;
    if (visited.has(key)) continue;
    visited.add(key);

    if (c < 0 || c >= cols || r < 0 || r >= rows) continue;
    const currentCode = grid[r][c] ? grid[r][c].code : null;
    if (currentCode !== targetCode) continue;

    grid[r][c] = fillDelica;
    queue.push([c + 1, r], [c - 1, r], [c, r + 1], [c, r - 1]);
  }
}

document.getElementById('invertBtn').addEventListener('click', () => {
  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      if (grid[r][c]) {
        const invR = 255 - grid[r][c].r;
        const invG = 255 - grid[r][c].g;
        const invB = 255 - grid[r][c].b;
        grid[r][c] = findClosestDelica(invR, invG, invB);
      }
    }
  }
  render();
});

const imageInput = document.getElementById('imageInput');
imageInput.addEventListener('change', (e) => {
  const file = e.target.files[0];
  if (!file) return;
  const reader = new FileReader();
  reader.onload = (evt) => {
    img = new Image();
    img.onload = () => {
      imgScale = Math.min(canvas.width / img.width, canvas.height / img.height);
      document.getElementById('scaleSlider').value = imgScale;
      imgX = (canvas.width - img.width * imgScale) / 2;
      imgY = (canvas.height - img.height * imgScale) / 2;
      setTool('pan');
      render();
    };
    img.src = evt.target.result;
  };
  reader.readAsDataURL(file);
});

document.getElementById('ejectPhotoBtn').addEventListener('click', () => {
  if (!img) return;
  img = null;
  imageInput.value = '';
  render();
});

document.getElementById('clearAllBtn').addEventListener('click', () => {
  img = null;
  imageInput.value = '';
  grid = Array(rows).fill(null).map(() => Array(cols).fill(null));
  bgTolerance = 0;
  document.getElementById('bgToleranceSlider').value = 0;
  document.getElementById('bgTolVal').innerText = 0;
  render();
});

function getPointerPos(e) {
  const rect = canvas.getBoundingClientRect();
  const scaleX = canvas.width / rect.width;
  const scaleY = canvas.height / rect.height;
  const clientX = e.touches ? e.touches[0].clientX : e.clientX;
  const clientY = e.touches ? e.touches[0].clientY : e.clientY;
  return {
    x: (clientX - rect.left) * scaleX,
    y: (clientY - rect.top) * scaleY,
    rawX: clientX,
    rawY: clientY
  };
}

function handleDrawingAction(mouseX, mouseY) {
  // magic wand bgsampling
  if (currentTool === 'wand' && img) {
    const targetX = Math.floor(mouseX - imgX);
    const targetY = Math.floor(mouseY - imgY);
    const processed = getProcessedImageCanvas();
    if (processed && targetX >= 0 && targetX < processed.width && targetY >= 0 && targetY < processed.height) {
      const pCtx = processed.getContext('2d');
      const pixel = pCtx.getImageData(targetX, targetY, 1, 1).data;
      bgKeyColor = { r: pixel[0], g: pixel[1], b: pixel[2] };
      const hex = "#" + ((1 << 24) + (pixel[0] << 16) + (pixel[1] << 8) + pixel[2]).toString(16).slice(1);
      document.getElementById('bgSampleSwatch').style.backgroundColor = hex;
      document.getElementById('bgSampleHex').innerText = hex;

      if (bgTolerance === 0) {
        bgTolerance = 45;
        document.getElementById('bgToleranceSlider').value = 45;
        document.getElementById('bgTolVal').innerText = 45;
      }
      render();
    }
    return;
  }

  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      const { x, y, w, h } = getBeadCoords(c, r);
      if (mouseX >= x && mouseX <= x + w && mouseY >= y && mouseY <= y + h) {
        if (currentTool === 'paint') {
          grid[r][c] = activeDelica;
          render();
        } else if (currentTool === 'erase') {
          grid[r][c] = null;
          render();
        } else if (currentTool === 'fill') {
          const targetCode = grid[r][c] ? grid[r][c].code : null;
          floodFill(c, r, targetCode, activeDelica);
          render();
        } else if (currentTool === 'eyedropper' && grid[r][c]) {
          selectDelica(grid[r][c]);
        }
        return;
      }
    }
  }
}

function onPointerStart(e) {
  isInteracting = true;
  const pos = getPointerPos(e);
  if (currentTool === 'pan') {
    startDragX = pos.rawX - imgX;
    startDragY = pos.rawY - imgY;
  } else {
    handleDrawingAction(pos.x, pos.y);
  }
}

function onPointerMove(e) {
  if (!isInteracting) return;
  const pos = getPointerPos(e);
  if (currentTool === 'pan') {
    if (img) {
      imgX = pos.rawX - startDragX;
      imgY = pos.rawY - startDragY;
      render();
    }
  } else if (currentTool === 'paint' || currentTool === 'erase') {
    handleDrawingAction(pos.x, pos.y);
  }
}

function onPointerEnd() { isInteracting = false; }

canvas.addEventListener('mousedown', onPointerStart);
window.addEventListener('mousemove', onPointerMove);
window.addEventListener('mouseup', onPointerEnd);

canvas.addEventListener('touchstart', (e) => { e.preventDefault(); onPointerStart(e); }, { passive: false });
window.addEventListener('touchmove', (e) => { if (isInteracting) onPointerMove(e); }, { passive: false });
window.addEventListener('touchend', onPointerEnd);

function setTool(tool) {
  document.querySelectorAll('.rack-btn').forEach(b => b.classList.remove('active'));
  document.getElementById(`tool-${tool}`).classList.add('active');
  currentTool = tool;
  canvas.style.cursor = (tool === 'pan' ? 'grab' : (tool === 'wand' ? 'copy' : (tool === 'paint' ? 'crosshair' : 'default')));
}

['pan', 'wand', 'paint', 'fill', 'erase', 'eyedropper'].forEach(tool => {
  document.getElementById(`tool-${tool}`).addEventListener('click', () => setTool(tool));
});

function selectDelica(delica) {
  activeDelica = delica;
  document.getElementById('activeDbCode').innerText = delica.code;
  document.getElementById('activeDbName').innerText = delica.name;
  document.querySelectorAll('.vial').forEach(v => {
    v.classList.toggle('active-reagent', v.dataset.code === delica.code);
  });
}

function renderPaletteTray() {
  const paletteContainer = document.getElementById('palette');
  paletteContainer.innerHTML = '';

  const catFilter = document.getElementById('paletteCategoryFilter').value;
  const searchTerm = document.getElementById('paletteSearch').value.toLowerCase();

  const filtered = MIYUKI_DELICAS.filter(d => {
    const matchesCat = (catFilter === 'all') || (d.cat === catFilter);
    const matchesSearch = d.code.toLowerCase().includes(searchTerm) || d.name.toLowerCase().includes(searchTerm);
    return matchesCat && matchesSearch;
  });

  filtered.forEach(delica => {
    const vial = document.createElement('div');
    vial.className = 'vial' + (activeDelica.code === delica.code ? ' active-reagent' : '');
    vial.dataset.code = delica.code;
    vial.style.backgroundColor = delica.hex;
    vial.innerHTML = `<span>${delica.code.replace('DB', '')}</span>`;
    vial.title = `${delica.code}: ${delica.name}`;
    vial.addEventListener('click', () => selectDelica(delica));
    paletteContainer.appendChild(vial);
  });
}

document.getElementById('paletteCategoryFilter').addEventListener('change', renderPaletteTray);
document.getElementById('paletteSearch').addEventListener('input', renderPaletteTray);

document.getElementById('scaleSlider').addEventListener('input', (e) => {
  imgScale = parseFloat(e.target.value);
  render();
});
document.getElementById('contrastSlider').addEventListener('input', () => render());
document.getElementById('opacitySlider').addEventListener('input', () => render());

document.getElementById('hideUnderlayBtn').addEventListener('click', () => {
  showUnderlay = !showUnderlay;
  document.getElementById('hideText').innerText = showUnderlay ? 'Hide Slide' : 'Show Slide';
  render();
});

document.getElementById('stitchSelect').addEventListener('change', (e) => {
  stitchMode = e.target.value;
  const colsInput = document.getElementById('colsInput');
  if (stitchMode === 'peyote_even' && cols % 2 !== 0) {
    cols += 1;
    colsInput.value = cols;
    syncGrid();
  } else if (stitchMode === 'peyote_odd' && cols % 2 === 0) {
    cols += 1;
    colsInput.value = cols;
    syncGrid();
  }
  updateCanvasSize();
});

document.getElementById('beadProfileSelect').addEventListener('change', (e) => {
  currentBeadProfile = e.target.value;
  updateCanvasSize();
});

function syncGrid() {
  const newGrid = Array(rows).fill(null).map(() => Array(cols).fill(null));
  for (let r = 0; r < Math.min(rows, grid.length); r++) {
    for (let c = 0; c < Math.min(cols, grid[0].length); c++) {
      newGrid[r][c] = grid[r][c];
    }
  }
  grid = newGrid;
}

function handleDimInputs() {
  cols = parseInt(document.getElementById('colsInput').value) || 2;
  rows = parseInt(document.getElementById('rowsInput').value) || 2;
  if (stitchMode === 'peyote_even' && cols % 2 !== 0) cols += 1;
  if (stitchMode === 'peyote_odd' && cols % 2 === 0) cols += 1;
  document.getElementById('colsInput').value = cols;
  syncGrid();
  updateCanvasSize();
}

document.getElementById('colsInput').addEventListener('change', handleDimInputs);
document.getElementById('rowsInput').addEventListener('change', handleDimInputs);

// PDF export
document.getElementById('exportPdfBtn').addEventListener('click', () => {
  const { jsPDF } = window.jspdf;
  const doc = new jsPDF('p', 'mm', 'a4');
  const { w, h } = getCellMetrics();

  doc.setFont('courier', 'bold');
  doc.setFontSize(13);
  doc.text(`BEADLAB SYNTHESIS REPORT — ${stitchMode.toUpperCase()}`, 15, 14);
  doc.setFont('courier', 'normal');
  doc.setFontSize(8);
  doc.text(`DESIGNED WITH BEADLAB BY @briannaspishock | GRID: ${cols}x${rows}`, 15, 19);

  const maxW = 180;
  const maxH = 250;
  const cellRatio = h / w;
  const pdfCellW = Math.min(maxW / cols, maxH / (rows * cellRatio), 5.5);
  const pdfCellH = pdfCellW * cellRatio;
  const startX = 15;
  const startY = 24;

  const colorCounts = {};

  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      const bead = grid[r][c];
      const rgb = bead ? { r: bead.r, g: bead.g, b: bead.b } : { r: 255, g: 255, b: 255 };

      if (bead) {
        colorCounts[bead.code] = (colorCounts[bead.code] || 0) + 1;
      }

      doc.setFillColor(rgb.r, rgb.g, rgb.b);
      doc.setDrawColor(215, 215, 215);

      let y = startY + (r * pdfCellH);
      if (stitchMode.startsWith('peyote') && c % 2 === 1) {
        y += pdfCellH / 2;
      }
      doc.rect(startX + (c * pdfCellW), y, pdfCellW, pdfCellH, 'FD');
    }
  }

  // miyuki key
  doc.addPage();
  doc.setFont('courier', 'bold');
  doc.setFontSize(14);
  doc.text("MATERIALS: MIYUKI DELICA COLORS", 15, 18);
  doc.setFontSize(9);
  doc.setFont('courier', 'normal');
  doc.text("Pattern formulated with BeadLab (@briannaspishock)", 15, 25);

  let keyY = 34;
  doc.setFont('courier', 'bold');
  doc.text("SWATCH", 15, keyY);
  doc.text("CODE", 35, keyY);
  doc.text("NAME", 60, keyY);
  doc.text("COUNT", 150, keyY);
  doc.text("% TOTAL", 175, keyY);
  doc.line(15, keyY + 2, 195, keyY + 2);

  keyY += 8;
  doc.setFont('courier', 'normal');

  const totalBeads = cols * rows;
  const usedCodes = Object.keys(colorCounts);

  if (usedCodes.length === 0) {
    doc.text("No bead colors placed in grid.", 15, keyY);
  } else {
    usedCodes.forEach(code => {
      const delica = MIYUKI_DELICAS.find(d => d.code === code);
      const count = colorCounts[code];
      const pct = ((count / totalBeads) * 100).toFixed(1);

      doc.setFillColor(delica.r, delica.g, delica.b);
      doc.setDrawColor(150, 150, 150);
      doc.rect(15, keyY - 4, 10, 5, 'FD');

      doc.text(delica.code, 35, keyY);
      doc.text(delica.name.slice(0, 32), 60, keyY);
      doc.text(`${count}`, 150, keyY);
      doc.text(`${pct}%`, 175, keyY);

      keyY += 7;
      if (keyY > 275) {
        doc.addPage();
        keyY = 20;
      }
    });
  }

  doc.save(`beadlab-grid-${stitchMode}.pdf`);
});

renderPaletteTray();
setTool('pan');
updateCanvasSize();
</script>
</body>
</html>
"""

components.html(beadlab_html, height=890, scrolling=True)

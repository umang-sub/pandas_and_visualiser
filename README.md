<div align="center">

<!-- ═══════════════════════════════════════════════════════════ -->
<!--                   MATRIX RAIN HEADER                       -->
<!-- ═══════════════════════════════════════════════════════════ -->

<svg width="900" height="300" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      .bg { fill: #000000; }
      .rain { font-family: 'Courier New', monospace; fill: #003B00; font-size: 12px; }
      .rain-bright { font-family: 'Courier New', monospace; fill: #00FF41; font-size: 12px; }
      .rain-mid { font-family: 'Courier New', monospace; fill: #00AA20; font-size: 12px; }
      .t { font-family: 'Courier New', monospace; }

      @keyframes r0  { 0%{opacity:0;transform:translateY(-20px)} 10%{opacity:1} 90%{opacity:1} 100%{opacity:0;transform:translateY(300px)} }
      @keyframes r1  { 0%{opacity:0;transform:translateY(-20px)} 10%{opacity:1} 90%{opacity:1} 100%{opacity:0;transform:translateY(300px)} }
      @keyframes glo { 0%,100%{opacity:1;filter:drop-shadow(0 0 12px #00FF41)} 50%{opacity:.85;filter:drop-shadow(0 0 24px #00FF41)} }
      @keyframes glo2{ 0%,100%{opacity:1;filter:drop-shadow(0 0 8px #00E5FF)}  50%{opacity:.8; filter:drop-shadow(0 0 18px #00E5FF)} }
      @keyframes blink{ 0%,100%{opacity:1} 50%{opacity:.3} }
      @keyframes scanline{ 0%{transform:translateY(-300px)} 100%{transform:translateY(300px)} }
      @keyframes pulse{ 0%,100%{opacity:.6} 50%{opacity:1} }

      .c0{animation:r0 2.8s 0.0s linear infinite}
      .c1{animation:r0 3.1s 0.3s linear infinite}
      .c2{animation:r0 2.5s 0.6s linear infinite}
      .c3{animation:r0 3.4s 0.1s linear infinite}
      .c4{animation:r0 2.9s 0.8s linear infinite}
      .c5{animation:r0 2.6s 0.4s linear infinite}
      .c6{animation:r0 3.2s 0.9s linear infinite}
      .c7{animation:r0 2.7s 0.2s linear infinite}
      .c8{animation:r0 3.0s 0.7s linear infinite}
      .c9{animation:r0 2.4s 0.5s linear infinite}
      .c10{animation:r0 3.3s 1.1s linear infinite}
      .c11{animation:r0 2.8s 1.3s linear infinite}
      .c12{animation:r0 3.1s 0.2s linear infinite}
      .c13{animation:r0 2.6s 1.0s linear infinite}
      .c14{animation:r0 3.5s 0.6s linear infinite}
      .c15{animation:r0 2.9s 1.4s linear infinite}
      .c16{animation:r0 2.7s 0.3s linear infinite}
      .c17{animation:r0 3.2s 1.2s linear infinite}

      .title-glow{animation:glo 3s ease-in-out infinite}
      .sub-glow{animation:glo2 2.5s ease-in-out infinite}
      .blink{animation:blink 1s step-end infinite}
      .scan{animation:scanline 4s linear infinite;opacity:.05}
      .pulse{animation:pulse 2s ease-in-out infinite}
    </style>

    <filter id="gf">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="gf2">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <linearGradient id="lineGrad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#00FF41" stop-opacity="0"/>
      <stop offset="30%" stop-color="#00FF41" stop-opacity="1"/>
      <stop offset="70%" stop-color="#00E5FF" stop-opacity="1"/>
      <stop offset="100%" stop-color="#00E5FF" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="boxGrad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#003B00" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#001A2E" stop-opacity="0.8"/>
    </linearGradient>
  </defs>

  <!-- Background -->
  <rect class="bg" width="900" height="300"/>

  <!-- Grid lines -->
  <g opacity="0.06" stroke="#00FF41" stroke-width="0.5">
    <line x1="0" y1="50" x2="900" y2="50"/>
    <line x1="0" y1="100" x2="900" y2="100"/>
    <line x1="0" y1="150" x2="900" y2="150"/>
    <line x1="0" y1="200" x2="900" y2="200"/>
    <line x1="0" y1="250" x2="900" y2="250"/>
    <line x1="50" y1="0" x2="50" y2="300"/>
    <line x1="150" y1="0" x2="150" y2="300"/>
    <line x1="250" y1="0" x2="250" y2="300"/>
    <line x1="350" y1="0" x2="350" y2="300"/>
    <line x1="450" y1="0" x2="450" y2="300"/>
    <line x1="550" y1="0" x2="550" y2="300"/>
    <line x1="650" y1="0" x2="650" y2="300"/>
    <line x1="750" y1="0" x2="750" y2="300"/>
    <line x1="850" y1="0" x2="850" y2="300"/>
  </g>

  <!-- Matrix rain columns -->
  <g class="rain c0"><text x="18" y="10">1</text><text x="18" y="24">0</text><text x="18" y="38">1</text><text x="18" y="52">1</text><text x="18" y="66">0</text><text x="18" y="80">0</text><text x="18" y="94">1</text><text x="18" y="108">0</text><text x="18" y="122">1</text></g>
  <g class="rain-mid c1"><text x="48" y="10">ψ</text><text x="48" y="24">7</text><text x="48" y="38">F</text><text x="48" y="52">2</text><text x="48" y="66">A</text><text x="48" y="80">9</text><text x="48" y="94">D</text><text x="48" y="108">3</text><text x="48" y="122">E</text></g>
  <g class="rain c2"><text x="78" y="10">0</text><text x="78" y="24">1</text><text x="78" y="38">1</text><text x="78" y="52">0</text><text x="78" y="66">1</text><text x="78" y="80">0</text><text x="78" y="94">0</text><text x="78" y="108">1</text><text x="78" y="122">1</text></g>
  <g class="rain-mid c3"><text x="108" y="10">B</text><text x="108" y="24">4</text><text x="108" y="38">C</text><text x="108" y="52">8</text><text x="108" y="66">1</text><text x="108" y="80">F</text><text x="108" y="94">6</text><text x="108" y="108">A</text><text x="108" y="122">2</text></g>
  <g class="rain c4"><text x="138" y="10">1</text><text x="138" y="24">0</text><text x="138" y="38">0</text><text x="138" y="52">1</text><text x="138" y="66">1</text><text x="138" y="80">0</text><text x="138" y="94">1</text><text x="138" y="108">0</text><text x="138" y="122">0</text></g>
  <g class="rain-mid c5"><text x="168" y="10">σ</text><text x="168" y="24">μ</text><text x="168" y="38">π</text><text x="168" y="52">∑</text><text x="168" y="66">∞</text><text x="168" y="80">√</text><text x="168" y="94">∂</text><text x="168" y="108">∇</text><text x="168" y="122">λ</text></g>
  <g class="rain c6"><text x="718" y="10">0</text><text x="718" y="24">1</text><text x="718" y="38">0</text><text x="718" y="52">1</text><text x="718" y="66">0</text><text x="718" y="80">1</text><text x="718" y="94">1</text><text x="718" y="108">0</text><text x="718" y="122">1</text></g>
  <g class="rain-mid c7"><text x="748" y="10">E</text><text x="748" y="24">9</text><text x="748" y="38">3</text><text x="748" y="52">D</text><text x="748" y="66">A</text><text x="748" y="80">7</text><text x="748" y="94">F</text><text x="748" y="108">2</text><text x="748" y="122">B</text></g>
  <g class="rain c8"><text x="778" y="10">1</text><text x="778" y="24">1</text><text x="778" y="38">0</text><text x="778" y="52">0</text><text x="778" y="66">1</text><text x="778" y="80">0</text><text x="778" y="94">1</text><text x="778" y="108">1</text><text x="778" y="122">0</text></g>
  <g class="rain-mid c9"><text x="808" y="10">α</text><text x="808" y="24">β</text><text x="808" y="38">γ</text><text x="808" y="52">δ</text><text x="808" y="66">ε</text><text x="808" y="80">ζ</text><text x="808" y="94">η</text><text x="808" y="108">θ</text><text x="808" y="122">ι</text></g>
  <g class="rain c10"><text x="838" y="10">0</text><text x="838" y="24">1</text><text x="838" y="38">0</text><text x="838" y="52">1</text><text x="838" y="66">1</text><text x="838" y="80">0</text><text x="838" y="94">0</text><text x="838" y="108">1</text><text x="838" y="122">0</text></g>
  <g class="rain-mid c11"><text x="868" y="10">C</text><text x="868" y="24">5</text><text x="868" y="38">F</text><text x="868" y="52">1</text><text x="868" y="66">8</text><text x="868" y="80">B</text><text x="868" y="94">4</text><text x="868" y="108">E</text><text x="868" y="122">7</text></g>

  <!-- Scanline effect -->
  <rect class="scan" x="0" y="0" width="900" height="8" fill="#00FF41"/>

  <!-- Center glow box -->
  <rect x="150" y="75" width="600" height="155" rx="8" ry="8" fill="url(#boxGrad)" stroke="#00FF41" stroke-width="0.8" stroke-opacity="0.5"/>
  <rect x="151" y="76" width="598" height="153" rx="7" ry="7" fill="none" stroke="#00E5FF" stroke-width="0.3" stroke-opacity="0.3"/>

  <!-- Corner brackets -->
  <g stroke="#00FF41" stroke-width="1.5" fill="none" opacity="0.9">
    <path d="M155 82 L155 78 L162 78"/>
    <path d="M745 82 L745 78 L738 78"/>
    <path d="M155 222 L155 226 L162 226"/>
    <path d="M745 222 L745 226 L738 226"/>
  </g>

  <!-- Separator line -->
  <rect x="200" y="148" width="500" height="1" fill="url(#lineGrad)" opacity="0.7"/>

  <!-- Main title -->
  <text x="450" y="135" text-anchor="middle" class="t title-glow"
        font-size="46" font-weight="bold" font-family="'Courier New', monospace"
        fill="#00FF41" filter="url(#gf2)" letter-spacing="4">
    PANDAS ANALYZER
  </text>

  <!-- Subtitle -->
  <text x="450" y="178" text-anchor="middle" class="t sub-glow"
        font-size="15" font-family="'Courier New', monospace"
        fill="#00E5FF" letter-spacing="3">
    ◈  DATA ANALYSIS  &amp;  VISUALIZATION ENGINE  ◈
  </text>

  <!-- Status line -->
  <text x="450" y="210" text-anchor="middle" class="t pulse"
        font-size="11" font-family="'Courier New', monospace"
        fill="#00FF41" opacity="0.8" letter-spacing="2">
    [ PYTHON · PANDAS · MATPLOTLIB · SEABORN · NUMPY ]
  </text>

  <!-- Bottom blink cursor -->
  <text x="452" y="228" text-anchor="middle" class="t blink"
        font-size="12" font-family="'Courier New', monospace" fill="#00FF41">█</text>

  <!-- Top label -->
  <text x="163" y="73" class="t" font-size="9" font-family="'Courier New', monospace"
        fill="#00FF41" opacity="0.6">SYS::INIT</text>
  <text x="680" y="73" class="t" font-size="9" font-family="'Courier New', monospace"
        fill="#00FF41" opacity="0.6" text-anchor="end">v1.0.0::READY</text>
</svg>

</div>

---

<div align="center">

<!-- ═══════════════  BADGE ROW  ═══════════════ -->

![Python](https://img.shields.io/badge/Python-3.8%2B-00FF41?style=for-the-badge&logo=python&logoColor=00FF41&labelColor=0D0D0D&color=003B00)
![Pandas](https://img.shields.io/badge/Pandas-2.x-00E5FF?style=for-the-badge&logo=pandas&logoColor=00E5FF&labelColor=0D0D0D&color=001A2E)
![NumPy](https://img.shields.io/badge/NumPy-1.x-BD00FF?style=for-the-badge&logo=numpy&logoColor=BD00FF&labelColor=0D0D0D&color=1A0030)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.x-FFD700?style=for-the-badge&logo=python&logoColor=FFD700&labelColor=0D0D0D&color=2A2000)
![Seaborn](https://img.shields.io/badge/Seaborn-0.x-FF4500?style=for-the-badge&logo=python&logoColor=FF4500&labelColor=0D0D0D&color=2A0A00)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-FF6B35?style=for-the-badge&logo=jupyter&logoColor=FF6B35&labelColor=0D0D0D&color=2A1500)

</div>

---

<!-- ═══════════════════════════════════════════════════════════ -->
<!--                    METRICS DASHBOARD SVG                   -->
<!-- ═══════════════════════════════════════════════════════════ -->

<div align="center">

<svg width="900" height="90" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      .met-bg  { fill: #0A0A0A; }
      .card    { fill: #0D0D0D; stroke-width: 1; rx: 6; }
      .m-lbl   { font-family: 'Courier New', monospace; font-size: 9px; letter-spacing: 1px; }
      .m-val   { font-family: 'Courier New', monospace; font-size: 22px; font-weight: bold; }
      .m-sub   { font-family: 'Courier New', monospace; font-size: 8px; letter-spacing: 2px; }
      @keyframes countup { from{opacity:0} to{opacity:1} }
      .appear  { animation: countup 1.5s ease-in forwards; }
      @keyframes barpulse { 0%,100%{opacity:.7} 50%{opacity:1} }
      .bar-anim { animation: barpulse 2s ease-in-out infinite; }
    </style>
  </defs>
  <rect class="met-bg" width="900" height="90"/>

  <!-- Card 1: Rows -->
  <rect x="10" y="8" width="160" height="74" rx="6" fill="#0D1A0D" stroke="#00FF41" stroke-width="0.8"/>
  <text x="90" y="26" text-anchor="middle" class="m-lbl" fill="#00FF41" opacity="0.7">DATASET ROWS</text>
  <text x="90" y="56" text-anchor="middle" class="m-val appear" fill="#00FF41">200</text>
  <text x="90" y="72" text-anchor="middle" class="m-sub" fill="#00FF41" opacity="0.5">SYNTHETIC RECORDS</text>
  <rect x="14" y="78" width="152" height="2" rx="1" fill="#00FF41" opacity="0.3" class="bar-anim"/>

  <!-- Card 2: Columns -->
  <rect x="183" y="8" width="160" height="74" rx="6" fill="#001020" stroke="#00E5FF" stroke-width="0.8"/>
  <text x="263" y="26" text-anchor="middle" class="m-lbl" fill="#00E5FF" opacity="0.7">FEATURES</text>
  <text x="263" y="56" text-anchor="middle" class="m-val appear" fill="#00E5FF">5</text>
  <text x="263" y="72" text-anchor="middle" class="m-sub" fill="#00E5FF" opacity="0.5">COLUMNS · CSV FORMAT</text>
  <rect x="187" y="78" width="152" height="2" rx="1" fill="#00E5FF" opacity="0.3" class="bar-anim"/>

  <!-- Card 3: Visualizations -->
  <rect x="356" y="8" width="160" height="74" rx="6" fill="#150020" stroke="#BD00FF" stroke-width="0.8"/>
  <text x="436" y="26" text-anchor="middle" class="m-lbl" fill="#BD00FF" opacity="0.7">CHART TYPES</text>
  <text x="436" y="56" text-anchor="middle" class="m-val appear" fill="#BD00FF">10+</text>
  <text x="436" y="72" text-anchor="middle" class="m-sub" fill="#BD00FF" opacity="0.5">MATPLOTLIB · SEABORN</text>
  <rect x="360" y="78" width="152" height="2" rx="1" fill="#BD00FF" opacity="0.3" class="bar-anim"/>

  <!-- Card 4: Menu Options -->
  <rect x="529" y="8" width="160" height="74" rx="6" fill="#1A1200" stroke="#FFD700" stroke-width="0.8"/>
  <text x="609" y="26" text-anchor="middle" class="m-lbl" fill="#FFD700" opacity="0.7">MENU OPTIONS</text>
  <text x="609" y="56" text-anchor="middle" class="m-val appear" fill="#FFD700">8</text>
  <text x="609" y="72" text-anchor="middle" class="m-sub" fill="#FFD700" opacity="0.5">INTERACTIVE INTERFACE</text>
  <rect x="533" y="78" width="152" height="2" rx="1" fill="#FFD700" opacity="0.3" class="bar-anim"/>

  <!-- Card 5: OOP -->
  <rect x="702" y="8" width="190" height="74" rx="6" fill="#1A0500" stroke="#FF4500" stroke-width="0.8"/>
  <text x="797" y="26" text-anchor="middle" class="m-lbl" fill="#FF4500" opacity="0.7">OOP METHODS</text>
  <text x="797" y="56" text-anchor="middle" class="m-val appear" fill="#FF4500">18+</text>
  <text x="797" y="72" text-anchor="middle" class="m-sub" fill="#FF4500" opacity="0.5">ENCAPSULATED CLASS</text>
  <rect x="706" y="78" width="182" height="2" rx="1" fill="#FF4500" opacity="0.3" class="bar-anim"/>
</svg>

</div>

---

## `// 01` · OVERVIEW

<div align="center">

<svg width="900" height="110" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      .ob { font-family: 'Courier New', monospace; }
      @keyframes stream { 0%{stroke-dashoffset:1000} 100%{stroke-dashoffset:0} }
      .flow { stroke-dasharray: 1000; animation: stream 4s linear infinite; }
    </style>
  </defs>
  <rect width="900" height="110" fill="#050505"/>

  <!-- Binary stream top -->
  <text x="0" y="14" class="ob" font-size="9" fill="#003B00" letter-spacing="3">
    01001000 01100101 01101100 01101100 01101111 00100000 01000100 01100001 01110100 01100001 00100000 01010011 01100011 01101001 01100101 01101110 01100011 01100101 00100001 01101001 01100101 01101110 01100011 01100101 00100001
  </text>

  <!-- Pipeline nodes -->
  <!-- Node 1: CSV -->
  <rect x="20" y="35" width="110" height="44" rx="5" fill="#0D1A0D" stroke="#00FF41" stroke-width="1"/>
  <text x="75" y="52" text-anchor="middle" class="ob" font-size="9" fill="#00FF41" opacity="0.7">INPUT</text>
  <text x="75" y="68" text-anchor="middle" class="ob" font-size="13" fill="#00FF41">📂 CSV</text>

  <!-- Arrow 1 -->
  <line x1="130" y1="57" x2="185" y2="57" stroke="#00FF41" stroke-width="1.5" class="flow" stroke-dasharray="5,3" opacity="0.8"/>
  <polygon points="185,52 195,57 185,62" fill="#00FF41" opacity="0.8"/>

  <!-- Node 2: SalesDataFrame -->
  <rect x="195" y="28" width="150" height="58" rx="5" fill="#001020" stroke="#00E5FF" stroke-width="1.5"/>
  <text x="270" y="48" text-anchor="middle" class="ob" font-size="9" fill="#00E5FF" opacity="0.7">CLASS</text>
  <text x="270" y="64" text-anchor="middle" class="ob" font-size="12" fill="#00E5FF">SalesDataFrame</text>
  <text x="270" y="78" text-anchor="middle" class="ob" font-size="8" fill="#00E5FF" opacity="0.5">⬡ CORE ENGINE</text>

  <!-- Arrow 2 -->
  <line x1="345" y1="57" x2="400" y2="57" stroke="#00E5FF" stroke-width="1.5" class="flow" stroke-dasharray="5,3" opacity="0.8"/>
  <polygon points="400,52 410,57 400,62" fill="#00E5FF" opacity="0.8"/>

  <!-- Node 3: Processing -->
  <rect x="410" y="28" width="150" height="58" rx="5" fill="#150020" stroke="#BD00FF" stroke-width="1"/>
  <text x="485" y="48" text-anchor="middle" class="ob" font-size="9" fill="#BD00FF" opacity="0.7">PROCESSING</text>
  <text x="485" y="64" text-anchor="middle" class="ob" font-size="11" fill="#BD00FF">⚙ ANALYZE &amp; CLEAN</text>
  <text x="485" y="78" text-anchor="middle" class="ob" font-size="8" fill="#BD00FF" opacity="0.5">STATS · MISSING · MATH</text>

  <!-- Arrow 3 -->
  <line x1="560" y1="57" x2="615" y2="57" stroke="#BD00FF" stroke-width="1.5" class="flow" stroke-dasharray="5,3" opacity="0.8"/>
  <polygon points="615,52 625,57 615,62" fill="#BD00FF" opacity="0.8"/>

  <!-- Node 4: Visualize -->
  <rect x="625" y="28" width="150" height="58" rx="5" fill="#1A1200" stroke="#FFD700" stroke-width="1"/>
  <text x="700" y="48" text-anchor="middle" class="ob" font-size="9" fill="#FFD700" opacity="0.7">OUTPUT</text>
  <text x="700" y="64" text-anchor="middle" class="ob" font-size="11" fill="#FFD700">📊 VISUALIZE</text>
  <text x="700" y="78" text-anchor="middle" class="ob" font-size="8" fill="#FFD700" opacity="0.5">PLOTS · PNG EXPORT</text>

  <!-- Arrow 4 -->
  <line x1="775" y1="57" x2="830" y2="57" stroke="#FFD700" stroke-width="1.5" class="flow" stroke-dasharray="5,3" opacity="0.8"/>
  <polygon points="830,52 840,57 830,62" fill="#FFD700" opacity="0.8"/>

  <!-- Node 5: Export -->
  <rect x="840" y="35" width="50" height="44" rx="5" fill="#1A0500" stroke="#FF4500" stroke-width="1"/>
  <text x="865" y="52" text-anchor="middle" class="ob" font-size="8" fill="#FF4500" opacity="0.7">SAVE</text>
  <text x="865" y="68" text-anchor="middle" class="ob" font-size="11" fill="#FF4500">💾</text>

  <!-- Binary stream bottom -->
  <text x="0" y="102" class="ob" font-size="9" fill="#003B00" letter-spacing="3">
    11010000 01110011 01100001 01101100 01100101 01110011 01100100 01100001 01110100 01100001 01100110 01110010 01100001 01101101 01100101 01110000 01111001 01110100 01101000 01101111 01101110 01110110 01101001 01111010
  </text>
</svg>

</div>

> A comprehensive **Sales Data Analysis & Visualization** tool built in Python.
> Encapsulates all data science operations inside a single `SalesDataFrame` class —
> from raw CSV ingestion to advanced statistical analysis, multi-library visualization,
> and interactive menu-driven user interface. Built for academic excellence and real-world applicability.

---

## `// 02` · FEATURES

<div align="center">

<svg width="900" height="220" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      .fb { font-family: 'Courier New', monospace; }
      @keyframes glow3 { 0%,100%{opacity:.8} 50%{opacity:1} }
      .fg { animation: glow3 3s ease-in-out infinite; }
    </style>
  </defs>
  <rect width="900" height="220" fill="#050505"/>

  <!-- Row 1 -->
  <!-- Feature 1 -->
  <rect x="10" y="10" width="200" height="90" rx="6" fill="#0D1A0D" stroke="#00FF41" stroke-width="0.8"/>
  <text x="30" y="35" class="fb" font-size="20" fill="#00FF41">📂</text>
  <text x="60" y="35" class="fb" font-size="12" fill="#00FF41" font-weight="bold">DATA LOADING</text>
  <line x1="14" y1="45" x2="206" y2="45" stroke="#00FF41" stroke-width="0.4" opacity="0.4"/>
  <text x="20" y="60" class="fb" font-size="9" fill="#00FF41" opacity="0.8">→ CSV file ingestion</text>
  <text x="20" y="73" class="fb" font-size="9" fill="#00FF41" opacity="0.8">→ Synthetic data generator</text>
  <text x="20" y="86" class="fb" font-size="9" fill="#00FF41" opacity="0.8">→ Auto path resolution</text>

  <!-- Feature 2 -->
  <rect x="222" y="10" width="200" height="90" rx="6" fill="#001020" stroke="#00E5FF" stroke-width="0.8"/>
  <text x="242" y="35" class="fb" font-size="20" fill="#00E5FF">🔍</text>
  <text x="272" y="35" class="fb" font-size="12" fill="#00E5FF" font-weight="bold">EXPLORATION</text>
  <line x1="226" y1="45" x2="418" y2="45" stroke="#00E5FF" stroke-width="0.4" opacity="0.4"/>
  <text x="232" y="60" class="fb" font-size="9" fill="#00E5FF" opacity="0.8">→ Head / tail preview</text>
  <text x="232" y="73" class="fb" font-size="9" fill="#00E5FF" opacity="0.8">→ Column schema display</text>
  <text x="232" y="86" class="fb" font-size="9" fill="#00E5FF" opacity="0.8">→ dtypes &amp; info</text>

  <!-- Feature 3 -->
  <rect x="434" y="10" width="200" height="90" rx="6" fill="#150020" stroke="#BD00FF" stroke-width="0.8"/>
  <text x="454" y="35" class="fb" font-size="20" fill="#BD00FF">⚙</text>
  <text x="479" y="35" class="fb" font-size="12" fill="#BD00FF" font-weight="bold">MATH OPS</text>
  <line x1="438" y1="45" x2="630" y2="45" stroke="#BD00FF" stroke-width="0.4" opacity="0.4"/>
  <text x="444" y="60" class="fb" font-size="9" fill="#BD00FF" opacity="0.8">→ Sum / Mean / Median</text>
  <text x="444" y="73" class="fb" font-size="9" fill="#BD00FF" opacity="0.8">→ Std / Min / Max</text>
  <text x="444" y="86" class="fb" font-size="9" fill="#BD00FF" opacity="0.8">→ Aggregate functions</text>

  <!-- Feature 4 -->
  <rect x="646" y="10" width="244" height="90" rx="6" fill="#1A1200" stroke="#FFD700" stroke-width="0.8"/>
  <text x="666" y="35" class="fb" font-size="20" fill="#FFD700">🔗</text>
  <text x="691" y="35" class="fb" font-size="12" fill="#FFD700" font-weight="bold">COMBINE &amp; SPLIT</text>
  <line x1="650" y1="45" x2="886" y2="45" stroke="#FFD700" stroke-width="0.4" opacity="0.4"/>
  <text x="656" y="60" class="fb" font-size="9" fill="#FFD700" opacity="0.8">→ Merge / Concat DataFrames</text>
  <text x="656" y="73" class="fb" font-size="9" fill="#FFD700" opacity="0.8">→ Split by value / regex</text>
  <text x="656" y="86" class="fb" font-size="9" fill="#FFD700" opacity="0.8">→ Pivot table creation</text>

  <!-- Row 2 -->
  <!-- Feature 5 -->
  <rect x="10" y="118" width="200" height="90" rx="6" fill="#1A0500" stroke="#FF4500" stroke-width="0.8"/>
  <text x="30" y="143" class="fb" font-size="20" fill="#FF4500">🛠</text>
  <text x="55" y="143" class="fb" font-size="12" fill="#FF4500" font-weight="bold">MISSING DATA</text>
  <line x1="14" y1="153" x2="206" y2="153" stroke="#FF4500" stroke-width="0.4" opacity="0.4"/>
  <text x="20" y="168" class="fb" font-size="9" fill="#FF4500" opacity="0.8">→ Detect missing values</text>
  <text x="20" y="181" class="fb" font-size="9" fill="#FF4500" opacity="0.8">→ Fill / drop / replace</text>
  <text x="20" y="194" class="fb" font-size="9" fill="#FF4500" opacity="0.8">→ Row-level inspection</text>

  <!-- Feature 6 -->
  <rect x="222" y="118" width="200" height="90" rx="6" fill="#0A1A00" stroke="#7FFF00" stroke-width="0.8"/>
  <text x="242" y="143" class="fb" font-size="20" fill="#7FFF00">📈</text>
  <text x="267" y="143" class="fb" font-size="12" fill="#7FFF00" font-weight="bold">STATISTICS</text>
  <line x1="226" y1="153" x2="418" y2="153" stroke="#7FFF00" stroke-width="0.4" opacity="0.4"/>
  <text x="232" y="168" class="fb" font-size="9" fill="#7FFF00" opacity="0.8">→ Describe / Skewness</text>
  <text x="232" y="181" class="fb" font-size="9" fill="#7FFF00" opacity="0.8">→ Variance / Percentiles</text>
  <text x="232" y="194" class="fb" font-size="9" fill="#7FFF00" opacity="0.8">→ Full describe(include=all)</text>

  <!-- Feature 7 -->
  <rect x="434" y="118" width="200" height="90" rx="6" fill="#001510" stroke="#00FFAA" stroke-width="0.8"/>
  <text x="454" y="143" class="fb" font-size="20" fill="#00FFAA">📊</text>
  <text x="479" y="143" class="fb" font-size="12" fill="#00FFAA" font-weight="bold">MATPLOTLIB</text>
  <line x1="438" y1="153" x2="630" y2="153" stroke="#00FFAA" stroke-width="0.4" opacity="0.4"/>
  <text x="444" y="168" class="fb" font-size="9" fill="#00FFAA" opacity="0.8">→ Bar · Line · Scatter</text>
  <text x="444" y="181" class="fb" font-size="9" fill="#00FFAA" opacity="0.8">→ Pie · Histogram · Stack</text>
  <text x="444" y="194" class="fb" font-size="9" fill="#00FFAA" opacity="0.8">→ Heatmap · Multi-plot</text>

  <!-- Feature 8 -->
  <rect x="646" y="118" width="244" height="90" rx="6" fill="#10001A" stroke="#EE82EE" stroke-width="0.8"/>
  <text x="666" y="143" class="fb" font-size="20" fill="#EE82EE">🎨</text>
  <text x="691" y="143" class="fb" font-size="12" fill="#EE82EE" font-weight="bold">SEABORN</text>
  <line x1="650" y1="153" x2="886" y2="153" stroke="#EE82EE" stroke-width="0.4" opacity="0.4"/>
  <text x="656" y="168" class="fb" font-size="9" fill="#EE82EE" opacity="0.8">→ Boxplot / Violinplot</text>
  <text x="656" y="181" class="fb" font-size="9" fill="#EE82EE" opacity="0.8">→ Seaborn Barplot</text>
  <text x="656" y="194" class="fb" font-size="9" fill="#EE82EE" opacity="0.8">→ Statistical styling options</text>
</svg>

</div>

---

## `// 03` · VISUALIZATION GALLERY

<div align="center">

<svg width="900" height="310" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      .vb { font-family: 'Courier New', monospace; }
      @keyframes barrise { from{transform:scaleY(0)} to{transform:scaleY(1)} }
      .bar-rise { transform-origin: bottom; animation: barrise 1.2s ease-out forwards; }
      @keyframes linedraw { from{stroke-dashoffset:500} to{stroke-dashoffset:0} }
      .line-draw { stroke-dasharray:500; animation: linedraw 2s ease-in-out forwards; }
      @keyframes fadein { from{opacity:0} to{opacity:1} }
      .fade { animation: fadein 1.5s ease-in forwards; }
    </style>
  </defs>
  <rect width="900" height="310" fill="#050505"/>

  <!-- ─── CHART 1: BAR CHART ─── -->
  <rect x="10" y="10" width="265" height="290" rx="6" fill="#0A0A0A" stroke="#00FF41" stroke-width="0.8"/>
  <text x="142" y="30" text-anchor="middle" class="vb" font-size="10" fill="#00FF41" letter-spacing="2">SALES BY REGION</text>
  <text x="142" y="44" text-anchor="middle" class="vb" font-size="8" fill="#00FF41" opacity="0.5">[ BAR CHART ]</text>
  <line x1="20" y1="52" x2="265" y2="52" stroke="#00FF41" stroke-width="0.4" opacity="0.3"/>

  <!-- Y-axis -->
  <line x1="45" y1="60" x2="45" y2="265" stroke="#00FF41" stroke-width="0.6" opacity="0.5"/>
  <!-- X-axis -->
  <line x1="45" y1="265" x2="260" y2="265" stroke="#00FF41" stroke-width="0.6" opacity="0.5"/>

  <!-- Y labels -->
  <text x="40" y="64"  text-anchor="end" class="vb" font-size="7" fill="#00FF41" opacity="0.6">1000</text>
  <text x="40" y="114" text-anchor="end" class="vb" font-size="7" fill="#00FF41" opacity="0.6">750</text>
  <text x="40" y="164" text-anchor="end" class="vb" font-size="7" fill="#00FF41" opacity="0.6">500</text>
  <text x="40" y="214" text-anchor="end" class="vb" font-size="7" fill="#00FF41" opacity="0.6">250</text>
  <text x="40" y="264" text-anchor="end" class="vb" font-size="7" fill="#00FF41" opacity="0.6">0</text>

  <!-- Grid lines -->
  <line x1="45" y1="63"  x2="260" y2="63"  stroke="#00FF41" stroke-width="0.3" stroke-dasharray="3,3" opacity="0.2"/>
  <line x1="45" y1="113" x2="260" y2="113" stroke="#00FF41" stroke-width="0.3" stroke-dasharray="3,3" opacity="0.2"/>
  <line x1="45" y1="163" x2="260" y2="163" stroke="#00FF41" stroke-width="0.3" stroke-dasharray="3,3" opacity="0.2"/>
  <line x1="45" y1="213" x2="260" y2="213" stroke="#00FF41" stroke-width="0.3" stroke-dasharray="3,3" opacity="0.2"/>

  <!-- Bars: North=21568, South=22400, East=19200, West=21060, Central=18400 -->
  <!-- normalized to 200px height max -->
  <!-- North: ~172px  South: ~179px  East: ~153px  West: ~168px  Central: ~147px -->
  <rect x="55"  y="93"  width="28" height="172" fill="#00FF41" opacity="0.85" rx="2" class="bar-rise"/>
  <rect x="98"  y="86"  width="28" height="179" fill="#00CC33" opacity="0.85" rx="2" class="bar-rise"/>
  <rect x="141" y="112" width="28" height="153" fill="#009922" opacity="0.85" rx="2" class="bar-rise"/>
  <rect x="184" y="97"  width="28" height="168" fill="#007711" opacity="0.85" rx="2" class="bar-rise"/>
  <rect x="227" y="118" width="28" height="147" fill="#005500" opacity="0.85" rx="2" class="bar-rise"/>

  <!-- X labels -->
  <text x="69"  y="278" text-anchor="middle" class="vb" font-size="7" fill="#00FF41" opacity="0.8">N</text>
  <text x="112" y="278" text-anchor="middle" class="vb" font-size="7" fill="#00FF41" opacity="0.8">S</text>
  <text x="155" y="278" text-anchor="middle" class="vb" font-size="7" fill="#00FF41" opacity="0.8">E</text>
  <text x="198" y="278" text-anchor="middle" class="vb" font-size="7" fill="#00FF41" opacity="0.8">W</text>
  <text x="241" y="278" text-anchor="middle" class="vb" font-size="7" fill="#00FF41" opacity="0.8">C</text>

  <!-- Value labels on bars -->
  <text x="69"  y="89"  text-anchor="middle" class="vb" font-size="7" fill="#00FF41">21.5k</text>
  <text x="112" y="82"  text-anchor="middle" class="vb" font-size="7" fill="#00FF41">22.4k</text>
  <text x="155" y="108" text-anchor="middle" class="vb" font-size="7" fill="#00FF41">19.2k</text>
  <text x="198" y="93"  text-anchor="middle" class="vb" font-size="7" fill="#00FF41">21.0k</text>
  <text x="241" y="114" text-anchor="middle" class="vb" font-size="7" fill="#00FF41">18.4k</text>

  <text x="142" y="298" text-anchor="middle" class="vb" font-size="7" fill="#00FF41" opacity="0.5">Region</text>

  <!-- ─── CHART 2: LINE CHART ─── -->
  <rect x="287" y="10" width="312" height="290" rx="6" fill="#0A0A0A" stroke="#00E5FF" stroke-width="0.8"/>
  <text x="443" y="30" text-anchor="middle" class="vb" font-size="10" fill="#00E5FF" letter-spacing="2">SALES TREND BY YEAR</text>
  <text x="443" y="44" text-anchor="middle" class="vb" font-size="8" fill="#00E5FF" opacity="0.5">[ LINE CHART ]</text>
  <line x1="297" y1="52" x2="592" y2="52" stroke="#00E5FF" stroke-width="0.4" opacity="0.3"/>

  <!-- Y-axis -->
  <line x1="330" y1="60" x2="330" y2="265" stroke="#00E5FF" stroke-width="0.6" opacity="0.5"/>
  <line x1="330" y1="265" x2="585" y2="265" stroke="#00E5FF" stroke-width="0.6" opacity="0.5"/>

  <!-- Y grid -->
  <line x1="330" y1="65"  x2="585" y2="65"  stroke="#00E5FF" stroke-width="0.3" stroke-dasharray="3,3" opacity="0.2"/>
  <line x1="330" y1="115" x2="585" y2="115" stroke="#00E5FF" stroke-width="0.3" stroke-dasharray="3,3" opacity="0.2"/>
  <line x1="330" y1="165" x2="585" y2="165" stroke="#00E5FF" stroke-width="0.3" stroke-dasharray="3,3" opacity="0.2"/>
  <line x1="330" y1="215" x2="585" y2="215" stroke="#00E5FF" stroke-width="0.3" stroke-dasharray="3,3" opacity="0.2"/>

  <!-- Y labels -->
  <text x="325" y="68"  text-anchor="end" class="vb" font-size="7" fill="#00E5FF" opacity="0.6">1000</text>
  <text x="325" y="118" text-anchor="end" class="vb" font-size="7" fill="#00E5FF" opacity="0.6">750</text>
  <text x="325" y="168" text-anchor="end" class="vb" font-size="7" fill="#00E5FF" opacity="0.6">500</text>
  <text x="325" y="218" text-anchor="end" class="vb" font-size="7" fill="#00E5FF" opacity="0.6">250</text>

  <!-- Product A line: 2021=480, 2022=620, 2023=550 → y = 265 - (val/1000)*200 -->
  <!-- 2021: y=169, 2022=141, 2023=155  x: 380, 457, 535 -->
  <polyline points="380,169 457,141 535,155" fill="none" stroke="#00E5FF" stroke-width="2" class="line-draw"/>
  <circle cx="380" cy="169" r="4" fill="#00E5FF"/>
  <circle cx="457" cy="141" r="4" fill="#00E5FF"/>
  <circle cx="535" cy="155" r="4" fill="#00E5FF"/>

  <!-- Product B line -->
  <polyline points="380,195 457,160 535,175" fill="none" stroke="#00FFAA" stroke-width="2" class="line-draw"/>
  <circle cx="380" cy="195" r="4" fill="#00FFAA"/>
  <circle cx="457" cy="160" r="4" fill="#00FFAA"/>
  <circle cx="535" cy="175" r="4" fill="#00FFAA"/>

  <!-- Product C line -->
  <polyline points="380,215 457,188 535,165" fill="none" stroke="#BD00FF" stroke-width="2" class="line-draw"/>
  <circle cx="380" cy="215" r="4" fill="#BD00FF"/>
  <circle cx="457" cy="188" r="4" fill="#BD00FF"/>
  <circle cx="535" cy="165" r="4" fill="#BD00FF"/>

  <!-- X labels -->
  <text x="380" y="278" text-anchor="middle" class="vb" font-size="8" fill="#00E5FF" opacity="0.8">2021</text>
  <text x="457" y="278" text-anchor="middle" class="vb" font-size="8" fill="#00E5FF" opacity="0.8">2022</text>
  <text x="535" y="278" text-anchor="middle" class="vb" font-size="8" fill="#00E5FF" opacity="0.8">2023</text>

  <!-- Legend -->
  <rect x="338" y="289" width="8" height="8" fill="#00E5FF"/>
  <text x="350" y="297" class="vb" font-size="7" fill="#00E5FF">Prod A</text>
  <rect x="395" y="289" width="8" height="8" fill="#00FFAA"/>
  <text x="407" y="297" class="vb" font-size="7" fill="#00FFAA">Prod B</text>
  <rect x="452" y="289" width="8" height="8" fill="#BD00FF"/>
  <text x="464" y="297" class="vb" font-size="7" fill="#BD00FF">Prod C</text>

  <!-- ─── CHART 3: HEATMAP ─── -->
  <rect x="611" y="10" width="279" height="290" rx="6" fill="#0A0A0A" stroke="#BD00FF" stroke-width="0.8"/>
  <text x="750" y="30" text-anchor="middle" class="vb" font-size="10" fill="#BD00FF" letter-spacing="2">CORRELATION MATRIX</text>
  <text x="750" y="44" text-anchor="middle" class="vb" font-size="8" fill="#BD00FF" opacity="0.5">[ HEATMAP ]</text>
  <line x1="621" y1="52" x2="882" y2="52" stroke="#BD00FF" stroke-width="0.4" opacity="0.3"/>

  <!-- Heatmap cells: 3x3 (SalesID, Sales, Year) -->
  <!-- Row labels -->
  <text x="660" y="100" text-anchor="end" class="vb" font-size="8" fill="#BD00FF" opacity="0.8">SalesID</text>
  <text x="660" y="155" text-anchor="end" class="vb" font-size="8" fill="#BD00FF" opacity="0.8">Sales</text>
  <text x="660" y="210" text-anchor="end" class="vb" font-size="8" fill="#BD00FF" opacity="0.8">Year</text>

  <!-- Col labels -->
  <text x="695" y="75" text-anchor="middle" class="vb" font-size="7" fill="#BD00FF" opacity="0.8">SalesID</text>
  <text x="750" y="75" text-anchor="middle" class="vb" font-size="7" fill="#BD00FF" opacity="0.8">Sales</text>
  <text x="805" y="75" text-anchor="middle" class="vb" font-size="7" fill="#BD00FF" opacity="0.8">Year</text>

  <!-- Cell (0,0): 1.00 - deep purple -->
  <rect x="665" y="80" width="60" height="50" rx="2" fill="#6B00FF" opacity="0.9" class="fade"/>
  <text x="695" y="110" text-anchor="middle" class="vb" font-size="11" fill="white">1.00</text>
  <!-- Cell (0,1): -0.02 - near black -->
  <rect x="720" y="80" width="60" height="50" rx="2" fill="#1A0A2E" opacity="0.9" class="fade"/>
  <text x="750" y="110" text-anchor="middle" class="vb" font-size="11" fill="#888">-0.02</text>
  <!-- Cell (0,2): 0.01 - near black -->
  <rect x="775" y="80" width="60" height="50" rx="2" fill="#120820" opacity="0.9" class="fade"/>
  <text x="805" y="110" text-anchor="middle" class="vb" font-size="11" fill="#888">0.01</text>
  <!-- Cell (1,0): -0.02 -->
  <rect x="665" y="130" width="60" height="50" rx="2" fill="#1A0A2E" opacity="0.9" class="fade"/>
  <text x="695" y="160" text-anchor="middle" class="vb" font-size="11" fill="#888">-0.02</text>
  <!-- Cell (1,1): 1.00 - deep purple -->
  <rect x="720" y="130" width="60" height="50" rx="2" fill="#6B00FF" opacity="0.9" class="fade"/>
  <text x="750" y="160" text-anchor="middle" class="vb" font-size="11" fill="white">1.00</text>
  <!-- Cell (1,2): -0.04 -->
  <rect x="775" y="130" width="60" height="50" rx="2" fill="#150820" opacity="0.9" class="fade"/>
  <text x="805" y="160" text-anchor="middle" class="vb" font-size="11" fill="#888">-0.04</text>
  <!-- Cell (2,0): 0.01 -->
  <rect x="665" y="180" width="60" height="50" rx="2" fill="#120820" opacity="0.9" class="fade"/>
  <text x="695" y="210" text-anchor="middle" class="vb" font-size="11" fill="#888">0.01</text>
  <!-- Cell (2,1): -0.04 -->
  <rect x="720" y="180" width="60" height="50" rx="2" fill="#150820" opacity="0.9" class="fade"/>
  <text x="750" y="210" text-anchor="middle" class="vb" font-size="11" fill="#888">-0.04</text>
  <!-- Cell (2,2): 1.00 - deep purple -->
  <rect x="775" y="180" width="60" height="50" rx="2" fill="#6B00FF" opacity="0.9" class="fade"/>
  <text x="805" y="210" text-anchor="middle" class="vb" font-size="11" fill="white">1.00</text>

  <!-- Color scale -->
  <defs>
    <linearGradient id="heatGrad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%"   stop-color="#00008B"/>
      <stop offset="50%"  stop-color="#1A0A2E"/>
      <stop offset="100%" stop-color="#6B00FF"/>
    </linearGradient>
  </defs>
  <rect x="665" y="245" width="170" height="10" rx="2" fill="url(#heatGrad)"/>
  <text x="665" y="268" class="vb" font-size="7" fill="#BD00FF" opacity="0.7">-1.0</text>
  <text x="750" y="268" text-anchor="middle" class="vb" font-size="7" fill="#BD00FF" opacity="0.7">0.0</text>
  <text x="835" y="268" text-anchor="end" class="vb" font-size="7" fill="#BD00FF" opacity="0.7">+1.0</text>
  <text x="750" y="283" text-anchor="middle" class="vb" font-size="7" fill="#BD00FF" opacity="0.5">correlation scale</text>
</svg>

</div>

<div align="center">

<svg width="900" height="200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      .pb { font-family: 'Courier New', monospace; }
      @keyframes scatterIn { from{opacity:0;r:0} to{opacity:.8;r:4} }
      .dot { animation: scatterIn 1s ease-out forwards; }
      @keyframes pieIn { from{opacity:0} to{opacity:1} }
      .pie { animation: pieIn 1.5s ease-out forwards; }
    </style>
  </defs>
  <rect width="900" height="200" fill="#050505"/>

  <!-- ─── SCATTER PLOT ─── -->
  <rect x="10" y="5" width="420" height="190" rx="6" fill="#0A0A0A" stroke="#FFD700" stroke-width="0.8"/>
  <text x="220" y="22" text-anchor="middle" class="pb" font-size="10" fill="#FFD700" letter-spacing="2">SCATTER PLOT · SalesID vs Sales</text>
  <line x1="20" y1="30" x2="425" y2="30" stroke="#FFD700" stroke-width="0.4" opacity="0.3"/>

  <!-- Axes -->
  <line x1="45" y1="40" x2="45" y2="170" stroke="#FFD700" stroke-width="0.6" opacity="0.5"/>
  <line x1="45" y1="170" x2="410" y2="170" stroke="#FFD700" stroke-width="0.6" opacity="0.5"/>

  <!-- Scatter dots: random-looking but fixed -->
  <circle cx="65"  cy="90"  r="4" fill="#FFD700" opacity="0.8" class="dot"/>
  <circle cx="85"  cy="145" r="4" fill="#FFD700" opacity="0.8" class="dot"/>
  <circle cx="105" cy="55"  r="4" fill="#FFD700" opacity="0.8" class="dot"/>
  <circle cx="125" cy="120" r="4" fill="#FFD700" opacity="0.8" class="dot"/>
  <circle cx="145" cy="75"  r="4" fill="#FFD700" opacity="0.8" class="dot"/>
  <circle cx="165" cy="158" r="4" fill="#FFD700" opacity="0.8" class="dot"/>
  <circle cx="185" cy="95"  r="4" fill="#FFD700" opacity="0.8" class="dot"/>
  <circle cx="205" cy="60"  r="4" fill="#FFD700" opacity="0.8" class="dot"/>
  <circle cx="225" cy="140" r="4" fill="#FFD700" opacity="0.8" class="dot"/>
  <circle cx="245" cy="105" r="4" fill="#FFD700" opacity="0.8" class="dot"/>
  <circle cx="265" cy="72"  r="4" fill="#FFD700" opacity="0.8" class="dot"/>
  <circle cx="285" cy="130" r="4" fill="#FFD700" opacity="0.8" class="dot"/>
  <circle cx="305" cy="50"  r="4" fill="#FFD700" opacity="0.8" class="dot"/>
  <circle cx="325" cy="162" r="4" fill="#FFD700" opacity="0.8" class="dot"/>
  <circle cx="345" cy="88"  r="4" fill="#FFD700" opacity="0.8" class="dot"/>
  <circle cx="365" cy="115" r="4" fill="#FFD700" opacity="0.8" class="dot"/>
  <circle cx="385" cy="68"  r="4" fill="#FFD700" opacity="0.8" class="dot"/>

  <text x="220" y="185" text-anchor="middle" class="pb" font-size="7" fill="#FFD700" opacity="0.5">SalesID →</text>
  <text x="18"  y="105" text-anchor="middle" class="pb" font-size="7" fill="#FFD700" opacity="0.5" transform="rotate(-90,18,105)">Sales ↑</text>

  <!-- ─── PIE / DONUT CHART ─── -->
  <rect x="450" y="5" width="440" height="190" rx="6" fill="#0A0A0A" stroke="#FF4500" stroke-width="0.8"/>
  <text x="670" y="22" text-anchor="middle" class="pb" font-size="10" fill="#FF4500" letter-spacing="2">PIE CHART · SALES BY REGION</text>
  <line x1="460" y1="30" x2="882" y2="30" stroke="#FF4500" stroke-width="0.4" opacity="0.3"/>

  <!-- Donut slices (using path arcs) -->
  <!-- Center: 570, 105 r=65 -->
  <!-- North: 21% ~75deg, South: 22% ~80deg, East: 20% ~72deg, West: 21% ~76deg, Central: 18% ~65deg -->
  <!-- Outer r=65 inner r=35 -->
  <!-- N: 0→75  S: 75→155  E: 155→227  W: 227→303  C: 303→368 (=368°) -->

  <!-- North - #00FF41 -->
  <path d="M570,40 A65,65 0 0,1 623,58 L603,75 A35,35 0 0,0 570,70 Z" fill="#00FF41" opacity="0.85" class="pie"/>
  <!-- South - #00E5FF -->
  <path d="M623,58 A65,65 0 0,1 604,152 L585,132 A35,35 0 0,0 603,75 Z" fill="#00E5FF" opacity="0.85" class="pie"/>
  <!-- East - #BD00FF -->
  <path d="M604,152 A65,65 0 0,1 519,148 L535,128 A35,35 0 0,0 585,132 Z" fill="#BD00FF" opacity="0.85" class="pie"/>
  <!-- West - #FFD700 -->
  <path d="M519,148 A65,65 0 0,1 517,60 L535,82 A35,35 0 0,0 535,128 Z" fill="#FFD700" opacity="0.85" class="pie"/>
  <!-- Central - #FF4500 -->
  <path d="M517,60 A65,65 0 0,1 570,40 L570,70 A35,35 0 0,0 535,82 Z" fill="#FF4500" opacity="0.85" class="pie"/>

  <!-- Donut hole -->
  <circle cx="570" cy="100" r="34" fill="#0A0A0A"/>
  <text x="570" y="97"  text-anchor="middle" class="pb" font-size="9"  fill="#FF4500">Sales</text>
  <text x="570" y="110" text-anchor="middle" class="pb" font-size="8"  fill="#FF4500" opacity="0.7">Region</text>

  <!-- Legend -->
  <rect x="660" y="50" width="10" height="10" rx="2" fill="#00FF41"/>
  <text x="675" y="60" class="pb" font-size="9" fill="#00FF41">North (21%)</text>
  <rect x="660" y="70" width="10" height="10" rx="2" fill="#00E5FF"/>
  <text x="675" y="80" class="pb" font-size="9" fill="#00E5FF">South (22%)</text>
  <rect x="660" y="90" width="10" height="10" rx="2" fill="#BD00FF"/>
  <text x="675" y="100" class="pb" font-size="9" fill="#BD00FF">East  (20%)</text>
  <rect x="660" y="110" width="10" height="10" rx="2" fill="#FFD700"/>
  <text x="675" y="120" class="pb" font-size="9" fill="#FFD700">West  (21%)</text>
  <rect x="660" y="130" width="10" height="10" rx="2" fill="#FF4500"/>
  <text x="675" y="140" class="pb" font-size="9" fill="#FF4500">Central(18%)</text>
</svg>

</div>

---

## `// 04` · CLASS ARCHITECTURE

<div align="center">

<svg width="900" height="380" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      .ab { font-family: 'Courier New', monospace; }
      @keyframes arrowPulse { 0%,100%{opacity:.6} 50%{opacity:1} }
      .ap { animation: arrowPulse 2s ease-in-out infinite; }
    </style>
    <marker id="arrow" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#00E5FF" opacity="0.8"/>
    </marker>
    <marker id="arrow2" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#00FF41" opacity="0.8"/>
    </marker>
  </defs>
  <rect width="900" height="380" fill="#050505"/>

  <!-- ═══ MAIN CLASS BOX ═══ -->
  <rect x="270" y="10" width="360" height="340" rx="8" fill="#0A0A0A" stroke="#00E5FF" stroke-width="1.5"/>

  <!-- Class header -->
  <rect x="270" y="10" width="360" height="40" rx="8" fill="#001020" stroke="#00E5FF" stroke-width="1.5"/>
  <rect x="270" y="40" width="360" height="10" fill="#001020"/>
  <text x="450" y="35" text-anchor="middle" class="ab" font-size="14" fill="#00E5FF" font-weight="bold" letter-spacing="2">SalesDataFrame</text>

  <!-- Divider -->
  <line x1="270" y1="58" x2="630" y2="58" stroke="#00E5FF" stroke-width="0.8" opacity="0.6"/>

  <!-- Attributes -->
  <text x="280" y="73" class="ab" font-size="9" fill="#00E5FF" opacity="0.5">— ATTRIBUTES —</text>
  <text x="285" y="88"  class="ab" font-size="10" fill="#00FFAA">◆ self.data : DataFrame | None</text>

  <!-- Divider 2 -->
  <line x1="270" y1="98" x2="630" y2="98" stroke="#00E5FF" stroke-width="0.8" opacity="0.4"/>

  <!-- Methods -->
  <text x="280" y="112" class="ab" font-size="9" fill="#00E5FF" opacity="0.5">— METHODS —</text>

  <!-- Init / Destructor -->
  <text x="285" y="127" class="ab" font-size="9.5" fill="#00FF41">+ __init__(self)</text>
  <text x="285" y="141" class="ab" font-size="9.5" fill="#00FF41">+ __del__(self)</text>

  <line x1="280" y1="148" x2="620" y2="148" stroke="#00E5FF" stroke-width="0.3" stroke-dasharray="4,4" opacity="0.3"/>

  <!-- Core ops -->
  <text x="285" y="162" class="ab" font-size="9.5" fill="#00FFAA">+ load(filepath: str)</text>
  <text x="285" y="176" class="ab" font-size="9.5" fill="#00FFAA">+ explore(option: int)</text>
  <text x="285" y="190" class="ab" font-size="9.5" fill="#00FFAA">+ mathematical(col: str)</text>
  <text x="285" y="204" class="ab" font-size="9.5" fill="#00FFAA">+ handle_missing(...)</text>
  <text x="285" y="218" class="ab" font-size="9.5" fill="#00FFAA">+ descriptive_statistics()</text>

  <line x1="280" y1="225" x2="620" y2="225" stroke="#00E5FF" stroke-width="0.3" stroke-dasharray="4,4" opacity="0.3"/>

  <!-- DataFrame ops -->
  <text x="285" y="239" class="ab" font-size="9.5" fill="#BD00FF">+ combine(other, how, on)</text>
  <text x="285" y="253" class="ab" font-size="9.5" fill="#BD00FF">+ split(col, value, regex)</text>
  <text x="285" y="267" class="ab" font-size="9.5" fill="#BD00FF">+ search_sort(col, value, ...)</text>
  <text x="285" y="281" class="ab" font-size="9.5" fill="#BD00FF">+ filter(col, condition, value)</text>
  <text x="285" y="295" class="ab" font-size="9.5" fill="#BD00FF">+ aggregate(col, func)</text>
  <text x="285" y="309" class="ab" font-size="9.5" fill="#BD00FF">+ create_pivot(index, col, val)</text>

  <line x1="280" y1="316" x2="620" y2="316" stroke="#00E5FF" stroke-width="0.3" stroke-dasharray="4,4" opacity="0.3"/>

  <!-- Viz ops -->
  <text x="285" y="330" class="ab" font-size="9.5" fill="#FFD700">+ visualize_*(...)  · save_visualization(path)</text>

  <!-- Left annotation: Attributes -->
  <rect x="10" y="60" width="220" height="80" rx="5" fill="#0A0A0A" stroke="#00FF41" stroke-width="0.8"/>
  <text x="120" y="78" text-anchor="middle" class="ab" font-size="9" fill="#00FF41" opacity="0.7">ENCAPSULATION</text>
  <text x="20" y="95"  class="ab" font-size="8.5" fill="#00FF41">→ self.data hidden inside class</text>
  <text x="20" y="108" class="ab" font-size="8.5" fill="#00FF41">→ All access via methods</text>
  <text x="20" y="121" class="ab" font-size="8.5" fill="#00FF41">→ No direct attribute exposure</text>
  <line x1="230" y1="100" x2="270" y2="100" stroke="#00FF41" stroke-width="1" stroke-dasharray="4,3" marker-end="url(#arrow2)" class="ap"/>

  <!-- Right annotation: OOP -->
  <rect x="660" y="60" width="230" height="80" rx="5" fill="#0A0A0A" stroke="#BD00FF" stroke-width="0.8"/>
  <text x="775" y="78" text-anchor="middle" class="ab" font-size="9" fill="#BD00FF" opacity="0.7">OOP PRINCIPLES</text>
  <text x="670" y="95"  class="ab" font-size="8.5" fill="#BD00FF">→ Constructor / Destructor</text>
  <text x="670" y="108" class="ab" font-size="8.5" fill="#BD00FF">→ Method overloading pattern</text>
  <text x="670" y="121" class="ab" font-size="8.5" fill="#BD00FF">→ Operator override (__del__)</text>
  <line x1="630" y1="100" x2="660" y2="100" stroke="#BD00FF" stroke-width="1" stroke-dasharray="4,3" marker-end="url(#arrow)" class="ap"/>

  <!-- Bottom annotation: Viz -->
  <rect x="160" y="360" width="580" height="15" rx="4" fill="#0A0A0A" stroke="#FFD700" stroke-width="0.6"/>
  <text x="450" y="372" text-anchor="middle" class="ab" font-size="8" fill="#FFD700" opacity="0.8">
    visualize_bar · visualize_line · visualize_scatter · visualize_pie · visualize_histogram · visualize_heatmap · visualize_stack · visualize_boxplot · visualize_violin · multiple_plots
  </text>
</svg>

</div>

---

## `// 05` · TECH STACK

<div align="center">

<svg width="900" height="80" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      .tb { font-family: 'Courier New', monospace; }
      @keyframes techpulse { 0%,100%{opacity:0.7} 50%{opacity:1} }
      .tp0{animation:techpulse 2.0s 0.0s ease-in-out infinite}
      .tp1{animation:techpulse 2.0s 0.3s ease-in-out infinite}
      .tp2{animation:techpulse 2.0s 0.6s ease-in-out infinite}
      .tp3{animation:techpulse 2.0s 0.9s ease-in-out infinite}
      .tp4{animation:techpulse 2.0s 1.2s ease-in-out infinite}
      .tp5{animation:techpulse 2.0s 1.5s ease-in-out infinite}
    </style>
  </defs>
  <rect width="900" height="80" fill="#050505"/>

  <rect x="10"  y="10" width="130" height="60" rx="6" fill="#0D1A0D" stroke="#00FF41" stroke-width="1" class="tp0"/>
  <text x="75"  y="35" text-anchor="middle" class="tb" font-size="18" fill="#00FF41">🐍</text>
  <text x="75"  y="55" text-anchor="middle" class="tb" font-size="10" fill="#00FF41">Python 3.8+</text>

  <rect x="158" y="10" width="130" height="60" rx="6" fill="#001020" stroke="#00E5FF" stroke-width="1" class="tp1"/>
  <text x="223" y="35" text-anchor="middle" class="tb" font-size="18" fill="#00E5FF">🐼</text>
  <text x="223" y="55" text-anchor="middle" class="tb" font-size="10" fill="#00E5FF">Pandas 2.x</text>

  <rect x="306" y="10" width="130" height="60" rx="6" fill="#150020" stroke="#BD00FF" stroke-width="1" class="tp2"/>
  <text x="371" y="35" text-anchor="middle" class="tb" font-size="18" fill="#BD00FF">🔢</text>
  <text x="371" y="55" text-anchor="middle" class="tb" font-size="10" fill="#BD00FF">NumPy 1.x</text>

  <rect x="454" y="10" width="130" height="60" rx="6" fill="#1A1200" stroke="#FFD700" stroke-width="1" class="tp3"/>
  <text x="519" y="35" text-anchor="middle" class="tb" font-size="18" fill="#FFD700">📊</text>
  <text x="519" y="55" text-anchor="middle" class="tb" font-size="10" fill="#FFD700">Matplotlib 3.x</text>

  <rect x="602" y="10" width="130" height="60" rx="6" fill="#1A0500" stroke="#FF4500" stroke-width="1" class="tp4"/>
  <text x="667" y="35" text-anchor="middle" class="tb" font-size="18" fill="#FF4500">🎨</text>
  <text x="667" y="55" text-anchor="middle" class="tb" font-size="10" fill="#FF4500">Seaborn 0.x</text>

  <rect x="750" y="10" width="140" height="60" rx="6" fill="#10001A" stroke="#EE82EE" stroke-width="1" class="tp5"/>
  <text x="820" y="35" text-anchor="middle" class="tb" font-size="18" fill="#EE82EE">📓</text>
  <text x="820" y="55" text-anchor="middle" class="tb" font-size="10" fill="#EE82EE">Jupyter Notebook</text>
</svg>

</div>

---

## `// 06` · DATASET SCHEMA

<div align="center">

<svg width="900" height="200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>.ds{font-family:'Courier New',monospace;}</style>
  </defs>
  <rect width="900" height="200" fill="#050505"/>

  <!-- Header -->
  <rect x="10" y="10" width="880" height="30" rx="4" fill="#001020" stroke="#00E5FF" stroke-width="0.8"/>
  <text x="50"  y="29" class="ds" font-size="11" fill="#00E5FF" font-weight="bold">COLUMN</text>
  <text x="220" y="29" class="ds" font-size="11" fill="#00E5FF" font-weight="bold">DTYPE</text>
  <text x="350" y="29" class="ds" font-size="11" fill="#00E5FF" font-weight="bold">RANGE / VALUES</text>
  <text x="580" y="29" class="ds" font-size="11" fill="#00E5FF" font-weight="bold">DESCRIPTION</text>

  <!-- Row 1 -->
  <rect x="10" y="42" width="880" height="28" rx="2" fill="#0A0A0A" stroke="#003030" stroke-width="0.5"/>
  <text x="50"  y="61" class="ds" font-size="10" fill="#00FFAA">SalesID</text>
  <text x="220" y="61" class="ds" font-size="10" fill="#BD00FF">int64</text>
  <text x="350" y="61" class="ds" font-size="10" fill="#FFD700">1 → 200</text>
  <text x="580" y="61" class="ds" font-size="10" fill="#888">Unique sequential identifier</text>

  <!-- Row 2 -->
  <rect x="10" y="72" width="880" height="28" rx="2" fill="#050508" stroke="#003030" stroke-width="0.5"/>
  <text x="50"  y="91" class="ds" font-size="10" fill="#00FFAA">Product</text>
  <text x="220" y="91" class="ds" font-size="10" fill="#BD00FF">object</text>
  <text x="350" y="91" class="ds" font-size="10" fill="#FFD700">Product A–E</text>
  <text x="580" y="91" class="ds" font-size="10" fill="#888">Product category (5 types)</text>

  <!-- Row 3 -->
  <rect x="10" y="102" width="880" height="28" rx="2" fill="#0A0A0A" stroke="#003030" stroke-width="0.5"/>
  <text x="50"  y="121" class="ds" font-size="10" fill="#00FFAA">Region</text>
  <text x="220" y="121" class="ds" font-size="10" fill="#BD00FF">object</text>
  <text x="350" y="121" class="ds" font-size="10" fill="#FFD700">North/South/East/West/Central</text>
  <text x="580" y="121" class="ds" font-size="10" fill="#888">Geographic sales region</text>

  <!-- Row 4 -->
  <rect x="10" y="132" width="880" height="28" rx="2" fill="#050508" stroke="#003030" stroke-width="0.5"/>
  <text x="50"  y="151" class="ds" font-size="10" fill="#00FFAA">Sales</text>
  <text x="220" y="151" class="ds" font-size="10" fill="#BD00FF">int64</text>
  <text x="350" y="151" class="ds" font-size="10" fill="#FFD700">108 → 997 (mean ≈ 550)</text>
  <text x="580" y="151" class="ds" font-size="10" fill="#888">Revenue in units (synthetic)</text>

  <!-- Row 5 -->
  <rect x="10" y="162" width="880" height="28" rx="2" fill="#0A0A0A" stroke="#003030" stroke-width="0.5"/>
  <text x="50"  y="181" class="ds" font-size="10" fill="#00FFAA">Year</text>
  <text x="220" y="181" class="ds" font-size="10" fill="#BD00FF">int64</text>
  <text x="350" y="181" class="ds" font-size="10" fill="#FFD700">2021 · 2022 · 2023</text>
  <text x="580" y="181" class="ds" font-size="10" fill="#888">Fiscal year of the sale</text>
</svg>

</div>

---

## `// 07` · INSTALLATION

```bash
# Clone or navigate to project directory
cd visualizer/

# Install dependencies
pip install pandas numpy matplotlib seaborn jupyter

# Run the CLI program
python sales_data_analyzer.py

# Launch Jupyter Notebook
jupyter notebook sales_data_analyzer.ipynb
```

---

## `// 08` · CONSOLE INTERACTION

<div align="center">

<svg width="900" height="370" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      .cb  { font-family: 'Courier New', monospace; }
      @keyframes cursor { 0%,100%{opacity:1} 50%{opacity:0} }
      .cur { animation: cursor 1s step-end infinite; }
      @keyframes typein { from{opacity:0} to{opacity:1} }
      .ti  { animation: typein 0.5s ease-in forwards; }
    </style>
  </defs>

  <!-- Terminal window -->
  <rect width="900" height="370" rx="10" fill="#0D0D0D" stroke="#00FF41" stroke-width="1"/>

  <!-- Title bar -->
  <rect width="900" height="30" rx="10" fill="#1A1A1A"/>
  <rect y="20" width="900" height="10" fill="#1A1A1A"/>
  <circle cx="20" cy="15" r="6" fill="#FF4500" opacity="0.9"/>
  <circle cx="40" cy="15" r="6" fill="#FFD700" opacity="0.9"/>
  <circle cx="60" cy="15" r="6" fill="#00FF41" opacity="0.9"/>
  <text x="450" y="20" text-anchor="middle" class="cb" font-size="10" fill="#888">sales_data_analyzer.py — bash</text>

  <!-- Content -->
  <!-- Header -->
  <text x="20" y="55"  class="cb" font-size="10" fill="#00FF41">========== Data Analytic &amp; Visualization Program ==========</text>
  <text x="20" y="70"  class="cb" font-size="10" fill="#00E5FF">Please select an option:</text>
  <text x="20" y="85"  class="cb" font-size="10" fill="#888">1. Load Dataset</text>
  <text x="20" y="99"  class="cb" font-size="10" fill="#888">2. Explore Data</text>
  <text x="20" y="113" class="cb" font-size="10" fill="#888">3. Perform DataFrame Operations</text>
  <text x="20" y="127" class="cb" font-size="10" fill="#888">4. Handle Missing Data</text>
  <text x="20" y="141" class="cb" font-size="10" fill="#888">5. Generate Descriptive Statistics</text>
  <text x="20" y="155" class="cb" font-size="10" fill="#888">6. Data Visualization</text>
  <text x="20" y="169" class="cb" font-size="10" fill="#888">7. Save Visualization</text>
  <text x="20" y="183" class="cb" font-size="10" fill="#888">8. Exit</text>
  <text x="20" y="197" class="cb" font-size="10" fill="#00FF41">===========================================================</text>

  <text x="20" y="215" class="cb" font-size="10" fill="#00E5FF">Enter your choice: <tspan fill="#00FF41">1</tspan></text>
  <text x="20" y="231" class="cb" font-size="10" fill="#888">-- Load Dataset --</text>
  <text x="20" y="247" class="cb" font-size="10" fill="#00E5FF">Enter the path of the dataset (CSV file): data/<tspan fill="#00FF41">sales_data.csv</tspan></text>
  <text x="20" y="263" class="cb" font-size="10" fill="#00FFAA">Dataset loaded successfully!</text>

  <line x1="10" y1="275" x2="890" y2="275" stroke="#00FF41" stroke-width="0.4" stroke-dasharray="4,4" opacity="0.3"/>

  <text x="20" y="292" class="cb" font-size="10" fill="#00E5FF">Enter your choice: <tspan fill="#00FF41">2</tspan></text>
  <text x="20" y="308" class="cb" font-size="10" fill="#888">-- Explore Data --  →  <tspan fill="#00FF41">1. Display the first 5 rows</tspan></text>

  <text x="20" y="325" class="cb" font-size="10" fill="#555">   SalesID    Product   Region  Sales  Year</text>
  <text x="20" y="339" class="cb" font-size="10" fill="#00FFAA">0        1  Product D    South    755  2021</text>
  <text x="20" y="353" class="cb" font-size="10" fill="#00FFAA">1        2  Product E     East    534  2023</text>

  <!-- Cursor -->
  <text x="20" y="368" class="cb" font-size="10" fill="#00FF41">$ <tspan class="cur">█</tspan></text>
</svg>

</div>

---

## `// 09` · PROJECT STRUCTURE

```
visualizer/
│
├── 📓 sales_data_analyzer.ipynb    ← Jupyter Notebook (cell-by-cell execution)
├── 🐍 sales_data_analyzer.py       ← CLI Python program (menu-driven)
│
└── 📁 data/
    └── 📄 sales_data.csv           ← Synthetic dataset (200 rows × 5 cols)
```

---

## `// 10` · PROGRAM FLOW

<div align="center">

<svg width="900" height="170" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>.fb{font-family:'Courier New',monospace;}</style>
    <marker id="fa" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0,8 3,0 6" fill="#00FF41" opacity="0.8"/>
    </marker>
  </defs>
  <rect width="900" height="170" fill="#050505"/>

  <!-- Nodes -->
  <rect x="10"  y="60" width="100" height="45" rx="5" fill="#0D1A0D" stroke="#00FF41" stroke-width="1"/>
  <text x="60"  y="78" text-anchor="middle" class="fb" font-size="9" fill="#00FF41">START</text>
  <text x="60"  y="94" text-anchor="middle" class="fb" font-size="8" fill="#00FF41" opacity="0.7">main()</text>

  <line x1="110" y1="82" x2="145" y2="82" stroke="#00FF41" stroke-width="1" marker-end="url(#fa)"/>

  <rect x="145" y="55" width="110" height="55" rx="5" fill="#001020" stroke="#00E5FF" stroke-width="1"/>
  <text x="200" y="76" text-anchor="middle" class="fb" font-size="9" fill="#00E5FF">LOAD CSV</text>
  <text x="200" y="90" text-anchor="middle" class="fb" font-size="8" fill="#00E5FF" opacity="0.7">sdf.load()</text>
  <text x="200" y="103" text-anchor="middle" class="fb" font-size="7" fill="#00E5FF" opacity="0.5">SalesDataFrame</text>

  <line x1="255" y1="82" x2="290" y2="82" stroke="#00E5FF" stroke-width="1" marker-end="url(#fa)"/>

  <rect x="290" y="55" width="110" height="55" rx="5" fill="#150020" stroke="#BD00FF" stroke-width="1"/>
  <text x="345" y="76" text-anchor="middle" class="fb" font-size="9" fill="#BD00FF">EXPLORE</text>
  <text x="345" y="90" text-anchor="middle" class="fb" font-size="8" fill="#BD00FF" opacity="0.7">.explore()</text>
  <text x="345" y="103" text-anchor="middle" class="fb" font-size="7" fill="#BD00FF" opacity="0.5">head/tail/info</text>

  <line x1="400" y1="82" x2="435" y2="82" stroke="#BD00FF" stroke-width="1" marker-end="url(#fa)"/>

  <rect x="435" y="55" width="110" height="55" rx="5" fill="#1A1200" stroke="#FFD700" stroke-width="1"/>
  <text x="490" y="76" text-anchor="middle" class="fb" font-size="9" fill="#FFD700">PROCESS</text>
  <text x="490" y="90" text-anchor="middle" class="fb" font-size="8" fill="#FFD700" opacity="0.7">ops/stats/clean</text>
  <text x="490" y="103" text-anchor="middle" class="fb" font-size="7" fill="#FFD700" opacity="0.5">math/filter/agg</text>

  <line x1="545" y1="82" x2="580" y2="82" stroke="#FFD700" stroke-width="1" marker-end="url(#fa)"/>

  <rect x="580" y="55" width="110" height="55" rx="5" fill="#1A0500" stroke="#FF4500" stroke-width="1"/>
  <text x="635" y="76" text-anchor="middle" class="fb" font-size="9" fill="#FF4500">VISUALIZE</text>
  <text x="635" y="90" text-anchor="middle" class="fb" font-size="8" fill="#FF4500" opacity="0.7">.visualize_*()</text>
  <text x="635" y="103" text-anchor="middle" class="fb" font-size="7" fill="#FF4500" opacity="0.5">plot/seaborn/hmap</text>

  <line x1="690" y1="82" x2="725" y2="82" stroke="#FF4500" stroke-width="1" marker-end="url(#fa)"/>

  <rect x="725" y="55" width="110" height="55" rx="5" fill="#0A1A00" stroke="#7FFF00" stroke-width="1"/>
  <text x="780" y="76" text-anchor="middle" class="fb" font-size="9" fill="#7FFF00">SAVE / EXIT</text>
  <text x="780" y="90" text-anchor="middle" class="fb" font-size="8" fill="#7FFF00" opacity="0.7">.save_viz()</text>
  <text x="780" y="103" text-anchor="middle" class="fb" font-size="7" fill="#7FFF00" opacity="0.5">PNG export</text>

  <line x1="835" y1="82" x2="870" y2="82" stroke="#7FFF00" stroke-width="1" marker-end="url(#fa)"/>

  <rect x="870" y="64" width="22" height="35" rx="4" fill="#0A0A0A" stroke="#00FF41" stroke-width="0.8"/>
  <text x="881" y="87" text-anchor="middle" class="fb" font-size="7" fill="#00FF41" writing-mode="tb">END</text>

  <!-- Loop back arrow -->
  <path d="M490,110 Q490,150 345,150 Q200,150 200,110" fill="none" stroke="#00FF41" stroke-width="0.8" stroke-dasharray="4,3" opacity="0.4" marker-end="url(#fa)"/>
  <text x="345" y="163" text-anchor="middle" class="fb" font-size="8" fill="#00FF41" opacity="0.5">← loop until Exit (choice 8)</text>
</svg>

</div>

---

## `// 11` · OOP PRINCIPLES APPLIED

<div align="center">

<svg width="900" height="100" xmlns="http://www.w3.org/2000/svg">
  <defs><style>.ob{font-family:'Courier New',monospace;}</style></defs>
  <rect width="900" height="100" fill="#050505"/>

  <rect x="10"  y="10" width="205" height="80" rx="6" fill="#0D1A0D" stroke="#00FF41" stroke-width="0.8"/>
  <text x="112" y="32" text-anchor="middle" class="ob" font-size="10" fill="#00FF41" font-weight="bold">ENCAPSULATION</text>
  <text x="20"  y="52" class="ob" font-size="8.5" fill="#00FF41" opacity="0.8">→ Data wrapped in SalesDataFrame</text>
  <text x="20"  y="65" class="ob" font-size="8.5" fill="#00FF41" opacity="0.8">→ State managed via self.data</text>
  <text x="20"  y="78" class="ob" font-size="8.5" fill="#00FF41" opacity="0.8">→ Controlled access through methods</text>

  <rect x="228" y="10" width="205" height="80" rx="6" fill="#001020" stroke="#00E5FF" stroke-width="0.8"/>
  <text x="330" y="32" text-anchor="middle" class="ob" font-size="10" fill="#00E5FF" font-weight="bold">ABSTRACTION</text>
  <text x="238" y="52" class="ob" font-size="8.5" fill="#00E5FF" opacity="0.8">→ Complex ops hidden behind methods</text>
  <text x="238" y="65" class="ob" font-size="8.5" fill="#00E5FF" opacity="0.8">→ User calls .visualize_bar() simply</text>
  <text x="238" y="78" class="ob" font-size="8.5" fill="#00E5FF" opacity="0.8">→ Internals not exposed to caller</text>

  <rect x="446" y="10" width="205" height="80" rx="6" fill="#150020" stroke="#BD00FF" stroke-width="0.8"/>
  <text x="548" y="32" text-anchor="middle" class="ob" font-size="10" fill="#BD00FF" font-weight="bold">CONSTRUCTOR / DESTRUCTOR</text>
  <text x="456" y="52" class="ob" font-size="8.5" fill="#BD00FF" opacity="0.8">→ __init__ sets self.data = None</text>
  <text x="456" y="65" class="ob" font-size="8.5" fill="#BD00FF" opacity="0.8">→ __del__ releases data from memory</text>
  <text x="456" y="78" class="ob" font-size="8.5" fill="#BD00FF" opacity="0.8">→ Object lifecycle fully managed</text>

  <rect x="664" y="10" width="226" height="80" rx="6" fill="#1A1200" stroke="#FFD700" stroke-width="0.8"/>
  <text x="777" y="32" text-anchor="middle" class="ob" font-size="10" fill="#FFD700" font-weight="bold">REUSABILITY</text>
  <text x="674" y="52" class="ob" font-size="8.5" fill="#FFD700" opacity="0.8">→ Instantiate multiple SalesDataFrame</text>
  <text x="674" y="65" class="ob" font-size="8.5" fill="#FFD700" opacity="0.8">→ combine() merges two instances</text>
  <text x="674" y="78" class="ob" font-size="8.5" fill="#FFD700" opacity="0.8">→ Works on any valid CSV dataset</text>
</svg>

</div>

---

## `// 12` · ASSUMPTIONS

- Dataset must be in **CSV format** with headers in the first row.
- When no dataset file is found, a **200-row synthetic dataset** is auto-generated at `data/sales_data.csv`.
- Mathematical and statistical operations apply to **numeric columns only**; non-numeric columns are skipped automatically.
- All visualizations default to `plt.show()` in CLI mode; in Jupyter, `%matplotlib inline` is active.
- Missing value handling is **non-destructive** by default — the user selects the strategy interactively.

---

<!-- ═══════════════════════════════════════════════════════════ -->
<!--                       FOOTER SVG                          -->
<!-- ═══════════════════════════════════════════════════════════ -->

<div align="center">

<svg width="900" height="80" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      .foot{font-family:'Courier New',monospace;}
      @keyframes footscan{0%{transform:translateX(-900px)}100%{transform:translateX(900px)}}
      .fscan{animation:footscan 6s linear infinite;opacity:.05}
      @keyframes glof{0%,100%{opacity:.9}50%{opacity:.6}}
      .gf{animation:glof 2.5s ease-in-out infinite}
    </style>
    <linearGradient id="fg1" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%"   stop-color="#00FF41" stop-opacity="0"/>
      <stop offset="20%"  stop-color="#00FF41" stop-opacity="1"/>
      <stop offset="80%"  stop-color="#00E5FF" stop-opacity="1"/>
      <stop offset="100%" stop-color="#00E5FF" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <rect width="900" height="80" fill="#000000"/>
  <rect class="fscan" x="0" y="0" width="200" height="80" fill="#00FF41"/>
  <rect x="0" y="0" width="900" height="1" fill="url(#fg1)" opacity="0.6"/>
  <rect x="0" y="79" width="900" height="1" fill="url(#fg1)" opacity="0.6"/>
  <text x="450" y="28" text-anchor="middle" class="foot gf" font-size="13" fill="#00FF41" letter-spacing="3" font-weight="bold">
    ◈ PANDAS ANALYZER &amp; DATA VISUALIZATION ◈
  </text>
  <text x="450" y="47" text-anchor="middle" class="foot" font-size="9" fill="#00E5FF" opacity="0.7" letter-spacing="4">
    PYTHON · DATA ANALYSIS · BRING ON YOUR CODING ATTITUDE
  </text>
  <text x="450" y="65" text-anchor="middle" class="foot" font-size="8" fill="#00FF41" opacity="0.4" letter-spacing="2">
    Quality is our Motto. · Shaping skills for scaling higher.
  </text>
</svg>

</div>

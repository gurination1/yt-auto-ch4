import os
try:
    from dotenv import load_dotenv
    load_dotenv()
    for ep in [".env", "../.env", "../../.env", "/mnt/g/yt-auto-fleet/.env"]:
        if os.path.exists(ep):
            load_dotenv(ep, override=False)
except Exception:
    pass

# Auto-load local_env.sh if present to populate environment variables
def _autoload_local_env():
    for env_path in [".env", "local_env.sh", "../local_env.sh",  "/root/local_env.sh"]:
        if os.path.exists(env_path):
            try:
                with open(env_path, "r", encoding="utf-8") as f:
                    for line in f:
                        line = line.strip()
                        if not line or line.startswith("#"):
                            continue
                        if line.startswith("export "):
                            line = line[7:]
                        if "=" in line:
                            k, v = line.split("=", 1)
                            k = k.strip()
                            v = v.strip().strip('"').strip("'")
                            if k and k not in os.environ and v:
                                os.environ[k] = v
            except Exception:
                pass

_autoload_local_env()

# ── Gemini Key Pool ──────────────────────────────────────────────────────────
def _load_keys() -> list[str]:
    keys: list[str] = []
    multi = os.environ.get("GEMINI_API_KEYS", "").strip()
    if multi:
        keys.extend(k.strip() for k in multi.split(",") if k.strip())
    single = os.environ.get("GEMINI_API_KEY", "").strip()
    if single and not keys:
        keys.append(single)
    return list(dict.fromkeys(keys))

GEMINI_API_KEYS: list[str] = _load_keys()
GEMINI_API_KEY: str = GEMINI_API_KEYS[0] if GEMINI_API_KEYS else ""

GEMINI_JUDGE_API_KEY: str = os.environ.get("GEMINI_JUDGE_API_KEY", "").strip() or GEMINI_API_KEY

# ── Other APIs ───────────────────────────────────────────────────────────────
PEXELS_API_KEY   = os.environ.get("PEXELS_API_KEY", "")
PIXABAY_API_KEY  = os.environ.get("PIXABAY_API_KEY", "")
COVERR_API_KEY   = os.environ.get("COVERR_API_KEY", "")
NASA_API_KEY     = os.environ.get("NASA_API_KEY", "DEMO_KEY")
KLIPY_API_KEY    = os.environ.get("KLIPY_API_KEY", "")
FREESOUND_API_KEY = os.environ.get("FREESOUND_API_KEY", "")

# ── YouTube OAuth ────────────────────────────────────────────────────────────
YT_CLIENT_ID     = os.environ.get("YT_CLIENT_ID", "")
YT_CLIENT_SECRET = os.environ.get("YT_CLIENT_SECRET", "")
YT_REFRESH_TOKEN = os.environ.get("YT_REFRESH_TOKEN", "")

# ── Gemini Models ────────────────────────────────────────────────────────────
GEMINI_FLASH        = "gemini-3.6-flash"
GEMINI_FLASH_BACKUP = "gemini-3.5-flash-lite"
GEMINI_PRO          = "gemini-3.6-flash"
GEMINI_TTS_MODEL    = "gemini-2.5-flash-preview-tts"
GEMINI_API_BASE     = "https://generativelanguage.googleapis.com/v1beta"

GEMINI_VOICES    = ["Fenrir", "Puck", "Charon", "Orus", "Kore", "Aoede"]
EDGE_VOICES      = ["en-US-GuyNeural", "en-US-AndrewNeural", "en-US-ChristopherNeural", "en-US-EricNeural", "en-US-BrianNeural", "en-US-AvaNeural", "en-US-EmmaNeural", "en-US-SteffanNeural"]
KOKORO_VOICES    = ["af_heart","af_bella","af_nicole","af_sarah","af_sky","af_aoede","am_adam","am_michael","am_fenrir","am_puck"]

# ── Video Specs ──────────────────────────────────────────────────────────────
SHORTS_W, SHORTS_H = 1080, 1920
LONG_W,   LONG_H   = 1920, 1080
FPS                 = 30
TOPIC_LOG_SIZE      = 90

HOOK_PATTERNS = [
    "The {topic} fact that breaks a rule you learned in school",
    "In exactly 30 seconds you'll never see {topic} the same way",
    "Scientists found something inside {topic} that shouldn't exist",
    "The {topic} detail that 99% of people never notice — even experts",
    "What {topic} does when no one is watching will disturb you",
    "The one thing about {topic} that every textbook gets wrong",
    "This single {topic} fact overturns 100 years of assumptions",
    "You've seen {topic} your whole life. You've never actually seen it.",
]

THUMBNAIL_LAYOUTS = [
    "dark_top_bar",
    "centered_gradient",
    "bottom_third",
    "split_left",
]

# ── Channel Boundary & Topic Isolation (Channel 4: Marvel Engeneering - Engineering Marvels & How It Works) ──
CHANNEL_NICHE = os.environ.get("CHANNEL_NICHE", "engineering")

CHANNEL_BOUNDARY = {
    "channel_id": "ch4",
    "name": "Channel 4: Marvel Engeneering (Engineering Marvels & How It Works)",
    "niche_description": "Colossal machines, extreme mechanisms, how things work under extreme physical forces, heavy industrial equipment, impossible structural megaprojects, and mind-blowing kinetic feats.",
    "allowed_subclusters": [
        "extreme kinetic and aerospace mechanics: aircraft carrier catapults, jet engine thrust reversers, turbopumps, and hypersonic wind tunnels",
        "subterranean and subsea engineering marvels: liquid nitrogen ground-freezing TBMs, undersea immersed tubes, and earthquake-proof base isolators",
        "colossal heavy-lifting machinery: Bagger 293 bucket-wheel excavators, crawler-transporters, and semi-submersible heavy-lift vessels",
        "supertall skyscraper physics and wind damping: tuned mass dampers, aerodynamic vortex shedding, and high-speed elevator counterweights",
        "hydraulic and nautical marvels: Panama Canal gravity water locks, Delta Works storm surge barriers, and dry dock hydraulic gates"
    ],
    "strict_negative_constraints": [
        "NO space astronomy, astrophysics, deep space telescopes, or black holes.",
        "NO financial markets, corporate trading, crypto, hedge funds, or business strategy.",
        "NO wildlife documentaries, zoology, animals, insects, or plant biology.",
        "NO ancient warfare, Roman legions, swords, or medieval castles.",
        "NO ghosts, supernatural folklore, UFOs, cryptids, or alien conspiracies."
    ],
    "negative_keywords": [
        "astronomy", "astrophysics", "telescope", "james webb", "black hole", "cosmology", "galaxy", "supernova",
        "crypto", "bitcoin", "ethereum", "stock market", "hedge fund", "private equity", "tax-loss", "wall street", "venture capital",
        "wildlife documentary", "zoology", "apex predator", "venomous snake", "insect swarm", "mammal species",
        "siege weapon", "roman army", "roman legion", "gladiator", "medieval battle", "ancient warfare", "siege catapult", "trebuchet",
        "ufo sighting", "alien abduction", "haunted house", "ghost ship", "bermuda triangle", "cryptid", "bigfoot"
    ]
}

CHANNEL_SUBCLUSTERS = CHANNEL_BOUNDARY["allowed_subclusters"]
SCIENCE_SUBCLUSTERS = CHANNEL_SUBCLUSTERS
NATURE_SUBCLUSTERS = CHANNEL_SUBCLUSTERS
NATURAL_WORLD_SUBCLUSTERS = CHANNEL_SUBCLUSTERS
HISTORY_SUBCLUSTERS = CHANNEL_SUBCLUSTERS
MYSTERY_SUBCLUSTERS = CHANNEL_SUBCLUSTERS
ENGINEERING_SUBCLUSTERS = CHANNEL_SUBCLUSTERS
NICHE_SUBCLUSTERS = CHANNEL_SUBCLUSTERS

YT_CATEGORY_EDUCATION = "27"
YT_CATEGORY_SCIENCE   = "28"
YT_CATEGORY_DEFAULT   = "28"
NASA_BROLL_ENABLED    = True

RICH_FALLBACK_TOPICS = [
    {
        "topic": "The Aircraft Carrier Steam Catapult: How a burst of 1,000 PSI steam hurls a 35-ton fighter jet from 0 to 165 mph in two seconds",
        "short_hook": "How do you launch a 35-ton fighter jet off a ship in two seconds flat?",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "extreme kinetic and aerospace mechanics: aircraft carrier catapults, jet engine thrust reversers, turbopumps, and hypersonic wind tunnels"
    },
    {
        "topic": "The Taipei 101 Tuned Mass Damper: How a 660-ton pendulum suspended on 8 steel cables keeps a 1,600-foot skyscraper from snapping in typhoons",
        "short_hook": "Why is there a 660-ton golden ball suspended inside this skyscraper?",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "supertall skyscraper physics and wind damping: tuned mass dampers, aerodynamic vortex shedding, and high-speed elevator counterweights"
    },
    {
        "topic": "Cryogenic Ground Freezing: How engineers freeze millions of gallons of underground water solid with liquid nitrogen to drill tunnels under rivers",
        "short_hook": "Engineers freeze entire underground rivers solid just to dig a tunnel.",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "subterranean and subsea engineering marvels: liquid nitrogen ground-freezing TBMs, undersea immersed tubes, and earthquake-proof base isolators"
    },
    {
        "topic": "The Bagger 293 Excavator: The 14,000-ton monster machine on Earth shifting 240,000 tons of earth daily with a 70-foot rotating wheel of blades",
        "short_hook": "This single machine weighs more than 30 Boeing 747s.",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "colossal heavy-lifting machinery: Bagger 293 bucket-wheel excavators, crawler-transporters, and semi-submersible heavy-lift vessels"
    },
    {
        "topic": "The Dockwise Vanguard: The semi-submersible heavy-lift ship that sinks its own deck below the ocean to scoop up 110,000-ton oil platforms",
        "short_hook": "This ship intentionally sinks itself under water to carry other ships.",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "colossal heavy-lifting machinery: Bagger 293 bucket-wheel excavators, crawler-transporters, and semi-submersible heavy-lift vessels"
    },
    {
        "topic": "Jet Engine Thrust Reversers: How titanium clamshell cascades redirect 100,000 pounds of jet exhaust forward to stop airliners on icy runways",
        "short_hook": "How does a jet engine instantly slam the brakes on ice?",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "extreme kinetic and aerospace mechanics: aircraft carrier catapults, jet engine thrust reversers, turbopumps, and hypersonic wind tunnels"
    },
    {
        "topic": "The Panama Canal Gravity Locks: How massive water gates lift 100,000-ton container ships 85 feet above sea level with zero electric water pumps",
        "short_hook": "How do 100,000-ton ships climb 85 feet over a mountain using pure gravity?",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "hydraulic and nautical marvels: Panama Canal gravity water locks, Delta Works storm surge barriers, and dry dock hydraulic gates"
    },
    {
        "topic": "The Maeslantkering Barrier: Two Eiffel-Tower-sized floating steel barrier gates that automatically swing shut to block 16-foot North Sea tidal surges",
        "short_hook": "These two floating steel gates are the size of two Eiffel Towers.",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "hydraulic and nautical marvels: Panama Canal gravity water locks, Delta Works storm surge barriers, and dry dock hydraulic gates"
    },
    {
        "topic": "Deepwater Capping Stacks: The 3-story 300-ton hydraulic steel valve lowered 5,000 feet underwater to seal high-pressure blowout oil wells",
        "short_hook": "How do you plug an erupting oil well 5,000 feet beneath the sea?",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "colossal heavy-lifting machinery: Bagger 293 bucket-wheel excavators, crawler-transporters, and semi-submersible heavy-lift vessels"
    },
    {
        "topic": "Gotthard Base Tunnel Drilling: How 400-meter-long TBMs bored 57 kilometers through boiling Alpine granite under 7,500 feet of mountain pressure",
        "short_hook": "Digging through 57 kilometers of boiling solid granite under the Alps.",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "subterranean and subsea engineering marvels: liquid nitrogen ground-freezing TBMs, undersea immersed tubes, and earthquake-proof base isolators"
    },
    {
        "topic": "High-Speed Rail Pantographs: Why overhead electric wires must zig-zag back and forth to keep train pantographs from being sliced in half",
        "short_hook": "Why do high-speed train power lines zig-zag instead of running straight?",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "extreme kinetic and aerospace mechanics: aircraft carrier catapults, jet engine thrust reversers, turbopumps, and hypersonic wind tunnels"
    },
    {
        "topic": "The Falkirk Wheel: The world's only rotating boat lift using the electric power of 8 boiling kettles to lift 600 tons of water and canal boats",
        "short_hook": "This giant rotating wheel lifts 600 tons using less power than 8 boiling kettles.",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "hydraulic and nautical marvels: Panama Canal gravity water locks, Delta Works storm surge barriers, and dry dock hydraulic gates"
    },
    {
        "topic": "Nuclear Submarine Ballast Systems: How 10,000-ton steel submarines dive 1,000 feet deep and blast high-pressure air to surface in seconds",
        "short_hook": "How does a 10,000-ton nuclear submarine surface from the deep abyss in seconds?",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "hydraulic and nautical marvels: Panama Canal gravity water locks, Delta Works storm surge barriers, and dry dock hydraulic gates"
    },
    {
        "topic": "Military Hovercraft Neoprene Skirts: How 150-ton LCAC amphibious vehicles float on low-pressure trapped air over solid land and swamp",
        "short_hook": "How can a 150-ton military vessel float over solid land without touching it?",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "extreme kinetic and aerospace mechanics: aircraft carrier catapults, jet engine thrust reversers, turbopumps, and hypersonic wind tunnels"
    },
    {
        "topic": "Burj Khalifa Vortex Shedding: How aerodynamic spiral setbacks confuse high-altitude desert winds so the world's tallest tower doesn't sway into collapse",
        "short_hook": "Why is the Burj Khalifa shaped like a spiral staircase?",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "supertall skyscraper physics and wind damping: tuned mass dampers, aerodynamic vortex shedding, and high-speed elevator counterweights"
    },
    {
        "topic": "Tokyo G-Cans Flood Cathedral: The massive subterranean surge cavern powered by 14,000-horsepower jet turbine engines to save Tokyo from monsoons",
        "short_hook": "Tokyo built an underground cathedral powered by aircraft jet engines to stop floods.",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "subterranean and subsea engineering marvels: liquid nitrogen ground-freezing TBMs, undersea immersed tubes, and earthquake-proof base isolators"
    },
    {
        "topic": "Rocket Stage Separation Pyrotechnics: How explosive bolts and solid retro-rockets fire in 5 milliseconds to jettison booster tanks at Mach 6",
        "short_hook": "How do rockets detach booster stages at Mach 6 without blowing up?",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "extreme kinetic and aerospace mechanics: aircraft carrier catapults, jet engine thrust reversers, turbopumps, and hypersonic wind tunnels"
    },
    {
        "topic": "Subsea Immersed Tube Tunneling: How 50,000-ton concrete tunnel segments are precast on land, floated to sea, and sunk into underwater trenches",
        "short_hook": "Engineers build subsea tunnels by sinking giant concrete boxes to the seafloor.",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "subterranean and subsea engineering marvels: liquid nitrogen ground-freezing TBMs, undersea immersed tubes, and earthquake-proof base isolators"
    },
    {
        "topic": "Duga Over-the-Horizon Radar: The colossal 150-meter-tall antenna array in Chernobyl that beamed 10-megawatt tapping pulses across the Atlantic",
        "short_hook": "The Soviet mega-antenna that tapped into radios worldwide during the Cold War.",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "extreme kinetic and aerospace mechanics: aircraft carrier catapults, jet engine thrust reversers, turbopumps, and hypersonic wind tunnels"
    },
    {
        "topic": "Heavy Haul Train Dynamic Braking: How 20,000-ton iron ore trains convert immense gravitational kinetic energy into pure heat without wearing brakes",
        "short_hook": "How do 20,000-ton trains stop on steep mountains without destroying their brakes?",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "extreme kinetic and aerospace mechanics: aircraft carrier catapults, jet engine thrust reversers, turbopumps, and hypersonic wind tunnels"
    },
    {
        "topic": "The Liebherr LR 13000: The world's most powerful crawler crane that hoists 3,000 tons of steel with 1,500 tons of suspended counterweights",
        "short_hook": "The world's strongest crane can lift 3,000 tons of steel into the sky.",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "colossal heavy-lifting machinery: Bagger 293 bucket-wheel excavators, crawler-transporters, and semi-submersible heavy-lift vessels"
    },
    {
        "topic": "Hydraulic Synchronized Bridge Jacking: How multi-million-pound pre-built bridges are slid into place across highways in 48 hours without closing traffic",
        "short_hook": "How engineers slide an entire multi-lane highway bridge into place in 48 hours.",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "hydraulic and nautical marvels: Panama Canal gravity water locks, Delta Works storm surge barriers, and dry dock hydraulic gates"
    },
    {
        "topic": "Aircraft Oleo Struts: How nitrogen and hydraulic fluid shock absorbers swallow 200,000 pounds of kinetic touchdown energy in milliseconds",
        "short_hook": "What keeps a 200-ton jet from shattering into pieces when it slams onto the runway?",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "extreme kinetic and aerospace mechanics: aircraft carrier catapults, jet engine thrust reversers, turbopumps, and hypersonic wind tunnels"
    },
    {
        "topic": "TBM Tungsten Carbide Disc Cutters: How 17-inch rolling steel cutters exert 25 tons of focused hydraulic thrust to pulverize bedrock into chips",
        "short_hook": "These rolling steel wheels crack solid mountain bedrock with 25 tons of force.",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "subterranean and subsea engineering marvels: liquid nitrogen ground-freezing TBMs, undersea immersed tubes, and earthquake-proof base isolators"
    },
    {
        "topic": "Cryogenic Vacuum Piping: How rocket fuel lines pump liquid hydrogen at minus 253 degrees Celsius through vacuum-jacketed double walls without boil-off",
        "short_hook": "How do you transport liquid hydrogen at minus 253 degrees without it boiling away?",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "extreme kinetic and aerospace mechanics: aircraft carrier catapults, jet engine thrust reversers, turbopumps, and hypersonic wind tunnels"
    }
]

def validate_config():
    missing = []
    if not GEMINI_API_KEYS:
        missing.append("GEMINI_API_KEY or GEMINI_API_KEYS")
    
    check_vars = []
    if PEXELS_API_KEY:
        check_vars.append(("PEXELS_API_KEY", PEXELS_API_KEY))
    if os.environ.get("DISABLE_YT_UPLOAD") != "1":
        check_vars.extend([
            ("YT_CLIENT_ID", YT_CLIENT_ID),
            ("YT_CLIENT_SECRET", YT_CLIENT_SECRET),
            ("YT_REFRESH_TOKEN", YT_REFRESH_TOKEN)
        ])
    for var, val in check_vars:
        if not val:
            missing.append(var)
    if missing:
        raise ValueError(f"Missing required env vars: {', '.join(missing)}")
    n = len(GEMINI_API_KEYS)
    print(f"[Config] {n} Gemini generation key(s) loaded.")
    if GEMINI_JUDGE_API_KEY != GEMINI_API_KEY:
        print("[Config] Separate GEMINI_JUDGE_API_KEY active — Judge uses its own quota.")
    if COVERR_API_KEY:
        print("[Config] Coverr API: enabled (cinematic B-roll tier active).")
    if NASA_API_KEY:
        print(f"[Config] NASA API: enabled (key={'DEMO_KEY (rate-limited)' if NASA_API_KEY == 'DEMO_KEY' else 'custom'}).")
    if KLIPY_API_KEY:
        print("[Config] Klipy API: enabled (GIF/meme B-roll tier active).")
    if FREESOUND_API_KEY:
        print("[Config] Freesound API: enabled (CC0 ambient music tier active).")

# ── Social / Beacons Link ───────────────────────────────────────────────────
BEACONS_LINK = os.environ.get("BEACONS_LINK", "https://beacons.ai/edu_fun")

# ── Fleet Niche Profiles & Digital Fingerprints ──────────────────────────────
FLEET_NICHE_PROFILES = {
    "science": {
        "channel_id": "ch1",
        "name": "Science & Frontier Tech",
        "gemini_voice": "Fenrir",
        "kokoro_voice": "am_adam",
        "edge_voice": "en-US-GuyNeural",
        "cadence_speed": 1.02,
        "vocal_tone": "bold_authority",
        "persona_desc": "precise, analytical, 1.02x",
        "subtitle_fonts": ["Rajdhani", "Montserrat", "Bebas Neue"],
        "c_base": "&H00FFFFFF&",          # Base: Pure White (#FFFFFF)
        "c_active": "&H00FFE500&",        # Active: Electric Cyan (#00E5FF)
        "c_power": "&H00FF8800&",         # Power Accent: Neon Blue/Orange
        "outline_color": "&H00100505&",   # Outline: 9px #050510 (obsidian navy)
        "shadow_color": "&H80000000&",    # Shadow: 3px
        "outline_w": 9,
        "shadow_d": 3,
        "blur": 1,
        "margin_v": 440,
        "procedural_chords": [
            [("D", "min"), ("G", "maj"), ("C", "maj"), ("A", "min")],
            [("E", "min"), ("A", "min"), ("D", "maj"), ("B", "min")],
            [("C", "maj"), ("A", "min"), ("F", "maj"), ("G", "maj")],
        ],
        "music_bpm": 120,
        "foley_type": "digital_tech",
        "ducking": {
            "attack": 15,
            "release": 180,
            "ratio": 4.0,
            "threshold": 0.07,
            "music_vol": 0.22,
            "sfx_vol": 0.28,
        },
        "container_metadata": {
            "artist": "Axiom Lab Studios / Science & Frontier Tech",
            "genre": "Science & Technology / Quantum Astrophysics",
            "comment": "Autonomous analytical documentary series on frontier science, quantum physics, and advanced technology.",
        },
        "color_curves": "eq=contrast=1.08:saturation=1.14:gamma=0.95,colorbalance=bs=0.06:bm=0.02:rs=-0.02",
        "badge_text": "⚛ QUANTUM LAB",
        "badge_border": "#00E5FF",
        "badge_bg": "#050B14",
        "thumb_font": "Rajdhani",
        "thumb_color1": "#FFFFFF",
        "thumb_color2": "#00E5FF",
        "thumb_border": "#050510",
    },
    "nature": {
        "channel_id": "ch2",
        "name": "Nature & Extreme Biology",
        "gemini_voice": "Kore",
        "kokoro_voice": "af_heart",
        "edge_voice": "en-US-AvaNeural",
        "cadence_speed": 0.98,
        "vocal_tone": "deep_curiosity",
        "persona_desc": "wonder, rhythmic cadence, 0.98x",
        "subtitle_fonts": ["Komika Axis", "Gilroy", "Montserrat", "Bebas Neue"],
        "c_base": "&H00F0FFF0&",          # Base: Honeydew Soft Organic White (#F0FFF0)
        "c_active": "&H0066FF00&",        # Active: Bioluminescent Lime (#00FF66)
        "c_power": "&H0000E6FF&",         # Power Accent: Sun Gold
        "outline_color": "&H00102005&",   # Outline: 8px #052010 (abyssal black-green)
        "shadow_color": "&H80081002&",    # Shadow: 3px
        "outline_w": 8,
        "shadow_d": 3,
        "blur": 0,
        "margin_v": 440,
        "procedural_chords": [
            [("E", "min"), ("G", "maj"), ("D", "maj"), ("C", "maj")],
            [("A", "min"), ("C", "maj"), ("G", "maj"), ("F", "maj")],
            [("D", "min"), ("A#", "maj"), ("F", "maj"), ("C", "maj")],
        ],
        "music_bpm": 92,
        "foley_type": "organic_nature",
        "ducking": {
            "attack": 40,
            "release": 350,
            "ratio": 2.8,
            "threshold": 0.09,
            "music_vol": 0.26,
            "sfx_vol": 0.25,
        },
        "container_metadata": {
            "artist": "BioSphere Explorations / Wild Earth Media",
            "genre": "Nature & Wildlife / Extreme Biology",
            "comment": "Documentary expedition exploring abyssal fauna, evolutionary adaptations, and planetary ecosystems.",
        },
        "color_curves": "eq=contrast=1.05:saturation=1.18:gamma=0.98,colorbalance=gs=0.05:gh=0.03:rh=0.02:bh=-0.03",
        "badge_text": "🌿 EXTREME NATURE",
        "badge_border": "#00FF66",
        "badge_bg": "#041408",
        "thumb_font": "Komika Axis",
        "thumb_color1": "#F0FFF0",
        "thumb_color2": "#00FF66",
        "thumb_border": "#052010",
    },
    "history": {
        "channel_id": "ch3",
        "name": "History & Warfare Tactics",
        "gemini_voice": "Charon",
        "kokoro_voice": "am_michael",
        "edge_voice": "en-US-ChristopherNeural",
        "cadence_speed": 0.96,
        "vocal_tone": "dark_revelation",
        "persona_desc": "grave, baritone historical storyteller, 0.96x",
        "subtitle_fonts": ["Cinzel", "TheBoldFont", "Bebas Neue"],
        "c_base": "&H00C7E8F5&",          # Base: Antique Parchment (#F5E8C7)
        "c_active": "&H0000D7FF&",        # Active: Imperial Gold (#FFD700)
        "c_power": "&H003333CC&",         # Power Accent: Imperial Crimson
        "outline_color": "&H00000A1A&",   # Outline: 9px #1A0A00 (bronze mahogany)
        "shadow_color": "&H8000050D&",    # Shadow: 4px
        "outline_w": 9,
        "shadow_d": 4,
        "blur": 2,
        "margin_v": 440,
        "procedural_chords": [
            [("A", "min"), ("D", "min"), ("E", "maj"), ("A", "min")],
            [("D", "min"), ("G", "min"), ("A", "maj"), ("D", "min")],
            [("E", "min"), ("B", "min"), ("C", "maj"), ("B", "maj")],
        ],
        "music_bpm": 80,
        "foley_type": "historical_warfare",
        "ducking": {
            "attack": 20,
            "release": 300,
            "ratio": 3.8,
            "threshold": 0.08,
            "music_vol": 0.24,
            "sfx_vol": 0.29,
        },
        "container_metadata": {
            "artist": "Chronos Archive / Historical Warfare Documentaries",
            "genre": "History & Military Strategy / Tactical Chronicles",
            "comment": "Declassified tactical warfare chronicles, ancient siege mechanics, and empire collapse records.",
        },
        "color_curves": "eq=contrast=1.10:saturation=0.95:gamma=0.93,colorbalance=rs=0.05:rh=0.06:gh=0.02:bs=-0.04:bh=-0.06",
        "badge_text": "⚔ DECLASSIFIED ARCHIVE",
        "badge_border": "#FFD700",
        "badge_bg": "#1A0800",
        "thumb_font": "Cinzel",
        "thumb_color1": "#F5E8C7",
        "thumb_color2": "#FFD700",
        "thumb_border": "#1A0A00",
    },
    "mystery": {
        "channel_id": "ch4",
        "name": "Mysteries & Unexplained",
        "gemini_voice": "Puck",
        "kokoro_voice": "am_fenrir",
        "edge_voice": "en-US-EricNeural",
        "cadence_speed": 1.00,
        "vocal_tone": "suspenseful_mystery",
        "persona_desc": "inquisitive, suspenseful, 1.00x",
        "subtitle_fonts": ["Montserrat Black", "Montserrat", "Archivo Black", "Bebas Neue"],
        "c_base": "&H00E0E0E0&",          # Base: Spectral Silver (#E0E0E0)
        "c_active": "&H0000FFDF&",        # Active: Acid Yellow (#DFFF00)
        "c_power": "&H00FF00B8&",         # Power Accent: Neon Violet
        "outline_color": "&H0014000B&",   # Outline: 10px #0B0014 (obsidian violet)
        "shadow_color": "&H6054003B&",    # Shadow: 4px Violet Drop Shadow (#3B0054)
        "outline_w": 10,
        "shadow_d": 4,
        "blur": 1,
        "margin_v": 440,
        "procedural_chords": [
            [("B", "min"), ("F", "min"), ("G", "maj"), ("C#", "min")],
            [("C", "min"), ("F#", "dim"), ("G#", "maj"), ("D", "min")],
            [("E", "min"), ("A#", "dim"), ("B", "min"), ("F", "maj")],
        ],
        "music_bpm": 104,
        "foley_type": "mystery_eerie",
        "ducking": {
            "attack": 30,
            "release": 400,
            "ratio": 3.0,
            "threshold": 0.10,
            "music_vol": 0.28,
            "sfx_vol": 0.26,
        },
        "container_metadata": {
            "artist": "Enigma Files / Anomalies & Unexplained",
            "genre": "Mystery & Investigation / Archaeological Paradoxes",
            "comment": "Declassified investigations into archaeological enigmas, geological anomalies, and unexplained paradoxes.",
        },
        "color_curves": "eq=contrast=1.12:saturation=0.92:gamma=0.90,colorbalance=bs=0.07:bm=-0.03:rs=-0.04:rh=0.03:bh=0.04",
        "badge_text": "👁 UNEXPLAINED FILE",
        "badge_border": "#DFFF00",
        "badge_bg": "#0B0014",
        "thumb_font": "Montserrat Black",
        "thumb_color1": "#E0E0E0",
        "thumb_color2": "#DFFF00",
        "thumb_border": "#0B0014",
    },
    "engineering": {
        "channel_id": "ch4",
        "name": "Marvel Engeneering (Engineering Marvels & How It Works)",
        "gemini_voice": "Orus",
        "kokoro_voice": "am_puck",
        "edge_voice": "en-US-BrianNeural",
        "cadence_speed": 1.04,
        "vocal_tone": "bold_authority",
        "persona_desc": "resonant, punchy industrial, 1.04x",
        "subtitle_fonts": ["Barlow Condensed", "Bebas Neue", "Anton"],
        "c_base": "&H00FFFFFF&",          # Base: Blueprint Titanium White (#FFFFFF)
        "c_active": "&H000055FF&",        # Active: Safety Orange (#FF5500)
        "c_power": "&H0000CCFF&",         # Power Accent: Hazard Yellow
        "outline_color": "&H00241E1A&",   # Outline: 9px #1A1E24 (machined dark slate)
        "shadow_color": "&H80120F0D&",    # Shadow: 3px Machine Slate Shadow
        "outline_w": 9,
        "shadow_d": 3,
        "blur": 0,
        "margin_v": 440,
        "procedural_chords": [
            [("C", "min"), ("D#", "maj"), ("F", "maj"), ("G", "min")],
            [("D", "min"), ("F", "maj"), ("G", "maj"), ("A", "min")],
            [("G", "min"), ("A#", "maj"), ("C", "maj"), ("D", "min")],
        ],
        "music_bpm": 130,
        "foley_type": "industrial_machinery",
        "ducking": {
            "attack": 12,
            "release": 150,
            "ratio": 4.5,
            "threshold": 0.06,
            "music_vol": 0.23,
            "sfx_vol": 0.32,
        },
        "container_metadata": {
            "artist": "Marvel Engeneering / Engineering Marvels & How It Works",
            "genre": "Engineering & Technology / Colossal Machines & Extreme Feats",
            "comment": "Documenting colossal machines, extreme kinetic mechanisms, and how impossible engineering feats work.",
        },
        "color_curves": "eq=contrast=1.12:saturation=1.16:gamma=0.94,colorbalance=rs=0.02:rh=0.05:gh=0.02:bs=0.04:bh=-0.03",
        "badge_text": "⚙ ENGINEERING MARVEL",
        "badge_border": "#FF5500",
        "badge_bg": "#101418",
        "thumb_font": "Barlow Condensed",
        "thumb_color1": "#FFFFFF",
        "thumb_color2": "#FF5500",
        "thumb_border": "#1A1E24",
    },
    "business": {
        "channel_id": "ch5",
        "name": "Mind Here Business (Business, Global Trade & Market Secrets)",
        "gemini_voice": "Charon",
        "kokoro_voice": "am_michael",
        "edge_voice": "en-US-ChristopherNeural",
        "cadence_speed": 1.02,
        "vocal_tone": "bold_authority",
        "persona_desc": "authoritative financial & trade investigator, 1.02x",
        "subtitle_fonts": ["Montserrat", "Montserrat Black", "Bebas Neue"],
        "c_base": "&H00FFFFFF&",          # Base: Pure Crisp White (#FFFFFF)
        "c_active": "&H00A3E500&",        # Active: Wealth Emerald (#00E5A3)
        "c_power": "&H0000D7FF&",         # Power Accent: Gold (#FFD700)
        "outline_color": "&H000A0805&",   # Outline: 9px #05080A (obsidian navy)
        "shadow_color": "&H80000000&",    # Shadow: 3px
        "outline_w": 9,
        "shadow_d": 3,
        "blur": 1,
        "margin_v": 440,
        "procedural_chords": [
            [("C", "min"), ("Ab", "maj"), ("Eb", "maj"), ("Bb", "maj")],
            [("D", "min"), ("Bb", "maj"), ("F", "maj"), ("C", "maj")],
            [("A", "min"), ("F", "maj"), ("C", "maj"), ("G", "maj")],
        ],
        "music_bpm": 112,
        "foley_type": "digital_tech",
        "ducking": {
            "attack": 20,
            "release": 250,
            "ratio": 3.8,
            "threshold": 0.08,
            "music_vol": 0.22,
            "sfx_vol": 0.28,
        },
        "container_metadata": {
            "artist": "Mind Here Business / Global Trade & Corporate Investigations",
            "genre": "Business & Economics / Global Trade & Market Secrets",
            "comment": "Investigative documentary series on global supply chain chokepoints, corporate monopolies, and market secrets.",
        },
        "color_curves": "eq=contrast=1.12:saturation=1.10:gamma=0.95,colorbalance=rs=0.03:gs=0.04:bs=-0.02",
        "badge_text": "$ TRADE SECRETS",
        "badge_border": "#00E5A3",
        "badge_bg": "#05120C",
        "thumb_font": "Montserrat",
        "thumb_color1": "#FFFFFF",
        "thumb_color2": "#00E5A3",
        "thumb_border": "#05080A",
    },
}

def get_channel_profile(niche: str = None) -> dict:
    if not niche:
        niche = os.environ.get("CHANNEL_NICHE", CHANNEL_NICHE).lower()
    return FLEET_NICHE_PROFILES.get(niche, FLEET_NICHE_PROFILES.get("science", {}))

# Niche-adaptive active voice settings
_curr_profile = get_channel_profile()
DEFAULT_GEMINI_VOICE = _curr_profile.get("gemini_voice", "Fenrir")
DEFAULT_EDGE_VOICE = _curr_profile.get("edge_voice", "en-US-AndrewNeural")
DEFAULT_KOKORO_VOICE = _curr_profile.get("kokoro_voice", "am_adam")
VOICE_PITCH = 0.0
VOICE_RATE = _curr_profile.get("cadence_speed", 1.02)


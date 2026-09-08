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
GEMINI_FLASH        = "gemini-2.5-flash"
GEMINI_FLASH_BACKUP = "gemini-2.5-flash-lite"
GEMINI_PRO          = "gemini-2.5-flash"
GEMINI_TTS_MODEL    = "gemini-2.5-flash-preview-tts"
GEMINI_API_BASE     = "https://generativelanguage.googleapis.com/v1beta"

GEMINI_VOICES    = ["Fenrir", "Puck", "Charon", "Orus", "Kore"]
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

# ── Channel Boundary & Topic Isolation (Channel 4: Mysteries & Unexplained) ──
CHANNEL_NICHE = os.environ.get("CHANNEL_NICHE", "mystery")

CHANNEL_BOUNDARY = {
    "channel_id": "ch4",
    "name": "Channel 4: Mysteries & Unexplained",
    "niche_description": "Out-of-place artifacts (OOPArts), unexplained subterranean voids and acoustic hums, deep sea acoustic anomalies (The Bloop, Julia), eerie maritime ghost ships, vanished expeditions, and unsolved historical paradoxes.",
    "allowed_subclusters": [
        "archaeological out-of-place artifacts (OOPArts) and ancient enigmas",
        "unexplained geological voids, acoustic hums, and subterranean cavities",
        "deep sea acoustic anomalies, oceanic voids, and unexplained broadcasts",
        "historical vanishings, eerie maritime ghost vessels, and vanished expeditions",
        "unsolved physical anomalies, strange atmospheric lights, and terrestrial mysteries"
    ],
    "strict_negative_constraints": [
        "NO modern civil engineering, modern construction, modern TBMs, modern dams, or modern skyscrapers.",
        "NO standard wildlife documentaries, zoology, or routine animal behavior facts.",
        "NO stock market finance, crypto, economics, hedge funds, or business strategy.",
        "NO standard ancient siege weapons, routine Roman legion formations, or standard battle tactics."
    ],
    "negative_keywords": [
        "modern civil engineering",
        "tunnel boring machine",
        "tbm",
        "modern dam",
        "modern skyscraper",
        "highway construction",
        "bridge construction",
        "liebherr crane",
        "bagger 288",
        "bagger 293",
        "wildlife documentary",
        "zoology",
        "animal behavior",
        "insect mating",
        "endangered species",
        "crypto",
        "bitcoin",
        "stock market",
        "wall street",
        "hedge fund",
        "private equity",
        "tax-loss",
        "quantum computing",
        "quantum error correction",
        "crispr",
        "gene editing",
        "siege engine",
        "roman legion tactic",
        "phalanx formation",
        "gladiator battle",
        "trebuchet mechanics"
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
YT_CATEGORY_SCIENCE   = "27"
YT_CATEGORY_DEFAULT   = "27"
NASA_BROLL_ENABLED    = True

RICH_FALLBACK_TOPICS = [
    {
        "topic": "The Antikythera Mechanism: The 2,000-year-old geared astronomical computer discovered in a Roman shipwreck",
        "short_hook": "How did Greeks build a clockwork computer 2,000 years ago?",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "archaeological out-of-place artifacts (OOPArts) and ancient enigmas"
    },
    {
        "topic": "The Bloop: The ultra-low frequency deep ocean sound detected across 5,000 kilometers of the Pacific in 1997",
        "short_hook": "What made a sound across 5,000 kilometers of ocean?",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "deep sea acoustic anomalies, oceanic voids, and unexplained broadcasts"
    },
    {
        "topic": "The Mary Celeste Mystery: The seaworthy merchant vessel discovered sailing with cargo untouched and all crew vanished",
        "short_hook": "The ghost ship found sailing with not a soul onboard.",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "historical vanishings, eerie maritime ghost vessels, and vanished expeditions"
    },
    {
        "topic": "The Voynich Manuscript: The 15th-century parchment codex written in an undeciphered script with unknown flora",
        "short_hook": "The 600-year-old book that no cryptographer can read.",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "archaeological out-of-place artifacts (OOPArts) and ancient enigmas"
    },
    {
        "topic": "The Taos Hum: The pervasive low-frequency acoustic drone heard by 2% of residents that microphones fail to isolate",
        "short_hook": "The mysterious hum that drives an entire town mad.",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "unexplained geological voids, acoustic hums, and subterranean cavities"
    },
    {
        "topic": "The Devil's Kettle Waterfall: The Minnesota river where half of the water vanishes into a bottomless geological pothole",
        "short_hook": "Where does the water from this bottomless waterfall go?",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "unexplained geological voids, acoustic hums, and subterranean cavities"
    },
    {
        "topic": "The Baltic Sea Anomaly: The 200-foot geometric circular disc resting 300 feet below the surface with bizarre sonar echoes",
        "short_hook": "What is the 200-foot disc resting under the Baltic Sea?",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "deep sea acoustic anomalies, oceanic voids, and unexplained broadcasts"
    },
    {
        "topic": "The Hessdalen Lights: The unexplained geometric plasma orbs dancing over a Norwegian valley since 1981",
        "short_hook": "The glowing orbs that appear over this valley for decades.",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "unsolved physical anomalies, strange atmospheric lights, and terrestrial mysteries"
    },
    {
        "topic": "The Flannan Isle Lighthouse Vanishing: How three veteran keepers vanished from a locked island in 1900 with clocks stopped",
        "short_hook": "Three lighthouse keepers vanished from a locked island.",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "historical vanishings, eerie maritime ghost vessels, and vanished expeditions"
    },
    {
        "topic": "The Roman Dodecahedron: The hollow bronze 12-sided artifacts excavated across northern Europe with zero recorded purpose",
        "short_hook": "Romans made these bronze objects, but nobody knows why.",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "archaeological out-of-place artifacts (OOPArts) and ancient enigmas"
    },
    {
        "topic": "The Sailing Stones of Racetrack Playa: Heavy dolomite boulders moving across desert mud leaving hundreds of yards of tracks",
        "short_hook": "The desert rocks that slide across the mud by themselves.",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "unsolved physical anomalies, strange atmospheric lights, and terrestrial mysteries"
    },
    {
        "topic": "The Dyatlov Pass Incident: The midnight evacuation and unexplained high-energy trauma of nine hikers in the Ural Mountains",
        "short_hook": "What forced nine hikers to cut open their tent in subzero cold?",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "historical vanishings, eerie maritime ghost vessels, and vanished expeditions"
    },
    {
        "topic": "The Yonaguni Monument: The colossal submerged sandstone terraces off Japan displaying precise 90-degree carved stone angles",
        "short_hook": "Is this submerged stone pyramid man-made or natural?",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "archaeological out-of-place artifacts (OOPArts) and ancient enigmas"
    },
    {
        "topic": "The Wow! Signal: The 72-second narrowband hydrogen line radio signal detected by Ohio State's Big Ear in 1977",
        "short_hook": "The 72-second radio signal that came from deep space.",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "unsolved physical anomalies, strange atmospheric lights, and terrestrial mysteries"
    },
    {
        "topic": "The Lost Colony of Roanoke: How 115 English colonists vanished without a struggle leaving only 'CROATOAN' carved on a post",
        "short_hook": "115 colonists vanished, leaving only a single word carved.",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "historical vanishings, eerie maritime ghost vessels, and vanished expeditions"
    },
    {
        "topic": "The Richat Structure: The 40-kilometer concentric geological circular dome in Mauritania visible from space",
        "short_hook": "The giant geological eye in the Sahara desert.",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "unexplained geological voids, acoustic hums, and subterranean cavities"
    },
    {
        "topic": "The Upsweep Sound: The unidentified seasonal deep-ocean acoustic signal recorded continuously by NOAA hydrophones since 1991",
        "short_hook": "The mysterious acoustic howl echoing through the Pacific.",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "deep sea acoustic anomalies, oceanic voids, and unexplained broadcasts"
    },
    {
        "topic": "The Baghdad Battery: The 2,000-year-old terracotta jars holding copper cylinders and iron rods resembling galvanic cells",
        "short_hook": "Did ancient civilizations build electric batteries 2,000 years ago?",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "archaeological out-of-place artifacts (OOPArts) and ancient enigmas"
    },
    {
        "topic": "The Movile Cave Subterranean Biosphere: The Romanian cavern sealed from the surface for 5 million years with sulfuric atmosphere",
        "short_hook": "A sealed cave cut off from Earth for 5 million years.",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "unexplained geological voids, acoustic hums, and subterranean cavities"
    },
    {
        "topic": "G\u00f6bekli Tepe Megaliths: The 11,500-year-old temple complex erected millennia before pottery, metal tools, or wheel transport",
        "short_hook": "How was the world's oldest stone temple built before metal?",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "archaeological out-of-place artifacts (OOPArts) and ancient enigmas"
    },
    {
        "topic": "The Marfa Lights of West Texas: The mysterious dancing nocturnal glowing spheres witnessed in the desert since 1883",
        "short_hook": "The mysterious glowing desert spheres nobody can explain.",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "unsolved physical anomalies, strange atmospheric lights, and terrestrial mysteries"
    },
    {
        "topic": "The Julia Acoustic Broadcast: The chilling four-minute high-amplitude ocean broadcast recorded across the equatorial Pacific",
        "short_hook": "The chilling deep-sea sound heard across an entire ocean.",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "deep sea acoustic anomalies, oceanic voids, and unexplained broadcasts"
    },
    {
        "topic": "The Oak Island Money Pit: The 200-year-old engineered shaft protected by underground flooding booby traps",
        "short_hook": "The buried treasure pit engineered with self-flooding traps.",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "archaeological out-of-place artifacts (OOPArts) and ancient enigmas"
    },
    {
        "topic": "The Lake Baikal Ice Rings: The massive 4-kilometer circular melting formations on Siberian ice visible only from orbit",
        "short_hook": "The giant 4-kilometer circles that appear on Siberian ice.",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "unexplained geological voids, acoustic hums, and subterranean cavities"
    },
    {
        "topic": "The SS Ourang Medan: The Dutch freighter found floating in 1947 with the entire crew dead with terror-stricken expressions",
        "short_hook": "The ghost ship whose entire crew died with look of terror.",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "historical vanishings, eerie maritime ghost vessels, and vanished expeditions"
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

DEFAULT_GEMINI_VOICE = "Fenrir"
DEFAULT_KOKORO_VOICE = "am_adam"
VOICE_PITCH = 0.0
VOICE_RATE = 1.02

DATABASE_PATH = 'stats.db'

ROLES: list[str] = []

# Configuration
ONLINE_ROLE_NAME = "🎮 Online"
ROLES.append(ONLINE_ROLE_NAME)

# PROD Id's
WEBHOOK_CHANNEL_ID = 1291111515977551892
MOD_ROLE_ID = 1222930361848303736
SCOREBOARD_CHANNEL_ID = 1343755601070657566

# Role IDs for achievements and deaths
MOST_DEATHS_ROLE = "💀 Skill Issue"
ROLES.append(MOST_DEATHS_ROLE)

LEAST_DEATHS_ROLE = "👷‍♂️ Safety First"
ROLES.append(LEAST_DEATHS_ROLE)

MOST_ADVANCEMENTS_ROLE = "👑 Overachiever"
ROLES.append(MOST_ADVANCEMENTS_ROLE)

LEAST_ADVANCEMENTS_ROLE = "🌱 Beginner"
ROLES.append(LEAST_ADVANCEMENTS_ROLE)

MOST_PLAYTIME_ROLE = "🕒 No Life"
ROLES.append(MOST_PLAYTIME_ROLE)

LEAST_PLAYTIME_ROLE = "💤 Sleeping"
ROLES.append(LEAST_PLAYTIME_ROLE)


# Minecraft to Discord username mapping
MINECRAFT_TO_DISCORD = {
    "LuigiTime34": "luigi_is_better",
    "_gingercat_": "sblujay",
    "KerDreigerTiger": ".kaiserleopold",
    "Block_Builder": "kazzpyr",
    "AmbiguouSaurus": "bobbilby",
    "wwffd": "wizardcat1000",
    "BurgersAreYumYum": "ih8tk",
    "Dinnerbone5117": "salmon5117_73205",
    "Frogloverender": "frogloverender",
    "Sweatshirtboi16": "sweatshirtboi16",
    "MindJames": "mindjames_93738",
    "therealgoos": "therealgoos",
    "BigSharkyBRo": "car248.",
    "Brandonslay": "ctslayer.",
    "ItzT1g3r": "greattigergaming",
    "The_Rock_Gaming": "the_rock_gaming",
    "THERYZEN7": "asillygooberguy",
    "spleeftrappedlol": "neoptolemus_"
}

# Special characters for detecting death and advancement messages
DEATH_MARKER = "⚰️"
ADVANCEMENT_MARKER = "⭐"

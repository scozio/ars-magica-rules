# Ars Magica 5th Edition Rules Database

A comprehensive, community-driven database of Ars Magica 5th Edition rules, virtues, flaws, abilities, houses, arts, and core mechanics. This repository serves as the data backend for the [Ars Magica Professional TTRPG Hub](https://charactergens.com/arsmagicatome/).

## 📋 Overview

This repository contains JSON-formatted data for:
- **Virtues** - Character advantages and supernatural abilities
- **Flaws** - Character disadvantages and story complications  
- **Abilities** - Skills, knowledge, and supernatural powers
- **Houses of Hermes** - All 13 great houses of the Order
- **Hermetic Arts** - The 5 Techniques and 10 Forms
- **Core Mechanics** - Essential game rules and systems

## 🗂️ Repository Structure

```
ars-magica-rules/
├── README.md
├── LICENSE
├── .gitignore
├── schema.json                    # JSON schema definitions
├── virtues/
│   ├── hermetic-virtues.json      # Virtues specific to Hermetic magi
│   ├── general-virtues.json       # General character virtues
│   └── supernatural-virtues.json  # Supernatural abilities
├── flaws/
│   ├── hermetic-flaws.json        # Flaws affecting Hermetic magic
│   ├── general-flaws.json         # General character flaws
│   └── story-flaws.json           # Story-driven flaws
├── abilities/
│   ├── general-abilities.json     # General skills and knowledge
│   ├── academic-abilities.json    # Academic and scholarly abilities
│   └── arcane-abilities.json      # Magical and supernatural abilities
├── houses/
│   └── houses-of-hermes.json      # All 13 Houses of Hermes
├── arts/
│   ├── techniques.json            # The 5 Hermetic Techniques
│   └── forms.json                 # The 10 Hermetic Forms
└── mechanics/
    └── core-rules.json            # Core game mechanics and rules
```

## 📊 Data Format

All data files follow standardized JSON schemas for consistency and API compatibility.

### Virtues Format
```json
{
  "virtues": [
    {
      "name": "The Gift",
      "type": "Supernatural",
      "category": "Special",
      "points": 0,
      "description": "The supernatural ability to learn and cast Hermetic magic.",
      "requirements": "Required for all magi",
      "source": "Core Rulebook",
      "page": 45
    }
  ]
}
```

### Flaws Format
```json
{
  "flaws": [
    {
      "name": "Blatant Gift",
      "type": "Hermetic",
      "category": "Major",
      "points": 3,
      "description": "The character's Gift is particularly obvious and disturbing.",
      "requirements": "Must have The Gift",
      "source": "Core Rulebook",
      "page": 52
    }
  ]
}
```

### Abilities Format
```json
{
  "abilities": [
    {
      "name": "Magic Theory",
      "type": "Arcane",
      "description": "Knowledge of the principles of Hermetic magic.",
      "specialties": ["Inventing spells", "Enchanting items"],
      "source": "Core Rulebook",
      "page": 67
    }
  ]
}
```

### Houses Format
```json
{
  "houses": [
    {
      "name": "Flambeau",
      "type": "Societas",
      "philosophy": "Problems should be solved directly and decisively.",
      "benefit": "Puissant Ignem",
      "description": "Warriors and battle-mages of the Order.",
      "favored": "Combat magic, military tactics",
      "disfavored": "Lengthy deliberation, complex politics",
      "source": "Core Rulebook",
      "page": 12
    }
  ]
}
```

### Arts Format
```json
{
  "techniques": [
    {
      "name": "Creo",
      "pronunciation": "KRAY-oh",
      "description": "The Art of Creation. Creo brings things into being.",
      "applications": "Creation, healing, restoration",
      "examples": "Healing wounds, creating objects",
      "source": "Core Rulebook",
      "page": 77
    }
  ],
  "forms": [
    {
      "name": "Ignem",
      "pronunciation": "IG-nem", 
      "description": "The Form of fire. Ignem affects fire, heat, and light.",
      "scope": "Fire, heat, light, energy",
      "examples": "Flames, heat, light, lightning",
      "source": "Core Rulebook",
      "page": 78
    }
  ]
}
```

### Mechanics Format
```json
{
  "mechanics": [
    {
      "name": "Stress Die",
      "category": "Dice Rolling",
      "description": "A ten-sided die used for important actions.",
      "details": "Roll 1 for botch check, 0 for double and roll again",
      "source": "Core Rulebook",
      "page": 6
    }
  ]
}
```

## 🎯 Content Goals

### Target Numbers
- **500+ Spells** (handled by separate spell database)
- **150+ Virtues** across all categories
- **150+ Flaws** across all types
- **100+ Abilities** covering all skill areas
- **13 Houses** complete with all details
- **15 Arts** (5 Techniques + 10 Forms)
- **50+ Core Mechanics** covering all essential rules

### Quality Standards
- ✅ **100% Official Compliance** - All content follows Ars Magica 5th Edition rules
- ✅ **Professional Descriptions** - Clear, accurate, and game-ready text
- ✅ **Consistent Formatting** - Standardized JSON schemas throughout
- ✅ **Source Attribution** - Page references for all official content
- ✅ **Community Review** - Peer validation for accuracy

## 🤝 Contributing

We welcome contributions from the Ars Magica community! This project aims to become the definitive digital reference for Ars Magica 5th Edition.

### How to Contribute

1. **Fork** this repository
2. **Create a feature branch** (`git checkout -b feature/new-virtues`)
3. **Add or modify** JSON files following the established format
4. **Validate** your JSON syntax and schema compliance
5. **Test** with the [Rules Database tool](https://charactergens.com/arsmagicatome/ars_magica_rules_database.html)
6. **Submit a pull request** with detailed description

### Contribution Guidelines

#### Adding New Content
- Follow the established JSON schema for each data type
- Include proper source attribution with page numbers
- Use consistent naming and terminology
- Provide complete, accurate descriptions
- Test JSON syntax validity before submitting

#### Content Sources
**Accepted Sources:**
- Ars Magica 5th Edition Core Rulebook
- Official Atlas Games supplements
- Houses of Hermes series
- Tribunal books
- Realm books (Divine, Infernal, Faerie, Magic)

**Community Content:**
- Must be clearly marked as community-created
- Should include detailed explanation/justification
- Subject to community review and approval

#### Quality Requirements
- **Accuracy** - Must match official Ars Magica 5th Edition rules
- **Completeness** - All required fields must be populated
- **Consistency** - Follow established naming conventions
- **Attribution** - Include source and page references

### Code of Conduct
- Be respectful and constructive in all interactions
- Focus on improving the resource for the entire community
- Cite sources accurately and completely
- Accept feedback gracefully and provide helpful reviews

## 🔧 API Integration

This repository is designed to integrate with the Ars Magica Professional TTRPG Hub via GitHub API. The tools automatically:

- Fetch data from repository branches
- Cache content for performance
- Validate JSON schemas
- Display formatted content
- Enable cross-references between tools

### Integration Tools
- **[Rules Database](https://charactergens.com/arsmagicatome/ars_magica_rules_database.html)** - Browse and search all rules content
- **[Spell Builder](https://charactergens.com/arsmagicatome/ars_magica_spell_builder.html)** - Create spells with rules integration
- **[Character Generator](https://charactergens.com/arsmagicatome/ars_magica_character_generator.html)** - Generate characters using virtue/flaw data
- **[Master Hub](https://charactergens.com/arsmagicatome/ars_magica_master_hub.html)** - Unified access to all tools

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Attribution
This work is based on **Ars Magica Fifth Edition** by Atlas Games. Ars Magica is a trademark of Atlas Games. This is a fan-created resource and is not affiliated with or endorsed by Atlas Games.

### Content License
- **Official Content**: Descriptions and rules text are paraphrased and referenced with proper attribution
- **Community Content**: Licensed under MIT for open collaboration
- **Data Structure**: JSON schemas and database organization licensed under MIT

## 🙏 Acknowledgments

- **Atlas Games** for creating the incredible Ars Magica game system
- **The Ars Magica Community** for decades of creativity and support
- **Contributors** who help build and maintain this resource
- **Beta Testers** who help validate accuracy and usability

## 📞 Support

- **Issues**: Use GitHub Issues for bug reports and feature requests
- **Discussions**: Use GitHub Discussions for questions and community chat
- **Tools Support**: Visit [CharacterGens](https://charactergens.com) for tool-specific help

## 🚀 Getting Started

1. **Browse the data** using the [Rules Database](https://charactergens.com/arsmagicatome/ars_magica_rules_database.html)
2. **Fork this repository** to contribute your own content
3. **Integrate with tools** by configuring the GitHub API settings
4. **Join the community** to help improve this resource

---

**Ready to dive into the mysteries of Hermetic magic?** Start exploring the database and join our community of digital magi! 🏰✨

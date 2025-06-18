# Metadata System

This directory uses extracted metadata files to preserve documentation while keeping JSON files as simple arrays.

## File Structure

- `filename.json` - Contains the actual data as a simple array
- `filename.metadata.json` - Contains metadata about the file (title, description, version, etc.)

## Example

**academic_abilities.json:**
```json
[
  {
    "name": "Artes Liberales",
    "category": "Academic",
    "description": "The seven liberal arts..."
  }
]
```

**academic_abilities.metadata.json:**
```json
{
  "title": "Academic Abilities",
  "description": "Scholarly abilities requiring formal education",
  "version": "1.0",
  "source": "Ars Magica 5th Edition",
  "last_updated": "2025-06-13",
  "extraction_info": {
    "original_file": "academic_abilities.json",
    "extracted_array": "abilities",
    "item_count": 6,
    "extracted_on": "2025-06-18T14:30:22",
    "script_version": "1.0"
  }
}
```

## Usage

- The main JSON files are used by applications (Rules Database, etc.)
- The metadata files provide documentation and versioning information
- Both files should be kept in sync when making updates

## Restoration

To restore the original format with embedded metadata, use the restoration script:
```bash
python json_metadata_restorer.py
```

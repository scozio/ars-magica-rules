#!/usr/bin/env python3
"""
JSON Metadata Restorer
Restores JSON files by merging arrays with their metadata files.
"""

import os
import json
import glob

def restore_file(json_file):
    """Restore a JSON file by merging with its metadata."""
    metadata_file = json_file.replace('.json', '.metadata.json')
    
    if not os.path.exists(metadata_file):
        print(f"⏭️  {json_file} - No metadata file found, skipping")
        return False
    
    try:
        # Read array data
        with open(json_file, 'r', encoding='utf-8') as f:
            array_data = json.load(f)
        
        # Read metadata
        with open(metadata_file, 'r', encoding='utf-8') as f:
            metadata = json.load(f)
        
        # Remove extraction_info if present
        if 'extraction_info' in metadata:
            extraction_info = metadata.pop('extraction_info')
            data_key = extraction_info.get('extracted_array', 'data')
        else:
            data_key = 'data'
        
        # Create restored format
        restored_data = {
            'metadata': metadata,
            data_key: array_data
        }
        
        # Write restored file
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(restored_data, f, indent=2, ensure_ascii=False)
        
        print(f"🔧 {json_file} - Restored with metadata")
        return True
        
    except Exception as e:
        print(f"❌ {json_file} - Error: {e}")
        return False

def main():
    print("🔄 JSON Metadata Restorer")
    print("=" * 50)
    
    json_files = glob.glob("*.json")
    json_files = [f for f in json_files if not f.endswith('.metadata.json')]
    
    restored = 0
    for json_file in sorted(json_files):
        if restore_file(json_file):
            restored += 1
    
    print(f"\n📊 Restored {restored} files")

if __name__ == "__main__":
    main()

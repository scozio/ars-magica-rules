#!/usr/bin/env python3
"""
Git Merge Conflict Resolver
Automatically removes Git merge conflict markers from files and keeps the HEAD version.
"""

import os
import re
import sys
import glob
from pathlib import Path

class MergeConflictResolver:
    def __init__(self):
        self.conflict_pattern = re.compile(
            r'<<<<<<< HEAD\n(.*?)\n=======\n.*?\n>>>>>>> [a-f0-9]+',
            re.DOTALL | re.MULTILINE
        )
        self.fixed_files = []
        self.error_files = []

    def fix_file(self, filepath):
        """Remove merge conflict markers from a single file."""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if file has conflict markers
            if '<<<<<<< HEAD' not in content:
                print(f"✅ {filepath} - No conflicts found")
                return False
            
            # Remove conflict markers and keep HEAD version
            fixed_content = self.conflict_pattern.sub(r'\1', content)
            
            # Also handle any remaining conflict markers (edge cases)
            fixed_content = re.sub(r'<<<<<<< HEAD\n', '', fixed_content)
            fixed_content = re.sub(r'\n=======.*?\n>>>>>>> [a-f0-9]+', '', fixed_content, flags=re.DOTALL)
            
            # Write fixed content back to file
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(fixed_content)
            
            print(f"🔧 {filepath} - Fixed merge conflicts")
            self.fixed_files.append(filepath)
            return True
            
        except Exception as e:
            print(f"❌ {filepath} - Error: {e}")
            self.error_files.append((filepath, str(e)))
            return False

    def validate_json(self, filepath):
        """Validate that the fixed JSON is syntactically correct."""
        try:
            import json
            with open(filepath, 'r', encoding='utf-8') as f:
                json.load(f)
            print(f"✅ {filepath} - JSON validation passed")
            return True
        except json.JSONDecodeError as e:
            print(f"❌ {filepath} - JSON validation failed: {e}")
            return False
        except Exception as e:
            print(f"❌ {filepath} - Validation error: {e}")
            return False

    def fix_directory(self, directory='.', pattern='*.json'):
        """Fix all files matching pattern in directory."""
        print(f"🔍 Scanning {directory} for {pattern} files with merge conflicts...")
        
        # Find all matching files
        if directory == '.':
            files = glob.glob(pattern, recursive=True)
            files.extend(glob.glob(f"**/{pattern}", recursive=True))
        else:
            files = glob.glob(os.path.join(directory, pattern), recursive=True)
            files.extend(glob.glob(os.path.join(directory, f"**/{pattern}"), recursive=True))
        
        if not files:
            print(f"❌ No {pattern} files found in {directory}")
            return
        
        print(f"📁 Found {len(files)} files to check")
        
        # Process each file
        for filepath in files:
            self.fix_file(filepath)
        
        # Validate JSON files if any were fixed
        if self.fixed_files and pattern == '*.json':
            print("\n🔍 Validating fixed JSON files...")
            for filepath in self.fixed_files:
                self.validate_json(filepath)
        
        # Summary
        print(f"\n📊 Summary:")
        print(f"   ✅ Fixed: {len(self.fixed_files)} files")
        print(f"   ❌ Errors: {len(self.error_files)} files")
        
        if self.fixed_files:
            print(f"\n📝 Fixed files:")
            for filepath in self.fixed_files:
                print(f"   - {filepath}")
        
        if self.error_files:
            print(f"\n❌ Error files:")
            for filepath, error in self.error_files:
                print(f"   - {filepath}: {error}")

    def create_backup(self, directory='.'):
        """Create backup of files before fixing."""
        import shutil
        import datetime
        
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_dir = f"backup_before_conflict_fix_{timestamp}"
        
        print(f"💾 Creating backup in {backup_dir}...")
        
        try:
            os.makedirs(backup_dir, exist_ok=True)
            
            # Copy all JSON files to backup
            json_files = glob.glob("*.json", recursive=True)
            json_files.extend(glob.glob("**/*.json", recursive=True))
            
            for filepath in json_files:
                if '<<<<<<< HEAD' in open(filepath, 'r', encoding='utf-8').read():
                    dest_path = os.path.join(backup_dir, os.path.basename(filepath))
                    shutil.copy2(filepath, dest_path)
                    print(f"   📋 Backed up: {filepath}")
            
            print(f"✅ Backup created successfully")
            return backup_dir
            
        except Exception as e:
            print(f"❌ Backup failed: {e}")
            return None

def main():
    resolver = MergeConflictResolver()
    
    print("🔧 Git Merge Conflict Resolver")
    print("=" * 50)
    
    # Parse command line arguments
    if len(sys.argv) > 1:
        if sys.argv[1] == '--help' or sys.argv[1] == '-h':
            print("Usage:")
            print("  python conflict_resolver.py [options] [directory]")
            print("")
            print("Options:")
            print("  --backup    Create backup before fixing")
            print("  --no-backup Skip backup creation")
            print("  --pattern   File pattern to match (default: *.json)")
            print("")
            print("Examples:")
            print("  python conflict_resolver.py")
            print("  python conflict_resolver.py --backup")
            print("  python conflict_resolver.py --pattern '*.txt'")
            print("  python conflict_resolver.py /path/to/repo")
            return
    
    # Parse arguments
    create_backup = '--no-backup' not in sys.argv
    pattern = '*.json'
    directory = '.'
    
    for i, arg in enumerate(sys.argv[1:], 1):
        if arg == '--pattern' and i + 1 < len(sys.argv):
            pattern = sys.argv[i + 1]
        elif arg.startswith('/') or arg.startswith('./') or os.path.isdir(arg):
            directory = arg
    
    # Create backup if requested
    if create_backup:
        backup_dir = resolver.create_backup(directory)
        if backup_dir:
            print(f"💡 Tip: If something goes wrong, restore from {backup_dir}\n")
    
    # Fix conflicts
    resolver.fix_directory(directory, pattern)
    
    # Suggest next steps
    if resolver.fixed_files:
        print(f"\n🚀 Next steps:")
        print(f"   1. Review the fixed files to ensure they look correct")
        print(f"   2. Test your application to make sure everything works")
        print(f"   3. Commit the changes:")
        print(f"      git add .")
        print(f"      git commit -m 'Resolved merge conflicts in JSON files'")
        print(f"      git push origin main")

if __name__ == "__main__":
    main()
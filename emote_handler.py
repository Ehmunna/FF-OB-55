# --- START OF FILE emote_handler.py ---
import re
import random

# Bright Colors List
SAFE_COLORS = [
    "[FF0000]", "[00FF00]", "[0000FF]", "[FFFF00]", "[FF00FF]", "[00FFFF]", "[FFFFFF]", "[FFA500]",
    "[FFC0CB]", "[ADD8E6]", "[90EE90]", "[DC143C]", "[00CED1]", "[9400D3]", "[FF1493]",
    "[7CFC00]", "[FF4500]", "[DAA520]", "[00BFFF]", "[00FF7F]", "[4682B4]", "[1E90FF]"
]

def load_emotes_from_file(filename="emotes.json"):
    all_aliases = {}
    categorized_emotes = {}
    current_category = "Uncategorized"
    
    print(f"'{filename}' LOADING EMOTES FROM FILE...")

    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
            
        for line in lines:
            line = line.strip()
            if not line: continue
                
            if line.startswith("#"):
                current_category = line.replace("#", "").strip()
                if current_category not in categorized_emotes:
                    categorized_emotes[current_category] = []
                continue
            
            match = re.search(r"'([^']+)':\s*(\d+)", line)
            if match:
                alias = match.group(1).strip().lower()
                emote_id = int(match.group(2))
                
                all_aliases[alias] = emote_id
                
                if current_category not in categorized_emotes:
                    categorized_emotes[current_category] = []
                
                if alias not in categorized_emotes[current_category]:
                    categorized_emotes[current_category].append(alias)

    except FileNotFoundError:
        print(f"Error: {filename} Not Found")
    except Exception as e:
        print(f"Error loading emotes: {e}")
        
    print(f"Total Loaded: {len(all_aliases)} emotes.")
    return all_aliases, categorized_emotes

def get_menu_pages(categorized_emotes):
    pages = []
    # YAHAN CHANGE KIYA HAI: Ab ye bolega "Bas naam likho"
    current_msg = "[B][C][FF0000]🔥 EMOTE MENU LIST 🔥\n"
    
    for category, emotes in categorized_emotes.items():
        if not emotes: continue
            
        header = f"\n[B][C][00FFFF]━━ {category} ━━\n"
        
        if len(current_msg) + len(header) > 400:
            pages.append(current_msg + "\n[00FF00](Next Page...)")
            current_msg = f"[B][C][00FFFF]━━ {category} (Cont) ━━\n"
        else:
            current_msg += header

        for name in emotes:
            color = random.choice(SAFE_COLORS)
            # Format: name
            line_item = f"{color}➥ {name}\n"
            
            if len(current_msg) + len(line_item) > 450:
                pages.append(current_msg + "\n[00FF00](Next Page...)")
                current_msg = f"[B][C][00FFFF]━━ {category} (Cont) ━━\n" + line_item
            else:
                current_msg += line_item
        
    pages.append(current_msg + "\n[B][C][FF0000]End of List.")
    return pages
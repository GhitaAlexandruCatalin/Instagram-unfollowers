#!/usr/bin/env python3
"""
Instagram Followers Checker - Safe Method
"""

import json
import os
from datetime import datetime

def load_json_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error reading JSON from {filepath}: {e}")
        return None

def extract_usernames(data):
    usernames = set()
    if isinstance(data, list):
        for item in data:
            if isinstance(item, dict):
                if 'string_list_data' in item:
                    for entry in item.get('string_list_data', []):
                        if 'value' in entry:
                            usernames.add(entry['value'])
                elif 'username' in item:
                    usernames.add(item['username'])
                elif 'user' in item and isinstance(item['user'], dict):
                    usernames.add(item['user'].get('username', ''))
    return usernames

def main():
    print("=" * 40)
    print("Instagram Followers Checker (Safe)")
    print("=" * 40 + "\n")
    
    export_folder = input("Path to Instagram export folder (Enter for current dir): ").strip() or "."
    
    followers_file, following_file = None, None
    patterns = {
        'followers': ['followers_1.json', 'followers.json', 'connections/followers_and_following/followers.json', 'followers_and_following/followers.json'],
        'following': ['following.json', 'following_1.json', 'connections/followers_and_following/following.json', 'followers_and_following/following.json']
    }
    
    for pattern in patterns['followers']:
        path = os.path.join(export_folder, pattern)
        if os.path.exists(path):
            followers_file = path
            break
            
    for pattern in patterns['following']:
        path = os.path.join(export_folder, pattern)
        if os.path.exists(path):
            following_file = path
            break
    
    if not followers_file:
        followers_file = input("Enter full path to followers.json: ").strip()
    if not following_file:
        following_file = input("Enter full path to following.json: ").strip()
    
    print("\nLoading data...")
    followers_data = load_json_file(followers_file)
    following_data = load_json_file(following_file)
    
    if not followers_data or not following_data:
        print("Failed to load JSON files.")
        return
    
    followers = extract_usernames(followers_data)
    following = extract_usernames(following_data)
    
    if not followers or not following:
        print("Could not extract usernames. JSON format might be different.")
        return
        
    print(f"Followers: {len(followers)}")
    print(f"Following: {len(following)}")
    
    not_following_back = following - followers
    you_dont_follow_back = followers - following
    mutual = followers & following
    
    print("\n" + "=" * 40)
    print("RESULTS")
    print("=" * 40)
    
    print(f"\nStats:")
    print(f"  Followers: {len(followers)}")
    print(f"  Following: {len(following)}")
    print(f"  Mutual: {len(mutual)}")
    
    if not_following_back:
        print(f"\nNot following you back ({len(not_following_back)}):")
        for user in sorted(not_following_back):
            print(f"  @{user}")
    else:
        print("\nEveryone you follow follows you back.")
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"instagram_check_safe_{timestamp}.txt"
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("Instagram Followers Check (Safe)\n")
        f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 40 + "\n\n")
        
        f.write(f"Stats:\n")
        f.write(f"  Followers: {len(followers)}\n")
        f.write(f"  Following: {len(following)}\n")
        f.write(f"  Mutual: {len(mutual)}\n\n")
        
        f.write(f"Not following you back ({len(not_following_back)}):\n")
        for user in sorted(not_following_back):
            f.write(f"  @{user}\n")
        
        f.write(f"\nYou don't follow back ({len(you_dont_follow_back)}):\n")
        for user in sorted(you_dont_follow_back):
            f.write(f"  @{user}\n")
    
    print(f"\nResults saved to: {filename}")
    print("Done.")

if __name__ == "__main__":
    main()

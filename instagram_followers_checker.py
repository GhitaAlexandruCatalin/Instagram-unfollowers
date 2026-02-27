#!/usr/bin/env python3
"""
Instagram Followers Checker
"""

import instaloader
import getpass
from datetime import datetime

def get_followers_set(profile):
    print("Downloading followers...")
    followers = {follower.username for follower in profile.get_followers()}
    print(f"Found {len(followers)} followers.")
    return followers

def get_following_set(profile):
    print("Downloading following...")
    following = {followee.username for followee in profile.get_followees()}
    print(f"Following {len(following)} users.")
    return following

def main():
    print("=" * 40)
    print("Instagram Followers Checker")
    print("=" * 40 + "\n")
    
    loader = instaloader.Instaloader()
    
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    
    try:
        print("\nAuthenticating...")
        loader.login(username, password)
        print("Authentication successful.\n")
    except instaloader.exceptions.TwoFactorAuthRequiredException:
        two_factor_code = input("2FA code required: ")
        try:
            loader.two_factor_login(two_factor_code)
            print("Authentication successful.\n")
        except Exception as e:
            print(f"2FA Error: {e}")
            return
    except Exception as e:
        print(f"Authentication Error: {e}")
        return
    
    try:
        profile = instaloader.Profile.from_username(loader.context, username)
        
        followers = get_followers_set(profile)
        following = get_following_set(profile)
        
        not_following_back = following - followers
        you_dont_follow_back = followers - following
        
        print("\n" + "=" * 40)
        print("RESULTS")
        print("=" * 40)
        
        print(f"\nStats:")
        print(f"  Followers: {len(followers)}")
        print(f"  Following: {len(following)}")
        print(f"  Mutual: {len(followers & following)}")
        
        if not_following_back:
            print(f"\nNot following you back ({len(not_following_back)}):")
            for user in sorted(not_following_back):
                print(f"  @{user}")
        else:
            print("\nEveryone you follow follows you back.")
        
        if you_dont_follow_back:
            print(f"\nYou don't follow back ({len(you_dont_follow_back)}):")
            for user in sorted(you_dont_follow_back):
                print(f"  @{user}")
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"instagram_check_{timestamp}.txt"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("Instagram Followers Check\n")
            f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Username: @{username}\n")
            f.write("=" * 40 + "\n\n")
            
            f.write(f"Stats:\n")
            f.write(f"  Followers: {len(followers)}\n")
            f.write(f"  Following: {len(following)}\n")
            f.write(f"  Mutual: {len(followers & following)}\n\n")
            
            f.write(f"Not following you back ({len(not_following_back)}):\n")
            for user in sorted(not_following_back):
                f.write(f"  @{user}\n")
            
            f.write(f"\nYou don't follow back ({len(you_dont_follow_back)}):\n")
            for user in sorted(you_dont_follow_back):
                f.write(f"  @{user}\n")
        
        print(f"\nResults saved to: {filename}")
        
    except Exception as e:
        print(f"\nError: {e}")
    
    print("\nDone.")

if __name__ == "__main__":
    main()

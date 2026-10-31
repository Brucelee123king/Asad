"""Change the password of one category: python3 change_password.py <o|pma|fa|hk|lc|pg|nv> [NEWPASSWORD]
Writes the new password into /home/user/keystore/section_passwords.json and prints it. Then run ./admin_publish.sh "change password of <cat>".
People who knew the old password are locked out of that category at their next online launch (they must type the new one)."""
import sys, json, secrets
p = '/home/user/keystore/section_passwords.json'
pw = json.load(open(p)); c = sys.argv[1]; assert c in pw, list(pw)
A = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789'
new = sys.argv[2] if len(sys.argv) > 2 else '-'.join(''.join(secrets.choice(A) for _ in range(4)) for _ in range(2))
pw[c] = new; json.dump(pw, open(p, 'w'), indent=1)
print(c, '->', new)

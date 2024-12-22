from collections import Counter
import sys

MAX_SECRETS = 2000

# Find next secret
mix_and_prune = lambda lhs, rhs: (lhs ^ rhs) & ((1 << 24) - 1)
def next_secret(secret):
    secret = mix_and_prune(secret, (secret << 6))
    secret = mix_and_prune(secret, (secret >> 5))
    secret = mix_and_prune(secret, (secret << 11))
    return secret

# Get counter mapping each 4-element tuple to its final sell price
def get_counter_from_starting_secret(secret):
    secrets = [secret]          # List of generated secrets
    last4_to_final_price = {}   # Answer, still expressed as a dict
    for i in range(MAX_SECRETS):
        # Generate next secret and store
        secrets.append(next_secret(secrets[-1]))

        # Continue if still can't generate the tuples
        if i < 4: continue

        # Build the tuple for the last 4 increments and save it if it has not been previously found
        last4 = tuple(secrets[j + 1] % 10 - secrets[j] % 10 for j in range(i - 3, i + 1))
        last4_to_final_price[last4] = last4_to_final_price.get(last4, secrets[-1] % 10)

    # Return as counter
    return Counter(last4_to_final_price)
    
if __name__ == "__main__":
    # Map each tuple to its corresponding final score
    counter = sum((get_counter_from_starting_secret(int(line.strip())) for line in sys.stdin.readlines()), Counter())

    # Print largest score
    print(counter.most_common(1)[0][1])

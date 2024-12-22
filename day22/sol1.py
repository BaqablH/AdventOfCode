from functools import reduce
import sys

MAX_SECRETS = 2000

# Find next secret
mix_and_prune = lambda lhs, rhs: (lhs ^ rhs) & ((1 << 24) - 1)
def next_secret(secret):
    secret = mix_and_prune(secret, (secret << 6))
    secret = mix_and_prune(secret, (secret >> 5))
    secret = mix_and_prune(secret, (secret << 11))
    return secret

# Generate the MAX_SECRETS-th secret
get_last_secret = lambda secret_0 : reduce(lambda s, _: next_secret(s), range(MAX_SECRETS), secret_0)
    
if __name__ == "__main__":
    print(sum(get_last_secret(int(line.strip())) for line in sys.stdin.readlines()))

import heapq as pq

# Consts
INF: int = 10**9
ENTRANCE_POSITIONS: list[int] = list(range(3, 10, 2))
DESTINATION_POS: dict[str, int] = dict(zip("ABCD", ENTRANCE_POSITIONS))
LETTER_COST: dict[str: int] = {c : 10**i for i, c in enumerate("ABCD")}

# Read initial state (amphipods setting) and initial cost (needed cost to make the amphipods go to and from the main corridor)
def get_initial_state(inp: list[str]) -> tuple[int, tuple[str, int, int]]:
    SMALL_CORRIDOR_LENGTH = len(inp) - 3

    # Accumulate initial costs and amphipods
    initial_cost: int = 0
    amphipods: list[tuple[str, int, int]] = []
    for expected_letter, pos in DESTINATION_POS.items():
        first_fail: int = next(i for i in range(SMALL_CORRIDOR_LENGTH, 0, -1) if inp[i + 1][pos] != expected_letter)
        for dist_to_main_corridor in range(first_fail, 0, -1):
            initial_cost += dist_to_main_corridor * (LETTER_COST[inp[dist_to_main_corridor + 1][pos]] + LETTER_COST[expected_letter])
            amphipods.append((inp[dist_to_main_corridor + 1][pos], pos, dist_to_main_corridor))
    return initial_cost, tuple(sorted(amphipods))

# Get the next state after moving the given amphipod (in index idx) from old_pos to new_pos
def get_next_state(state, idx: int, old_pos: int, new_pos: int, from_entrance: bool):
    return tuple((c,
                  new_pos if i == idx else pos,
                  stack_pos - int(pos == old_pos)
                  ) for i, (c, pos, stack_pos) in enumerate(state) if not (not from_entrance and i == idx))

def find_min_cost(inp: list[str]):
    # Initialize Dijsktra search
    initial_cost, initial_state = get_initial_state(inp)
    PQ = []
    pq.heappush(PQ, (initial_cost, initial_state))
    state_dist = {initial_state: initial_cost}

    # Run Dijkstra
    while len(PQ) > 0:
        # Get next state
        cost, state = pq.heappop(PQ)

        # If the state is empty, it means all amphipods arrived to their position
        if state == (): break

        # Ignore redundant
        if cost != state_dist[state]: continue

        # Explore neighbors
        for idx, (c, pos, stack_pos) in enumerate(state):
            # Ignore blocked elements
            if stack_pos > 1: continue

            from_entrance: bool = (pos in ENTRANCE_POSITIONS)

            # Store which directions we can go to
            occupied_positions = set(p for _, p, _ in state)
            exploration_directions = []
            if from_entrance or DESTINATION_POS[c] > pos: exploration_directions += [range(pos + 1, 12)]
            if from_entrance or DESTINATION_POS[c] < pos: exploration_directions += [range(pos - 1, 0, -1)]

            # Look for each possible destination
            for dir in exploration_directions:
                for l, new_pos in enumerate(dir):
                    to_entrance: bool = (new_pos in ENTRANCE_POSITIONS)
                    to_destination: bool = new_pos == DESTINATION_POS[c]

                    # Stop if obstacle found, continue if the position cannot be a destination
                    if ((not to_entrance) or (not from_entrance and to_destination)) and new_pos in occupied_positions: break
                    if ((from_entrance and to_entrance) or (not from_entrance and not to_destination)): continue
                    
                    # Store next state 
                    next_cost, next_state = cost + (l + 1) * LETTER_COST[c], get_next_state(state, idx, pos, new_pos, from_entrance)
                    if state_dist.get(next_state, INF) > next_cost:
                        pq.heappush(PQ, (next_cost, next_state))
                        state_dist[next_state] = next_cost

    return state_dist[()]

EXTRA_LINES = ["  #D#C#B#A#", "  #D#B#A#C#"]
inp = list(open('../inputs/23.inp', 'r'))
print(find_min_cost(inp))
print(find_min_cost(inp[:3] + EXTRA_LINES + inp[3:]))


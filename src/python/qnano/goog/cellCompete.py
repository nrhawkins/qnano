def cellCompete(states, days):

    if days == 0:
        return states
    if len(states) < 1:
        return states
    new_states = states.copy()

    for d in range(1, days+1):
        states = new_states.copy()
        for i in range(0, len(states)):
            left = states[i-1] if i > 0 else 0
            right = states[i+1] if i < len(states) - 1 else 0
            if left == right:
                new_states[i] = 0
            else:
                new_states[i] = 1

    return new_states


#states = [1,0,0,0,0,1,0,0]
#days = 1

states = [1,1,1,0,1,1,1,1]
days = 2

print(cellCompete(states, days))

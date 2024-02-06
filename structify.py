def count_intersections(radian_measures, identifiers):
    # Pairing start and end
    chords = {}
    for val, identifier in zip(radian_measures, identifiers):
        idx = int(identifier[2:])  # Prepare the chord index
        if identifier.startswith('s_'):
            if idx not in chords:
                chords[idx] = [val]
            else:
                chords[idx].insert(0, val)
        else:
            chords[idx].append(val)
    #print(chords)
            
    events = []
    for val, identifier in zip(radian_measures, identifiers):
        if identifier.startswith('s_'):
            events.append((val, 'start', int(identifier[2:])))
        else:
            events.append((val, 'end', int(identifier[2:])))

    #print(events)
    active_chords = []
    intersections = 0
    for _, event_type, idx in events:
        if event_type == 'start':
            start, end = chords[idx]
            # Check intersections with active chords
            for active_start, active_end in active_chords:
                if (start < active_start < end and end < active_end) or (start < active_end < end and active_start < start):
                    intersections += 1
            active_chords.append((start, end))
        else:
            # print(chords[idx])
            # print("active",active_chords)
            active_chords.remove(tuple(chords[idx]))
    
    return intersections
#[0.9, 1.3, 1.70, 2.92]
#["s_1", "e_1", "s_2", "e_2"]
radian_measures =  [0.78, 1.47, 1.77, 3.92]
identifiers = ["s_1", "s_2", "e_1", "e_2"]

print(count_intersections(radian_measures,identifiers))





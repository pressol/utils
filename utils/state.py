from states_reader import reader, map_state

def getstates(ItemSpec):
    states = reader ()
    statemap = map_state ()
    itemstatemap = None
    for i in statemap:
        if ItemSpec == i:
            itemstatemap = statemap[ItemSpec]
        else:
            itemstatemap = "general_item"
    if itemstatemap is None: exit (1)
    return states[itemstatemap]
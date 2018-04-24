def group_name(animal):
    name = None
    while name is None and not animal.endswith('s'):
        if animal == 'ants':
            return 'colony'
        elif animal == 'bees':
            return 'hive'
        elif animal == 'cats':
            return 'litter'
        elif animal == 'dogs':
            return 'pack'
        animal += 's'
    return name

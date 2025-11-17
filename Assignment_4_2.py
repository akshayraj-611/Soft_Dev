parts = [
    (1,'500-1', 'Hammer',2,  'Pieces'),
    (2,'503','Screwdriver',3,'Pieces'),
    (3,'555','Nail',10,'Pieces'),
    (4,'620','Wrench',1,'Piece'),
    (5,'701-A','Bolt',25,'Pieces')
]
inventory = {part_number: (quantity, unit) for (_, part_number, _, quantity, unit) in parts}

print(inventory)


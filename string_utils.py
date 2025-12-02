


def split_before_each_uppercases(formula):
    if not formula:
        return []
    res = []
    start = 0
    for i in range(1, len(formula)):
        if formula[i].isupper():
            res.append(formula[start:i])
            start = i
    res.append(formula[start:])
    return res






def split_at_first_digit(formula):
    for i, c in enumerate(formula):
        if c.isdigit():
            return formula[:i], int(formula[i:])
    return formula, 1






def count_atoms_in_molecule(molecular_formula):
    """Takes a molecular formula (string) and returns a dictionary of atom counts."""

    parts = split_before_each_uppercases(molecular_formula)
    atom_counts = {}

    for part in parts:
        element, count = split_at_first_digit(part)

        if element not in atom_counts:
            atom_counts[element] = 0

        atom_counts[element] += count

    return atom_counts






def parse_chemical_reaction(reaction_equation):
    """Takes a reaction equation (string) and returns reactants and products as lists.  
    Example: 'H2 + O2 -> H2O' → (['H2', 'O2'], ['H2O'])"""
    reaction_equation = reaction_equation.replace(" ", "")  # Remove spaces for easier parsing
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")

def count_atoms_in_reaction(molecules_list):
    """Takes a list of molecular formulas and returns a list of atom count dictionaries.  
    Example: ['H2', 'O2'] → [{'H': 2}, {'O': 2}]"""
    molecules_atoms_count = []
    for molecule in molecules_list:
        molecules_atoms_count.append(count_atoms_in_molecule(molecule))
    return molecules_atoms_count
